# -*- coding: utf-8 -*-

import wx
import wx.xrc

try:
    del app
except:
    pass

class get_rate_of_return ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"投資報酬率計算", pos = wx.DefaultPosition, size = wx.Size( 330,345 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		self.title_earns = wx.StaticText( self, wx.ID_ANY, u"總獲利", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_earns.Wrap( -1 )

		bSizer.Add( self.title_earns, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.total_earn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.total_earn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tital_cost = wx.StaticText( self, wx.ID_ANY, u"總成本", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tital_cost.Wrap( -1 )

		bSizer.Add( self.tital_cost, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.total_cost = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.total_cost, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tital_years = wx.StaticText( self, wx.ID_ANY, u"年數", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tital_years.Wrap( -1 )

		bSizer.Add( self.tital_years, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.total_years = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer.Add( self.total_years, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.cal_button = wx.Button( self, wx.ID_ANY, u"計算", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Bind(wx.EVT_BUTTON, self.operation_Digital,self.cal_button)
		bSizer.Add( self.cal_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.rate_of_return = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.rate_of_return.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer.Add( self.rate_of_return, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def operation_Digital( self , event):
		earns = self.total_earn.GetValue()
		costs = self.total_cost.GetValue()
		years = self.total_years.GetValue()
		if earns.isdigit() and costs.isdigit() and years.isdigit():
			result = int(earns) / int(costs) / int(years) * 100
			self.rate_of_return.SetValue(str(result)+'%')

                
if __name__ == '__main__':
    app = wx.App()
    frm = get_rate_of_return(None)
    frm.Show()
    app.MainLoop()
