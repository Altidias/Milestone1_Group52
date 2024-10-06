#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from nutrition_app_gui import main_frame as MainFrameBase, result_frame as ResultFrameBase, tracker_frame as TrackerFrameBase
from searching.search import SearchHandler
from tracker.tracker import TrackerHandler
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np
import os
import sys
import subprocess
from visualization.visualization import VisualizationHandler

class MainFrame(MainFrameBase):
    def __init__(self):
        super().__init__(None)
        self.search_handler = SearchHandler()

        self.m_panel_filter_controls.Hide()
        self.m_panel_search_controls.Show()
        self.m_listBox_food_search.Hide()

        self.m_bmToggleBtn_filter_panel.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_filter_panel)
        self.m_toggleBtn_range_filter.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_range_filter)
        self.m_toggleBtn_level_filter.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_level_filter)
        self.m_button_filter_apply.Hide()
        self.m_panel_range_controls.Hide()
        self.m_panel_level_controls.Hide()
        self.m_button_filter_apply.Bind(wx.EVT_BUTTON, self.on_apply_filter)
        self.m_searchCtrl_food_search.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search_button)
        self.m_searchCtrl_food_search.Bind(wx.EVT_TEXT, self.on_text_input)
        self.m_listBox_food_search.Bind(wx.EVT_LISTBOX, self.on_listbox_select)
        self.result_frame = None
        self.populate_nutrient_choices()
        self.Show()

        self.m_button_tracker.Bind(wx.EVT_BUTTON, self.on_open_tracker)

    def populate_nutrient_choices(self):
        nutrients = [col for col in self.search_handler.database_df.columns if col != 'food']
        self.m_listBox_nutrient_selection.AppendItems(nutrients)

    def on_toggle_filter_panel(self, event):
        if self.m_panel_filter_controls.IsShown():
            self.m_panel_filter_controls.Hide()
        else:
            self.m_panel_filter_controls.Show()
        self.Layout()

    def on_toggle_range_filter(self, event):
        if self.m_toggleBtn_range_filter.GetValue():
            self.m_toggleBtn_level_filter.SetValue(False)
            self.m_panel_range_controls.Show()
            self.m_panel_level_controls.Hide()
            self.m_button_filter_apply.Show()
        else:
            self.m_panel_range_controls.Hide()
            if not self.m_toggleBtn_level_filter.GetValue():
                self.m_button_filter_apply.Hide()
        self.Layout()

    def on_toggle_level_filter(self, event):
        if self.m_toggleBtn_level_filter.GetValue():
            self.m_toggleBtn_range_filter.SetValue(False)
            self.m_panel_level_controls.Show()
            self.m_panel_range_controls.Hide()
            self.m_button_filter_apply.Show()
        else:
            self.m_panel_level_controls.Hide()
            if not self.m_toggleBtn_range_filter.GetValue():
                self.m_button_filter_apply.Hide()
        self.Layout()

    def on_text_input(self, event):
        query = self.m_searchCtrl_food_search.GetValue()
        if query:
            matches = self.search_handler.search_food(query)
            if not matches.empty:
                self.update_food_list(matches['food'].tolist())
                self.m_listBox_food_search.Show()
            else:
                self.m_listBox_food_search.Hide()
        else:
            self.m_listBox_food_search.Hide()
        self.Layout()

    def update_food_list(self, food_list):
        self.m_listBox_food_search.Clear()
        self.m_listBox_food_search.AppendItems(food_list)

    def on_listbox_select(self, event):
        selected_item = self.m_listBox_food_search.GetStringSelection()
        self.m_searchCtrl_food_search.SetValue(selected_item)
        self.m_listBox_food_search.Hide()
        self.Layout()

    def on_search_button(self, event):
        query = self.m_searchCtrl_food_search.GetValue()
        if query:
            food_item = self.search_handler.get_food_item(query)
            if food_item is not None:
                self.result_frame = ResultFrame(self, food_item=food_item, search_handler=self.search_handler)
                self.result_frame.Show()
                self.Hide()
            else:
                wx.MessageBox(f"No information found for '{query}'", "Food Not Found", wx.OK | wx.ICON_WARNING)
        else:
            wx.MessageBox("Please enter a food item to search.", "Input Error", wx.OK | wx.ICON_WARNING)

    def on_apply_filter(self, event):
        nutrient = self.m_listBox_nutrient_selection.GetStringSelection()
        if not nutrient:
            wx.MessageBox("Please select a nutrient.", "Input Error", wx.OK | wx.ICON_WARNING)
            return

        if self.m_toggleBtn_level_filter.GetValue():
            level = self.m_choice_filter_level.GetStringSelection().lower()
            if not level:
                wx.MessageBox("Please select a level.", "Input Error", wx.OK | wx.ICON_WARNING)
                return
            filtered_df = self.search_handler.filter_by_level(nutrient, level)
        elif self.m_toggleBtn_range_filter.GetValue():
            min_val = self.m_spinCtrlDouble_range_min.GetValue()
            max_val = self.m_spinCtrlDouble_range_max.GetValue()
            if min_val > max_val:
                max_val = min_val
                self.m_spinCtrlDouble_range_max.SetValue(min_val)
            filtered_df = self.search_handler.filter_by_range(nutrient, min_val, max_val)
        else:
            wx.MessageBox("Please select a filter type.", "Input Error", wx.OK | wx.ICON_WARNING)
            return

        if filtered_df.empty:
            wx.MessageBox("No foods found in the criteria.", "No Results", wx.OK | wx.ICON_INFORMATION)
        else:
            self.result_frame = ResultFrame(self, filtered_df=filtered_df, nutrient=nutrient)
            self.result_frame.Show()
            self.Hide()

    def on_open_tracker(self, event):
        self.tracker_frame = TrackerFrame(self, search_handler=self.search_handler, data_handler=self.search_handler.data_handler)
        self.tracker_frame.Show()
        self.Hide()

