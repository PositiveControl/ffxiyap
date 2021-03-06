#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.2 on Tue Jan 22 16:53:04 2008

import wx

# begin wxGlade: extracode
# end wxGlade



class OptionsFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
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
        return self.PathToLogs
    def OnBrowse(self,evt):
        # In this case we include a "New directory" button. 
        dlg = wx.DirDialog(self, "Choose a directory:",
                          style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        self.PathToLogs = dlg.GetPath()
        dlg.Destroy()
    
# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = OptionsFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
