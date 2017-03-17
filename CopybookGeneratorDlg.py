#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade f172c83ff51d+ on Fri Mar 17 08:33:21 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from wx import InfoBar
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.combo_box_mode = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.text_ctrl_page_width = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_page_height = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_margin_x = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_margin_y = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_width = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_height = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_space_x = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_space_y = wx.TextCtrl(self, wx.ID_ANY, "")
        self.combo_box_font = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.combo_box_grid_type = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.checkbox_pinyin = wx.CheckBox(self, wx.ID_ANY, _(u"\u8f93\u51fa\u62fc\u97f3"))
        self.text_ctrl_pages_limit = wx.TextCtrl(self, wx.ID_ANY, _("0"))
        self.text_ctrl_input = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_select_input = wx.Button(self, wx.ID_ANY, _("..."))
        self.text_ctrl_output = wx.TextCtrl(self, wx.ID_ANY, "")
        self.checkbox_keep_tempfiles = wx.CheckBox(self, wx.ID_ANY, _(u"\u4fdd\u7559\u4e2d\u95f4\u6587\u4ef6"))
        self.bar_info = InfoBar(self, wx.ID_ANY)
        self.button_2 = wx.Button(self, wx.ID_ANY, _(u"\u751f\u6210"))
        self.button_1 = wx.Button(self, wx.ID_ANY, _(u"\u5173\u4e8e"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnSelectPreMode, self.combo_box_mode)
        self.Bind(wx.EVT_TEXT, self.OnInputText, self.text_ctrl_input)
        self.Bind(wx.EVT_BUTTON, self.OnSelectInput, self.button_select_input)
        self.Bind(wx.EVT_BUTTON, self.OnGenerate, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.OnAbout, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_(u"\u5b57\u5e16\u751f\u6210\u5668"))
        self.combo_box_mode.SetMinSize((300, -1))
        self.text_ctrl_input.SetMinSize((500, -1))
        self.button_select_input.SetMinSize((40, 40))
        self.text_ctrl_output.SetMinSize((500, -1))
        self.text_ctrl_output.Enable(False)
        self.button_2.SetMinSize((120, -1))
        self.button_2.SetDefault()
        self.button_1.SetMinSize((120, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_3.Add((20, 20), 0, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, _(u"\u9884\u8bbe\u6a21\u5f0f\uff1a"))
        sizer_11.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(self.combo_box_mode, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 10), 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, _(u"\u9875\u9762\u5bbd\uff1a"))
        sizer_8.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(self.text_ctrl_page_width, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_8.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add((10, 20), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _(u"\u9875\u9762\u9ad8\uff1a"))
        sizer_8.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(self.text_ctrl_page_height, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_8.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add((10, 20), 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, _(u"\u6a2a\u8fb9\u8ddd\uff1a"))
        sizer_8.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(self.text_ctrl_margin_x, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_8.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add((10, 20), 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, _(u"\u7eb5\u8fb9\u8ddd\uff1a"))
        sizer_8.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(self.text_ctrl_margin_y, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_8.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add((0, 0), 0, 0, 0)
        sizer_8.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_8, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 10), 0, 0, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, _(u"\u5b57\u4f53\u5bbd\uff1a"))
        sizer_9.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_width, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_9.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add((10, 20), 0, 0, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, _(u"\u5b57\u4f53\u9ad8\uff1a"))
        sizer_9.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_height, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_13 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_9.Add(label_13, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add((10, 20), 0, 0, 0)
        label_14 = wx.StaticText(self, wx.ID_ANY, _(u"\u6a2a\u95f4\u8ddd\uff1a"))
        sizer_9.Add(label_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_space_x, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_15 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_9.Add(label_15, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add((10, 20), 0, 0, 0)
        label_16 = wx.StaticText(self, wx.ID_ANY, _(u"\u7eb5\u95f4\u8ddd\uff1a"))
        sizer_9.Add(label_16, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_space_y, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_17 = wx.StaticText(self, wx.ID_ANY, _("cm"))
        sizer_9.Add(label_17, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 10), 0, 0, 0)
        label_18 = wx.StaticText(self, wx.ID_ANY, _(u"\u5b57\u4f53\uff1a"))
        sizer_10.Add(label_18, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(self.combo_box_font, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add((20, 20), 0, 0, 0)
        label_19 = wx.StaticText(self, wx.ID_ANY, _(u"\u6846\u7c7b\u578b\uff1a"))
        sizer_10.Add(label_19, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(self.combo_box_grid_type, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add((20, 20), 0, 0, 0)
        sizer_10.Add(self.checkbox_pinyin, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_10, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 10), 0, 0, 0)
        label_22 = wx.StaticText(self, wx.ID_ANY, _(u"\u9875\u6570\u9650\u5236\uff1a"))
        sizer_13.Add(label_22, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13.Add(self.text_ctrl_pages_limit, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13.Add((0, 0), 0, 0, 0)
        sizer_13.Add((0, 0), 0, 0, 0)
        sizer_13.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_13, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        label_20 = wx.StaticText(self, wx.ID_ANY, _(u"\u8f93\u5165\u6587\u4ef6\uff1a"))
        sizer_7.Add(label_20, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.text_ctrl_input, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add((5, 20), 0, 0, 0)
        sizer_7.Add(self.button_select_input, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_7, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 10), 0, 0, 0)
        label_21 = wx.StaticText(self, wx.ID_ANY, _(u"\u8f93\u51fa\u6587\u4ef6\uff1a"))
        sizer_12.Add(label_21, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add(self.text_ctrl_output, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add((10, 20), 0, 0, 0)
        sizer_12.Add(self.checkbox_keep_tempfiles, 0, 0, 0)
        sizer_12.Add((0, 0), 0, 0, 0)
        sizer_6.Add(sizer_12, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_6.Add(self.bar_info, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_4.Add((20, 357), 0, 0, 0)
        sizer_5.Add(self.button_2, 2, 0, 0)
        sizer_5.Add((20, 20), 0, 0, 0)
        sizer_5.Add(self.button_1, 1, 0, 0)
        sizer_4.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_3.Add((20, 20), 0, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnSelectPreMode(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnSelectPreMode' not implemented!")
        event.Skip()

    def OnInputText(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnInputText' not implemented!")
        event.Skip()

    def OnSelectInput(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnSelectInput' not implemented!")
        event.Skip()

    def OnGenerate(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnGenerate' not implemented!")
        event.Skip()

    def OnAbout(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'OnAbout' not implemented!")
        event.Skip()

# end of class MyFrame
