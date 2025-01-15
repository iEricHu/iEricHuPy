# EHWX.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import wx
import wx.xrc
import wx.grid
import os
import sys

# <PyCmt: EHUIForm Element:
#   FormName, Form TypeForm Number,
#   ObjName, ObjCaption, ObjType, ObjEvent,  \
#   DataInput: DataType, DataRange, ErrMsg, \
#   DataOutput: DBTableName; DBColName; DBSQL; \
#   Data Collect; DataOutput Counter DBTbl and DBCol  >

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHWX.py !')
# </PyDecl: RunTime>
class EHUIFormCreate(wx.Frame):
    c_lstObjChoiceFormType=['ERPTrade', 'UserForm']
    c_lstObjTypeChoices = [u'TextCtrl', u'ComboBox', u'Choice', u'CheckBox']
    c_lstGridCfgdObjTitleCol = [u'FormName', u'ObjName', 'objCaption', u'ObjList', u'SysEvt']

    c_intStaticTextMinWidth: int = 90
    c_intTextInputMinWidth: int =300
    c_intTabObjShrink: int = 12

    def __init__(
            self,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.RESIZE_BORDER,
            name=wx.EmptyString
    ):
        self.appWX = wx.App()
        self.m_panelFormPara = None
        self.m_staticTextFormType = None
        self.m_choiceFormType = None
        self.m_staticTextFormName = None
        self.m_textCtrlFormName = None
        self.m_panelObjPara = None
        self.m_staticTextObjName = None
        self.m_textCtrlObjName = None
        self.m_staticTextObjCaption = None
        self.m_textCtrlObjCaption = None
        self.m_staticTextObjType = None
        self.m_choiceObjType = None
        self.m_buttonObjAdd = None
        self.m_panelObjCfg = None
        self.m_notebookObjCfg = None
        self.m_panelObjCfgListPage = None
        self.m_staticTextObjText = None
        self.m_listBoxObjListChoices = None
        self.m_listBoxObjList = None
        self.m_textCtrlObjText = None
        self.m_buttonObjTextAdd = None
        self.m_buttonObjTextRemove = None
        self.m_panelObjEventPage = None
        self.m_panelObjCfgDBTblColPage = None
        self.m_choiceDBTblName = None
        self.m_staticTextObjDBColName = None
        self.m_choiceDBColName = None
        self.m_choiceDBColName = None
        self.m_panelObjCfgDBSQLPage = None
        self.m_panelObjCfgDBSQLPage = None
        self.m_textCtrlDBSQL = None
        self.m_textCtrlDBSQL = None
        self.m_buttonDBSQLPreview = None
        self.m_buttonDBSQLPreview = None
        self.m_panelObjCfgd = None
        self.m_notebookObjCfgd = None
        self.m_panelObjCfgdGridPage = None
        self.m_gridObjCfgd = None
        self.m_buttonGridCfgdItemRemove = None
        self.m_panelObjEvtCfgdGridPage = None
        self.m_gridObjEvtCfgd = None
        self.m_buttonGridEvtCfgdItemRemove = None
        self.m_panelObjBtnOKCancel = None

        super().__init__(
            parent=None,
            id=id,
            pos=pos,
            size=size,
            style=style,
            name=name
        )
        self.Bind(wx.EVT_CLOSE, self.fnClose)
        self.Bind(wx.EVT_CHAR_HOOK, self.fnOnCharHook)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # <PyCmt: EHUI Base BoxSizer>
        bSizerBaseEHUIObj = wx.BoxSizer(wx.VERTICAL)

        self.fnPanelFormPara(bSizerBaseEHUIObj)
        self.fnPanelObjPara(bSizerBaseEHUIObj)
        self.fnPanelObjCfg(bSizerBaseEHUIObj)
        self.fnPanelObjCfgd(bSizerBaseEHUIObj)
        self.fnPanelOKCancel(bSizerBaseEHUIObj)

        self.SetSizer(bSizerBaseEHUIObj)
        self.Layout()
        self.Centre(wx.BOTH)
        if c_blnEHDebugMode: print('EHUI.__init__ Done!')

    # <PyCmt: EHUIFormCrate Class SubFunc: fnPanelFormPara>
    def fnPanelFormPara(self, bSizerBaseEHUIObj):
        # <PyCmt: Form Parameter Panel>
        self.m_panelFormPara = \
            wx.Panel(
                parent=self,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelFormPara'
            )
        # <PyCmt: Form Parameter fgSizer>
        fgSizerFormPara = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerFormPara.SetFlexibleDirection(wx.BOTH)
        fgSizerFormPara.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # <PyCmt: FormType Label(wxStaticText)>
        self.m_staticTextFormType = \
            wx.StaticText(
                parent=self.m_panelFormPara,
                id=wx.ID_ANY,
                label=u'Form Type: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextFormType'
            )
        self.m_staticTextFormType.Wrap(-1)
        self.m_staticTextFormType.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth, wx.DefaultSize.height)
        )
        fgSizerFormPara.Add(window=self.m_staticTextFormType, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)

        # <PyCmt: FormType ListBox(wxChoice)>
        self.m_choiceFormType = \
            wx.Choice(
                parent=self.m_panelFormPara,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                choices=self.c_lstObjChoiceFormType,
                style=0,
                name='self.m_choiceFormType'
            )
        self.m_choiceFormType.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_choiceFormType.Bind(wx.EVT_CHOICE, self.fnEvtBtnObjAddEnable)
        self.m_choiceFormType.SetSelection(0)
        fgSizerFormPara.Add(self.m_choiceFormType, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: FormName Label(wxStaticText)>
        self.m_staticTextFormName = \
            wx.StaticText(
                parent=self.m_panelFormPara,
                id=wx.ID_ANY,
                label=u'Form Name: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextFormName'
            )
        self.m_staticTextFormName.Wrap(-1)
        self.m_staticTextFormName.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth, wx.DefaultSize.height)
        )
        fgSizerFormPara.Add(window=self.m_staticTextFormName, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)

        # <PyCmt: FormName InputBox(wxTextCtrl)>
        self.m_textCtrlFormName = \
            wx.TextCtrl(
                parent=self.m_panelFormPara,
                id=wx.ID_ANY,
                value=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_textCtrlFormName'
            )
        self.m_textCtrlFormName.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_textCtrlFormName.Bind(wx.EVT_TEXT, self.fnEvtBtnObjAddEnable)
        fgSizerFormPara.Add(window=self.m_textCtrlFormName, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        # <PyCmt: Form Parameter fgSizer Setup>
        self.m_panelFormPara.SetSizer(fgSizerFormPara)
        self.m_panelFormPara.Layout()
        fgSizerFormPara.Fit(self.m_panelFormPara)
        # <PyCmt: Form Parameter Panel Add Into bSizerBaseEHUIObj>
        bSizerBaseEHUIObj.Add(window=self.m_panelFormPara, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        # </PyCmt: Form Parameter Panel>
    # </PyCmt: EHUIFormCrate Class SubFunc: fnPanelFormPara>

    # <PyCmt: EHUIFormCrate Class SubFunc: fnPanelObjPara>
    def fnPanelObjPara(self, bSizerBaseEHUIObj):
        # <PyCmt: Object Parameter Panel>
        self.m_panelObjPara = \
            wx.Panel(
                parent=self,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjPara'
            )
        # <PyCmt: ObjPara FlexGrid Sizer>
        fgSizerObjPara = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerObjPara.SetFlexibleDirection(wx.BOTH)
        fgSizerObjPara.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # <PyCmt: objName Label(wxStaticText)>
        self.m_staticTextObjName = \
            wx.StaticText(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                label=u'Object Name: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextObjName'
            )
        self.m_staticTextObjName.Wrap(-1)
        self.m_staticTextObjName.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth, wx.DefaultSize.height)
        )
        fgSizerObjPara.Add(window=self.m_staticTextObjName, proportion=0, flag=wx.ALL, border=5)
        # <PyCmt: objName InputBox(wxTextCtrl)>
        self.m_textCtrlObjName = \
            wx.TextCtrl(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                value=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_textCtrlObjName'
            )
        self.m_textCtrlObjName.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_textCtrlObjName.Bind(wx.EVT_TEXT, self.fnEvtBtnObjAddEnable)
        fgSizerObjPara.Add(self.m_textCtrlObjName, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: objCaption Label(wxStaticText)>
        self.m_staticTextObjCaption = \
            wx.StaticText(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                label=u'Object Caption: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextObjCaption'
            )
        self.m_staticTextObjCaption.Wrap(-1)
        self.m_staticTextObjCaption.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth, wx.DefaultSize.height)
        )
        fgSizerObjPara.Add(window=self.m_staticTextObjCaption, proportion=0, flag=wx.ALL, border=5)
        # <PyCmt: objCaption InputBox(wxTextCtrl)>
        self.m_textCtrlObjCaption = \
            wx.TextCtrl(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                value=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_textCtrlObjCaption'
            )
        self.m_textCtrlObjCaption.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_textCtrlObjCaption.Bind(wx.EVT_TEXT, self.fnEvtBtnObjAddEnable)
        fgSizerObjPara.Add(self.m_textCtrlObjCaption, 0, wx.ALL | wx.EXPAND, 5)
        # <PyCmt: objType Label(wxStaticText)>
        self.m_staticTextObjType = \
            wx.StaticText(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                label=u'Object Type: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextObjType'
            )
        self.m_staticTextObjType.Wrap(-1)
        self.m_staticTextObjType.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth, wx.DefaultSize.height)
        )
        fgSizerObjPara.Add(self.m_staticTextObjType, 0, wx.ALL, 5)
        # <PyCmt: objType ListBox(wxChoice)>
        self.m_choiceObjType = \
            wx.Choice(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                choices=self.c_lstObjTypeChoices,
                style=0,
                name='self.m_choiceObjType'
            )
        self.m_choiceObjType.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_choiceObjType.Bind(wx.EVT_CHOICE, self.fnEvtBtnObjAddEnable)
        self.m_choiceObjType.SetSelection(0)
        fgSizerObjPara.Add(self.m_choiceObjType, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: before ObjAddBtn Add Spacer >
        fgSizerObjPara.Add(size=(0, 0), proportion=1, flag=wx.EXPAND, border=5)

        # <PyCmt: Object Add Button >
        self.m_buttonObjAdd = \
            wx.Button(
                parent=self.m_panelObjPara,
                id=wx.ID_ANY,
                label=u'Obj Add',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonObjAdd'
            )
        self.m_buttonObjAdd.Enable(False)
        fgSizerObjPara.Add(self.m_buttonObjAdd, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        # <PyCmt: Object Parameter fgSizer Setup>
        self.m_panelObjPara.SetSizer(fgSizerObjPara)
        self.m_panelObjPara.Layout()
        fgSizerObjPara.Fit(self.m_panelObjPara)
        bSizerBaseEHUIObj.Add(self.m_panelObjPara, 0, wx.ALL | wx.EXPAND, 5)
        # </PyCmt: Object Parameter Panel>
    # </PyCmt: EHUIFormCrate Class SubFunc: fnPanelObjPara>

    # <PyCmt: EHUIFormCrate Class SubFunc: fnPanelObjCfg>
    def fnPanelObjCfg(self, bSizerBaseEHUIObj):
        # <PyCmt: Object Config Panel>
        self.m_panelObjCfg = \
            wx.Panel(
                parent=self,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjCfgListPage'
            )
        fgSizerObjCfg = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerObjCfg.SetFlexibleDirection(wx.BOTH)
        fgSizerObjCfg.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjCfg.SetSizer(fgSizerObjCfg)

        # <PyCmt: ObjConfig MultiPage(wx.notebook)>
        self.m_notebookObjCfg = \
            wx.Notebook(
                parent=self.m_panelObjCfg,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_notebookObjCfg'
            )
        self.m_notebookObjCfg.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.fnEvtNBObjCfgPageChgd)
        fgSizerNBObjCfg = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerNBObjCfg.SetFlexibleDirection(wx.BOTH)
        fgSizerNBObjCfg.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_notebookObjCfg.SetSizer(fgSizerNBObjCfg)
        fgSizerObjCfg.Add(self.m_notebookObjCfg, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: Obj List Page, Page1(wx.Panel; TabPage)>
        self.m_panelObjCfgListPage = \
            wx.Panel(
                parent=self.m_notebookObjCfg,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjCfgListPage'
            )
        self.m_notebookObjCfg.AddPage(self.m_panelObjCfgListPage, 'ObjList')
        fgSizerObjCfgListPage = wx.FlexGridSizer(rows=0, cols=3, vgap=0, hgap=0)
        fgSizerObjCfgListPage.SetFlexibleDirection(wx.BOTH)
        fgSizerObjCfgListPage.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjCfgListPage.SetSizer(fgSizerObjCfgListPage)
        # <PyDebug: DO NOT ADD Notebook Page into Notebook Sizer!>
        # fgSizerNBObjCfg.Add(self.m_panelObjCfgListPage, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: ObjText Label(wxStaticText)>
        self.m_staticTextObjText = \
            wx.StaticText(
                parent=self.m_panelObjCfgListPage,
                id=wx.ID_ANY,
                label=u'Item Text: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextObjText'
            )
        self.m_staticTextObjText.Wrap(-1)
        self.m_staticTextObjText.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth - self.c_intTabObjShrink, wx.DefaultSize.height)
        )
        fgSizerObjCfgListPage.Add(self.m_staticTextObjText, 0, wx.ALL, 5)

        # <PyCmt: ObjList ListBox(wxListBox)>
        self.m_listBoxObjListChoices = []
        self.m_listBoxObjList = \
            wx.ListBox(
                parent=self.m_panelObjCfgListPage,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                choices=self.m_listBoxObjListChoices,
                style=0,
                name='m_listBoxObjList'
            )
        self.m_listBoxObjList.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_listBoxObjList.Bind(wx.EVT_LISTBOX, self.fnEvtBtnObjAddEnable)
        self.m_listBoxObjList.Bind(wx.EVT_LISTBOX, self.fnEvtBtnObjListRemoveEnable)
        fgSizerObjCfgListPage.Add(self.m_listBoxObjList, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: before m_textCtrlObjText Add Spacer >
        fgSizerObjCfgListPage.Add(size=(0, 0), proportion=1, flag=wx.EXPAND, border=5)
        # <PyCmt: before m_textCtrlObjText Add Spacer >
        fgSizerObjCfgListPage.Add(size=(0, 0), proportion=1, flag=wx.EXPAND, border=5)

        # <PyCmt: ObjText InputBox(wxTextCtrl)>
        self.m_textCtrlObjText = \
            wx.TextCtrl(
                parent=self.m_panelObjCfgListPage,
                id=wx.ID_ANY,
                value=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_textCtrlObjText'
            )
        self.m_textCtrlObjText.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        self.m_textCtrlObjText.Bind(wx.EVT_TEXT, self.fnEvtBtnObjListAddEnable)
        fgSizerObjCfgListPage.Add(self.m_textCtrlObjText, 0, wx.ALL, 5)

        # <PyCmt: before m_textCtrlObjText Add Spacer >
        fgSizerObjCfgListPage.Add(size=(0, 0), proportion=1, flag=wx.EXPAND, border=5)
        # <PyCmt: before m_textCtrlObjText Add Spacer >
        fgSizerObjCfgListPage.Add(size=(0, 0), proportion=1, flag=wx.EXPAND, border=5)

        # <PyCmt: ObjText Add Button (wxButton)>
        self.m_buttonObjTextAdd = \
            wx.Button(
                parent=self.m_panelObjCfgListPage,
                id=wx.ID_ANY,
                label=u'Item Add',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonObjTextAdd'
            )
        self.m_buttonObjTextAdd.Bind(wx.EVT_BUTTON, self.fnEvtBtnObjListAddClick)
        self.m_buttonObjTextAdd.Enable(False)
        fgSizerObjCfgListPage.Add(self.m_buttonObjTextAdd, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        # <PyCmt: ObjText Remove Button (wxButton)>
        self.m_buttonObjTextRemove = \
            wx.Button(
                parent=self.m_panelObjCfgListPage,
                id=wx.ID_ANY,
                label=u'Item Remove',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_buttonObjTextRemove'
            )
        self.m_buttonObjTextRemove.Bind(wx.EVT_BUTTON, self.fnEvtBtnObjListRemoveClick)
        self.m_buttonObjTextRemove.Enable(False)
        fgSizerObjCfgListPage.Add(self.m_buttonObjTextRemove, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        # <PyCmt: ObjList Parameter fgSizer Setup>
        self.m_panelObjCfgListPage.Layout()
        fgSizerObjCfgListPage.Fit(self.m_panelObjCfgListPage)
        self.m_notebookObjCfg.Layout()
        fgSizerNBObjCfg.Fit(self.m_notebookObjCfg)
        # </PyCmt: ObjList ListPage, Page1(wx.Panel; TabPage)>


        # <PyCmt: ObjEvent Page, Page2(wx.Panel; TabPage)>
        self.m_panelObjEventPage = \
            wx.Panel(
                parent=self.m_notebookObjCfg,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjEventPage'
            )
        self.m_notebookObjCfg.AddPage(self.m_panelObjEventPage, 'ObjEvent')
        fgSizerObjEventPage = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerObjEventPage.SetFlexibleDirection(wx.BOTH)
        fgSizerObjEventPage.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjEventPage.SetSizer(fgSizerObjEventPage)
        # <PyCmt: ObjEvent Page, Page2(wx.Panel; TabPage)>

        # <PyCmt: ObjList DBTblColPage, Page3(wx.Panel; TabPage)>
        self.m_panelObjCfgDBTblColPage = \
            wx.Panel(
                parent=self.m_notebookObjCfg,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjCfgListPage'
            )
        self.m_notebookObjCfg.AddPage(self.m_panelObjCfgDBTblColPage, 'DBTblCol')
        fgSizerObjCfgDBTblColPage = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerObjCfgDBTblColPage.SetFlexibleDirection(wx.BOTH)
        fgSizerObjCfgDBTblColPage.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjCfgDBTblColPage.SetSizer(fgSizerObjCfgDBTblColPage)

        m_staticTextObjDBTblName = \
            wx.StaticText(
                parent=self.m_panelObjCfgDBTblColPage,
                id=wx.ID_ANY,
                label=u'DB Tbl: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_staticTextObjDBTblName'
            )
        m_staticTextObjDBTblName.Wrap(-1)
        m_staticTextObjDBTblName.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth - self.c_intTabObjShrink, wx.DefaultSize.height))
        fgSizerObjCfgDBTblColPage.Add(m_staticTextObjDBTblName, 0, wx.ALL, 5)

        lstDBTblName = []
        self.m_choiceDBTblName = \
            wx.Choice(
                parent=self.m_panelObjCfgDBTblColPage,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                choices=lstDBTblName,
                style=0,
                name='self.m_choiceDBTblName'
            )
        self.m_choiceDBTblName.Enabled = False
        self.m_choiceDBTblName.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        fgSizerObjCfgDBTblColPage.Add(window=self.m_choiceDBTblName, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)

        self.m_staticTextObjDBColName = \
            wx.StaticText(
                parent=self.m_panelObjCfgDBTblColPage,
                id=wx.ID_ANY,
                label=u'DB Coll: ',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_staticTextObjDBColName'
            )
        self.m_staticTextObjDBColName.Wrap(-1)
        m_staticTextObjDBTblName.SetMinSize(
            wx.Size(self.c_intStaticTextMinWidth - self.c_intTabObjShrink, wx.DefaultSize.height))
        fgSizerObjCfgDBTblColPage.Add(self.m_staticTextObjDBColName, 0, wx.ALL, 5)

        lstDBColName = []
        self.m_choiceDBColName = \
            wx.Choice(
                parent=self.m_panelObjCfgDBTblColPage,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                choices=lstDBColName,
                style=0,
                name='self.m_choiceDBColName'
            )
        self.m_choiceDBColName.Enabled = False
        self.m_choiceDBColName.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        fgSizerObjCfgDBTblColPage.Add(window=self.m_choiceDBColName, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        # </PyCmt: ObjList DBTblColPage, Page3(wx.Panel; TabPage)>

        # <PyCmt: ObjList DBSQLPage, Page3(wx.Panel; TabPage)>
        self.m_panelObjCfgDBSQLPage = \
            wx.Panel(
                parent=self.m_notebookObjCfg,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjCfgListPage'
            )
        self.m_notebookObjCfg.AddPage(self.m_panelObjCfgDBSQLPage, 'DBSQLCol')
        fgSizerObjCfgDBSQLPage = wx.FlexGridSizer(rows=0, cols=1, vgap=0, hgap=0)
        fgSizerObjCfgDBSQLPage.SetFlexibleDirection(wx.BOTH)
        fgSizerObjCfgDBSQLPage.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjCfgDBSQLPage.SetSizer(fgSizerObjCfgDBSQLPage)

        self.m_textCtrlDBSQL = \
            wx.TextCtrl(
                parent=self.m_panelObjCfgDBSQLPage,
                id=wx.ID_ANY,
                value=wx.EmptyString,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TE_MULTILINE | wx.TE_BESTWRAP,
                name='m_textCtrlDBSQL'
            )
        self.m_textCtrlDBSQL.SetMinSize(
            wx.Size(self.c_intTextInputMinWidth, wx.DefaultSize.height)
        )
        fgSizerObjCfgDBSQLPage.Add(window=self.m_textCtrlDBSQL, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)

        self.m_buttonDBSQLPreview = \
            wx.Button(
                parent=self.m_panelObjCfgDBSQLPage,
                id=wx.ID_ANY,
                label=u'SQL Preview',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonDBSQLPreview'
            )
        fgSizerObjCfgDBSQLPage.Add(self.m_buttonDBSQLPreview, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        # </PyCmt: ObjList DBSQLPage, Page3(wx.Panel; TabPage)>

        self.m_panelObjCfg.Layout()
        fgSizerObjCfg.Fit(self.m_panelObjCfg)
        bSizerBaseEHUIObj.Add(self.m_panelObjCfg, 0, wx.EXPAND | wx.ALL, 5)
        # </PyCmt: Object Config Panel>
    # </PyCmt: EHUIFormCrate Class SubFunc: fnPanelObjCfg>

    # <PyCmt: EHUIFormCrate Class SubFunc: fnPanelObjCfgd>
    def fnPanelObjCfgd(self, bSizerBaseEHUIObj):
        # <PyCmt: Object Configed Grid Panel>
        self.m_panelObjCfgd = \
            wx.Panel(
                parent=self,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjCfgd'
            )
        fgSizerObjCfgd = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizerObjCfgd.SetFlexibleDirection(wx.BOTH)
        fgSizerObjCfgd.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjCfgd.SetSizer(fgSizerObjCfgd)

        # <PyCmt: ObjConfiged MultiPage(wx.notebook)>
        self.m_notebookObjCfgd = \
            wx.Notebook(
                parent=self.m_panelObjCfgd,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_notebookObjCfgd'
            )
        self.m_notebookObjCfgd.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.fnEvtNBObjCfgdPageChgd)
        fgSizerNBObjCfgd = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerNBObjCfgd.SetFlexibleDirection(wx.BOTH)
        fgSizerNBObjCfgd.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_notebookObjCfgd.SetSizer(fgSizerNBObjCfgd)
        fgSizerObjCfgd.Add(self.m_notebookObjCfgd, 0, wx.ALL | wx.EXPAND, 5)


        # <PyCmt: Obj Cfgd Page, Page1(wx.Panel; TabPage)>
        self.m_panelObjCfgdGridPage = \
            wx.Panel(
                parent=self.m_notebookObjCfgd,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjCfgdGridPage'
            )
        self.m_notebookObjCfgd.AddPage(self.m_panelObjCfgdGridPage, 'ObjCfgd')
        fgSizerObjCfgdGridPage = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerObjCfgdGridPage.SetFlexibleDirection(wx.BOTH)
        fgSizerObjCfgdGridPage.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjCfgdGridPage.SetSizer(fgSizerObjCfgdGridPage)
        # <PyDebug: DO NOT ADD Notebook Page into Notebook Sizer!>
        # fgSizerNBObjCfg.Add(self.m_panelObjCfgListPage, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: Configed Obj Parameter Grid (wxGrid)>
        self.m_gridObjCfgd = \
            wx.grid.Grid(
                parent=self.m_panelObjCfgdGridPage,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_gridObjCfgd'
            )
        self.m_gridObjCfgd.Bind(
            wx.grid.EVT_GRID_SELECT_CELL,
            self.fnEvtGridSelChg
        )
        # Grid
        self.m_gridObjCfgd.CreateGrid(len(self.c_lstGridCfgdObjTitleCol), 5)
        self.m_gridObjCfgd.EnableEditing(False)
        self.m_gridObjCfgd.EnableGridLines(True)
        self.m_gridObjCfgd.DisableRowResize(True)
        self.m_gridObjCfgd.EnableDragGridSize(True)
        self.m_gridObjCfgd.SetMargins(0, 0)

        # Columns
        self.m_gridObjCfgd.EnableDragColSize(True)
        self.m_gridObjCfgd.EnableDragColMove(False)
        self.m_gridObjCfgd.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        for strTitleCol in self.c_lstGridCfgdObjTitleCol:
            self.m_gridObjCfgd.SetColLabelValue(self.c_lstGridCfgdObjTitleCol.index(strTitleCol), strTitleCol)

        # Rows
        self.m_gridObjCfgd.EnableDragRowSize(False)
        self.m_gridObjCfgd.EnableDragRowMove(True)
        self.m_gridObjCfgd.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.m_gridObjCfgd.SetSelectionMode(wx.grid.Grid.GridSelectRows)

        # Cell Defaults
        self.m_gridObjCfgd.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        fgSizerObjCfgdGridPage.Add(self.m_gridObjCfgd,  0, wx.ALL, 5)

        self.m_buttonGridCfgdItemRemove = \
            wx.Button(
                parent=self.m_panelObjCfgdGridPage,
                id=wx.ID_ANY,
                label=u'Remove',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonGridCfgdItemRemove'
            )
        self.m_buttonGridCfgdItemRemove.Enable(False)
        self.m_buttonGridCfgdItemRemove.Bind(wx.EVT_BUTTON, self.fnEvtBtnCfgdObjRemoveClick)
        fgSizerObjCfgdGridPage.Add(self.m_buttonGridCfgdItemRemove, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        # <PyCmt: Configed Object Grid fgSizer Setup>
        self.m_panelObjCfgdGridPage.Layout()
        fgSizerObjCfgdGridPage.Fit(self.m_panelObjCfgdGridPage)
        self.m_notebookObjCfgd.Layout()
        fgSizerNBObjCfgd.Fit(self.m_notebookObjCfgd)

        # <PyCmt: Obj Event Cfgd Page, Page2(wx.Panel; TabPage)>
        self.m_panelObjEvtCfgdGridPage = \
            wx.Panel(
                parent=self.m_notebookObjCfgd,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjEvtCfgdGridPage'
            )
        self.m_notebookObjCfgd.AddPage(self.m_panelObjEvtCfgdGridPage, 'ObjCfgd')
        fgSizerObjEvtCfgdGridPage = wx.FlexGridSizer(rows=0, cols=2, vgap=0, hgap=0)
        fgSizerObjEvtCfgdGridPage.SetFlexibleDirection(wx.BOTH)
        fgSizerObjEvtCfgdGridPage.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_panelObjEvtCfgdGridPage.SetSizer(fgSizerObjEvtCfgdGridPage)
        # <PyDebug: DO NOT ADD Notebook Page into Notebook Sizer!>
        # fgSizerNBObjCfg.Add(self.m_panelObjCfgListPage, 0, wx.ALL | wx.EXPAND, 5)

        # <PyCmt: Configed Obj Event Parameter Grid (wxGrid)>
        self.m_gridObjEvtCfgd = \
            wx.grid.Grid(
                parent=self.m_panelObjEvtCfgdGridPage,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='self.m_gridObjEvtCfgd'
            )
        self.m_gridObjEvtCfgd.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.fnEvtGridSelChg)
        # Grid
        self.m_gridObjEvtCfgd.CreateGrid(len(self.c_lstGridCfgdObjTitleCol), 5)
        self.m_gridObjEvtCfgd.EnableEditing(False)
        self.m_gridObjEvtCfgd.EnableGridLines(True)
        self.m_gridObjEvtCfgd.DisableRowResize(True)
        self.m_gridObjEvtCfgd.EnableDragGridSize(True)
        self.m_gridObjEvtCfgd.SetMargins(0, 0)

        # Columns
        self.m_gridObjEvtCfgd.EnableDragColSize(True)
        self.m_gridObjEvtCfgd.EnableDragColMove(False)
        self.m_gridObjEvtCfgd.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        for strTitleCol in self.c_lstGridCfgdObjTitleCol:
            self.m_gridObjEvtCfgd.SetColLabelValue(self.c_lstGridCfgdObjTitleCol.index(strTitleCol), strTitleCol)

        # Rows
        self.m_gridObjEvtCfgd.EnableDragRowSize(False)
        self.m_gridObjEvtCfgd.EnableDragRowMove(True)
        self.m_gridObjEvtCfgd.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.m_gridObjEvtCfgd.SetSelectionMode(wx.grid.Grid.GridSelectRows)

        # Cell Defaults
        self.m_gridObjEvtCfgd.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        fgSizerObjEvtCfgdGridPage.Add(self.m_gridObjEvtCfgd,  0, wx.ALL, 5)

        self.m_buttonGridEvtCfgdItemRemove = \
            wx.Button(
                parent=self.m_panelObjEvtCfgdGridPage,
                id=wx.ID_ANY,
                label=u'Remove',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonGridEvtCfgdItemRemove'
            )
        self.m_buttonGridEvtCfgdItemRemove.Enable(False)
        self.m_buttonGridEvtCfgdItemRemove.Bind(wx.EVT_BUTTON, self.fnEvtBtnCfgdObjRemoveClick)
        fgSizerObjEvtCfgdGridPage.Add(self.m_buttonGridEvtCfgdItemRemove, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        # <PyCmt: Configed Object Grid fgSizer Setup>
        self.m_panelObjEvtCfgdGridPage.Layout()
        fgSizerObjEvtCfgdGridPage.Fit(self.m_panelObjEvtCfgdGridPage)
        self.m_notebookObjCfgd.Layout()
        fgSizerNBObjCfgd.Fit(self.m_notebookObjCfgd)

        self.m_panelObjCfgd.Layout()
        fgSizerObjCfgd.Fit(self.m_panelObjCfgd)
        bSizerBaseEHUIObj.Add(self.m_panelObjCfgd, 0, wx.EXPAND | wx.ALL, 5)
        # </PyCmt: Object Configed Grid Panel>
    # </PyCmt: EHUIFormCrate Class SubFunc: fnPanelObjCfgd>

    # <PyCmt: EHUIFormCrate Class SubFunc: fnPanelOKCancel>
    def fnPanelOKCancel(self, bSizerBaseEHUIObj):
        # <PyCmt: OK;Cancel Btn Grid Panel>
        self.m_panelObjBtnOKCancel = \
            wx.Panel(
                parent=self,
                id=wx.ID_ANY,
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL,
                name='m_panelObjBtnOKCancel'
            )
        gbSizerBtnOKCancel = wx.GridBagSizer(0, 0)
        gbSizerBtnOKCancel.SetFlexibleDirection(wx.BOTH)
        gbSizerBtnOKCancel.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        m_buttonOK = \
            wx.Button(
                parent=self.m_panelObjBtnOKCancel,
                id=wx.ID_ANY,
                label=u'OK',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonOK'
            )
        gbSizerBtnOKCancel.Add(m_buttonOK, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        m_buttonCancel = \
            wx.Button(
                parent=self.m_panelObjBtnOKCancel,
                id=wx.ID_ANY,
                label=u'Cancel',
                pos=wx.DefaultPosition,
                size=wx.DefaultSize,
                style=0,
                name='m_buttonCancel'
            )
        m_buttonCancel.Bind(wx.EVT_BUTTON, self.fnOnBtnClose)
        gbSizerBtnOKCancel.Add(m_buttonCancel, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        gbSizerBtnOKCancel.AddGrowableCol(0)
        gbSizerBtnOKCancel.AddGrowableRow(0)

        self.m_panelObjBtnOKCancel.SetSizer(gbSizerBtnOKCancel)
        self.m_panelObjBtnOKCancel.Layout()
        gbSizerBtnOKCancel.Fit(self.m_panelObjBtnOKCancel)
        bSizerBaseEHUIObj.Add(self.m_panelObjBtnOKCancel, 0, wx.ALL | wx.EXPAND, 5)
        # </PyCmt: OK; Cancel Btn Grid Panel>
    # </PyCmt: EHUIFormCrate Class SubFunc: fnPanelOKCancel>

    # <PyCmt: EHUIFormCrate SubFunc: fnShow>
    def fnShow(self):
        # self.m_panelObjCfgListPage.Hide()
        # self.m_panelObjCfgd.Hide()
        self.Fit()
        self.Centre(wx.BOTH)
        self.SetWindowStyleFlag(self.GetWindowStyleFlag() | wx.STAY_ON_TOP)
        self.Show()
        if c_blnEHDebugMode: print('EHUI.fnShow Done!')
        self.appWX.MainLoop()
        if c_blnEHDebugMode: print('EHUI.appWX.MainLoop Done!')
    # </PyCmt: EHUIFormCrate SubFunc: fnShow>

    # <PyCmt: EHUIFormCrate SubFunc>
    def fnClose(self, event):
        event.Skip()
        self.Destroy()
        self.appWX.ExitMainLoop()

    def fnOnCharHook(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.fnClose(event)
        else:
            event.Skip()

    def fnOnBtnClose(self, event):
        self.fnClose(event)

    def fnEvtBtnObjAddEnable(self, event):
        # strObjName = event.GetEventObject().GetName()
        event.Skip()

        strObjType = self.m_choiceObjType.GetStringSelection()
        blnChoiceObjEnable = False
        if strObjType == 'TextCtrl':
            blnChoiceObjEnable = True
            self.m_panelObjCfgListPage.Hide()
        elif strObjType == 'ComboBox':
            blnChoiceObjEnable = True
            self.m_panelObjCfgListPage.Show()
        elif strObjType == 'Choice':
            self.m_panelObjCfgListPage.Show()
            blnChoiceObjEnable = self.m_listBoxObjList.GetCount() > 0
        elif strObjType == 'ListBox':
            self.m_panelObjCfgListPage.Show()
            blnChoiceObjEnable = self.m_listBoxObjList.GetCount() > 0
        blnBtnObjAddEnable = \
            len(self.m_textCtrlFormName.GetValue()) > 0 and \
            len(self.m_textCtrlObjName.GetValue()) > 0 and \
            blnChoiceObjEnable
        self.m_buttonObjAdd.Enable(blnBtnObjAddEnable)
        self.Fit()
        self.Layout()

    def fnEvtNBObjCfgPageChgd(self, event):
        event.Skip()
        self.m_choiceDBTblName.Enabled = True

    def fnEvtBtnObjListAddEnable(self, event):
        event.Skip()
        self.m_buttonObjTextAdd.Enable(len(self.m_textCtrlObjText.GetValue()) > 0)

    def fnEvtBtnObjListAddClick(self, event):
        event.Skip()
        self.m_listBoxObjList.Append(self.m_textCtrlObjText.GetValue())
        self.m_textCtrlObjText.Clear()

    def fnEvtBtnObjListRemoveEnable(self, event):
        event.Skip()
        self.m_buttonObjTextRemove.Enable(self.m_listBoxObjList.GetSelections() is not None)

    def fnEvtBtnObjListRemoveClick(self, event):
        event.Skip()
        self.m_listBoxObjList.Delete(self.m_listBoxObjList.GetSelection())

    def fnEvtBtnCfgdObjRemoveClick(self, event):
        event.Skip()
        self.m_gridObjCfgd.DeleteRows(self.m_gridObjCfgd.GetGridCursorRow(), 1)

    def fnEvtNBObjCfgdPageChgd(self, event):
        event.Skip()
        self.m_choiceDBTblName.Enabled = True

    def fnEvtGridSelChg(self, event):
        event.Skip()
        lstSeltdRow = self.m_gridObjCfgd.GetSelectedRows()
        self.m_buttonGridCfgdItemRemove.Enable = \
            len(self.m_gridObjCfgd.GetCellValue(lstSeltdRow[0], self.c_lstGridCfgdObjTitleCol.index('ObjName'))) > 0
    # </PyCmt: EHUIFormCrate SubFunc>

def fnUIFormCreateShow():
    clsEHUIFormCreate=EHUIFormCreate()
    clsEHUIFormCreate.fnShow()

class EHXWForm(wx.Frame):
    def __init__(self,
                 strFormCaption='',
                 tupPosition=None,
                 tupSize=None,
                 lngStyle=None,
                 strFrameName=''
                 )->wx.Frame:
        if tupPosition is None: tupPosition = (100,100)
        if tupSize is None: tupSize = (400,200)
        if lngStyle is None: lngStyle = wx.DEFAULT_FRAME_STYLE

        self.appWX=wx.App()
        super().__init__(
            parent=None,
            id=wx.ID_ANY,
            title=strFormCaption,
            pos=tupPosition,
            size=tupSize,
            style=lngStyle,
            name=strFrameName
        )
        objPanel=wx.Panel(self)

        objSizer=wx.BoxSizer(wx.VERTICAL)

        # <PyCmt: Page>
        # lstPageCaption=['A', 'B']
        # fnAddwxTab( \
        #     objPanel=objPanel, \
        #     objSizer=objSizer, \
        #     lstPageCaption=lstPageCaption \
        # )

        # <PyCmt: Button>
        # lstBtnCaption = ['A', 'B']
        # lstBtnAction = ['D', 'E']
        # fnAddwxBtn( \
        #     objPanel=objPanel, \
        #     objSizer=objSizer, \
        #     lstBtnCaption=lstBtnCaption, \
        #     lstBtnAction=lstBtnAction \
        # )

        # <Python: Static Text>
        # fnAddwxStaticText( \
        #     objPanel=objPanel, \
        #     objSizer=objSizer, \
        #     strTxtCaption='Static Text Test Caption' \
        # )

        # <Python: Text Ctrl>
        # lstTextCtrlID = ['A', 'B']
        # fnAddwxTextCtrl(objPanel=objPanel, objSizer=objSizer, lstTextCtrlID=lstTextCtrlID)

        objPanel.SetSizer(objSizer)
        objSizer.Fit(self)

    def fnEHXWFormShow(self):
        self.Show()
        self.appWX.MainLoop()

def fnAddwxTab(
    objPanel:wx.Panel,
    objSizer:wx.BoxSizer,
    lstPageCaption:list
):
    objTab=EHwxTab(objPanel=objPanel, lstPageCaption=lstPageCaption)
    objNotebook=objTab.parent
    objSizer.Add(objNotebook, 1, wx.ALL | wx.EXPAND, 5)

def fnAddwxBtn(
        objPanel,
        objSizer,
        lstBtnCaption,
        lstBtnAction,
        lstPos=None
):
    if len(lstBtnCaption)!=len(lstBtnAction): return None

    tupPos=()
    intRun=0
    for strBtnCaption, strBtnAction in zip(lstBtnCaption, lstBtnAction):
        if lstPos is None:
            if len(tupPos)==0: tupPos=(100,50)
        else:
            tupPos=lstPos[intRun]

        btnRun=wx.Button(parent=objPanel, label=strBtnCaption, pos=tupPos )
        # btnRun.Bind(wx.EVT_BUTTON, lambda event, action=strBtnAction: fnwxBtnClick(event, action))
        # btnRun.Bind(wx.EVT_BUTTON, lambda event, action=strBtnAction: print('strBtnAction: ', action))
        # btnRun.Bind(wx.EVT_BUTTON, lambda event: print('strBtnAction: ', strBtnAction)) #incorrect one!
        btnRun.Bind(wx.EVT_BUTTON, lambda event, action=strBtnAction: fnwxBtnClick(action))
        objSizer.Add(btnRun, 0 , wx.ALL, 5)
        intRun+=1

    def fnwxBtnClick(strBtnAction):
        print('strBtnAction: ', strBtnAction)

def fnAddwxStaticText(objPanel, objSizer, lstTxtCaption):
    for strTxtCaption in lstTxtCaption:
        objStatTxt=wx.StaticText(objPanel, label=strTxtCaption)
        objSizer.Add(objStatTxt, 0, wx.ALL, 10)

def fnAddwxTextCtrl(
        objPanel,
        objSizer,
        lstTextCtrlID,
        intStyle=0
):
    # blnProcEnter = False, \
    # blnProcTab = False, \
    # blnMultiLine = False, \
    # blnPwd = False, \
    # blnReadOnly = False, \
    # blnRich = False, \
    # blnRich2 = False, \
    # blnAutoUrl = False, \
    # blnNoHideSel = False, \
    # blnHScroll = False, \
    # blnNoVScroll = False, \
    # blnLeft = False, \
    # blnCentre = False, \
    # blnRight = False, \
    # blnDontWrap = False, \
    # blnCharWarp = False, \
    # blnWordWrap = False, \
    # blnBestWrap = False, \
    # blnCapitalize = False \
    # if blnProcEnter: intStyle=intStyle + wx.TE_PROCESS_ENTER
    # if blnProcTab: intStyle = intStyle + wx.TE_PROCESS_TAB
    # if blnMultiLine: intStyle = intStyle + wx.TE_MULTILINE
    # if blnPwd: intStyle = intStyle + wx.TE_PASSWORD
    # if blnReadOnly: intStyle = intStyle + wx.TE_READONLY
    # if blnRich: intStyle = intStyle + wx.TE_RICH
    # if blnRich2: intStyle = intStyle + wx.TE_RICH2
    # if blnAutoUrl: intStyle = intStyle + wx.TE_AUTO_URL
    # if blnNoHideSel: intStyle = intStyle + wx.TE_NOHIDESEL
    # if blnHScroll: intStyle = intStyle + wx.HSCROLL
    # if blnNoVScroll: intStyle = intStyle + wx.TE_NO_VSCROL
    # if blnLeft: intStyle = intStyle + wx.TE_LEFT
    # if blnCentre: intStyle = intStyle + wx.TE_CENTRE
    # if blnRight: intStyle = intStyle + wx.TE_RIGHT
    # if blnDontWrap: intStyle = intStyle + wx.TE_DONTWRAP
    # if blnCharWarp: intStyle = intStyle + wx.TE_CHARWRAP
    # if blnWordWrap: intStyle = intStyle + wx.TE_WORDWRAP
    # if blnBestWrap: intStyle = intStyle + wx.TE_BESTWRAP
    # if blnCapitalize: intStyle = intStyle + TE_CAPITALIZE

    for strTextCtrlID in lstTextCtrlID:
        objTxtCtrl = \
            wx.TextCtrl(
                parent=objPanel,
                name=strTextCtrlID,
                style=intStyle
            )
        objSizer.Add(objTxtCtrl, 0, wx.ALL, 5)

def fnAddwxChoice(
        objPanel:wx.Panel,
        objSizer:wx.BoxSizer,
        lstChoice:wx.Choice
):
    for dictChoice in lstChoice:
        strChoiceName = dictChoice.get('Name', '')
        lstChoice = dictChoice.get('lstItem', '')
        intStyle = dictChoice.get('intStyle', 0)
        objChoice= \
            wx.Choice(
                parent = objPanel,
                choices = lstChoice,
                style = intStyle,
                name = strChoiceName
            )
        objSizer.Add(objChoice, 0, wx.ALL, 5)

# def fnAddwxListBox(\
#     objPanel, \
#     objSizer, \
#     lstChoice \
# )
#     for dictChoice in lstChoice:
#         strChoiceName = dictItem.get('Name', '')
#         lstChoice = dictItem.get('lstItem', '')
#         intStyle = dictItem.get('intStyle', 0)
#         objChoice= \
#             wx.Choice( \
#                 parent = objPanel, \
#                 choices = lstChoice, \
#                 style = intStyle, \
#                 name = strChoiceName
#             )
#         objSizer.Add(objChoice, 0, wx.ALL, 5)

class EHwxTab(wx.Panel):
    def __init__(
            self,
            objPanel,
            lstPageCaption=None
    ):
        #<PyCmt: Self->Page>
        self.parent=wx.Notebook(objPanel)
        wx.Panel.__init__(self, parent=self.parent)

        intPage=1
        for strPageCaption in lstPageCaption:
            self.pageNum=intPage
            if not lstPageCaption is None:
                self.parent.AddPage(self, strPageCaption)
            intPage+=1