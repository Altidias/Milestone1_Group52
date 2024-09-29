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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 969,676 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Search Food:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer2.Add( self.m_staticText3, 0, wx.LEFT|wx.TOP, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl4.SetMinSize( wx.Size( 300,-1 ) )
        self.m_textCtrl4.SetMaxSize( wx.Size( 300,-1 ) )

        bSizer7.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
        self.m_listBox2.SetMinSize( wx.Size( 300,-1 ) )
        self.m_listBox2.SetMaxSize( wx.Size( 300,-1 ) )

        bSizer7.Add( self.m_listBox2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 5 )


        fgSizer2.Add( bSizer7, 1, 0, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer2.Add( self.m_button3, 0, wx.ALIGN_LEFT, 5 )


        bSizer1.Add( fgSizer2, 1, 0, 5 )

        self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid3.CreateGrid( 1, 34 )
        self.m_grid3.EnableEditing( False )
        self.m_grid3.EnableGridLines( True )
        self.m_grid3.EnableDragGridSize( False )
        self.m_grid3.SetMargins( 0, 0 )

        # Columns
        self.m_grid3.EnableDragColMove( False )
        self.m_grid3.EnableDragColSize( True )
        self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid3.AutoSizeRows()
        self.m_grid3.EnableDragRowSize( True )
        self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.m_grid3.SetMinSize( wx.Size( 450,75 ) )

        bSizer1.Add( self.m_grid3, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


