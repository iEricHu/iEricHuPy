# EHFile.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import os
import EHSymbolDef

# <PyDecl: Symbol Define & UDE import >
c_strPathSymbolLeft=EHSymbolDef.c_strPathSymbolLeft # '\'
c_strFileExtSymbol=EHSymbolDef.c_strFileExtSymbol # '.'
c_strFileNewSymbol=EHSymbolDef.c_strFileNewSymbol # '_'
# </PyDecl: Symbol Define & UDE import >

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHFile.py !')

import EHXW
def clsEHXW()->EHXW.EHXWClass:
    return EHXW.EHXWClass()
# </PyDecl: RunTime>

def fnFileNameOnly(strFilePath:str)->str:
    if isinstance(strFilePath, property):
        strFuncName = "EHFile.fnFileNameOnly"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not isinstance(strFilePath, str):
        strFuncName = "EHFile.fnFileNameOnly"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''

    if len(strFilePath)==0: return ''
    strFileNameOnly = os.path.basename(strFilePath)
    strFileNameOnly=strFileNameOnly.split(c_strFileExtSymbol)[0]
    return strFileNameOnly

def fnFileBaseName(strFilePath:str)->str:
    if isinstance(strFilePath, property):
        strFuncName = "EHFile.fnFileBaseName"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not isinstance(strFilePath, str):
        strFuncName = "EHFile.fnFileBaseName"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    return os.path.basename(strFilePath)

def fnFileNameExt(strFilePath:str)->str:
    if isinstance(strFilePath, property):
        strFuncName = "EHFile.fnFileNameExt"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not isinstance(strFilePath, str):
        strFuncName = "EHFile.fnFileNameExt"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''

    if len(strFilePath)==0: return ''
    strFileNameExt=os.path.splitext(strFilePath)[1]
    strFileNameExt=strFileNameExt.split(c_strFileExtSymbol)[-1]
    return strFileNameExt

def fnFilePathJoin(strFolderPath, strFileName, strFileExt='')->str:
    if isinstance(strFolderPath, property):
        strFuncName = "EHFile.fnFilePathJoin"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not isinstance(strFolderPath, str):
        strFuncName = "EHFile.fnFilePathJoin"
        strErrMsg = "strFolderPath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''

    if isinstance(strFileName, property):
        strFileName=getattr(strFileName,'_inner','')
    if not isinstance(strFileName, str):
        strFuncName = "EHFile.fnFilePathJoin"
        strErrMsg = "strFileName is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''

    if isinstance(strFileExt, property):
        strFileExt=getattr(strFileExt,'_inner','')
    if not isinstance(strFileExt, str):
        strFuncName = "EHFile.fnFilePathJoin"
        strErrMsg = "strFileExt is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''

    if len(strFileExt)>0: strFileName = strFileName + c_strFileExtSymbol + strFileExt

    strFilePath = os.path.join(strFolderPath, strFileName)
    return strFilePath

def fnFolderPathGet(strFilePath)->str:
    if isinstance(strFilePath, property):
        strFuncName = "EHFile.fnFolderPathGet"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not isinstance(strFilePath, str):
        strFuncName = "EHFile.fnFolderPathGet"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if len(strFilePath)==0: return ''
    strFolderPath = os.path.dirname(strFilePath)
    return strFolderPath

def fnFolderOS(
    blnOS:bool=False,
    mdlRun:object=None
)->str:
    # <PyCmt: mdlRun: Module Object>
    if not mdlRun is None:
        import inspect
        objCallerFrame: object = inspect.currentframe().f_back
        if not objCallerFrame is None:
            return fnFolderParent(strFilePath=objCallerFrame.f_code.co_filename)
    import EHXW
    if blnOS or not EHXW.p_blnXWMode:
        # <PyCmt: this py file path: __file__>
        import os
        return os.getcwd()
    else:
        return fnFolderParent(strFilePath = clsEHXW.p_strXWWBFilePath)

def fnFileJudge(strFilePath:str)->bool:
    return os.path.isfile(strFilePath)
def fnFilePathFormatted(strFilePath:str)->str:
    # <PyFunc: just like # strFilePath=strFilePath.replace('\\\\', '\\')>
    return os.path.normpath(strFilePath)

