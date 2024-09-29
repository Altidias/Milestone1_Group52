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

        self.m_listBox2.Hide()

        self.m_textCtrl4.Bind(wx.EVT_TEXT, self.on_text_input)

        self.m_listBox2.Bind(wx.EVT_LISTBOX, self.on_listbox_select)

        self.m_button3.Bind(wx.EVT_BUTTON, self.on_button_click)

        self.Bind(wx.EVT_LEFT_DOWN, self.on_frame_click)

        self.m_textCtrl4.Bind(wx.EVT_LEFT_DOWN, self.on_text_or_list_click)
        self.m_listBox2.Bind(wx.EVT_LEFT_DOWN, self.on_text_or_list_click)

        self.is_typing = True

        self.setup_grid()

        self.Show()

    def setup_grid(self):
        self.m_grid3.ClearGrid()

        columns = [col for col in self.search_handler.database_df.columns if col != 'food']

        self.m_grid3.DeleteCols(0, self.m_grid3.GetNumberCols())
        self.m_grid3.AppendCols(len(columns))
        for i, column in enumerate(columns):
            self.m_grid3.SetColLabelValue(i, column)

        self.m_grid3.SetRowLabelSize(0)

        self.m_grid3.AutoSizeColumns()

    def on_text_input(self, event):
        if not self.is_typing:
            return

        query = self.m_textCtrl4.GetValue()
        if query:
            matches = self.get_similar_items(query)
            if not matches.empty:
                self.update_list(matches['food'].tolist())
                self.m_listBox2.Show()
            else:
                self.m_listBox2.Hide()
        else:
            self.m_listBox2.Hide()

        self.Layout()

    def get_similar_items(self, query):
        return self.search_handler.search_food(query)

    def update_list(self, matches):
        self.m_listBox2.Clear()
        self.m_listBox2.Append(matches)

    def on_listbox_select(self, event):
        selected_item = self.m_listBox2.GetString(self.m_listBox2.GetSelection())
        self.is_typing = False

        self.m_textCtrl4.SetValue(selected_item)

        self.is_typing = True

    def on_button_click(self, event):
        selected_food = self.m_textCtrl4.GetValue()
        food_item = self.search_handler.get_food_item(selected_food)
        if food_item is not None:
            self.update_grid(food_item)
        else:
            wx.MessageBox(f"No information found for '{selected_food}'", "Food Not Found", wx.OK | wx.ICON_WARNING)

    def update_grid(self, food_item):
        self.m_grid3.DeleteRows(0, self.m_grid3.GetNumberRows())
        self.m_grid3.AppendRows(1)

        col = 0
        for nutrient, value in food_item.items():
            if nutrient != 'food':
                self.m_grid3.SetCellValue(0, col, str(value))
                col += 1

        self.m_grid3.AutoSizeRows()

    def on_frame_click(self, event):
        pos = event.GetPosition()

        if not self.m_textCtrl4.GetScreenRect().Contains(self.ScreenToClient(wx.GetMousePosition())) and \
           not self.m_listBox2.GetScreenRect().Contains(self.ScreenToClient(wx.GetMousePosition())):
            self.m_listBox2.Hide()
            self.Layout()
        
        event.Skip()

    def on_text_or_list_click(self, event):
        if self.m_textCtrl4.GetValue() and not self.m_listBox2.IsShown():
            self.m_listBox2.Show()
            self.Layout()
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
