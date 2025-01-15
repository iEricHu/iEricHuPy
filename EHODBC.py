# EHODBC.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import pyodbc

import EHDB
import EHSymbolDef
import EHUDE
import EHMsg

import EHNetwork
import EHFile

#<PyDecl: Symbol Config>
c_strNewLine:str = EHSymbolDef.c_strNewLine

c_strFileExtSymbol:str = EHSymbolDef.c_strFileExtSymbol
c_strVarbBracketLeft:str = EHSymbolDef.c_strVarbBracketLeft
c_strVarbBracketRight:str = EHSymbolDef.c_strVarbBracketRight
#<PyDecl: Symbol Config>

c_blnEHODBCDebugMode:bool = False

#<PyDecl: Specific String Config>
c_strCNNDBName:str = 'DBName'
c_strCNNUserID:str = 'UserID'
c_strCNNUserPwd:str = 'UserPwd'
c_strCNNCNNPwd:str = 'CNNPwd'
#</PyDecl: Specific String Config>

#<PyDecl: MySQL Config>
c_strCNNDftMySQL:str =  \
    'DRIVER={<DriverName>}' + \
    ';SERVER=<ServerAddress>' + \
    ';PORT=<ServerPort>' + \
    '<DBNameSection>' + \
    ';UID=<UserID>' + \
    ';Pwd=<UserPwd>' #+ \
    #';OPTION=16'
c_strDBTypeMySQL:str =  EHUDE.udeDBType.udeDBTypeMySQL.value
c_strCNNMySQLDBNameSection:str =  ';DATABASE=<DBName>'
c_strCNNDriverNameDftMySQL:str =  'MySQL ODBC 8.0 Unicode Driver'
c_strCNNUserIDMySQL:str = 'erpuser'
c_strCNNUserPwdMySQL:str = 'Zentel_ERPUser001'
#</PyDecl: MySQL Config>

#<PyDecl: MSSQL Config>
c_strCNNDftMSSQL:str =  \
    'DRIVER={<DriverName>}' + \
    ';SERVER=<ServerAddress>,<ServerPort>' + \
    ';DATABASE=<DBName>' + \
    ';UID=<UserID>' + \
    ';Pwd=<UserPwd>'
    #'OPTION=3;'
c_strDBTypeMSSQL:str = EHUDE.udeDBType.udeDBTypeMSSQL.value
c_strDriverNameDftMSSQL:str = 'SQL Server'
# c_strCNNUserIDMSSQL:str = 'erpuser'
# c_strCNNUserPwdMSSQL:str = 'user'
c_strCNNUserIDMSSQL:str = 'sa'
c_strCNNUserPwdMSSQL:str = 'sp54251806'
#</PyDecl: MSSQL Config>

#<PyDecl: Access Config>
# c_strCNNDftAccess:str = \
#     'Provider=Microsoft.Jet.OLEDB.4.0;' + \
#     'DATA SOURCE=<DBFilePath>;' + \
#     'Jet OLEDB:DATABASE PASSWORD=<CNNPwd>;' + \
#     '<JetSysDBSection>' + \
#     'USER ID=<UserID>;' + \
#     'PASSWORD=<UserPwd>; ' + \
#     'Mode=ReadWrite;'
# c_strAccessJetSysDBSection:str = 'Jet OLEDB:SYSTEM DATABASE=<SysDBFilePath>;'

c_strCNNDftAccess:str = \
    'Driver={Microsoft Access Driver (*.mdb, *.accdb)}' + \
    ';DBQ=<DBFilePath>' + \
    ';Pwd=<CNNPwd>' + \
    ';Mode=ReadWrite'
c_strDBTypeAccess:str = EHUDE.udeDBType.udeDBTypeAccess.value
c_strCNNPwdAccess:str = '6601'
c_strCNNUserIDAccess:str = 'Admin'
c_strCNNUserPwdAccess:str = ''
c_strMDWFileExtAccess:str = 'mdw'
#</PyDecl: Access Config>

#<PyDecl: DAO Config>
c_strDAOCNNAccess:str = \
    "DRIVER={<DriverName>}" + \
    ";UID=<UserName>" + \
    ";Pwd=<CNNPwd>" + \
    ";Trusted_Connection=Yes" + \
    ";OPTION=3"
#</PyDecl: DAO Config>