def fnFileExist(
    strFileName:str,
    strFolderPath:str='',
    blnFileNameNew:bool=False,
    intFileNew:int = 1
)->str:
    if len(strFolderPath)>0:
        strFilePath = \
            fnFilePathJoin(
                strFolderPath=strFolderPath,
                strFileName=strFileName
            )
    else:
        strFilePath=strFileName

    if len(os.path.dirname(strFilePath))==0:
        strFilePath=os.path.join(os.getcwd(), strFilePath)

    if os.path.exists(strFilePath):
        if blnFileNameNew:
            strFolderPath=fnFolderParent(strFilePath=strFilePath)
            strFileName = fnFileBaseName(strFilePath= strFilePath)
            strFileNameNew = \
                fnFileNameNew(
                    strFileName=strFileName,
                    intFileNew=intFileNew
                )
            strFilePath = \
                fnFileExist(
                    strFileName=strFileNameNew, 
                    strFolderPath=strFolderPath, 
                    blnFileNameNew=blnFileNameNew, 
                    intFileNew=intFileNew+1 
                )
        return strFilePath
    else:
        return strFilePath if blnFileNameNew else ''

def fnFileNameNew(
    strFileName:str,
    intFileNew:int
)->str:
    strFileNameBase=strFileName.split(c_strFileExtSymbol)[0]
    if intFileNew >0 and c_strFileNewSymbol in strFileNameBase:
        strFileNameBase=strFileNameBase.split(c_strFileNewSymbol)[0]
    strFileNameNew= \
        strFileNameBase.split(c_strFileExtSymbol)[0] + \
        c_strFileNewSymbol + str(intFileNew) + c_strFileExtSymbol + \
        strFileName.split(c_strFileExtSymbol)[1]
    return strFileNameNew
def fnFolderParent(strFilePath)->str:
    if isinstance(strFilePath, property):
        strFuncName = "EHFile.fnFolderParent"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not isinstance(strFilePath, str):
        strFuncName = "EHFile.fnFolderParent"
        strErrMsg = "strFilePath is not a string!"
        import EHMsg
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName
        )
        return ''
    if not c_strPathSymbolLeft in strFilePath: return ''
    return os.path.dirname(strFilePath)

def fnFolderChk(
    strFolderPath,
    blnCreate=False
)->str:
    blnErr = False
    if not c_strPathSymbolLeft in strFolderPath: blnErr = True
    if not os.path.exists(strFolderPath):
        if blnCreate:
            try:
                os.makedirs(strFolderPath)
            except Exception:
                blnErr = True
        else:
            blnErr = True
    if blnErr:
        strErrMsg = 'Folder not exist: %s' % strFolderPath
        strFuncName='EHFile.fnFolderChk'
        import EHMsg
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName= strFuncName, blnLog=True)
        return None
    return strFolderPath

def fnFilePathChk(strFilePath: str)->str:
    if not isinstance(strFilePath, str): return None
    if len(strFilePath) == 0: return None

    if fnFileExist(strFileName=strFilePath): return strFilePath

    if not c_strPathSymbolLeft in strFilePath:
        strFileName=strFilePath
    else:
        strFileName=strFilePath.split(c_strPathSymbolLeft)[-1]
    strFolderPath=os.getcwd()
    strFilePath=strFolderPath + c_strPathSymbolLeft + strFileName
    return strFilePath

def fnFilePicker(
    strWinCap:str = '',
    strWildcard:str = '',
    strDefaultDir:str = '',
    strFileName:str = '',
    blnWrite:bool = False
)->str | None:
    from PyQt6.QtWidgets import (
        QApplication,
        QFileDialog,
        QMessageBox
    )

    app = QApplication([])
    dlgFile = QFileDialog()

    if blnWrite:
        AcceptMode=QFileDialog.AcceptMode.AcceptSave
    else:
        AcceptMode = QFileDialog.AcceptMode.AcceptOpen

    dlgFile.setAcceptMode(AcceptMode)
    dlgFile.setFileMode(QFileDialog.FileMode.AnyFile)
    dlgFile.setNameFilter(strWildcard)
    dlgFile.setDefaultSuffix(strFileName)
    if strDefaultDir:
        dlgFile.setDirectory(strDefaultDir)

    if strWinCap:
        dlgFile.setWindowTitle(strWinCap)

    if dlgFile.exec() == QFileDialog.DialogCode.Accepted:
        file_path = dlgFile.selectedFiles()[0]
        strResult= file_path
    else:
        strResult= None
    dlgFile.destroy()
    app.exit(0)
    return strResult

    