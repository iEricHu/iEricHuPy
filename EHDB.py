# EHDB.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug
clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

# <PyCmt: import "Any" DataType>
from typing import Any

import datetime
import pyodbc

import EHUDE

import EHXW
import EHINI
import EHODBC
import EHSQLAnaly
import EHArray

# <PyDecl: Symbol Define & UDE import >
import EHSymbolDef
c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor # ';'
# </PyDecl: Symbol Define & UDE import >

#<PyDecl: DB INI>
c_strINIDBInitSectName:str = 'DBInit'
c_strINIDBInitAttrName:str = 'InitSection'

c_strINIDBSectNameDft:str = 'Database'
c_strDBTypeDft:str = EHUDE.udeDBType.udeDBTypeMySQL.value

c_strINIKwdCNN ='CNNStr'
c_strINIKwdDBType ='DBType'
c_strINIAttrNameDBName:str = 'DBName'
c_strINIAttrNameDBNameSection='DBNameSection'
c_strINIAttrNameServerAddr:str = 'ServerAddress'
c_strINIAttrNameDBFilePath:str = 'DBFilePath'
c_strINIAttrNameDBTblNameLCase='DBTableNameLowCase'

c_strCNNKwdUserID='<UserID>'
c_strCNNKwdUserPwd='<UserPwd>'
c_strCNNKwdCNNPwd='<CNNPwd>'

c_strUDTAttrKwdDBType:str = 'udeDBType'
c_strUDTAttrKwdDBName:str = 'strDBName'
c_strUDTAttrKwdServerAddr:str = 'strServerAddr'
c_strUDTAttrKwdDBFilePath:str = 'strDBFilePath'
c_strUDTAttrKwdStrCNN:str = 'strCNN'
c_strUDTAttrKwdObjCNN:str = 'objCNN'

#</PyDecl: DB INI>

c_strDBNameReplacement = "<EHDBName>"

#<PyCmt: Symbol & UDE import>'
c_strSQLSplitor=EHSymbolDef.c_strSQLSplitor
c_strDBNameAppendSymbol=EHSymbolDef.c_strDBNameAppendSymbol
udtCNN:type = EHUDE.udtCNN
udeDBTypeRun:type = EHUDE.udeDBType
#</PyCmt: Symbol & UDE import>'

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHDB.py !')
import EHSysMgt
c_strDBNameDft:str = EHSysMgt.c_strDBName

# </PyDecl: RunTime>

