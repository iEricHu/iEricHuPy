# EHMsg.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

from PyQt6.QtWidgets import  QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QTextOption
from PyQt6.QtCore import Qt

# <PyDecl: Symbol Define & UDE import >
import EHSymbolDef
c_strNewLine = EHSymbolDef.c_strNewLine # '\n'
c_strTab = EHSymbolDef.c_strTab  # '\t'

c_strFileExtSymbol=EHSymbolDef.c_strFileExtSymbol # '.'
c_strPathSymbolLeft=EHSymbolDef.c_strPathSymbolLeft # '\'
c_strFileDateSplitor=EHSymbolDef.c_strFileDateSplitor # '-'
# </PyDecl: Symbol Define & UDE import >

c_strLogFileName='EHPy'
c_strLogFileExtName='log'

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHMsg.py !')

# <PyCmt: Need Recheck>
# import EHXW
# def clsEHXW()->EHXW.EHXWClass:
#     return EHXW.EHXWClass()

s_strLogPath=''
# </PyDecl: RunTime>

class EHMsgClass:
    _instance=None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)#, *args, **kw)
            cls.s_strLogPath = ''
        return cls._instance
    def __init__(self):
        self.s_strLogPath = self.s_strLogPath

    @property
    def p_strLogPath(self):
        return self.s_strLogPath

    @p_strLogPath.setter
    def p_strLogPath(self, strLogPathNew):
        self.s_strLogPath=strLogPathNew

# <PyRegion: Msg Show>
def fnMsgPrt(
        strMsg='',
        strTitle='',
        strFuncName='',
        blnCmdPrint=False,
        blnLog=False,
        strLogPath=''
):
    # <PyCmt: Show Message depends on EHXW.p_blnXWMode >
    # if EHXW.p_blnXWMode: show in Window
    strMsg=str(strMsg)
    lstMsg=[strMsg]

    if len(strFuncName) > 0:
        strMsg=''.join(['FuncName: ', strFuncName])
        lstMsg.insert (0, strMsg)
    strMsg=c_strNewLine.join(lstMsg)

    # <PyCmt: Write to Log File>
    if blnLog:
        fnLog(
            strMsg=strMsg,
            blnLogClean=False,
            strLogPath=strLogPath
        )

    import EHXW
    if EHXW.p_blnXWMode and not blnCmdPrint:
        fnDlgOpt(strMsg=strMsg, strTitle=strTitle)
    else:
        fnMsgCmdPrint(strMsg=strMsg, strTitle=strTitle, blnNewLine=True )

def fnMsgCmdPrint(strMsg='', strTitle='', blnNewLine=True):
    strTitle=str(strTitle)
    lstMsg = []
    if len(strTitle)>0:  lstMsg.append(c_strNewLine + 'ErrTitle: '+ strTitle)

    if len(strMsg)>0:
        strMsg=strMsg.replace(c_strNewLine, c_strNewLine + c_strTab)
        lstMsg.append(strMsg)
    print(c_strNewLine.join(lstMsg),end=(c_strNewLine if blnNewLine else ''))

# </PyRegion: Msg Show>

# <PyRegion: Log File>
def fnLogFilePath(
    strFilePath='',
    blnDropSplitor = True,
    blnSetRunning = False,
    blnCleanDft = False
)->str:
    import EHFile
    global s_strLogPath
    clsEHMsg = EHMsgClass()
    if len(strFilePath)==0:
        if len(s_strLogPath)==0:
            if len(clsEHMsg.p_strLogPath)>0: return clsEHMsg.p_strLogPath
            import EHXW
            if EHXW.p_blnXWMode:
                strFilePath=clsEHXW.p_strXWWBFilePath
                strFolderPath = EHFile.fnFolderPathGet(strFilePath=strFilePath)
                strFileNameOnly = EHFile.fnFileNameOnly(strFilePath=strFilePath)
            else:
                strFolderPath = EHFile.fnFolderOS()
                strFileNameOnly=c_strLogFileName
            if blnDropSplitor and c_strFileDateSplitor in strFileNameOnly:
                strFileNameOnly = strFileNameOnly.split(c_strFileDateSplitor)[0].strip()
            strFileNameExt=c_strLogFileExtName
            strFilePath = EHFile.fnFilePathJoin(strFolderPath, strFileNameOnly, strFileNameExt)
            s_strLogPath = strFilePath
            if blnSetRunning:
                clsEHMsg.p_strLogPath = s_strLogPath
            elif blnCleanDft:
                clsEHMsg.p_strLogPath = ''
        return s_strLogPath
    else:
        strFolderPath = EHFile.fnFolderPathGet(strFilePath=strFilePath)
        strFileNameOnly = EHFile.fnFileNameOnly(strFilePath=strFilePath)
        strFileNameExt = c_strLogFileExtName

        if len(strFolderPath)==0: strFolderPath = EHFile.fnFolderOS()
        if blnDropSplitor and c_strFileDateSplitor in strFileNameOnly:
            strFileNameOnly = strFileNameOnly.split(c_strFileDateSplitor)[0].strip()
        strFilePath = EHFile.fnFilePathJoin(strFolderPath, strFileNameOnly, strFileNameExt)
        if blnSetRunning:
            clsEHMsg.p_strLogPath = strFilePath
        elif blnCleanDft:
            clsEHMsg.p_strLogPath = ''
        return strFilePath

def fnLog(
        strMsg,
        strLogPath='',
        strFuncName='',
        blnLogClean=False
)->bool:
    if len(strMsg)==0: return False
    import EHDate
    strTime=EHDate.fnNow(blnStr=True)

    if len(strFuncName)>0: strMsg=': '.join([strFuncName, strErrMsg])
    strMsg=strMsg.replace(c_strNewLine, c_strNewLine + c_strTab)

    lstMsg= [strTime]
    lstMsg.append(strMsg)

    strLogPath=fnLogFilePath(strFilePath=strLogPath)

    import EHTxt
    EHTxt.fnTxtOper(
        strFilePath=strLogPath,
        blnWrite=True,
        strMsgWrite=' '.join(lstMsg),
        blnOverWrite=blnLogClean
    )
    return True
# <PyRegion: Log File>

# <PyRegion: Option Dialog>
def fnDlgOpt(
    strMsg:str,
    strTitle:str='',
    blnMsgOnly:bool=True
)->bool:
    appWinPrint = QApplication.instance()
    if appWinPrint is None:
        app = QApplication([])

    qmbMsg= QMessageBox()
    if blnMsgOnly:
        icoStyle=QMessageBox.Icon.Information
        btnStyle=QMessageBox.StandardButton.Ok
    else:
        icoStyle = QMessageBox.Icon.Question
        btnStyle=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    btnDft=QMessageBox.StandardButton.Yes

    qmbMsg.setIcon(icoStyle)
    if len(strTitle)=='': strTitle=' '
    qmbMsg.setWindowTitle(strTitle)
    qmbMsg.setText(strMsg)
    qmbMsg.setStandardButtons(btnStyle)
    qmbMsg.setDefaultButton(btnDft)

    blnResultRun=qmbMsg.exec()

    blnResult=(blnResultRun==QMessageBox.StandardButton.Yes)
    # qmbMsg.destroy()
    return blnResult
# <PyRegion: Option Dialog>