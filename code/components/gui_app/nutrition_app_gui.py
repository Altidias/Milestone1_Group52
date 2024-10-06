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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutrition App"), pos = wx.DefaultPosition, size = wx.Size( 489,551 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        self.m_bmToggleBtn_filter_panel = wx.BitmapToggleButton( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"bitmaps/Filter.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_bmToggleBtn_filter_panel.SetBitmap( wx.Bitmap( u"bitmaps/Filter.png", wx.BITMAP_TYPE_ANY ) )
        bSizer16.Add( self.m_bmToggleBtn_filter_panel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button_tracker = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"Tracker"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_button_tracker, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        sbSizer5.Add( bSizer16, 1, 0, 5 )


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


        bSizer6.Add( bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutrition App - Search Results"), pos = wx.DefaultPosition, size = wx.Size( 1112,555 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( 1112,555 ) )

        sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        wSizer5 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_bpButton_back = wx.BitmapButton( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.m_bpButton_back.SetBitmap( wx.Bitmap( u"bitmaps/back_arrow.png", wx.BITMAP_TYPE_ANY ) )
        wSizer5.Add( self.m_bpButton_back, 0, wx.ALL, 5 )

        self.m_toggleBtn_pie_chart = wx.ToggleButton( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Pie"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer5.Add( self.m_toggleBtn_pie_chart, 0, wx.ALL, 5 )

        self.m_toggleBtn_bar_chart = wx.ToggleButton( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Bar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer5.Add( self.m_toggleBtn_bar_chart, 0, wx.ALL, 5 )

        self.m_button_macro = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Macro"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer5.Add( self.m_button_macro, 0, wx.ALL, 5 )

        self.m_button_micro = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"Micro"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer5.Add( self.m_button_micro, 0, wx.ALL, 5 )


        sbSizer7.Add( wSizer5, 1, 0, 5 )

        self.m_panel_bar_pie_chart = wx.Panel( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel_bar_pie_chart.SetMinSize( wx.Size( 800,500 ) )

        sbSizer7.Add( self.m_panel_bar_pie_chart, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid_result = wx.grid.Grid( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

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
        self.m_grid_result.SetMaxSize( wx.Size( 500,-1 ) )

        bSizer22.Add( self.m_grid_result, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        sbSizer7.Add( bSizer22, 1, wx.EXPAND, 5 )


        self.SetSizer( sbSizer7 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class tracker_frame
###########################################################################

class tracker_frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutrient Tracker"), pos = wx.DefaultPosition, size = wx.Size( 720,442 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_tracker = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bpButton_back = wx.BitmapButton( self.m_panel_tracker, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.m_bpButton_back.SetBitmap( wx.Bitmap( u"bitmaps/back_arrow.png", wx.BITMAP_TYPE_ANY ) )
        bSizer37.Add( self.m_bpButton_back, 0, wx.ALL, 5 )

        self.m_panel_nutrient_list = wx.Panel( self.m_panel_tracker, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        m_listBox_nutrientsChoices = []
        self.m_listBox_nutrients = wx.ListBox( self.m_panel_nutrient_list, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_nutrientsChoices, 0 )
        bSizer20.Add( self.m_listBox_nutrients, 0, wx.ALL|wx.EXPAND, 5 )


        self.m_panel_nutrient_list.SetSizer( bSizer20 )
        self.m_panel_nutrient_list.Layout()
        bSizer20.Fit( self.m_panel_nutrient_list )
        bSizer37.Add( self.m_panel_nutrient_list, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer111 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_goal = wx.StaticText( self.m_panel_tracker, wx.ID_ANY, _(u"Nutrient Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_goal.Wrap( -1 )

        bSizer111.Add( self.m_staticText_goal, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_spinCtrlDouble_nutrient_amount = wx.SpinCtrlDouble( self.m_panel_tracker, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0, 1 )
        self.m_spinCtrlDouble_nutrient_amount.SetDigits( 0 )
        bSizer111.Add( self.m_spinCtrlDouble_nutrient_amount, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.m_button_update_nutrient = wx.Button( self.m_panel_tracker, wx.ID_ANY, _(u"Update"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer111.Add( self.m_button_update_nutrient, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer6.Add( bSizer111, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel_tracker, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

        self.m_searchCtrl_food_search_intake = wx.SearchCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_CENTER )
        self.m_searchCtrl_food_search_intake.ShowSearchButton( True )
        self.m_searchCtrl_food_search_intake.ShowCancelButton( True )
        self.m_searchCtrl_food_search_intake.SetMinSize( wx.Size( 300,-1 ) )
        self.m_searchCtrl_food_search_intake.SetMaxSize( wx.Size( 300,-1 ) )

        sbSizer1.Add( self.m_searchCtrl_food_search_intake, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        m_listBox_food_search_intakeChoices = []
        self.m_listBox_food_search_intake = wx.ListBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_food_search_intakeChoices, 0 )
        self.m_listBox_food_search_intake.SetMinSize( wx.Size( 300,100 ) )
        self.m_listBox_food_search_intake.SetMaxSize( wx.Size( 300,-1 ) )

        sbSizer1.Add( self.m_listBox_food_search_intake, 0, wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.RIGHT, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_update_intake = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Update"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_button_update_intake, 0, wx.ALL, 5 )

        self.m_spinCtrlDouble_servings = wx.SpinCtrlDouble( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
        self.m_spinCtrlDouble_servings.SetDigits( 0 )
        bSizer17.Add( self.m_spinCtrlDouble_servings, 0, wx.ALL, 5 )

        self.m_staticText_intake = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"Servings"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_intake.Wrap( -1 )

        bSizer17.Add( self.m_staticText_intake, 0, wx.ALL, 5 )


        sbSizer1.Add( bSizer17, 1, wx.EXPAND, 5 )


        bSizer13.Add( sbSizer1, 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer13, 1, 0, 5 )


        bSizer37.Add( bSizer6, 1, wx.EXPAND, 5 )

        self.m_button_generate_report = wx.Button( self.m_panel_tracker, wx.ID_ANY, _(u"Generate Report"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer37.Add( self.m_button_generate_report, 0, wx.ALL, 5 )


        self.m_panel_tracker.SetSizer( bSizer37 )
        self.m_panel_tracker.Layout()
        bSizer37.Fit( self.m_panel_tracker )
        bSizer11.Add( self.m_panel_tracker, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


