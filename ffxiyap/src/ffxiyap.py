#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.2 on Mon Jan 21 20:28:55 2008

import wx
import ffxiparser as parser
import sys
from wx.lib.wordwrap import wordwrap

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.filemenu = wx.Menu()
        self.exportparse = wx.MenuItem(self.filemenu, 2, "Export Parse", "Export Current Parse", wx.ITEM_NORMAL)
        self.filemenu.AppendItem(self.exportparse)
        self.options = wx.MenuItem(self.filemenu,4,"Options","Log Location, Columns",wx.ITEM_NORMAL)
        self.filemenu.AppendItem(self.options)
        self.quit = wx.MenuItem(self.filemenu, 3, "Quit", "Quit YAP", wx.ITEM_NORMAL)
        self.filemenu.AppendItem(self.quit)
        self.frame_1_menubar.Append(self.filemenu, "File")
        self.helpmenu = wx.Menu()
        self.aboutmenu = wx.MenuItem(self.helpmenu, 5, "About", "About YAP", wx.ITEM_NORMAL)
        self.helpmenu.AppendItem(self.aboutmenu)
        self.frame_1_menubar.Append(self.helpmenu, "Help")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar()
        self.list_ctrl_1 = wx.ListCtrl(self.panel_1, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.button_1 = wx.Button(self.panel_1, -1, "Start Parse")
        self.button_2 = wx.Button(self.panel_1, -1, "Stop Parse")
        self.Bind(wx.EVT_BUTTON,self.Onb1,self.button_1)
        self.Bind(wx.EVT_BUTTON,self.Onb2,self.button_2)
        self.Bind(wx.EVT_MENU,self.OnQuit,self.quit)
        self.Bind(wx.EVT_MENU,self.OnAbout,self.aboutmenu)
        self.Bind(wx.EVT_MENU, self.OnOptions, self.options)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.columns = ['Player','Acc %','TTL Dmg','% of TTL Dmg',
                       'WS High','TTL WS Dmg','Crits','Crit %',
                       'Evades','Evade %',
                       'TTL Rng Dmg','Rng Acc %','TTL Spell Dmg',
                       'MB High','Addtl.Effect Dmg'
                       ]
        y = 0
        for x in self.columns:
            self.list_ctrl_1.InsertColumn(y,x,width=85)
            y = y + 1
        
        self.PathToLogs = PathToLogs
        self.frame_1_statusbar.SetStatusText('Ready')
        self.t = wx.CallLater(5000,self.OnTimer)
        self.t.Stop()
        self.button_2.Disable()
        
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("YAP: Final Fantasy XI Parser")
        self.list_ctrl_1.SetMinSize((600,300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.button_2, 0, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade
        
    def OnTimer(self):
        self.p.ParseLog()
        self.frame_1_statusbar.SetStatusText(self.p.GetCurrentLog())
        self.Update(self.p.GetValues(),self.p.GetCurrentLog())
        self.t.Restart(5000)
        
    def Onb2(self,evt):
        self.t.Stop()
        self.button_1.Enable()
        self.button_2.Disable()
        self.frame_1_statusbar.SetStatusText('Finished')
        
    def Onb1(self,evt):
        self.button_1.Disable()
        self.button_2.Enable()
        self.p = parser.Parser(self.PathToLogs)
        self.p.GetCurrentLine()
        self.OnTimer()
    
    def OnAbout(self,evt):
        info = wx.AboutDialogInfo()
        licenseText = """Copyright (c) 2008 Penguinwired Heavy Industries, James West

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE."""
        info.Name = "YAP: Yet Another Parser"
        info.Version = "0.2b"
        info.Copyright = "� 2008 Peguinwired Heavy Industries"
        info.WebSite = ("http://www.penguinwired.org/","penguinwired.org")
        info.Developers = ["James West"]
        info.Licence = wordwrap(licenseText,500,wx.ClientDC(self))
        wx.AboutBox(info)
        
    def OnQuit(self,evt):
        self.Close()    
    def OnOptions(self,evt):
        optionsframe = OptionsFrame(None, -1, "", self)   
    def Update(self,Players,CurrentLog):
        alldmg = 0
        self.list_ctrl_1.ClearAll()
        self.frame_1_statusbar.SetStatusText(CurrentLog)
        y = 0
        for x in self.columns:
            self.list_ctrl_1.InsertColumn(y,x,width=85)
            y = y + 1
        for name in Players:
            obj = Players[name]
            alldmg = obj.GetValue("ttldmg") + alldmg
            
        for name in Players:
            stats = self.CalculateValues(Players, name, alldmg)
            obj = Players[name]
            index = self.list_ctrl_1.InsertStringItem(sys.maxint,obj.GetValue("name"))
            y = 1
            for x in stats:
                self.list_ctrl_1.SetStringItem(index,y,str(x))
                y = y + 1
                
    def CalculateValues(self,Players,name,alldmg):
        obj = Players[name]
        try:
            accpnt = (float(obj.GetValue("hits")) / float(obj.GetValue("swings"))) * 100
            print obj.GetValue("hits"), obj.GetValue("swings")
            print accpnt
        except ZeroDivisionError:
            accpnt = 0
        try:
            pntofttldmg = (float(obj.GetValue("ttldmg")) / float(alldmg)) * 100
        except ZeroDivisionError:
            pntofttldmg = 0
        try:
            critpnt = (float(obj.GetValue("crit_count")) / float(obj.GetValue("hits"))) * 100
        except ZeroDivisionError:
            critpnt = 0
        try:
            racc = (float(obj.GetValue("rngmisses")) / float(obj.GetValue("rngattks"))) * 100
        except ZeroDivisionError:
            racc = 0            
        try:
            evapcnt = (float(obj.GetValue("evades")) / float(obj.GetValue("mobswings"))) * 100
        except ZeroDivisionError:
            evapcnt = 0
        
        stats = [accpnt,obj.GetValue("ttldmg"),pntofttldmg,obj.GetValue("ws_high"),
                 obj.GetValue("wsdmg"),obj.GetValue("crit_count"),critpnt,obj.GetValue("evades"),
                 evapcnt,obj.GetValue("rngdmg"),racc,obj.GetValue("ttlspelldmg"),
                 obj.GetValue("mb_high"),obj.GetValue("addeffectdmg")
                 ]
        
        print stats
        return stats
    def SetPathToLogs(self,NewLogPath):
        self.PathToLogs = NewLogPath           
# end of class MyFrame

class OptionsFrame(wx.Frame):
    def __init__(self,parent,id,title,caller):
        # begin wxGlade: MyFrame.__init__
        #kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self,parent,id,title,style=wx.DEFAULT_FRAME_STYLE)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.label_1 = wx.StaticText(self.notebook_1_pane_1, -1, "Log File Location:")
        self.txtLogFileLocation = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.button_7 = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.button_8 = wx.Button(self.notebook_1_pane_1, -1, "OK")
        self.button_9 = wx.Button(self.notebook_1_pane_1, -1, "Cancel")
        self.checkAccpnt = wx.CheckBox(self.notebook_1_pane_2, -1, "Acc %")
        self.checkPnctTTLDmg = wx.CheckBox(self.notebook_1_pane_2, -1, "% of TTL Dmg")
        self.checkTTLwsdmg = wx.CheckBox(self.notebook_1_pane_2, -1, "TTL WS Dmg")
        self.checkTTLDmg = wx.CheckBox(self.notebook_1_pane_2, -1, "TTL Dmg")
        self.checkws_high = wx.CheckBox(self.notebook_1_pane_2, -1, "WS High")
        self.checkCrit_count = wx.CheckBox(self.notebook_1_pane_2, -1, "Crits")
        self.checkCritPnct = wx.CheckBox(self.notebook_1_pane_2, -1, "Crit %")
        self.checkEvades = wx.CheckBox(self.notebook_1_pane_2, -1, "Evades")
        self.checkEvadePnct = wx.CheckBox(self.notebook_1_pane_2, -1, "Evade %")
        self.checkTTLRngDmg = wx.CheckBox(self.notebook_1_pane_2, -1, "TTL Rng Dmg")
        self.checkRngAccPcnt = wx.CheckBox(self.notebook_1_pane_2, -1, "Rng Acc %")
        self.checkTTLSpellDmg = wx.CheckBox(self.notebook_1_pane_2, -1, "TTL Spell Dmg")
        self.checkMB_High = wx.CheckBox(self.notebook_1_pane_2, -1, "MB High")
        self.checkAddEffect = wx.CheckBox(self.notebook_1_pane_2, -1, "Addtl. Effect Dmg")
        self.button_2 = wx.Button(self.notebook_1_pane_2, -1, "OK")
        self.button_3 = wx.Button(self.notebook_1_pane_2, -1, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.button_9)
        self.Bind(wx.EVT_BUTTON, self.OnOK, self.button_8)
        self.Bind(wx.EVT_BUTTON, self.OnOK, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.OnBrowse, self.button_7)
        #self.txtLogFileLocation.SetValue(PathToLogs)
        self.caller = caller
        self.Show(True)
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("YAP: Options")
        self.SetSize((484, 329))
        self.txtLogFileLocation.SetMinSize((175, 20))
        self.notebook_1_pane_1.SetMinSize((468, 264))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(6, 3, 5, 5)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add((20, 60), 0, 0, 0)
        sizer_7.Add(self.label_1, 0, wx.LEFT, 30)
        sizer_7.Add(self.txtLogFileLocation, 0, wx.LEFT, 5)
        sizer_7.Add(self.button_7, 0, wx.LEFT, 5)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add((314, 20), 0, 0, 0)
        sizer_8.Add(self.button_8, 0, wx.BOTTOM|wx.ALIGN_BOTTOM, 4)
        sizer_8.Add(self.button_9, 0, wx.BOTTOM|wx.ALIGN_BOTTOM, 4)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_6)
        grid_sizer_1.Add(self.checkAccpnt, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkPnctTTLDmg, 0, wx.TOP, 15)
        grid_sizer_1.Add(self.checkTTLwsdmg, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkTTLDmg, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkws_high, 0, wx.TOP, 15)
        grid_sizer_1.Add(self.checkCrit_count, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkCritPnct, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkEvades, 0, wx.TOP, 15)
        grid_sizer_1.Add(self.checkEvadePnct, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkTTLRngDmg, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkRngAccPcnt, 0, wx.TOP, 15)
        grid_sizer_1.Add(self.checkTTLSpellDmg, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkMB_High, 0, wx.LEFT|wx.TOP, 15)
        grid_sizer_1.Add(self.checkAddEffect, 0, wx.TOP, 15)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        sizer_3.Add(self.button_2, 0, wx.ALIGN_BOTTOM, 0)
        sizer_3.Add(self.button_3, 0, wx.RIGHT|wx.ALIGN_BOTTOM, 10)
        grid_sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(grid_sizer_1)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Log Files")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Columns")
        sizer_2.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade
    def OnQuit(self,evt):
        self.Close()       
        
    """TODO: Save options and quit"""
    def OnOK(self,evt):
        self.caller.SetPathToLogs(self.PathToLogs)
        self.Close()
        
    def OnBrowse(self,evt):
        # In this case we include a "New directory" button. 
        dlg = wx.DirDialog(self, "Choose a directory:",
                          style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.PathToLogs = dlg.GetPath()
            self.txtLogFileLocation.SetValue(self.PathToLogs)
        dlg.Destroy()
    
PathToLogs = "E:\\Program Files\\PlayOnline\\SquareEnix\\FINAL FANTASY XI\\TEMP"
ConsoleMode = False

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