class EHDBClass:
    _instance=None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)#, *args, **kw)
            cls.s_strDBName = ''
            cls.dictUDTCNN = {}
            cls.dictUDTCNNFail = {}
            cls.s_strINIFilePath = None
            cls.blnInited=cls.fnDBInit(cls)
            if not cls.dictUDTCNN.get(c_strINIDBSectNameDft) is None:
                cls.s_udeDBType=cls.dictUDTCNN[c_strINIDBSectNameDft].udeDBType
        return cls._instance

    def __init__(self):
        if not self.blnInited:
            self.s_strDBName = ''
            self.dictUDTCNN = {}
            self.dictUDTCNNFail = {}
            self.s_strINIFilePath = None
        pass

    @property
    def p_strDBNameDft(self)->str:
        return c_strDBNameDft
    @property
    def p_udeDBType(self)->udeDBTypeRun:
        # <PyCmt: self.s_udeDBType AS Default Database Type[From '[Database] INI Section']>
        return self.s_udeDBType

    def fnDBInit(self):
        if c_blnEHDebugMode:
            strMsg='fnDBInit Started!'
            strFuncName = 'EHDB.fnDBInit'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName)

        if EHXW.p_blnXWMode:
            clsEHXW=EHXW.EHXWClass()
            self.s_strINIFilePath=EHINI.fnINIFilePath(clsEHXW.p_strXWWBFilePath)
        else:
            self.s_strINIFilePath=EHINI.fnINIFilePath(strFilePath = '')

        dictDBINI=EHINI.fnINIDictGet(strINIFilePath = self.s_strINIFilePath)

        if c_blnEHDebugMode:
            for strKey, varValue in dictDBINI.items():
                print('strKey: {}, varValue: {}'.format(strKey, varValue))

        lstDBSectNameColl:list=[]
        if c_strINIDBSectNameDft in dictDBINI:
            dictDBINIInit=dictDBINI[c_strINIDBInitSectName]
            if c_strINIDBInitAttrName in  dictDBINIInit:
                strInitSection=dictDBINIInit[c_strINIDBInitAttrName].strip()
                if len(strInitSection)>0: lstDBSectNameColl=strInitSection.split(c_strAttrSplitor)
        if not c_strINIDBSectNameDft in lstDBSectNameColl:
            lstDBSectNameColl.insert(0,c_strINIDBSectNameDft)

        if c_blnEHDebugMode:
            strMsg='lstDBSectNameColl: {}'.format(lstDBSectNameColl)
            strFuncName = 'EHDB.fnDBInit'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName)

        for strSectName in lstDBSectNameColl:
            if c_blnEHDebugMode:
                strMsg = 'fnDBInit strSectName:{}'.format(strSectName)
                strFuncName = 'EHDB.fnDBInit'
                EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName)

            clsEHODBC= \
                EHODBC.EHODBCClass(
                    strSectName=strSectName,
                    dictCNN=dictDBINI[strSectName]
                )
            if not clsEHODBC.udtCNN.objCNN is None:
                self.dictUDTCNN[strSectName]=clsEHODBC.udtCNN
                return True
            else:
                if c_blnEHDebugMode:
                    strMsg = 'fnDBInit strSectName:{} Fail!'.format(strSectName)
                    strFuncName = 'EHDB.fnDBInit'
                    EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName)
                self.dictUDTCNNFail[strSectName]=clsEHODBC.udtCNN

def fnDBDecoDBClsInit(func):
    # <PyFunc: fnDBDecoDBClsInit>
    #    Desc: for Non-XWMode Function Call clsEHDB, 
    #       before Func Launch, clsEHDB Init first!
    #    Use By:
    #    Noticed:
    #    Parameter:
    #    Option:
    #    Return:
    # </PyFunc: fnDBDecoDBClsInit>
    clsEHDB=EHDBClass()
    return func

@fnDBDecoDBClsInit
def fnDBCNNGet(
        strSectName='',
        strDBName='',
        strAttrName=''
)-> udtCNN | udeDBTypeRun | None | Any:
    strSectNameRun = strSectName
    if len(strSectNameRun) == 0: strSectNameRun = c_strINIDBSectNameDft
    clsEHDB=EHDBClass()
    if len(strDBName)==0: strDBName=clsEHDB.dictUDTCNN[strSectNameRun].strDBName

    if strSectNameRun+strDBName in clsEHDB.dictUDTCNN: strSectNameRun=strSectNameRun+strDBName

    if not strSectNameRun in clsEHDB.dictUDTCNN:
        if strAttrName == c_strUDTAttrKwdDBType: return udeDBTypeRun.udeDBTypeNA
        return None

    udtCNN = clsEHDB.dictUDTCNN[strSectNameRun]
    strDBNameExisted=udtCNN.strDBName
    if len(strDBName)>0 and \
        strDBNameExisted != strDBName:
        dictCNN=clsEHDB.dictUDTCNN[strSectNameRun].dictCNN
        dictCNN[c_strINIAttrNameDBName]=strDBName
        strSectNameNew=strSectNameRun+strDBName
        strSectNameNew=EHArray.fnDictNewKeyGet(dictRun=dictCNN, strKey=strSectNameNew)
        clsEHODBC = \
            EHODBC.EHODBCClass(
                strSectName=strSectNameNew,
                dictCNN=dictCNN
            )
        if not clsEHODBC.udtCNN.objCNN is None:
            clsEHDB.dictUDTCNN[strSectNameNew] = clsEHODBC.udtCNN
            udtCNN = clsEHODBC.udtCNN
        else:
            if c_blnEHDebugMode:
                strMsg = 'fnDBCNNGet strSectName:{} Fail!'.format(strSectNameNew)
                strFuncName = 'EHDB.fnDBCNNGet'
                EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName)
            clsEHDB.dictUDTCNNFail[strSectNameNew]=clsEHODBC.udtCNN
            udtCNN = None
            return udtCNN
    if len(strAttrName)==0: return udtCNN
    if strAttrName == c_strUDTAttrKwdDBType:
        if udtCNN is None: return udeDBTypeRun.udeDBTypeNA
        return udtCNN.udeDBType
    elif strAttrName == c_strUDTAttrKwdDBName :
        return udtCNN.strDBName
    elif strAttrName == c_strUDTAttrKwdServerAddr :
        return udtCNN.strServerAddr
    elif strAttrName == c_strUDTAttrKwdDBFilePath :
        return udtCNN.strDBFilePath
    elif strAttrName == c_strUDTAttrKwdStrCNN :
        return udtCNN.strCNN
    elif strAttrName == c_strUDTAttrKwdObjCNN :
        return udtCNN.objCNN
    elif strAttrName in udtCNN.dictCNN:
        return udtCNN.dictCNN[strAttrName]
    else:
        return None