#<PyDecl: SpeclSet>
c_dictSpeclAttrColl:dict = \
    {'strSecName1':
         {'strAttrName1': 'AttrValue1',
          'strAttrName2': 'AttrValue2',
          'strAttrName3': 'AttrValue3'
          },
     'strSectName2':
         {c_strCNNUserID: 'AttrValue1',
          c_strCNNUserPwd: 'AttrValue2',
          c_strCNNCNNPwd: 'AttrValue3'
          }
     }
 #</PyDecl: SpeclSet>

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHODBC.py !')
# </PyDecl: RunTime>
def fnUserIDPwdGet(
        strSectName,
        udeDBTypeRun:EHUDE.udeDBType
)->list:
    lstCNNSecurity=['','','']
    blnSpeclAttrFill=False
    if  strSectName in c_dictSpeclAttrColl:
        dictSpeclAttrRun = c_dictSpeclAttrColl[strSectName]
        if c_strCNNUserID in dictSpeclAttrRun:
            lstCNNSecurity[0]=dictSpeclAttrRun[c_strCNNUserID]
            blnSpeclAttrFill = True
        if c_strCNNUserPwd in dictSpeclAttrRun:
            lstCNNSecurity[1]=dictSpeclAttrRun[c_strCNNUserPwd]
        if c_strCNNCNNPwd in dictSpeclAttrRun:
            lstCNNSecurity[2]=dictSpeclAttrRun[c_strCNNCNNPwd]
        if blnSpeclAttrFill:
            print('lstCNNSecurity: ', lstCNNSecurity)
            return lstCNNSecurity
    if udeDBTypeRun == EHUDE.udeDBType.udeDBTypeMySQL :
        lstCNNSecurity[0] = c_strCNNUserIDMySQL
        lstCNNSecurity[1] = c_strCNNUserPwdMySQL
    elif udeDBTypeRun == EHUDE.udeDBType.udeDBTypeMSSQL:
        lstCNNSecurity[0] = c_strCNNUserIDMSSQL
        lstCNNSecurity[1] = c_strCNNUserPwdMSSQL
    elif udeDBTypeRun == EHUDE.udeDBType.udeDBTypeAccess:
        lstCNNSecurity[0] = c_strCNNUserIDAccess
        lstCNNSecurity[1] = c_strCNNUserPwdAccess
        lstCNNSecurity[2] = c_strCNNPwdAccess
    else:
        strMsg = 'User ID/Password Get Error!'
        strFuncName = 'EHODBC.fnUserIDPwdGet'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
    return lstCNNSecurity

class EHODBCClass:
    def __init__(self,
                 strSectName,
                 dictCNN,
                 strDBName=''
                 )->EHUDE.udtCNN:
        self.s_udtCNN:EHUDE.udtCNN=None
        udtCNN=EHUDE.udtCNN()
        udtCNN.strSectName=strSectName
        udtCNN.dictCNN=dictCNN
        strCNN=''
        if EHDB.c_strINIKwdDBType in dictCNN:
            udtCNN.udeDBType=fnDBTypeCvrt(strDBType=dictCNN[EHDB.c_strINIKwdDBType])
        if len(strDBName)>0:
            udtCNN.strDBName = strDBName
        elif EHDB.c_strINIAttrNameDBName in dictCNN :
            udtCNN.strDBName=dictCNN[EHDB.c_strINIAttrNameDBName]

        if EHDB.c_strINIAttrNameDBNameSection in dictCNN:
            udtCNN.DBNameSection=dictCNN[EHDB.c_strINIAttrNameDBNameSection]
        elif len(udtCNN.strDBName)>0:
            udtCNN.DBNameSection = c_strCNNMySQLDBNameSection
        if EHDB.c_strINIAttrNameServerAddr in dictCNN:
            udtCNN.strServerAddr=dictCNN[EHDB.c_strINIAttrNameServerAddr]
        if EHDB.c_strINIAttrNameDBFilePath in dictCNN:
            udtCNN.strDBFilePath=dictCNN[EHDB.c_strINIAttrNameDBFilePath]
        strErrMsg = ''
        if EHDB.c_strINIKwdCNN in dictCNN:
            strCNN=dictCNN[EHDB.c_strINIKwdCNN]
        else:
            if EHDB.c_strDBTypeDft==c_strDBTypeMySQL:
                strCNN=c_strCNNDftMySQL
            elif EHDB.c_strDBTypeDft==c_strDBTypeMSSQL:
                strCNN=c_strCNNDftMSSQL
            elif EHDB.c_strDBTypeDft==c_strDBTypeAccess:
                strCNN=c_strCNNDftAccess
            else:
                strErrMsg='SectName: {} Can Not Find Connection String!'
                strFuncName='EHODBC.EHODBCClass'
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        if len(strErrMsg)==0: udtCNN.strCNN = strCNN

        strCNNRun=strCNN
        lstReplace=['<',EHDB.c_strINIAttrNameDBNameSection,'>']
        strReplace=''.join(lstReplace)
        strCNNRun=strCNNRun.replace(strReplace, udtCNN.DBNameSection)
        for strKey, strValue in dictCNN.items():
            lstReplace=['<',strKey,'>']
            strReplace=''.join(lstReplace)
            strCNNRun=strCNNRun.replace(strReplace, strValue)
        udtCNN.lstCNNSecurity = \
            fnUserIDPwdGet(
                strSectName=strSectName,
                udeDBTypeRun=udtCNN.udeDBType
            )
        strCNNRun = strCNNRun.replace(EHDB.c_strCNNKwdUserID, udtCNN.lstCNNSecurity[0])
        strCNNRun = strCNNRun.replace(EHDB.c_strCNNKwdUserPwd, udtCNN.lstCNNSecurity[1])
        strCNNRun = strCNNRun.replace(EHDB.c_strCNNKwdCNNPwd, udtCNN.lstCNNSecurity[2])
        if c_blnEHODBCDebugMode:
            strMsg = '__init__ strSectName: {}, strCNNRun: {}'.format(strSectName, strCNNRun)
            strFuncName = 'EHODBC.__init__'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName)
        udtCNN.strCNNRun=strCNNRun
        udtCNN.objCNN=\
            fnConnect(
                strCNN=strCNNRun,
                strServerAddr=udtCNN.strServerAddr,
                strDBFilePath=udtCNN.strDBFilePath
            )
        if not udtCNN.objCNN is None:
            udtCNN.objCursor=udtCNN.objCNN.cursor()
            self.blnCNN=True
        self.s_udtCNN = udtCNN

    @property
    def udtCNN(self):
        # EHODBCClass Init udtCNN
        return self.s_udtCNN
    def fnCNNClose(self):
        if self.blnCNN:
            for udtRun in self.udtCNN:
                try:
                    blnResult = udtRun.objCursor.close
                    print('udtRun.objCursor.close blnResult: {}'.formt(blnResult))
                    blnResult = udtRun.objCNN.close
                    print("udtRun.objCNN.close blnResult: {}".formt(blnResult))
                except pyodbc.Error as objErr:
                    strMsg = 'Connection close fail!' \
                        + c_strNewLine + 'strCNN: {}'.format(udtRun.strCNN) \
                        + c_strNewLine + objErr
                    strFuncName = 'EHODBC.fnCNNClose'
                    EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)

