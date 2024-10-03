#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from template_frame import MyFrame1 as BaseFrame
from searching.search import SearchHandler
from data_handler.data_handler import DataHandler

class MainFrame(BaseFrame):
    def __init__(self):
        super().__init__(None)
        self.search_handler = SearchHandler()
        self.data_handler = DataHandler()

        self.m_panel_filter.Hide()
        self.m_panel_search.Show()

        self.m_grid_search_result.Hide()
        self.m_grid_filter_result.Hide()
        self.m_staticText_search_result.Hide()
        self.m_staticText_filter_result.Hide()

        self.m_listBox_food_search.Hide()
        
        self.m_grid_search_result.SetRowLabelSize(0)

        self.m_searchCtrl_food_search.Bind(wx.EVT_TEXT, self.on_text_input)
        self.m_searchCtrl_food_search.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search_button)
        self.m_listBox_food_search.Bind(wx.EVT_LISTBOX, self.on_listbox_select)

        self.m_button_enable_filtering.Bind(wx.EVT_BUTTON, self.on_enable_filtering)
        self.m_button_enable_searching.Bind(wx.EVT_BUTTON, self.on_enable_searching)

        self.Bind(wx.EVT_LEFT_DOWN, self.on_frame_click)
        self.m_searchCtrl_food_search.Bind(wx.EVT_LEFT_DOWN, self.on_text_or_list_click)
        self.m_listBox_food_search.Bind(wx.EVT_LEFT_DOWN, self.on_text_or_list_click)

        self.populate_nutrient_choices()

        self.m_checkBox_level_filter.Bind(wx.EVT_CHECKBOX, self.on_level_filter_checked)
        self.m_checkBox_range_filter.Bind(wx.EVT_CHECKBOX, self.on_range_filter_checked)
        self.m_choice_nutrient_filter.Bind(wx.EVT_CHOICE, self.on_nutrient_selected)
        self.m_choice_filter_level.Bind(wx.EVT_CHOICE, self.on_level_selected)
        self.m_spinCtrlDouble_range_min.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_range_values_changed)
        self.m_spinCtrlDouble_range_max.Bind(wx.EVT_SPINCTRLDOUBLE, self.on_range_values_changed)

        self.m_spinCtrlDouble_range_min.Disable()
        self.m_spinCtrlDouble_range_max.Disable()
        self.m_choice_filter_level.Disable()

        self.is_typing = True
        self.Show()

    def on_enable_filtering(self, event):
        self.m_panel_search.Hide()
        self.m_panel_filter.Show()
        self.Layout()

    def on_enable_searching(self, event):
        self.m_panel_filter.Hide()
        self.m_panel_search.Show()
        self.Layout()

    def populate_nutrient_choices(self):
        nutrients = [col for col in self.search_handler.database_df.columns if col != 'food']
        self.m_choice_nutrient_filter.AppendItems(nutrients)

    def on_level_filter_checked(self, event):
        if self.m_checkBox_level_filter.IsChecked():
            self.m_checkBox_range_filter.SetValue(False)
            self.m_choice_filter_level.Enable()
            self.m_spinCtrlDouble_range_min.Disable()
            self.m_spinCtrlDouble_range_max.Disable()
        else:
            self.m_choice_filter_level.Disable()
        self.apply_filter()

    def on_range_filter_checked(self, event):
        if self.m_checkBox_range_filter.IsChecked():
            self.m_checkBox_level_filter.SetValue(False)
            self.m_spinCtrlDouble_range_min.Enable()
            self.m_spinCtrlDouble_range_max.Enable()
            self.m_choice_filter_level.Disable()
        else:
            self.m_spinCtrlDouble_range_min.Disable()
            self.m_spinCtrlDouble_range_max.Disable()
        self.apply_filter()

    def on_nutrient_selected(self, event):
        self.apply_filter()

    def on_level_selected(self, event):
        self.apply_filter()

    def on_range_values_changed(self, event):
        self.apply_filter()

    def apply_filter(self):
        nutrient = self.m_choice_nutrient_filter.GetStringSelection()
        if not nutrient:
            self.clear_filter_grid()
            return

        if self.m_checkBox_level_filter.IsChecked():
            level = self.m_choice_filter_level.GetStringSelection().lower()
            if not level:
                self.clear_filter_grid()
                return
            filtered_df = self.search_handler.filter_by_level(nutrient, level)
        elif self.m_checkBox_range_filter.IsChecked():
            min_val = self.m_spinCtrlDouble_range_min.GetValue()
            max_val = self.m_spinCtrlDouble_range_max.GetValue()
            if min_val > max_val:
                wx.MessageBox("Minimum value cannot be greater than maximum value.", "Error", wx.OK | wx.ICON_ERROR)
                return
            filtered_df = self.search_handler.filter_by_range(nutrient, min_val, max_val)
        else:
            self.clear_filter_grid()
            return

        if filtered_df.empty:
            wx.MessageBox("No matching foods found.", "Information", wx.OK | wx.ICON_INFORMATION)
            self.clear_filter_grid()
        else:
            self.update_filter_grid(filtered_df, nutrient)

    def update_filter_grid(self, df, nutrient):
        formatted_nutrient = ' '.join(word.capitalize() for word in nutrient.split())
        self.m_staticText_filter_result.SetLabel("Foods containing " + formatted_nutrient + " within the filter criteria")
        self.m_staticText_filter_result.Show()
        grid = self.m_grid_filter_result

        grid.Show()

        grid.ClearGrid()
        num_rows = grid.GetNumberRows()
        num_cols = grid.GetNumberCols()
        if num_rows > 0:
            grid.DeleteRows(0, num_rows, True)
        if num_cols > 0:
            grid.DeleteCols(0, num_cols, True)

        food_names = df['food'].tolist()
        grid.AppendCols(len(food_names))
        grid.AppendRows(1)

        for col_idx, food in enumerate(food_names):
            grid.SetColLabelValue(col_idx, food)

        grid.SetRowLabelValue(0, nutrient)

        grid.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        grid.AutoSizeRowLabelSize(0)

        for col_idx, value in enumerate(df[nutrient]):
            grid.SetCellValue(0, col_idx, str(value))

        grid.AutoSizeColumns()
        grid.AutoSizeRows()
        self.Layout()
        grid.ForceRefresh()

    def clear_filter_grid(self):
        grid = self.m_grid_filter_result
        grid.ClearGrid()
        num_rows = grid.GetNumberRows()
        num_cols = grid.GetNumberCols()
        if num_rows > 0:
            grid.DeleteRows(0, num_rows, True)
        if num_cols > 0:
            grid.DeleteCols(0, num_cols, True)
        grid.Hide()
        self.Layout()
        grid.ForceRefresh()

    def on_text_input(self, event):
        if not self.is_typing:
            return

        query = self.m_searchCtrl_food_search.GetValue()
        if query:
            matches = self.get_similar_items(query)
            if not matches.empty:
                self.update_list(matches['food'].tolist())
                self.m_listBox_food_search.Show()
            else:
                self.m_listBox_food_search.Hide()
        else:
            self.m_listBox_food_search.Hide()
        self.Layout()

    def get_similar_items(self, query):
        return self.search_handler.search_food(query)

    def update_list(self, matches):
        self.m_listBox_food_search.Clear()
        self.m_listBox_food_search.Append(matches)

    def on_listbox_select(self, event):
        selected_item = self.m_listBox_food_search.GetString(self.m_listBox_food_search.GetSelection())
        self.is_typing = False
        self.m_searchCtrl_food_search.SetValue(selected_item)
        self.is_typing = True

    def on_search_button(self, event):
        selected_food = self.m_searchCtrl_food_search.GetValue()
        self.perform_search(selected_food)
        self.m_listBox_food_search.Hide()
        self.Layout()

    def perform_search(self, query):
        food_item = self.search_handler.get_food_item(query)
        if food_item is not None:
            self.update_search_grid(food_item)
        else:
            wx.MessageBox(f"No information found for '{query}'", "Food Not Found", wx.OK | wx.ICON_WARNING)
            self.m_staticText_search_result.Hide()
            self.clear_search_grid()
        self.m_listBox_food_search.Hide()
        self.Layout()

    def update_search_grid(self, food_item):
        food_name = food_item['food']
        formatted_name = ' '.join(word.capitalize() for word in food_name.split())
        self.m_staticText_search_result.SetLabel(formatted_name + " Nutrition Information")
        self.m_staticText_search_result.Show()
        grid = self.m_grid_search_result

        grid.Show()

        grid.ClearGrid()
        num_rows = grid.GetNumberRows()
        num_cols = grid.GetNumberCols()
        if num_rows > 0:
            grid.DeleteRows(0, num_rows, True)
        if num_cols > 0:
            grid.DeleteCols(0, num_cols, True)

        nutrients = [col for col in food_item.index if col != 'food']
        grid.AppendCols(len(nutrients))
        grid.AppendRows(1)

        for col_idx, col_name in enumerate(nutrients):
            grid.SetColLabelValue(col_idx, col_name)

        grid.SetRowLabelValue(0, "")



        for col_idx, col_name in enumerate(nutrients):
            value = str(food_item[col_name])
            grid.SetCellValue(0, col_idx, value)

        grid.AutoSizeColumns()
        self.Layout()
        grid.ForceRefresh()

    def clear_search_grid(self):
        grid = self.m_grid_search_result
        grid.ClearGrid()
        num_rows = grid.GetNumberRows()
        num_cols = grid.GetNumberCols()
        if num_rows > 0:
            grid.DeleteRows(0, num_rows, True)
        if num_cols > 0:
            grid.DeleteCols(0, num_cols, True)
        grid.Hide()
        self.Layout()
        grid.ForceRefresh()

    def on_frame_click(self, event):
        pos = event.GetPosition()
        if not self.m_searchCtrl_food_search.GetScreenRect().Contains(self.ScreenToClient(wx.GetMousePosition())) and \
           not self.m_listBox_food_search.GetScreenRect().Contains(self.ScreenToClient(wx.GetMousePosition())):
            self.m_listBox_food_search.Hide()
            self.Layout()
        event.Skip()

    def on_text_or_list_click(self, event):
        if self.m_searchCtrl_food_search.GetValue() and not self.m_listBox_food_search.IsShown():
            self.m_listBox_food_search.Show()
            self.Layout()
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()