class ResultFrame(ResultFrameBase):
    def __init__(self, parent, food_item=None, filtered_df=None, nutrient=None, search_handler=None):
        super().__init__(parent)
        self.parent = parent
        self.food_item = food_item
        self.filtered_df = filtered_df
        self.nutrient = nutrient
        self.search_handler = search_handler

        self.m_toggleBtn_pie_chart.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_pie_chart)
        self.m_toggleBtn_bar_chart.Bind(wx.EVT_TOGGLEBUTTON, self.on_toggle_bar_chart)
        
        self.m_button_macro.Bind(wx.EVT_BUTTON, self.on_show_macro)
        self.m_button_micro.Bind(wx.EVT_BUTTON, self.on_show_micro)

        self.current_chart = 'pie'
        self.current_category = 'macro'
        self.m_toggleBtn_pie_chart.SetValue(True)
        self.m_toggleBtn_bar_chart.SetValue(False)

        self.m_bpButton_back.Bind(wx.EVT_BUTTON, self.on_back)

        if self.food_item is not None:
            self.SetMinSize(wx.Size(1200, 700))
            self.display_food_item()
        elif self.filtered_df is not None:
            self.display_filtered_results()

        self.toggle_chart_buttons()
        self.Layout()

    def toggle_chart_buttons(self):
        if self.food_item is not None:
            self.m_toggleBtn_pie_chart.Show()
            self.m_toggleBtn_bar_chart.Show()
            self.m_button_macro.Show()
            self.m_button_micro.Show()
            self.m_panel_bar_pie_chart.Show()
        else:
            self.m_toggleBtn_pie_chart.Hide()
            self.m_toggleBtn_bar_chart.Hide()
            self.m_button_macro.Hide()
            self.m_button_micro.Hide()
            self.m_panel_bar_pie_chart.Hide()
        self.Layout()

    def on_show_macro(self, event):
        self.current_category = 'macro'
        self.update_chart()

    def on_show_micro(self, event):
        self.current_category = 'micro'
        self.update_chart()

    def on_back(self, event):
        self.parent.Show()
        self.Close()

    def on_toggle_pie_chart(self, event):
        if self.current_chart != 'pie':
            self.current_chart = 'pie'
            self.m_toggleBtn_bar_chart.SetValue(False)
            self.update_chart()

    def on_toggle_bar_chart(self, event):
        if self.current_chart != 'bar':
            self.current_chart = 'bar'
            self.m_toggleBtn_pie_chart.SetValue(False)
            self.update_chart()

    def update_chart(self):
        for child in self.m_panel_bar_pie_chart.GetChildren():
            child.Destroy()

        if self.food_item is not None:
            nutrients = self.food_item.drop(['food', 'Nutrition Density', 'Caloric Value']).loc[lambda x: x > 0]
            
            if self.current_category == 'macro':
                nutrients = nutrients[nutrients.index.isin(self.search_handler.data_handler.MACRONUTRIENTS)]
            elif self.current_category == 'micro':
                nutrients = nutrients[nutrients.index.isin(self.search_handler.data_handler.MICRONUTRIENTS)]
            
            if nutrients.empty:
                wx.MessageBox(f"No {self.current_category}nutrient data available for this food item.", "Information", wx.OK | wx.ICON_INFORMATION)
                return

            visual_handler = VisualizationHandler(self.search_handler)
            panel_size = self.m_panel_bar_pie_chart.GetSize()
            dpi = 100
            fig_width = max(panel_size[0] / dpi, 5)  
            fig_height = max(panel_size[1] / dpi, 4)

            fig = Figure(figsize=(fig_width, fig_height), dpi=dpi)
            ax = fig.add_subplot(111)

            if self.current_chart == 'pie':
                title = f"{self.food_item['food']} - {self.current_category.capitalize()} Nutrients" if 'food' in self.food_item else f"{self.current_category.capitalize()} Nutrient Breakdown"
                visual_handler.draw_pie_chart_on_axes(
                    ax, nutrients, threshold=0.3, title=title, category=self.current_category
                )
            elif self.current_chart == 'bar':
                title = f"{self.food_item['food']} - {self.current_category.capitalize()} Nutrient Values" if 'food' in self.food_item else f"{self.current_category.capitalize()} Nutrient Values"
                visual_handler.draw_bar_graph_on_axes(ax, nutrients, title=title, category=self.current_category)

            # create the canvas and add it to the panel
            self.canvas = FigureCanvas(self.m_panel_bar_pie_chart, -1, fig)
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self.canvas, 1, wx.EXPAND)
            self.m_panel_bar_pie_chart.SetSizer(sizer)
            self.m_panel_bar_pie_chart.Layout()
            self.m_panel_bar_pie_chart.Refresh()

    def on_chart_resize(self, event):
        size = self.m_panel_bar_pie_chart.GetClientSize()
        dpi = self.canvas.GetFigure().dpi
        fig_width = max(size[0] / dpi, 5)
        fig_height = max(size[1] / dpi, 4)

        self.canvas.GetFigure().set_size_inches(fig_width, fig_height, forward=True)
        self.canvas.SetSize(size)
        self.canvas.draw()
        event.Skip()

    def display_food_item(self):
        self.m_panel_bar_pie_chart.Show()
        self.update_chart()
        grid = self.m_grid_result
        grid.ClearGrid()

        num_rows = grid.GetNumberRows()
        if num_rows > 0:
            grid.DeleteRows(0, num_rows, True)
        num_cols = grid.GetNumberCols()
        if num_cols > 0:
            grid.DeleteCols(0, num_cols, True)

        grid.AppendCols(2)

        nutrients = self.food_item.drop('food').to_dict()
        num_rows = len(nutrients)
        grid.AppendRows(num_rows)

        for idx, (nutrient, value) in enumerate(nutrients.items()):
            unit = self.search_handler.data_handler.get_nutrient_unit(nutrient)
            grid.SetCellValue(idx, 0, nutrient)
            grid.SetCellValue(idx, 1, f"{value} {unit}" if unit else str(value))
            grid.SetRowLabelValue(idx, "")

        grid.SetColLabelValue(0, "Nutrient")
        grid.SetColLabelValue(1, "Value")

        grid.SetRowLabelSize(0)
        grid.AutoSize()

        self.Layout()

    def display_filtered_results(self):
        self.m_panel_bar_pie_chart.Hide()
        grid = self.m_grid_result
        grid.ClearGrid()

        num_rows = grid.GetNumberRows()
        if num_rows > 0:
            grid.DeleteRows(0, num_rows, True)
        num_cols = grid.GetNumberCols()
        if num_cols > 0:
            grid.DeleteCols(0, num_cols, True)

        grid.AppendCols(2)
        self.filtered_df = self.filtered_df.reset_index(drop=True)
        num_rows = self.filtered_df.shape[0]
        grid.AppendRows(num_rows)

        for idx in range(num_rows):
            row = self.filtered_df.loc[idx]
            grid.SetCellValue(idx, 0, str(row['food']))
            grid.SetCellValue(idx, 1, str(row[self.nutrient]))
            grid.SetRowLabelValue(idx, "")

        grid.SetColLabelValue(0, "Food")
        grid.SetColLabelValue(1, self.nutrient.capitalize())
        grid.SetRowLabelSize(0)
        grid.AutoSize()

        grid_size = grid.GetBestSize()
        back_button_size = self.m_bpButton_back.GetSize()
        frame_width = max(grid_size.width, back_button_size.width) + 100  # Add some padding

        current_height = self.GetSize().GetHeight()
        self.SetSize(wx.Size(frame_width, current_height))
        self.SetMinSize(wx.Size(frame_width, -1)) 

        self.m_bpButton_back.SetPosition((10, current_height - back_button_size.GetHeight() - 10))

        self.Layout()