def fnExecSQL(strSQL, strSectName='')->(bool, str, pyodbc.Row | pyodbc.Cursor | list | None):
    return fnDBRSTGet(strSQLRun=strSQL, strSectName=strSectName, blnExec=True)

@fnDBDecoDBClsInit
def fnDBRSTGet(
        strSQLRun:str,
        strSectName:str = '',
        strDBName:str = '',
        blnCursorOnly:bool = False,
        blnExec:bool = False,
        blnErrRtn:bool = False,
        blnSQLPrint:bool = False
)->(bool, str, pyodbc.Cursor | list | pyodbc.Row | None):
    # <PyFunc: fnDBRSTGet>
    #    Desc: Get [pyodbc.Cursor; InsertID:int; pyodbc.Row] via 'fnDBCNNGet':udtCNN
    #    Use By:
    #    Noticed:
    #    Parameter:
    #        Para1:
    #        Para2:
    #        Para3:
    #    Option:
    #        OptPara1:
    #        OptPara2:
    #        OptPara3:
    #    Return:
    #       1. blnResult:bool
    #       2. strErrMsg
    #       3.1. pyodbc.Cursor or
    #       3.2. InsertID:int list or
    #       3.3. pyodbc.Row
    # </PyFunc: fnDBRSTGet>

    if len(strSQLRun)==0:
        strErrMsg='strSQLRun is Empty!'
        strFuncName='EHDB.fnDBRSTGet'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                objDBRows=None
            )

    udtCNN = \
        fnDBCNNGet(
            strSectName=strSectName,
            strDBName=strDBName
        )
    if udtCNN is None:
        strErrMsg='udtCNN Get Fail!'
        strFuncName='EHDB.fnDBRSTGet'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                objDBRows=None
            )

    if c_blnEHDebugMode:
        strErrMsg='strSQLRun: {0}'.format(strSQLRun)
        strFuncName='EHDB.fnDBRSTGet'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName)

    strDBTableNameLowCase=\
        fnDBCNNGet(
            strSectName=strSectName,
            strAttrName=c_strINIAttrNameDBTblNameLCase
        )
    blnDBTableNameLowCase=(strDBTableNameLowCase.upper()=='TRUE')

    strSQLRunSub= \
        EHSQLAnaly.fnSQLDstru(
            strSQL=strSQLRun,
            udeDBTypeRun=udtCNN.udeDBType,
            blnDBTableNameLowCase=blnDBTableNameLowCase,
            blnSQLPrint=blnSQLPrint
        )
    #<PyDebug: <EHDBName>, considering MySQL or MSSQL type>
    strDBNameRun:str = ''
    if len(strDBName)>0: strDBNameRun=''.join([strDBName, c_strDBNameAppendSymbol])
    strSQLRunSub = strSQLRunSub.replace(c_strDBNameReplacement, strDBNameRun)
    if c_blnEHDebugMode:
        EHMsg.fnMsgPrt('udtCNN.strCNN: {}'.format(udtCNN.strCNN))
        EHMsg.fnMsgPrt('strSQLRunSub: {}'.format(strSQLRunSub))
    if blnSQLPrint:
        EHMsg.fnMsgPrt(strMsg='strSQLRunSub: {}'.format(strSQLRunSub), blnCmdPrint=blnSQLPrint)

    objCursor=None
    objDBRows=None
    blnResult = False
    strErrTitle=''
    lstInsertID = []
    objErr=None
    try:
        udtCNN.objCursor=udtCNN.objCNN.cursor()
        objCursor = udtCNN.objCNN.cursor()
        if c_blnEHDebugMode:
            EHMsg.fnMsgPrt('objCursor.execute(strSQLRunSub): {}'.format(strSQLRunSub))
        objCursor.execute(strSQLRunSub)
        if blnCursorOnly:
            #<PyCmt: objCursor.description>
            # 0. column name (or alias, if specified in the SQL)
            # 1. type code
            # 2. None
            # 3. internal size (in bytes)
            # 4. precision
            # 5. scale
            # 6. nullable (True/False)
            pass
        elif blnExec:
            objCursor.commit()
            lstInsertID=fnLastIDGet()
        else:
            objDBRows=objCursor.fetchall()
            objDBRows = fnDBRSTValueFilter(lstRun=objDBRows)
        blnResult=True

    except pyodbc.OperationalError as Err:
        objErr=Err
        strErrTitle='pyodbc.OperationalError'
    except pyodbc.DataError as Err:
        objErr = Err
        strErrTitle='pyodbc.DataError'
    except pyodbc.IntegrityError as Err:
        objErr = Err
        strErrTitle='pyodbc.IntegrityError'
    except pyodbc.ProgrammingError as Err:
        objErr = Err
        strErrTitle='pyodbc.ProgrammingError'
    except pyodbc.NotSupportedError as Err:
        objErr = Err
        strErrTitle='pyodbc.ProgrammingError'
    except pyodbc.DatabaseError as Err:
        objErr = Err
        strErrTitle='pyodbc.ProgrammingError'
    except pyodbc.Error as Err:
        objErr = Err
        strErrTitle='pyodbc.ProgrammingError'
    except BaseException as Err:
        objErr = Err
        strErrTitle = 'Else Exception!'

    if not blnCursorOnly: objCursor.close()
    if not blnResult:
        if c_blnEHDebugMode:
            print('blnResult=False, Debug! ')
            print('blnCursorOnly: ', blnCursorOnly)
            print('blnExec: ', blnExec)
            print('strSQLRunSub: ', strSQLRunSub)

        strErrMsg='DB Execution Error!' + \
            '\nstrSQLRun: {}, '.format(strSQLRunSub)+ \
            '\nErr: {}'.format(str(objErr))
        strFuncName='EHDB.fnDBRSTGet'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                objDBRows=None
            )
    strErrMsg=''
    if blnCursorOnly:
        return True, strErrMsg, objCursor
    elif blnExec:
        return True, strErrMsg, lstInsertID
    else:
        return True, strErrMsg, objDBRows

