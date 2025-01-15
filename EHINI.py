# EHINI.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

from configparser import ConfigParser

import EHUDE
import EHFile

# <PyDecl: Symbol Define & UDE import >
import EHSymbolDef
c_strNewLine = EHSymbolDef.c_strNewLine

c_strPathSymbolLeft=EHSymbolDef.c_strPathSymbolLeft # '\'
c_strFileExtSymbol=EHSymbolDef.c_strFileExtSymbol # '.'
c_strFileDateSplitor=EHSymbolDef.c_strFileDateSplitor # '-'
# </PyDecl: Symbol Define & UDE import >
c_strProgIniFileName = "EHPy"
c_strINIFileExt = 'ini'

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHINI.py !')
# </PyDecl: RunTime>

# <PyComment: Path Oper>
def fnINIFilePathGet(strFilePath, strFolderPath='', strFileName='')->str:
    if os.path.isfile(strFilePath):
        strFolderPath= os.path.dirname(strFilePath)
        strFileName = os.path.basename(strFilePath)
    elif os.path.isdir(strFilePath):
        strFolderPath = strFilePath
    elif os.path.isfile(strFileName):
        strFilePath=strFileName
        strFolderPath= os.path.dirname(strFilePath)
        strFileName = os.path.basename(strFilePath)
    elif os.path.isdir(strFileName):
        strFolderPath = strFileName

    if not os.path.isdir(strFolderPath): strFolderPath=''
    #<PyCmt: if len(strFolderPath) == 0: strFolderPath=Current PY File Folder Path >
    if len(strFolderPath) == 0: strFolderPath = os.getcwd()
    if len(strFileName)==0: strFileName=c_strProgIniFileName
    if not strFileName.endswith(c_strFileExtSymbol + c_strINIFileExt):
        if c_strFileExtSymbol in strFileName: strFileName=strFileName[:strFileName.find(c_strFileExtSymbol)]
        strFileName=strFileName+ c_strFileExtSymbol + c_strINIFileExt
    strFilePath = os.path.join(strFolderPath, strFileName)
    if c_blnEHDebugMode: print('strFilePath: {}'.format(strFilePath))
    return strFilePath
# </PyComment: Path Oper>

# <PyComment: INI Oper>
def fnINIOper(
        udeOperType=EHUDE.udeINIOperType.udeINIOperTypeRead,
        strINIFilePath='',
        strSectName='',
        strAttrName='',
        blnLog = False
):
    if len(strINIFilePath) == 0:
        import EHDB
        clsEHDB=EHDB.EHDBClass
        strINIFilePath=clsEHDB.p_strINIFilePath
    if not EHFile.fnFileExist(strINIFilePath):
        import EHMsg
        strErrMsg="1INI File Not Exist!" \
           + c_strNewLine + 'strINIFilePath: {}'.format(strINIFilePath)
        strFuncName='EHINI.fnINIOper'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=blnLog )
        return None

    if udeOperType == EHUDE.udeINIOperType.udeINIOperTypeRead:
        CfgPrs=ConfigParser()
        CfgPrs.optionxform = staticmethod(str)
        CfgPrs.read(strINIFilePath)
        if len(strSectName) == 0:
            return CfgPrs.sections()
        else:
            if len(strAttrName) == 0:
                lstINIAttr = []
                for varINIAttr in CfgPrs[strSectName]:
                    lstINIAttr.append(varINIAttr)
                return lstINIAttr
            else:
                try:
                    return CfgPrs[strSectName][strAttrName]
                except KeyError :
                    return ''

def fnINIDictGet(
    strINIFilePath,
    blnLog=False
)->dict:
    if not EHFile.fnFileExist(strINIFilePath):
        import EHMsg
        strErrMsg="INI File Not Exist!" \
           + c_strNewLine +'strINIFilePath: {}'.format(strINIFilePath)
        strFuncName='EHINI.fnINIDictGet'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=blnLog)
        return None

    dictINI={}
    lstSectName=fnINIOper(strINIFilePath=strINIFilePath)
    for strSectName in lstSectName:
        lstAttrName=\
            fnINIOper(
                udeOperType=EHUDE.udeINIOperType.udeINIOperTypeRead,
                strINIFilePath=strINIFilePath,
                strSectName=strSectName
            )
        dictAttrRun={}
        for strAttrName in lstAttrName:
            strAttrValue = \
                fnINIOper(
                    udeOperType=EHUDE.udeINIOperType.udeINIOperTypeRead,
                    strINIFilePath=strINIFilePath,
                    strSectName=strSectName,
                    strAttrName=strAttrName
                )
            dictAttrRun[strAttrName]=strAttrValue
        dictINI[strSectName]=dictAttrRun
    return dictINI
# </PyComment: INI Oper>
# <PyRegion: INI FIle Path Process>
def fnINIFilePath(strFilePath:str, blnDropSplitor:bool = True)->str:
    strFolderPath = EHFile.fnFolderPathGet(strFilePath = strFilePath)
    strFileNameOnly = EHFile.fnFileNameOnly(strFilePath = strFilePath)
    strFileNameExt = EHFile.fnFileNameExt(strFilePath = strFilePath)

    if len(strFolderPath)==0: strFolderPath=EHFile.fnFolderOS()

    if len(strFileNameOnly)==0: strFileNameOnly=c_strProgIniFileName
    if blnDropSplitor and  c_strFileDateSplitor in strFileNameOnly:
        strFileNameOnly=strFileNameOnly.split(c_strFileDateSplitor)[0].strip()

    strFileNameExt = c_strINIFileExt
    strFilePath=EHFile.fnFilePathJoin(strFolderPath, strFileNameOnly, strFileNameExt)
    strFilePath=EHFile.fnFilePathChk(strFilePath = strFilePath)
    return strFilePath
# </PyRegion: INI FIle Path Process>
