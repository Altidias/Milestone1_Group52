# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1189,757 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        fgSizer3 = wx.FlexGridSizer( 0, 5, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.HORIZONTAL )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel_search = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_search, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        bSizer131 = wx.BoxSizer( wx.VERTICAL )

        self.m_searchCtrl_food_search = wx.SearchCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        self.m_searchCtrl_food_search.ShowSearchButton( True )
        self.m_searchCtrl_food_search.ShowCancelButton( True )
        self.m_searchCtrl_food_search.SetMinSize( wx.Size( 300,-1 ) )
        self.m_searchCtrl_food_search.SetMaxSize( wx.Size( 300,-1 ) )

        bSizer131.Add( self.m_searchCtrl_food_search, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        m_listBox_food_searchChoices = []
        self.m_listBox_food_search = wx.ListBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_food_searchChoices, 0 )
        self.m_listBox_food_search.SetMinSize( wx.Size( 300,100 ) )
        self.m_listBox_food_search.SetMaxSize( wx.Size( 300,100 ) )

        bSizer131.Add( self.m_listBox_food_search, 0, wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.RIGHT, 5 )


        sbSizer1.Add( bSizer131, 1, wx.FIXED_MINSIZE, 5 )

        self.m_button_enable_filtering = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Enable Filtering"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_button_enable_filtering, 0, wx.ALL, 5 )


        bSizer17.Add( sbSizer1, 1, 0, 5 )

        bSizer_search_results = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_search_result = wx.StaticText( self.m_panel_search, wx.ID_ANY, _(u"Food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_search_result.Wrap( -1 )

        bSizer_search_results.Add( self.m_staticText_search_result, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_grid_search_result = wx.grid.Grid( self.m_panel_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_search_result.CreateGrid( 1, 5 )
        self.m_grid_search_result.EnableEditing( False )
        self.m_grid_search_result.EnableGridLines( True )
        self.m_grid_search_result.EnableDragGridSize( False )
        self.m_grid_search_result.SetMargins( 0, 0 )

        # Columns
        self.m_grid_search_result.AutoSizeColumns()
        self.m_grid_search_result.EnableDragColMove( False )
        self.m_grid_search_result.EnableDragColSize( False )
        self.m_grid_search_result.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid_search_result.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_search_result.AutoSizeRows()
        self.m_grid_search_result.EnableDragRowSize( False )
        self.m_grid_search_result.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid_search_result.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_search_result.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.m_grid_search_result.SetMinSize( wx.Size( -1,75 ) )
        self.m_grid_search_result.SetMaxSize( wx.Size( -1,150 ) )

        bSizer_search_results.Add( self.m_grid_search_result, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer17.Add( bSizer_search_results, 1, wx.EXPAND, 5 )


        self.m_panel_search.SetSizer( bSizer17 )
        self.m_panel_search.Layout()
        bSizer17.Fit( self.m_panel_search )
        bSizer13.Add( self.m_panel_search, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        self.m_panel_filter = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_filter, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_nutrient_filter = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Nutrient"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_nutrient_filter.Wrap( -1 )

        bSizer11.Add( self.m_staticText_nutrient_filter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_choice_nutrient_filterChoices = []
        self.m_choice_nutrient_filter = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_nutrient_filterChoices, 0 )
        self.m_choice_nutrient_filter.SetSelection( 0 )
        bSizer11.Add( self.m_choice_nutrient_filter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        sbSizer2.Add( bSizer11, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox_level_filter = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_checkBox_level_filter, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_choice_filter_levelChoices = [ _(u"Low"), _(u"Mid"), _(u"High") ]
        self.m_choice_filter_level = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_filter_levelChoices, 0 )
        self.m_choice_filter_level.SetSelection( 0 )
        bSizer7.Add( self.m_choice_filter_level, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox_range_filter = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Range Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_checkBox_range_filter, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_range_min = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Min"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_range_min.Wrap( -1 )

        bSizer9.Add( self.m_staticText_range_min, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_spinCtrlDouble_range_min = wx.SpinCtrlDouble( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
        self.m_spinCtrlDouble_range_min.SetDigits( 0 )
        bSizer9.Add( self.m_spinCtrlDouble_range_min, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_range_max = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Max"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_range_max.Wrap( -1 )

        bSizer10.Add( self.m_staticText_range_max, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_spinCtrlDouble_range_max = wx.SpinCtrlDouble( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
        self.m_spinCtrlDouble_range_max.SetDigits( 0 )
        bSizer10.Add( self.m_spinCtrlDouble_range_max, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )


        sbSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

        self.m_button_enable_searching = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Enable Searching"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_button_enable_searching, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer19.Add( sbSizer2, 1, 0, 5 )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_filter_result = wx.StaticText( self.m_panel_filter, wx.ID_ANY, _(u"Nutrients"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_filter_result.Wrap( -1 )

        bSizer15.Add( self.m_staticText_filter_result, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_grid_filter_result = wx.grid.Grid( self.m_panel_filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_filter_result.CreateGrid( 1, 5 )
        self.m_grid_filter_result.EnableEditing( False )
        self.m_grid_filter_result.EnableGridLines( True )
        self.m_grid_filter_result.EnableDragGridSize( False )
        self.m_grid_filter_result.SetMargins( 0, 0 )

        # Columns
        self.m_grid_filter_result.AutoSizeColumns()
        self.m_grid_filter_result.EnableDragColMove( False )
        self.m_grid_filter_result.EnableDragColSize( False )
        self.m_grid_filter_result.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid_filter_result.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_filter_result.AutoSizeRows()
        self.m_grid_filter_result.EnableDragRowSize( False )
        self.m_grid_filter_result.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid_filter_result.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_filter_result.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.m_grid_filter_result.SetMinSize( wx.Size( -1,75 ) )
        self.m_grid_filter_result.SetMaxSize( wx.Size( -1,150 ) )

        bSizer15.Add( self.m_grid_filter_result, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer19.Add( bSizer15, 1, wx.EXPAND, 5 )


        self.m_panel_filter.SetSizer( bSizer19 )
        self.m_panel_filter.Layout()
        bSizer19.Fit( self.m_panel_filter )
        bSizer13.Add( self.m_panel_filter, 1, wx.EXPAND |wx.ALL, 5 )


        fgSizer3.Add( bSizer13, 1, wx.EXPAND, 5 )


        bSizer1.Add( fgSizer3, 1, 0, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


