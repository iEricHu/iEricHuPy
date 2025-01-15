# EHXLApp.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import xlwings.constants as xwcnst

import EHXW
import EHSymbolDef
import EHMsg
import EHUsrMgt

c_strAttrSplitorGeneral=EHSymbolDef.c_strAttrSplitorGeneral

c_strOnKeyCallFuncName = "fnOnKeyCall"
c_strOnKeyDBCNNReset="."

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHXLApp.py !')

def clsEHXW()->EHXW.EHXWClass:
    return EHXW.EHXWClass()

def p_objApp():
    return clsEHXW.p_objApp

def p_winAct():
    return clsEHXW.p_winAct

def p_wbXWWB():
    return clsEHXW.s_wbXWWB
# </PyDecl: RunTime>

class EHXLAppClass:
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls) #, *args, **kw)
            cls.s_blnAutoRunning=False
            cls.s_strStatusBarDefaultShow=''
        return cls._instance

    def __init__(self):
        self.s_strStatusBarDefaultShow = None

    @property
    def p_strStatusBarDefaultShow(self):
        return self.s_strStatusBarDefaultShow

    @property
    def p_blnAutoRunning(self):
        return self.s_blnAutoRunning

    def fnStatusBarSetup(
            self,
            strStatusShow='',
            blnStatusClean=False,
            blnSetAsDefault=False
    ):
        if blnStatusClean:
            p_objApp.api.StatusBar=False
        else:
            if blnSetAsDefault and len(strStatusShow)>0: self.s_strStatusBarDefaultShow=strStatusShow
            if len(strStatusShow)==0:
                if len(self.p_strStatusBarDefaultShow)>0:
                    strStatusShow=self.p_strStatusBarDefaultShow
                else:
                    strStatusShow=False
            p_objApp.api.StatusBar = strStatusShow
            if p_objApp.api.DisplayStatusBar and \
                p_objApp.api.CutCopyMode:
                p_objApp.api.DisplayStatusBar = True

    #<PyRegion: Excel Event>
    @staticmethod
    def fnWBAct():
        fnAppOnKey(strKey=c_strOnKeyDBCNNReset, strCallFunc="clsEHDBClass.fnDBCNNReset", blnCtrlKey=True)
        if EHUsrMgt.c_blnSysUserMgtAvail: fnRootMgtOnKey()

    def fnWBDeact(self):
        if not self.p_blnAutoRunning:
            #fnReportSheetDeactive
            EHUserMgt.fnRootMgtOnKey(blnKeyCancel=True)
            fnAppOnKey(strKey=c_strOnKeyDBCNNReset, strCallFunc="clsEHDBClass.fnDBCNNReset", blnCancelOnKey=True)

    def fnShtAct(self):
        pass
    def fnShtDeact(self):
        pass
    def fnShtChg(self):
        pass
    def fnShtDblClk(self):
        pass
    #</PyRegion: Excel Event>

def fnXLCmdLine(lngCmd)->str:
    pass
    # if len(lngCmd)>0:
        #lngStrLen = lstrlenW(lngCmd) * 2
        #If lngStrLen Then
        #    ReDim varbyteBuffer(0 To (lngStrLen - 1)) As Byte
        #    CopyMemory varbyteBuffer(0), ByVal lngCmd, lngStrLen
        #    fnExcelCmdLine = varbyteBuffer
        #End If

def fnXLAppReset(
        blnDisableFunc=False,
        blnScreenUpdate=False,
        blnEnableCopyFunc=False,
        blnCursorChg=False
):
    if not blnDisableFunc:
        if not blnEnableCopyFunc:
            p_objApp.api.Calculation = xwcnst.Calculation.xlCalculationManual
            p_objApp.api.CalculateBeforeSave = False
            if not p_wbXWWB is None: p_wbXWWB.api.PrecisionAsDisplayed = False
        if blnCursorChg: p_objApp.api.Cursor =xwcnst.MousePointer.xlWait
        p_objApp.api.DisplayAlerts = False
        p_objApp.api.EnableCancelKey = xwcnst.EnableCancelKey.xlInterrupt
        p_objApp.api.EnableEvents = False
        p_objApp.api.ScreenUpdating = blnScreenUpdate
    else:
        #fnReportSheetActivate
        p_winAct.api.Visible=True
        if not blnEnableCopyFunc:
            p_objApp.api.Calculation = xwcnst.Calculation.xlCalculationSemiautomatic
            p_objApp.api.CalculateBeforeSave = True
            if not p_wbXWWB is None: p_wbXWWB.api.PrecisionAsDisplayed = False
        if blnCursorChg: p_objApp.api.Cursor = xwcnst.MousePointer.xlDefault
        p_objApp.api.DisplayAlerts = True
        p_objApp.api.EnableCancelKey = xwcnst.EnableCancelKey.xlInterrupt
        p_objApp.api.EnableEvents = True
        p_objApp.api.ScreenUpdating = True
        p_winAct.api.ActiveWindow.Caption = False

def fnAppOnKey(
        strKey:str ,
        strCallFunc:str,
        blnCtrlKey:bool = False,
        blnShiftKey:bool = False,
        blnAltKey:bool = False,
        blnCancelOnKey:bool = False
):
    if p_objApp is None: return None

    strKeyCtrl = "^"
    strKeyShift = "+"
    strKeyAlt = "%"
    c_strCallFuncTemplate = "'<OnkeyCallFuncName> <CallFuncStr>'"

    strKeyRun = strKey
    if blnCtrlKey and not strKeyCtrl in strKeyRun:
        strKeyRun = strKeyCtrl + strKeyRun

    if blnCtrlKey and not blnShiftKey in strKeyRun:
        strKeyRun = strKeyShift + strKeyRun

    if blnAltKey and not strKeyAlt in strKeyRun:
        strKeyRun = strKeyAlt + strKeyRun

    strCallFuncRun = c_strCallFuncTemplate
    strCallFuncRun = strCallFuncRun.replace("<OnkeyCallFuncName>", c_strOnKeyCallFuncName)
    strCallFuncRun = strCallFuncRun.replace("<CallFuncStr>", strCallFunc)
    p_objApp.api.OnKey(strKeyRun, '' if blnCancelOnKey else strCallFuncRun)

def fnCustomList(
        strCustomList,
        blnListDel=False,
        strSplitor=c_strAttrSplitorGeneral
):
    if not strSplitor in strCustomList:
        strMsg = 'CustomList: \'{0}\' Without Splitor({1})!'.format(strCustomList, strSplitor)
        strFuncName = 'EHXLApp.fnCustomList'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return None

    lstCustomList = strCustomList.split(strSplitor)
    if blnListDel:
        intListIndex = p_objApp.api.GetCustomListNum(ListArray=lstCustomList)
        p_objApp.api.DeleteCustomList(ListNum=intListIndex)
    else:
        p_objApp.api.AddCustomList(ListArray=lstCustomList)

def fnRootMgtOnKey(blnKeyCancel:bool =False):
    if c_blnSysRootMgtFuncAvail:
        fnAppOnKey(
            strKey = c_strRootMgtKey,
            strCallFunc = c_strRootMgtOnKeyFuncName,
            blnCtrlKey = True,
            blnShiftKey = True,
            blnAltKey = False,
            blnCancelOnKey = blnKeyCancel
        )