#<PyRegion: ODBC Func>
def fnConnect(
        strCNN,
        strServerAddr='',
        strDBFilePath=''
)->pyodbc.Connection:
    if len(strCNN)==0: return None
    if len(strServerAddr)>0:
        blnNetStatus = EHNetwork.fnNetworkPing(strIP=strServerAddr)
        if not blnNetStatus: return None
    elif len(strDBFilePath)>0:
        if len(EHFile.fnFileExist(strFileName=strDBFilePath))==0:
            return None
    # <PyCmt:64Bits MySLQ Driver only>
    try:
        objCNN = pyodbc.connect(strCNN)
        return objCNN
    except pyodbc.Error as objErr:
        #<PyDebug: record p_strCNNNotAvail?>
        strMsg = 'Connection build fail!' \
            + c_strNewLine + 'strCNN: {}'.format(strCNN) \
            + c_strNewLine + 'Err: {}'.format(str(objErr))
        strFuncName = 'EHODBC.fnConnect'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return None
#</PyRegion: ODBC Func>
#<PyRegion: DB General Func>
def fnDBTypeCvrt(strDBType)->EHUDE.udeDBType:
    udeDBTypeRun=EHUDE.udeDBType
    if strDBType==c_strDBTypeMySQL:
        udeDBTypeRun=EHUDE.udeDBType.udeDBTypeMySQL
    elif strDBType==c_strDBTypeMSSQL:
        udeDBTypeRun=EHUDE.udeDBType.udeDBTypeMSSQL
    elif strDBType==c_strDBTypeAccess:
        udeDBTypeRun=EHUDE.udeDBType.udeDBTypeAccess
    return udeDBTypeRun

def fnODBCDriverInfoGet(strDBType=''):
    lstRun=pyodbc.drivers()
    if len(strDBType)==0:
        return lstRun
    else:
        for strDriver in lstRun:
            if strDBType in strDriver: return strDriver
#</PyRegion: DB General Func>
#<PyRegion: DAO Connection Func>
def fnDAOCNNGet(
        strDBType,
        strUserName='',
        strCNNPwd='',
        strFilePath=''
)->object:
    strDriveName = fnODBCDriverInfoGet(strDBType=strDBType)
    if not '\\\\' in strFilePath and \
        '\\' in strFilePath:
        strFilePath=strFilePath.replace('\\', '\\\\')

    strCNN=c_strDAOCNNAccess
    strCNN=strCNN.replace('<DriverName>', strDriveName)
    strCNN=strCNN.replace('<UserName>', strUserName)
    strCNN=strCNN.replace('<CNNPwd>', strCNNPwd)
    strCNN=strCNN.replace('<DBFilePath>', strFilePath)
    objCNN = pyodbc.connect(strCNN)

    return objCNN
#</PyRegion: DAO Connection Func>
#<PyRegion: Access DB Func>
def fnAccessFilePathMDWGet(strPath='')->str:
    if strPath=='': return ''

    strDBFolderPath=EHFile.fnFolderParent(strFilePath=strPath)
    strDBFileNameOnly=EHFile.fnFileNameOnly(strFilePath=strPath)
    strDBFilePath= \
        EHFile.fnFilePathJoin(
            strFolderPath=strDBFolderPath,
            strFileName=strDBFileNameOnly,
            strFileExt=c_strMDWFileExtAccess
        )
    strDBFilePath=EHFile.fnFileExist(strFileName=strDBFilePath)
    return strDBFilePath
#</PyRegion: Access DB Func>