class TrackerFrame(TrackerFrameBase):
    def __init__(self, parent, search_handler, data_handler):
        super().__init__(parent)
        self.parent = parent

        self.data_handler = data_handler
        self.search_handler = search_handler
        self.tracker_handler = TrackerHandler(self.data_handler, self.search_handler)


        self.m_bpButton_back.Bind(wx.EVT_BUTTON, self.on_back)
        self.m_listBox_nutrients.Bind(wx.EVT_LISTBOX, self.on_nutrient_selected)
        self.m_button_update_nutrient.Bind(wx.EVT_BUTTON, self.on_update_nutrient)
        self.m_searchCtrl_food_search_intake.Bind(wx.EVT_TEXT, self.on_intake_search_text)
        self.m_listBox_food_search_intake.Bind(wx.EVT_LISTBOX, self.on_intake_food_selected)
        self.m_button_update_intake.Bind(wx.EVT_BUTTON, self.on_update_intake)
        self.m_button_generate_report.Bind(wx.EVT_BUTTON, self.on_generate_report)

        self.m_spinCtrlDouble_servings.SetValue(1)  
        self.m_spinCtrlDouble_servings.SetRange(0.1, 100)  
        self.m_spinCtrlDouble_servings.SetIncrement(0.1)  


        self.selected_nutrient = None
        self.selected_food = None

        self.populate_nutrient_list()

        self.m_listBox_food_search_intake.Hide()

    def on_back(self, event):
        self.parent.Show()
        self.Close()

    def populate_nutrient_list(self):
        nutrients = [col for col in self.data_handler.database_df.columns if col not in ['food', 'Nutrition Density']]
        
        current_goals = self.tracker_handler.get_goal()
        
        self.m_listBox_nutrients.Clear()
        
        for nutrient in nutrients:
            unit = self.data_handler.get_nutrient_unit(nutrient)
            if unit:
                unit = unit.replace('/100g', '').strip()
            
            if nutrient in current_goals:
                self.m_listBox_nutrients.Append(f"{nutrient} ({unit}) (Goal: {current_goals[nutrient]} {unit})")
            else:
                self.m_listBox_nutrients.Append(f"{nutrient} ({unit})")

    def on_nutrient_selected(self, event):
        selected_item = self.m_listBox_nutrients.GetStringSelection()
        # Extract the nutrient name without the unit and goal
        self.selected_nutrient = selected_item.split(" (")[0]
        unit = selected_item.split("(")[1].split(")")[0]
        self.m_staticText_goal.SetLabel(f"{self.selected_nutrient} ({unit})")

        # Get the current goal value for the selected nutrient
        current_goals = self.tracker_handler.get_goal()
        current_value = current_goals.get(self.selected_nutrient, 0)
        self.m_spinCtrlDouble_nutrient_amount.SetValue(current_value)

    def on_update_nutrient(self, event):
        if self.selected_nutrient:
            goal_value = self.m_spinCtrlDouble_nutrient_amount.GetValue()
            self.tracker_handler.set_daily_goal({self.selected_nutrient: goal_value})
            unit = self.data_handler.get_nutrient_unit(self.selected_nutrient).replace('/100g', '').strip()
            wx.MessageBox(f"Goal for {self.selected_nutrient} set to {goal_value} {unit}", "Success", wx.OK | wx.ICON_INFORMATION)
            self.populate_nutrient_list()  # Refresh the nutrient list
            self.m_listBox_nutrients.SetStringSelection(f"{self.selected_nutrient} ({unit}) (Goal: {goal_value} {unit})")  # Reselect the updated item
        else:
            wx.MessageBox("Please select a nutrient to set the goal for.", "Input Error", wx.OK | wx.ICON_WARNING)

    def on_intake_search_text(self, event):
        query = self.m_searchCtrl_food_search_intake.GetValue()
        if query:
            matches = self.search_handler.search_food(query)
            if not matches.empty:
                self.update_intake_food_list(matches['food'].tolist())
                self.m_listBox_food_search_intake.Show()
            else:
                self.m_listBox_food_search_intake.Hide()
        else:
            self.m_listBox_food_search_intake.Hide()
        self.Layout()

    def update_intake_food_list(self, food_list):
        self.m_listBox_food_search_intake.Clear()
        self.m_listBox_food_search_intake.AppendItems(food_list)

    def on_intake_food_selected(self, event):
        self.selected_food = self.m_listBox_food_search_intake.GetStringSelection()
        self.m_searchCtrl_food_search_intake.SetValue(self.selected_food)
        self.m_listBox_food_search_intake.Hide()
        self.Layout()

    def on_update_intake(self, event):
        if self.selected_food:
            try:
                # get the number of servings from the spin control
                servings = self.m_spinCtrlDouble_servings.GetValue()
                
                # use current date for GUI updates
                self.tracker_handler.log_food_intake(self.selected_food, servings)
                wx.MessageBox(f"Added {servings} serving(s) of {self.selected_food} to your intake.", "Success", wx.OK | wx.ICON_INFORMATION)
                self.selected_food = None
                self.m_searchCtrl_food_search_intake.SetValue("")
                self.m_spinCtrlDouble_servings.SetValue(1)  # Reset to default value
            except ValueError as e:
                wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox("Please select a food to add to your intake.", "Input Error", wx.OK | wx.ICON_WARNING)

    def on_generate_report(self, event):
        pdf_path = self.generate_progress_report()
        if pdf_path:
            self.open_pdf(pdf_path)

    def generate_progress_report(self):
        user_data = self.data_handler.get_user_data()
        
        pdf_path = os.path.join('..', 'data', 'progress_report.pdf')
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        story = []

        styles = getSampleStyleSheet()
        story.append(Paragraph("Nutrient Tracker Progress Report", styles['Title']))
        story.append(Spacer(1, 12))

        dates = sorted(user_data['daily_intake'].keys(), reverse=True)

        for date in dates:
            story.append(Paragraph(f"Date: {date}", styles['Heading1']))
            story.append(Spacer(1, 6))

            # Daily Intake
            intake = user_data['daily_intake'].get(date, {})
            if intake:
                story.append(Paragraph("Daily Intake", styles['Heading2']))
                intake_data = [['Nutrient', 'Intake']] + [[k, f"{v:.2f}"] for k, v in intake.items()]
                intake_table = Table(intake_data, colWidths=[200, 100])
                intake_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 8),
                    ('TOPPADDING', (0, 1), (-1, -1), 3),
                    ('BOTTOMPADDING', (0, 1), (-1, -1), 1),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
                ]))
                story.append(intake_table)
                story.append(Spacer(1, 12))

            goals = user_data['historical_goals'].get(date, {})
            if goals:
                story.append(Paragraph("Daily Goals", styles['Heading2']))
                goals_data = [['Nutrient', 'Goal']] + [[k, f"{v:.2f}"] for k, v in goals.items()]
                goals_table = Table(goals_data, colWidths=[200, 100])
                goals_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 8),
                    ('TOPPADDING', (0, 1), (-1, -1), 3),
                    ('BOTTOMPADDING', (0, 1), (-1, -1), 1),
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
                ]))
                story.append(goals_table)
                story.append(Spacer(1, 12))

            if intake and goals:
                story.append(Paragraph("Goal Progress", styles['Heading2']))
                progress = {}
                for nutrient in goals:
                    if nutrient in intake:
                        progress[nutrient] = min((intake[nutrient] / goals[nutrient]) * 100 if goals[nutrient] != 0 else 0, 100)

                drawing = Drawing(400, 200)
                bc = VerticalBarChart()
                bc.x = 50
                bc.y = 50
                bc.height = 125
                bc.width = 300
                bc.data = [list(progress.values())]
                bc.categoryAxis.categoryNames = list(progress.keys())
                bc.valueAxis.valueMin = 0
                bc.valueAxis.valueMax = 100
                bc.valueAxis.valueStep = 20
                bc.categoryAxis.labels.boxAnchor = 'ne'
                bc.categoryAxis.labels.dx = 8
                bc.categoryAxis.labels.dy = -2
                bc.categoryAxis.labels.angle = 30
                bc.bars[0].fillColor = colors.green
                drawing.add(bc)
                story.append(drawing)

            story.append(PageBreak())

        doc.build(story)

        return pdf_path

    def open_pdf(self, pdf_path):
        if os.name == 'nt':  #windows
            os.startfile(pdf_path)
        elif os.name == 'posix':  # unix
            opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
            subprocess.call([opener, pdf_path])

    def display_daily_intake(self):
        daily_intake = self.tracker_handler.get_daily_intake()
        intake_str = "\n".join([f"{nutrient}: {value}" for nutrient, value in daily_intake.items()])
        wx.MessageBox(f"Daily Intake:\n{intake_str}", "Daily Intake", wx.OK | wx.ICON_INFORMATION)

    def display_goal_progress(self):
        progress = self.tracker_handler.check_goal_progress()
        progress_str = "\n".join([f"{nutrient}: {value:.2%}" for nutrient, value in progress.items()])
        wx.MessageBox(f"Goal Progress:\n{progress_str}", "Goal Progress", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
    app.MainLoop()