#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from template_frame import main_frame as MainFrameBase, result_frame as ResultFrameBase
from searching.search import SearchHandler
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import numpy as np
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

class ResultFrame(ResultFrameBase):
    def __init__(self, parent, food_item=None, filtered_df=None, nutrient=None, search_handler=None):
        super().__init__(parent)
        self.parent = parent
        self.food_item = food_item
        self.filtered_df = filtered_df
        self.nutrient = nutrient
        self.search_handler = search_handler

        if self.food_item is not None:
            self.SetMinSize(wx.Size(1200, 700))
            self.display_food_item()
        elif self.filtered_df is not None:
            self.SetMinSize(wx.Size(600, 700))
            self.display_filtered_results()

        self.m_bpButton_back.Bind(wx.EVT_BUTTON, self.on_back)

    def on_back(self, event):
        self.parent.Show()
        self.Close()

    def display_food_item(self):
        self.m_panel_pie_chart.Show()
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
            grid.SetCellValue(idx, 0, nutrient)
            grid.SetCellValue(idx, 1, str(value))
            grid.SetRowLabelValue(idx, "")

        grid.SetColLabelValue(0, "Nutrient")
        grid.SetColLabelValue(1, "Value")

        grid.SetRowLabelSize(0)
        grid.AutoSize()

        self.Layout()
        self.draw_pie_chart()

    def display_filtered_results(self):
        self.m_panel_pie_chart.Hide()
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

        self.Layout()

    def draw_pie_chart(self):
        for child in self.m_panel_pie_chart.GetChildren():
            child.Destroy()

        food_item = self.food_item
        nutrients = food_item.drop(['food', 'Nutrition Density', 'Caloric Value']).loc[lambda x: x > 0]

        if nutrients.empty:
            wx.MessageBox("No nutrient data available for this food item.", "Information", wx.OK | wx.ICON_INFORMATION)
            return

        visual_handler = VisualizationHandler(self.search_handler)
        fig, ax = plt.subplots(figsize=(5, 5))

        title = food_item['food'] if 'food' in food_item else "Nutrient Breakdown"
        title = title.capitalize()
        _, _, _ = visual_handler.draw_pie_chart_on_axes(
            ax, nutrients, threshold=0.3, title=title
        )

        self.canvas = FigureCanvas(self.m_panel_pie_chart, -1, fig)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.m_panel_pie_chart.SetSizer(sizer)
        self.m_panel_pie_chart.Layout()
        self.m_panel_pie_chart.Bind(wx.EVT_SIZE, self.on_pie_chart_resize)
        self.m_panel_pie_chart.Refresh()

    def on_pie_chart_resize(self, event):
        size = self.m_panel_pie_chart.GetClientSize()
        self.canvas.SetSize(size)
        self.canvas.draw()
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
    app.MainLoop()