def fnDBRSTValueFilter(lstRun:pyodbc.Row):
    if len(lstRun)==0:
        return lstRun
    if len(lstRun[0])==1:
        return [Elm[0] for Elm in lstRun]
    elif isinstance(lstRun[0], pyodbc.Row):
        return [list(Elm) for Elm in lstRun]
    else:
        return lstRun

def fnLastIDGet()->list:
    strSQL='SELECT LAST_INSERT_ID() '
    strSQLRun=strSQL
    udtCNN = fnDBCNNGet()
    objCursor = udtCNN.objCNN.cursor()
    objCursor.execute(strSQLRun)
    objDBRows = objCursor.fetchall()
    lstDBRows=fnDBRSTValueFilter(lstRun=objDBRows)
    return list(lstDBRows)

def fnDBEZCNNGet(
        strSQL:str = '',
        strTblName:str = '',
        strServerAddr:str = '',
        strServerPort:str  = '',
        strDBName:str = '',
        strDBFilePath:str = '',
        strUserID:str = '',
        strUserPassword:str = ''
)->list | None:
    if len(strSQL)==0 and len(strTblName)==0:
        return None
    elif len(strSQL)==0:
        strSQL= 'SELECT * FROM <TblName> '
        strSQL=strSQL.replace('<TblName>', strTblName)

    udeDBTypeRun=EHUDE.udeDBType.udeDBTypeMySQL
    if len(strServerAddr)==0: strServerAddr = '127.0.0.1'
    if len(strServerPort)==0: strServerPort = '3306'
    if len(strDBName)==0:strDBName = ''
    if len(strDBFilePath)==0:strDBFilePath = ''

    strCNN=''
    strCNNPwd=''
    strDATABASESection=''
    strDriverName=''
    if udeDBTypeRun==EHUDE.udeDBType.udeDBTypeMySQL:
        strCNN=EHODBC.c_strCNNDftMySQL
        strDriverName=EHODBC.c_strCNNDriverNameDftMySQL
        if len(strUserID)==0:strUserID = EHODBC.c_strCNNUserIDMySQL
        if len(strUserPassword)==0: strUserPassword = EHODBC.c_strCNNUserPwdMySQL

        strDATABASESection=EHODBC.c_strCNNMySQLDBNameSection
    elif udeDBTypeRun == EHUDE.udeDBType.udeDBTypeMSSQL:
        strCNN = EHODBC.c_strCNNDftMSSQL
        strDriverName = EHODBC.c_strDriverNameDftMSSQL
        if len(strUserID) == 0: strUserID = EHODBC.c_strCNNUserIDMSSQL
        if len(strUserPassword)==0: strUserPassword = EHODBC.c_strCNNUserPwdMSSQL
    elif udeDBTypeRun == EHUDE.udeDBType.udeDBTypeAccess:
        strCNN = EHODBC.c_strCNNDftAccess
        strCNNPwd = EHODBC.c_strCNNPwdAccess
        if len(strUserID)==0: strUserID = EHODBC.c_strCNNUserIDAccess
        if len(strUserPassword)==0: strUserPassword = EHODBC.c_strCNNUserPwdAccess

    strCNNRun=strCNN
    strCNNRun = strCNNRun.replace('<DriveName>', strDriverName)
    strCNNRun = strCNNRun.replace('<ServerAddress>', strServerAddr)
    strCNNRun = strCNNRun.replace('<ServerPort>', strServerPort)
    strCNNRun = strCNNRun.replace('<DATABASESection>', strDATABASESection)
    strCNNRun = strCNNRun.replace('<DBName>', strDBName)
    strCNNRun = strCNNRun.replace('<DBFilePath>', strDBFilePath)
    strCNNRun = strCNNRun.replace('<CNNPwd>', strCNNPwd)
    strCNNRun = strCNNRun.replace('<SysDBFilePath>', EHODBC.fnAccessFilePathMDWGet(strPath=strDBFilePath) )
    strCNNRun = strCNNRun.replace('<UserID>', strUserID)
    strCNNRun = strCNNRun.replace('<UserPwd>', strUserPassword)

    objCNN=EHODBC.fnConnect(strCNN=strCNNRun, strServerAddr=strServerAddr)
    objCursor=objCNN.cursor()

    lstDBRow=[]
    try:
        lstDBRow=objCursor.execute(strSQL).fetchall()
    except Exception as Err:
        strFuncName='EHDB.fnDBEZCNNGet'
        strMsg='strSQL Exec Fail: {}'.format(strSQL) + \
            'Err: {}'.format(str(Err))
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
    return lstDBRow