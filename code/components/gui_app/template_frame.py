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
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 489,551 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.Size( 489,551 ) )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_search_controls = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_search_controls, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_searchCtrl_food_search = wx.SearchCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_CENTER )
        self.m_searchCtrl_food_search.ShowSearchButton( True )
        self.m_searchCtrl_food_search.ShowCancelButton( True )
        self.m_searchCtrl_food_search.SetMinSize( wx.Size( 300,-1 ) )
        self.m_searchCtrl_food_search.SetMaxSize( wx.Size( 300,-1 ) )

        sbSizer1.Add( self.m_searchCtrl_food_search, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        m_listBox_food_searchChoices = []
        self.m_listBox_food_search = wx.ListBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_food_searchChoices, 0 )
        self.m_listBox_food_search.SetMinSize( wx.Size( 300,100 ) )
        self.m_listBox_food_search.SetMaxSize( wx.Size( 300,-1 ) )

        sbSizer1.Add( self.m_listBox_food_search, 0, wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.RIGHT, 5 )


        sbSizer5.Add( sbSizer1, 1, wx.EXPAND, 5 )

        self.m_bmToggleBtn_filter_panel = wx.BitmapToggleButton( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"bitmaps/Filter.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_bmToggleBtn_filter_panel.SetBitmap( wx.Bitmap( u"bitmaps/Filter.png", wx.BITMAP_TYPE_ANY ) )
        sbSizer5.Add( self.m_bmToggleBtn_filter_panel, 0, wx.ALL, 5 )


        self.m_panel_search_controls.SetSizer( sbSizer5 )
        self.m_panel_search_controls.Layout()
        sbSizer5.Fit( self.m_panel_search_controls )
        bSizer19.Add( self.m_panel_search_controls, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_panel_filter_controls = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_filter_controls, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_nutrient_filter = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Nutrient"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_nutrient_filter.Wrap( -1 )

        bSizer11.Add( self.m_staticText_nutrient_filter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        m_listBox_nutrient_selectionChoices = []
        self.m_listBox_nutrient_selection = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_nutrient_selectionChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE )
        self.m_listBox_nutrient_selection.SetMinSize( wx.Size( 200,300 ) )

        bSizer11.Add( self.m_listBox_nutrient_selection, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer2.Add( bSizer11, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_toggleBtn_range_filter = wx.ToggleButton( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Range"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_toggleBtn_range_filter, 0, wx.ALL, 5 )

        self.m_toggleBtn_level_filter = wx.ToggleButton( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Level"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_toggleBtn_level_filter, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_panel_range_controls = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_range_min = wx.StaticText( self.m_panel_range_controls, wx.ID_ANY, _(u"Min"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_range_min.Wrap( -1 )

        bSizer9.Add( self.m_staticText_range_min, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_spinCtrlDouble_range_min = wx.SpinCtrlDouble( self.m_panel_range_controls, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0.000000, 1 )
        self.m_spinCtrlDouble_range_min.SetDigits( 0 )
        bSizer9.Add( self.m_spinCtrlDouble_range_min, 0, wx.ALL, 5 )


        gSizer2.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_range_max = wx.StaticText( self.m_panel_range_controls, wx.ID_ANY, _(u"Max"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_range_max.Wrap( -1 )

        bSizer10.Add( self.m_staticText_range_max, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_spinCtrlDouble_range_max = wx.SpinCtrlDouble( self.m_panel_range_controls, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
        self.m_spinCtrlDouble_range_max.SetDigits( 0 )
        bSizer10.Add( self.m_spinCtrlDouble_range_max, 0, wx.ALL, 5 )


        gSizer2.Add( bSizer10, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel_range_controls.SetSizer( gSizer2 )
        self.m_panel_range_controls.Layout()
        gSizer2.Fit( self.m_panel_range_controls )
        bSizer6.Add( self.m_panel_range_controls, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_panel_level_controls = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

        m_choice_filter_levelChoices = [ _(u"Low"), _(u"Mid"), _(u"High") ]
        self.m_choice_filter_level = wx.Choice( self.m_panel_level_controls, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_filter_levelChoices, 0 )
        self.m_choice_filter_level.SetSelection( 0 )
        gSizer1.Add( self.m_choice_filter_level, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.m_panel_level_controls.SetSizer( gSizer1 )
        self.m_panel_level_controls.Layout()
        gSizer1.Fit( self.m_panel_level_controls )
        bSizer6.Add( self.m_panel_level_controls, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button_filter_apply = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Apply"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button_filter_apply, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer2.Add( bSizer6, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


        self.m_panel_filter_controls.SetSizer( sbSizer2 )
        self.m_panel_filter_controls.Layout()
        sbSizer2.Fit( self.m_panel_filter_controls )
        bSizer19.Add( self.m_panel_filter_controls, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer19 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class result_frame
###########################################################################

class result_frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 566,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bpButton_back = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.m_bpButton_back.SetBitmap( wx.Bitmap( u"bitmaps/back_arrow.png", wx.BITMAP_TYPE_ANY ) )
        bSizer37.Add( self.m_bpButton_back, 0, wx.ALL, 5 )

        self.m_panel_pie_chart = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer37.Add( self.m_panel_pie_chart, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_grid_result = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_result.CreateGrid( 5, 2 )
        self.m_grid_result.EnableEditing( False )
        self.m_grid_result.EnableGridLines( True )
        self.m_grid_result.EnableDragGridSize( False )
        self.m_grid_result.SetMargins( 30, 0 )

        # Columns
        self.m_grid_result.AutoSizeColumns()
        self.m_grid_result.EnableDragColMove( False )
        self.m_grid_result.EnableDragColSize( False )
        self.m_grid_result.SetColLabelValue( 0, _(u"Nutrient") )
        self.m_grid_result.SetColLabelValue( 1, _(u"Value") )
        self.m_grid_result.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid_result.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_result.AutoSizeRows()
        self.m_grid_result.EnableDragRowSize( False )
        self.m_grid_result.SetRowLabelSize( 0 )
        self.m_grid_result.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_result.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer37.Add( self.m_grid_result, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer37 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


