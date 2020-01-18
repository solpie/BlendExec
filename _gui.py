# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWin
###########################################################################

class MainWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer3.SetMinSize( wx.Size( 800,500 ) )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer4 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Reload", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button4, 0, wx.ALL, 5 )


		fgSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )

		m_listBox_bpyChoices = []
		self.m_listBox_bpy = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_bpyChoices, 0 )
		self.m_listBox_bpy.SetMinSize( wx.Size( 180,500 ) )

		fgSizer4.Add( self.m_listBox_bpy, 0, wx.ALL, 5 )


		bSizer5.Add( fgSizer4, 1, wx.EXPAND, 5 )


		fgSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer11.SetMinSize( wx.Size( 500,500 ) )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		m_choice_hwndChoices = []
		self.m_choice_hwnd = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_hwndChoices, 0 )
		self.m_choice_hwnd.SetSelection( 0 )
		self.m_choice_hwnd.SetMinSize( wx.Size( 500,-1 ) )

		bSizer10.Add( self.m_choice_hwnd, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_listbook2 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_RIGHT )
		self.m_listbook2.SetMinSize( wx.Size( -1,500 ) )

		self.m_panel4 = wx.Panel( self.m_listbook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook2.AddPage( self.m_panel4, u"head", True )
		self.m_panel5 = wx.Panel( self.m_listbook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_radioBtn1 = wx.RadioButton( self.m_panel5, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_radioBtn1, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer9 )
		self.m_panel5.Layout()
		bSizer9.Fit( self.m_panel5 )
		self.m_listbook2.AddPage( self.m_panel5, u"hand", False )

		bSizer11.Add( self.m_listbook2, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_listBox_bpy.Bind( wx.EVT_LISTBOX_DCLICK, self.on_list_DClick )
		self.m_choice_hwnd.Bind( wx.EVT_CHOICE, self.on_choice_hwnd )
		self.m_button3.Bind( wx.EVT_BUTTON, self.on_refresh_hwnd )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_list_DClick( self, event ):
		event.Skip()

	def on_choice_hwnd( self, event ):
		event.Skip()

	def on_refresh_hwnd( self, event ):
		event.Skip()


