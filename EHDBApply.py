# EHDBApply.py
# <PyDecl: Module Init, Setup DebugMode>
import datetime

import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init, Setup DebugMode>

import os
from typing import List, Any

import pyodbc

import EHArray
import EHDB
import EHDate
import EHMsg
import EHSQLAnaly
import EHSymbolDef
import EHUDE
import EHUsrMgt

# <PyDecl: Symbol Define & UDE import >
c_strNewLine:str = EHSymbolDef.c_strNewLine #'\n'
c_strTab:str = EHSymbolDef.c_strTab #'\t'

c_strDecimalPoint:str = EHSymbolDef.c_strDecimalPoint #'.'
c_strSQLValueBracketSymbol:str = EHSymbolDef.c_strSQLValueBracketSymbol # '\''
c_strAttrSplitor:str = EHSymbolDef.c_strAttrSplitor # ';'
c_strLineSplitor:str = EHSymbolDef.c_strLineSplitor # '&;'
c_strSQLSplitor:str = EHSymbolDef.c_strSQLSplitor #', '
c_strSQLBracketLeft:str = EHSymbolDef.c_strSQLBracketLeft #'('
c_strSQLBracketRight:str = EHSymbolDef.c_strSQLBracketRight #')'
c_strSQLCommaSplitor:str = EHSymbolDef.c_strSQLCommaSplitor #','

c_strDBInsertBracketReplace:str = c_strSQLValueBracketSymbol
c_strDBInsertBracketReplaceNew:str = \
    c_strSQLValueBracketSymbol + \
    c_strSQLValueBracketSymbol
c_strDBInsertNewLineReplace:str = '\n'
c_strDBInsertNewLineReplaceNew:str = EHSymbolDef.c_strNewLine #'\n'
# </PyDecl: Symbol Define & UDE import >

# <PyDecl: dictColSchema >
c_strTblCreateTmplt:str = \
    '<CreateTbl><TblName> ' + \
    '(' + \
    ' <SQLColTblCrt>' + \
    '<PrmKeyStr>' + \
    '<UqeNoStr>' + \
    ')'
c_strTblColSchemaTmplt:str = '<DataType><DataLenStr>'
c_strTblCrtColTmplt:str = '<ColName> <DataType><DataLenStr><NullableStr><AutoIncrementSrt>'
c_strTblCrtNullableTmplt:str = ' NOT NULL'
c_strTblCrtAutoIncrementTmplt:str = ' AUTO_INCREMENT'
c_strTblCrtDataLenTmplt:str = ''
c_strTblCrtDataLenTmpltNumChr:str = '(<DataLen>)'
c_strTblCrtPrimaryKeyTmplt:str = ', PRIMARY KEY(<PrmKeyCol>)'
c_strTblCrtUniqueNoTmplt:str = ', UNIQUE INDEX <UqeNo>_UNIQUE(<UqeNo> ASC)'

c_strSQLColSeltTmpltNum:str = 'IIF(ISNULL(<ColName>),\'<ColValueDefault>\',<ColName>) AS <ColNameAlias>'
c_strSQLColSeltTmpltBool:str = 'IIF(ISNULL(<ColName>),\'<ColValueDefault>\',<ColName>) AS <ColNameAlias>'
c_strSQLColSeltTmpltDate:str = 'IIF(ISNULL(<ColName>),\'<ColValueDefault>\',<ColName>) AS <ColNameAlias>'
c_strSQLColSeltTmpltText:str = 'TRIM(IIF(ISNULL(<ColName>),\'<ColValueDefault>\',<ColName>)) AS <ColNameAlias>'

c_strSQLColUpdApdTmpltNum:str = '<ColName>=<ColName>+<ColValue>'
c_strSQLColUpdApdTmpltBool:str = '<ColName>=<ColName> AND <ColValue>'
c_strSQLColUpdApdTmpltText:str = '<ColName>=CONCAT(<ColName>,IF(LENGTH(<ColName>)>0,\',\',\'\'),\'<ColValue>\')'
c_strSQLColUpdTmplt:str = '<ColName>=<ColValue> '
# </PyDecl: dictColSchema>

# <PyDecl: System DB Default ColName>
c_strColSchemaDictTmplt:str = '<DataType><DataLenStr>'

c_strDBTblColNameUqeNo:str = 'UniqueNo'
c_strDBTblColDataTypeUqeNo:str = 'int'
c_strTblCrtDataLenTmpltUqeNo:str = c_strTblCrtDataLenTmplt
c_intDBTblColDataLenUqeNo:int = 0

c_strDBTblColNameDeleted:str = 'Deleted'
c_strDBTblColDataTypeDeleted:str = 'varchar'
c_strTblCrtDataLenTmpltDeleted:str = c_strTblCrtDataLenTmpltNumChr
c_intDBTblColDataLenDeleted:int = 1
c_strDBTblColValDftDeleted:str='N'

c_strDBTblColNameLastVer:str = 'LastVer'
c_strDBTblColDataTypeLastVer:str = 'varchar'
c_strTblCrtDataLenTmpltLastVer:str = c_strTblCrtDataLenTmpltNumChr
c_intDBTblColDataLenLastVer = 1
c_strDBTblColValDftLastVer:str='Y'

c_strDBTblColNameUploader:str = 'Uploader'
c_strDBTblColDataTypeUploader:str = 'varchar'
c_strTblCrtDataLenTmpltUploader:str = c_strTblCrtDataLenTmpltNumChr
c_intDBTblColDataLenUploader = 20
c_strDBTblColValDftUploader:str='<Uploader>'

c_strDBTblColNameUpdateTime:str = 'UpdateTime'
c_strDBTblColDataTypeUpdateTime:str = 'datetime'
c_strTblCrtDataLenTmpltUpdateTime:str = c_strTblCrtDataLenTmplt
c_intDBTblColDataLenUpdateTime:int = 0
c_strDBTblColValDftUpdateTime:str='<UpdateTime>'

c_lstDBSysColName:list = \
    [c_strDBTblColNameUqeNo, c_strDBTblColNameDeleted, c_strDBTblColNameLastVer,
     c_strDBTblColNameUploader, c_strDBTblColNameUpdateTime]

c_lstDBSysColDataType:list = \
    [c_strDBTblColDataTypeUqeNo, c_strDBTblColDataTypeDeleted, c_strDBTblColDataTypeLastVer,
     c_strDBTblColDataTypeUploader, c_strDBTblColDataTypeUpdateTime]

c_lstDBSysColDataLenTmplt:list = \
    [c_strTblCrtDataLenTmpltUqeNo, c_strTblCrtDataLenTmpltDeleted, c_strTblCrtDataLenTmpltLastVer,
     c_strTblCrtDataLenTmpltUploader, c_strTblCrtDataLenTmpltUpdateTime]

c_lstDBSysColDataLen:list = \
    [c_intDBTblColDataLenUqeNo, c_intDBTblColDataLenDeleted, c_intDBTblColDataLenLastVer,
     c_intDBTblColDataLenUploader, c_intDBTblColDataLenUpdateTime]
# </PyDecl: System DB Default ColName>

# <PyDecl: DataType>
c_strMySQLDataTypeInt:str = 'int'  # MySQL DB: INT
c_strMySQLDataTypeFloat:str = 'float'  # MySQL DB: FLOAT
c_strMySQLDataTypeDbl:str = 'double'  # MySQL DB: DOUBLE
c_strMySQLDataTypeDecimal:str = 'decimal'  # MySQL DB: DECIMAL()
c_strMySQLDataTypeBool:str = 'bool'  # MySQL DB: BOOLEAN
c_strMySQLDataTypeVarChar:str = 'varchar'  # MySQL DB: VARCHAR()
c_strDataTypeStr:str = 'str'  # MySQL DB: VARCHAR()
c_strMySQLDataTypeDateTime:str = 'datetime'  # MySQL DB: DATETIME
c_strMySQLDataTypeDate:str = 'date'  # MySQL DB: DATETIME
c_strMySQLDataTypeTime:str = 'time'  # MySQL DB: TIME
c_strMySQLDataTypeBin:str = 'bin'
c_strMySQLDataTypeBLOB:str = 'BLOB'
c_lstMySQLDataType:list = [c_strMySQLDataTypeInt, c_strMySQLDataTypeFloat,
    c_strMySQLDataTypeDbl, c_strMySQLDataTypeDecimal, c_strMySQLDataTypeBool, c_strMySQLDataTypeVarChar,
    c_strMySQLDataTypeDateTime, c_strMySQLDataTypeDate]
c_lstMySQLDataTypeNum= [c_strMySQLDataTypeInt, c_strMySQLDataTypeFloat,
    c_strMySQLDataTypeDbl, c_strMySQLDataTypeDecimal]
c_lstMySQLDataTypeBool:list = [c_strMySQLDataTypeBool]
c_lstMySQLDataTypeText:list = [c_strMySQLDataTypeVarChar, c_strDataTypeStr]
c_lstMySQLDataTypeDateTime:list = [c_strMySQLDataTypeDateTime, c_strMySQLDataTypeDate, c_strMySQLDataTypeTime]

c_strNumFmtInt:str = '0'
c_strNumFmtDecimal:str = '0.0'
c_strNumFmtCurrency:str = '$0'
c_strNumberDBNumDft:str = '0'
c_strNumFmtBool:str = '@'
c_strNumFmtBoolDft:str = 'FALSE'

c_strNumFmtDateTime:str = 'YYYY/MM/DD HH:MM:SS'
c_strValDateTimeDft:str = '1900/00/00 00:00:00'
c_strNumFmtDBDateTime:str = 'YYYY-MM-DD HH:MM:SS'
c_strValDBDateTimeDft:str = '1900-00-00 00:00:00'
c_strNumFmtDBDateTimeFull:str = 'YYYY-MM-DD HH:MM:SS.0000'
c_strValDateTimeFullDft:str = '1900-00-00 00:00:00.0000'
c_strNumFmtDateTimeSmall:str = 'YYYY/MM/DD HH:MM'
c_strValDateTimeSmallDft: str = '1900/01/01 00:00'
c_strNumFmtDBDateTimeSmall:str = 'YYYY-MM-DD HH:MM'
c_strValDBDateTimeSmallDft:str = '1900-00-00 00:00'
c_strNumFmtDate1:str = 'YYYY/MM/DD'
c_strNumFmtDate2:str = '0000/00/00'
c_strNumFmtDate3:str = 'YYYYMMDD'
c_strNumFmtMonth:str = 'YYYY/MM'
c_strNumFmtMonth2:str = 'YYYYMM'
c_strNumFmtMonth1st:str = 'YYYY/MM/01'
c_strValDateDft:str = '1900/01/01'
c_strNumFmtDBDate:str = 'YYYY-MM-DD'
c_strValDBDateDft:str = '1900-01-01'
c_strNumFmtTime:str = 'hh:nn:ss'
c_strValTimeDft:str = '00:00:00'
c_strNumFmtTimeMicroSec:str = '#0.000000'
c_strNumFmtStr:str = '@'
c_strValStrDft:str = ''
c_strNumFmtGUID:str = 'GUID'
# </PyDecl: DataType>
c_intDBTblEnumColPosDBName:int = 0
c_intDBTblEnumColPosTblName:int = 2
c_intDBTblEnumColPosObjType:int = 3

# <PyDecl: varTableColSchema>
c_intTblColSchemaColPos:int = 0
c_intTblColSchemaColName:int = 1
c_intTblColSchemaColDataType:int = 2
c_intTblColSchemaColDataLen:int = 3
c_intTblColSchemaColDataScale:int = 4
c_intTblColSchemaColNullable:int = 5
c_intTblColSchemaColPrmKey:int = 6
c_intTblColSchemaColNumFmt:int = 7
c_intTblColSchemaColSQLDftValue:int = 8
c_intTblColSchemaColSQLColCrtTbl:int = 9
c_intTblColSchemaColSQLColSelt:int = 10
c_intTblColSchemaColSQLColUpdApd:int = 11
c_intTblColSchemaColSQLColErrMsg:int = 12
c_intTblColSchemaCount:int = c_intTblColSchemaColSQLColErrMsg
# </PyDecl: varTableColSchema>

# <PyDecl: DBUpdate>
c_strSQLUqeNoCrta:str = '<UqeNoColName>=\'<UqeNoColValue>\' '
# </PyDecl: DBUpdate>

# <PyDecl: RunTime>
clsEHUsrMgt=EHUsrMgt.EHUsrMgtClass()
if c_blnEHDebugMode: print('DebugMode Entry: EHDBApply.py !')
# </PyDecl: RunTime>

class EHDBApplyClass(object):
    _instance = None

    def __new__(cls, *args: object, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls) #, *args, **kw)
            cls.s_lstSysTbl = []
            cls.s_dictTblSchema = {}
            cls.fnDBApplyInit(cls)
        return cls._instance

    def __init__(self):
        pass

    @property
    def p_lstSysTbl(self) -> list:
        return self.s_lstSysTbl

    @property
    def p_dictTblSchema(self) -> dict:
        return self.s_dictTblSchema

    def fnDBApplyInit(self):
        pass
        # <PyCmt: Get s_lstSysTbl>
        # if len(self.s_lstSysTbl)==0 :
        #     strCriteria = \
        #         "Deleted<>'Y' " + \
        #         "AND LastVer='Y' " + \
        #         "AND TableShow<>'Y' "
        #     self.s_lstSysTbl = \
        #         fnDBRSTValueGet(
        #             strTblName=EHSysMgt.c_strTblNameSysTbl,
        #             strSectName=EHDB.c_strINIDBSectNameDft,
        #             lstColName=['TableName'],
        #             strCriteria=strCriteria
        #         )

# <PyRegion: DBCol>
def fnDBColSchemaGet(
        strSQLRun:str = '',
        strTblName:str = '',
        strSectName:str = '',
        strDBName:str = '',
        lstColNameCollUser:list = None,
        blnColNameUserSeqOnly:bool = False,
        lstElmCol:list = None,
        blnSysDftColElm:bool = False,
        blnValBlkSkip:bool = True,
        blnWithTblHead:bool = False,
        blnErrRtn:bool=False
) -> (bool, str, list | None, list | str | None):
    # <PyFunc: fnDBColSchemaGet>
    # Desc: Get DBColSchema from strSQL or DBTbl
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #       strSQLRun or strTblName
    #       strSectName= INI Config Section Name
    #       strTblName= DB TableName
    #       lstColNameCollUser= Get ColSchema with User Dedicated
    #       blnColNameUserSeqOnly= User defined 'lstColNameCollUser' for Show Out Seq Only
    #       lstElmCol= User defined Eliminate Col
    #       blnSysDftColElm= Eliminate 'UniqueNo', 'Deleted', 'LastVer', 'Uploader', 'UpdateTime' Cols
    #       blnWithTblHead= return List with ColName in Title Row
    #   Return:
    #       1. blnResult: bool
    #       2. strError: string
    #       3. DBColSchema: list (lstColSchema)
    #       4. DBColList: list (lstColName)
    # </PyFunc: fnDBColSchemaGet>

    strErrMsg=''
    if len(strSQLRun) == 0 and len(strTblName) == 0:
        strErrMsg = 'strSQLRun or strTblName Not Assign Yet!'
        strFuncName = 'EHDBApply.fnDBColSchemaGet'
        if blnErrRtn: return False, None, None, strErrMsg
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return False, strErrMsg, None, None

    if len(strSectName) == 0: strSectName = EHDB.c_strINIDBSectNameDft

    lstElmCol = \
        fnDBColElmGet(
            lstElmCol=lstElmCol,
            blnSysDftColElm=blnSysDftColElm,
        )

    # <PyCmt: get from previous Record: p_dictTblSchema >
    clsEHDBApply = EHDBApplyClass()
    strSectTblDictKey = strSectName + EHSymbolDef.c_strAttrSubNameSplitor + strTblName
    lstDictValue = clsEHDBApply.p_dictTblSchema.get(strSectTblDictKey)
    if not lstDictValue is None:
        lstColSchema = []
        lstColName = []
        for lstColSchemaRow in lstDictValue:
            strColName = lstColSchemaRow[c_intTblColSchemaColName]
            if not lstElmCol:
                lstColSchema.append(lstColSchemaRow)
                lstColName.append(strColName)
        return Ture, strErrMsg, lstColSchema, lstColName

    lstColSchema = []
    lstColName = []
    lstTblColSchemaTmplt:List[Any] =[''] *(c_intTblColSchemaCount+1)
    lstTblColSchemaOrig = []
    if blnWithTblHead:
        lstTblColSchemaRun = \
            ['ColPos', 'ColName', 'DataType', 'DataLen', 'DataScale', 'Nullable', 'PrimaryKey',
             'NumFmt', 'SQLDftValue', 'SQLColSelt', 'SQLUpdApd', 'ErrMsg']
        lstColSchema.append(lstTblColSchemaRun)

    udeDBType = \
        EHDB.fnDBCNNGet(
            strSectName=strSectName,
            strDBName=strDBName,
            strAttrName='udeDBType'
        )
    if udeDBType==EHUDE.udeDBType.udeDBTypeNA:
        strErrMsg = 'udeDBType == udeDBTypeNA!'
        strFuncName = 'EHDBApply.fnDBColSchemaGet'
        if blnErrRtn:
           return False, strErrMsg, None, None
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return False, None, None, strErrMsg
    elif udeDBType != EHUDE.udeDBType.udeDBTypeMySQL and \
        udeDBType != EHUDE.udeDBType.udeDBTypeMSSQL and \
        udeDBType != EHUDE.udeDBType.udeDBTypeAccess:
        strErrMsg = 'Beside MySQL, MSSQL, MSAccess, fnDBColSchemaGet Not Ready Yet!'
        strFuncName = 'EHDBApply.fnDBColSchemaGet'
        if blnErrRtn:
            return False, strErrMsg, None, None
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return False, strErrMsg, None, None

    if len(strSQLRun) == 0:
        strSQLRun = 'SELECT * FROM <TblName> '
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
    blnResult, strErrMsg, objCursorExec = \
        EHDB.fnDBRSTGet(
            strSQLRun = strSQLRun,
            strSectName = strSectName,
            strDBName = strDBName,
            blnCursorOnly = True,
            blnErrRtn = blnErrRtn
        )
    if not blnResult:
        return False, strErrMsg, None, None

    objColDescColl = objCursorExec.description
    if objColDescColl is None:
        strErrMsg = "Cursor Description is None!"
        strFuncName = "EHDBApply.fnDBColSchemaGet"
        return EHDebug.fnErrRtn(
            blnResult=blnResult,
            strErrMsg=strErrMsg,
            strFuncName=strFuncName,
            blnErrRtn=blnErrRtn,
            DBColSchema=None,
            DBColList=None
            )

    # <PyCmt: cursor.description tuple define>
    # tupCol[0]: ColName
    # tupCol[1]: DataType
    # tupCol[2]: None
    # tupCol[3]: DataLen
    # tupCol[5]: DataScale
    # tupCol[6]: Nullable
    # <PyCmt: EH Define>
    # 0. ColPos
    # 1. ColName (tupCol[0])
    # 2. DataType (tupCol[1].__name__)
    # 3. DataLen  (tupCol[3])
    # 4. DataScale (tupCol[5])
    # 5. Primary Key
    # 6. Nullable (tupCol[6])
    # 7. NumFmt
    # 8. SQL Default Value
    # 9. Col Select SQL
    # 10. Update Col SQL

    lstErrMsg:list=[]
    intColRun = 1
    for tupCol in objCursorExec.description:
        blnColElm = False
        strColName = tupCol[0]
        strColPos = intColRun
        strColDataType = tupCol[1].__name__
        strColDataType = strColDataType.lower()
        intDataLen = tupCol[3]
        intDataScale = tupCol[5]
        blnColNullable = tupCol[6]

        # <PyCmt: ColPos process>
        if not lstColNameCollUser is None:
            if strColName in lstColNameCollUser:
                if blnColNameUserSeqOnly: strColPos = '0' + str(lstColNameCollUser.index(strColName))
            else:
                blnColElm = True
        blnResult, strErrMsg, dictColSchema = \
            fnDBColSngSchemaDictCvrt(
                strColName=strColName,
                strColDataType=strColDataType,
                intDataLen=intDataLen,
                intDataScale=intDataScale,
                blnValBlkSkip=blnValBlkSkip,
                blnColNullable=blnColNullable,
                blnErrRtn = True
            )
        if not blnResult:
            lstErrMsg.append(strErrMsg)
        else:
            strColDataType = dictColSchema['strColDataType']
            intDataLen = dictColSchema['intDataLen']
            blnColNullable = dictColSchema['blnColNullable']
            blnColPrmKey = dictColSchema['blnColPrmKey']
            strColNumFmt = dictColSchema['strColNumFmt']
            strSQLColDft = dictColSchema['strSQLColDft']
            strSQLColTblCrt = dictColSchema['strSQLColTblCrtRun']
            strSQLColSelt = dictColSchema['strSQLColSeltRun']
            strSQLColUpd = dictColSchema['strSQLColUpdRun']

            lstTblColSchemaRun = lstTblColSchemaTmplt.copy()
            lstTblColSchemaRun[c_intTblColSchemaColPos] = int(strColPos)
            lstTblColSchemaRun[c_intTblColSchemaColName] = strColName
            lstTblColSchemaRun[c_intTblColSchemaColDataType] = strColDataType
            lstTblColSchemaRun[c_intTblColSchemaColDataLen] = intDataLen
            lstTblColSchemaRun[c_intTblColSchemaColDataScale] = intDataScale
            lstTblColSchemaRun[c_intTblColSchemaColPrmKey] = blnColPrmKey
            lstTblColSchemaRun[c_intTblColSchemaColNullable] = blnColNullable
            lstTblColSchemaRun[c_intTblColSchemaColNumFmt] = strColNumFmt
            lstTblColSchemaRun[c_intTblColSchemaColSQLDftValue] = strSQLColDft
            lstTblColSchemaRun[c_intTblColSchemaColSQLColCrtTbl] = strSQLColTblCrt
            lstTblColSchemaRun[c_intTblColSchemaColSQLColSelt] = strSQLColSelt
            lstTblColSchemaRun[c_intTblColSchemaColSQLColUpdApd] = strSQLColUpd

            if not blnColElm:
                lstColSchema.append(lstTblColSchemaRun)
                lstColName.append(strColName)
            lstTblColSchemaOrig.append(lstTblColSchemaRun)
        intColRun += 1
    if len(lstErrMsg)>0:
        strFuncName='EHDBApply.fnDBColSchemaGet'
        strErrMsg=c_strNewLine.join(lstErrMsg)
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                DBColSchema = None,
                DBColList = None
            )
    clsEHDBApply.s_dictTblSchema[strSectTblDictKey] = lstTblColSchemaOrig
    lstColSchema = EHArray.fnArraySort(lstRun=lstColSchema)
    return True, strErrMsg, lstColSchema, lstColName

def fnDBColElmGet(
        lstElmCol: list,
        blnSysDftColElm=False,
        blnUqeNoGet:bool = False
) -> list:
    # <PyFunc: fnDBColElmGet>
    #   Desc: Return Default Eliminate Col list
    # </PyFunc: fnDBColElmGet>
    if blnSysDftColElm:
        if not blnUqeNoGet and not c_strDBTblColNameUqeNo in lstElmCol: lstElmCol.append(c_strDBTblColNameUqeNo)
        if not c_strDBTblColNameDeleted in lstElmCol: lstElmCol.append(c_strDBTblColNameDeleted)
        if not c_strDBTblColNameLastVer in lstElmCol: lstElmCol.append(c_strDBTblColNameLastVer)
        if not c_strDBTblColNameUploader in lstElmCol: lstElmCol.append(c_strDBTblColNameUploader)
        if not c_strDBTblColNameUpdateTime in lstElmCol: lstElmCol.append(c_strDBTblColNameUpdateTime)
    return lstElmCol

def fnDBColStrSchemaDictCvrt(
        strColName: str,
        strColDataType: str,
        blnColWithSysDft: bool = False,
        strSplitor: str = c_strAttrSplitor
)->dict:
    # <PyFunc: fnDBColStrSchemaDictCvrt>
    #   Desc: String -> Dict: dictColSchema['strColName'] = strColValue
    #       Convert strColName, strColDataType to dictColSchema
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strColName: DB TableName
    #      strColDataType= Insert ColName
    #   Option:
    #   Return: dictTblSchema
    # </PyFunc: fnDBColStrSchemaDictCvrt>
    dictColSchema:dict = {}
    lstColName=strColName.split(strSplitor)
    lstColName=[strColName.strip() for strColName in lstColName]
    lstColName = [strColName.replace(' ', '') for strColName in lstColName]

    lstColDataType=strColDataType.split(strSplitor)
    if len(lstColName)!=len(lstColDataType):
        strErrMsg = 'fnDBColSngSchemaDictCvrt: strColName, strColDataType Qty Not Match!'
        dictColSchema['strErrMsg'] = strErrMsg
        dictColSchema['ColNameColl']=strColName
        dictColSchema['strColDataType']=strColDataType
        return dictColSchema

    for tupColSchema in zip(lstColName,lstColDataType):
        strColName=tupColSchema[0].strip()
        strColSchema=tupColSchema[1].strip()
        dictColSchema[strColName]=strColSchema
    if blnColWithSysDft:
        lstColName:list=list(dictColSchema.keys())
        lstColNameUpper:list = list(map(str.upper, dictColSchema.keys()))
        intRun=0
        for strColNameSys in c_lstDBSysColName:
            if not strColNameSys.upper() in lstColNameUpper or \
                (strColNameSys.upper() in lstColNameUpper and not strColNameSys in lstColNameUpper):
                if strColNameSys.upper() in lstColNameUpper and not strColNameSys in lstColNameUpper:
                    dictColSchema.pop(lstColName[lstColNameUpper.index(strColNameSys.upper())])
                strTblCrtColRun=c_strColSchemaDictTmplt
                strTblCrtColRun = strTblCrtColRun.replace('<DataType>',  c_lstDBSysColDataType[intRun])
                strTblCrtColRun = strTblCrtColRun.replace('<DataLenStr>', c_lstDBSysColDataLenTmplt[intRun])
                strTblCrtColRun = strTblCrtColRun.replace('<DataLen>', str(c_lstDBSysColDataLen[intRun]))
                dictColSchema[strColNameSys] = strTblCrtColRun
            intRun+=1
    return dictColSchema

def fnDBColDictSchemaCvrt(dictTblSchema:dict)->(bool, list|str):
    # <PyFunc: fnDBColSchemaCvrt>
    # Desc: dictColSchema->lstColSchema[c_intTblColSchemaCount+1]
    #   Follow fnDBColSchemaGet Output Format to convert dictTblSchema to lstColSchema
    #   dictTblSchema strKey as ColName, strValue as Col Data Type
    # Use By:
    # Noticed: Decided UniqueNo Col Position as First Col
    #           Not Included Nullable and PriKey of UniqueNo
    # Parameter:
    # Option:
    # Remark:
    #   c_intTblColSchemaColPos = 0
    #   c_intTblColSchemaColName = 1
    #   c_intTblColSchemaColDataType = 2
    #   c_intTblColSchemaColDataLen = 3
    #   c_intTblColSchemaColDataScale = 4
    #   c_intTblColSchemaColPrmKey = 5
    #   c_intTblColSchemaColNullable = 6
    #   c_intTblColSchemaColNumFmt = 7
    #   c_intTblColSchemaColSQLDftValue = 8
    #   c_intTblColSchemaColSQLColCrtTbl = 9
    #   c_intTblColSchemaColSQLColSelt = 10
    #   c_intTblColSchemaColSQLColUpdApd = 11
    # </PyFunc: fnDBColSchemaCvrt>
    lstColSchema = []
    lstErrMsg = []
    intRun = 0
    for strColName, strColDataType in dictTblSchema.items():
        lstColSchemaRun:List[Any] = [''] * (c_intTblColSchemaCount+1) #c_intTblColSchemaCount+1: Length
        strDataLen = ''

        lstColSchemaRun[c_intTblColSchemaColPos] = intRun
        lstColSchemaRun[c_intTblColSchemaColName] = strColName
        strColDataType = strColDataType.strip()

        # <PyCmt: Judge User Define Col DataType>
        if strColDataType[0:len(c_strMySQLDataTypeInt)] == c_strMySQLDataTypeInt:
            lstColSchemaRun[c_intTblColSchemaColDataType] = c_strMySQLDataTypeInt
        elif strColDataType[0:len(c_strMySQLDataTypeFloat)] == c_strMySQLDataTypeFloat:
            lstColSchemaRun[c_intTblColSchemaColDataType] = c_strMySQLDataTypeFloat
        elif strColDataType[0:len(c_strMySQLDataTypeDbl)] == c_strMySQLDataTypeDbl:
            lstColSchemaRun[c_intTblColSchemaColDataType] = c_strMySQLDataTypeDbl
        elif strColDataType[0:len(c_strMySQLDataTypeDecimal)] == c_strMySQLDataTypeDecimal:
            lstColSchemaRun[c_intTblColSchemaColDataType] = c_strMySQLDataTypeDecimal
            strDataLen = strColDataType[len(c_strMySQLDataTypeDecimal):]
            if not c_strSQLBracketLeft in strDataLen or not c_strSQLBracketRight in strDataLen:
                strErrMsgRun='ColName: {}, DataTypeSet: {} Error!'.\
                    format(lstColSchemaRun[c_intTblColSchemaColName], strColDataType)
                lstErrMsg.append(strErrMsgRun)
                lstColSchemaRun[c_intTblColSchemaColSQLColErrMsg]=strErrMsgRun
                lstColSchemaRun[c_intTblColSchemaColDataLen] = strColDataType
            else:
                strDataLen = strDataLen.strip()
                strDataLenSub = strDataLen[1:-1]
                if c_strSQLCommaSplitor in strDataLen:
                    lstColSchemaRun[c_intTblColSchemaColDataLen] = int(strDataLenSub.split(c_strSQLCommaSplitor)[0])
                    lstColSchemaRun[c_intTblColSchemaColDataScale] = int(strDataLenSub.split(c_strSQLCommaSplitor)[1])
                else:
                    lstColSchemaRun[c_intTblColSchemaColDataLen] = int(strDataLen)
        elif strColDataType[0:len(c_strMySQLDataTypeVarChar)] == c_strMySQLDataTypeVarChar:
            lstColSchemaRun[c_intTblColSchemaColDataType] = c_strMySQLDataTypeVarChar
            strDataLen = strColDataType[len(c_strMySQLDataTypeVarChar):]
            if not c_strSQLBracketLeft in strDataLen or not c_strSQLBracketRight in strDataLen:
                strErrMsgRun='ColName: {}, DataTypeSet: {} Error!'.\
                    format(lstColSchemaRun[c_intTblColSchemaColName], strColDataType)
                lstErrMsg.append(strErrMsgRun)
                lstColSchemaRun[c_intTblColSchemaColSQLColErrMsg]=strErrMsgRun
                lstColSchemaRun[c_intTblColSchemaColDataLen] = strDataLen
            else:
                strDataLen = strDataLen.strip()
                lstColSchemaRun[c_intTblColSchemaColDataLen] = int(strDataLen[1:-1])
        elif strColDataType[0:len(c_strMySQLDataTypeDateTime)] == c_strMySQLDataTypeDateTime:
            lstColSchemaRun[c_intTblColSchemaColDataType] = c_strMySQLDataTypeDateTime
        else:
            strErrMsgRun = 'ColName: {}, DataType: {} Can\'t Match MySQL DataType!'.\
                format(lstColSchemaRun[c_intTblColSchemaColName],strColDataType)
            lstErrMsg.append(strErrMsgRun)
            lstColSchemaRun[c_intTblColSchemaColSQLColErrMsg] = strErrMsgRun
            lstColSchemaRun[c_intTblColSchemaColDataLen] = strDataLen

        if lstColSchemaRun[c_intTblColSchemaColDataType] == c_strMySQLDataTypeDecimal:
            pass
        elif lstColSchemaRun[c_intTblColSchemaColDataType] == c_strMySQLDataTypeVarChar:
            lstColSchemaRun[c_intTblColSchemaColDataScale] = 0
        else:
            lstColSchemaRun[c_intTblColSchemaColDataLen] = 0
            lstColSchemaRun[c_intTblColSchemaColDataScale] = 0

        if strColName==c_strDBTblColNameUqeNo:
            lstColSchema.insert (0, lstColSchemaRun)
        else:
            lstColSchema.append(lstColSchemaRun)
        intRun += 1

    for intRun in range(0, len(lstColSchema)):
        lstColSchema[intRun][c_intTblColSchemaColPos] = intRun

    if len(lstErrMsg) > 0:
        strErrMsg=c_strNewLine.join(lstErrMsg)
        return False, strErrMsg
    return True, lstColSchema

def fnDBColSngSchemaDictCvrt(
        strColName:str,
        strColValue:str ='',
        lstColSchema:list = None,
        strColDataType:str = '',
        intDataLen:int = 0,
        intDataScale:int = 0,
        blnValBlkSkip:bool = False,
        blnColNullable:bool = True,
        blnColPrmKey:bool = False,
        blnColAutoIncrement:bool = False,
        lstValueApdColColl:list = None,
        blnErrRtn:bool = False
) -> (bool, str, dict):
    # <PyFunc: >
    #   Desc: Single Col lstColSchema[] -> dictColSchema with SQL Template
    #       Convert Input Col Parameter to 'dictColSchema' AS fnDBColSchemaGet output Fmt
    #       Base on Running lstColSchema, Col DataType to 'Select';'Update' SQL and with NumberFormat
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strColName= Input ColName
    #   Option:
    #      strColValue= Input Col Value
    #      lstColSchema= Reference ColSchema List
    #      strColDataType= Input ColDataType, Compare with
    #           MySQL DataType[int, float, double, decimal, bool, varchar, str, datetime, date]
    #      intDataLen= Input Data Length
    #      intDataScale= Input Data Scale
    #      blnColNullable= Input Col Nullable, 'true' or 'false'
    #      blnColPrmKey= Input Col Primary Key, 'true' or 'false'
    #      lstValueApdColColl= Col Name that need to Append Col Value
    #      blnErrShow= if not blnErrShow, EHMsg.fnPrtErr will be called
    #   Return: 
    # </PyFunc: >
    blnUpdApd:bool = False
    if not lstValueApdColColl is None: blnUpdApd = strColName in lstValueApdColColl

    strDataLen:str = ''

    strColNullable:str = ''
    strColAutoIncrement:str = ''

    strColNumFmt:str = ''
    strSQLColDft:str = ''
    strSQLColTblCrtDataLen:str = ''
    strSQLColSelt:str = ''
    strSQLColUpd:str = ''

    strColValueRun:str=''

    dictColSchema: dict = {
        'strColName': strColName,
        'strColDataType': strColDataType,
        'blnColNullable': blnColNullable,
        'strColNullable': strColNullable,
        'blnColPrmKey': blnColPrmKey,
        'blnColAutoIncrement': blnColAutoIncrement,
        'strColAutoIncrement': strColAutoIncrement,

        'strColNumFmt': strColNumFmt,
        'strSQLColDft': strSQLColDft,

        'strSQLColTblCrtDataLen': strSQLColTblCrtDataLen,
        'strSQLColSchema': '',
        'strSQLColSchemaRun': '',
        'strSQLColTblCrt': '',
        'strSQLColTblCrtRun': '',
        'strSQLColSelt': '',
        'strSQLColSeltRun': '',
        'strSQLColUpd' : '',
        'strSQLColUpdRun': '',
        'strColValue': '',
        'strColValueRun': '',
        'strErrMsg': ''
    }
    if lstColSchema is None and len(strColDataType) == 0:
        dictColSchema:dict = {}
        strErrMsg = 'Both lstColSchema=None, and len(strColDataType)==0!'
        strFuncName = 'EHDBApply.fnDBColSngSchemaDictCvrt'
        dictColSchema['strErrMsg'] = strErrMsg
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                dictColSchema=dictColSchema
            )

    elif not lstColSchema is None:
        if EHArray.fnArrayDimGet(lstRun=lstColSchema)==2:
            # <PyCmt: Get Col Info From lstColSchema>
            lstColName=[]
            for lstRow in lstColSchema:
                lstColName.append(lstRow[c_intTblColSchemaColName])
            intColIndex = lstColName.index(strColName)
            lstColSchema=lstColSchema[intColIndex]
        strColDataType = lstColSchema[c_intTblColSchemaColDataType]
        strDataLen = str(lstColSchema[c_intTblColSchemaColDataLen])
        if intDataLen==0 and strDataLen.isdigit() : intDataLen=int(strDataLen)
        strDataScale = str(lstColSchema[c_intTblColSchemaColDataScale])
        if intDataScale==0 and strDataScale.isdigit() : intDataScale = int(strDataScale)
        blnColNullable = lstColSchema[c_intTblColSchemaColNullable]
        blnColNullable=(str(blnColNullable).lower()!='false')
        blnColPrmKey = lstColSchema[c_intTblColSchemaColPrmKey]
        blnColPrmKey=(str(blnColPrmKey).lower()=='true')

    if strColName in c_lstDBSysColName:
        # <PyCmt: if strColName in System Col, get Attrib from Default>
        if strColName == c_strDBTblColNameUqeNo:
            strColDataType = c_strDBTblColDataTypeUqeNo
            intDataLen = c_intDBTblColDataLenUqeNo
            intDataScale = 0
            blnColNullable = False
            blnColPrmKey = True
            blnColAutoIncrement = True
        elif strColName == c_strDBTblColNameDeleted:
            strColDataType = c_strDBTblColDataTypeDeleted
            intDataLen = c_intDBTblColDataLenDeleted
            intDataScale = 0
            blnColNullable = False
            blnColPrmKey = True
            blnColAutoIncrement = False
        elif strColName == c_strDBTblColNameLastVer:
            strColDataType = c_strDBTblColDataTypeLastVer
            intDataLen = c_intDBTblColDataLenLastVer
            intDataScale = 0
            blnColNullable = False
            blnColPrmKey = True
            blnColAutoIncrement = False
        elif strColName == c_strDBTblColNameUploader:
            strColDataType = c_strDBTblColDataTypeUploader
            intDataLen = c_intDBTblColDataLenUploader
            intDataScale = 0
            blnColNullable = False
            blnColPrmKey = True
            blnColAutoIncrement = False
        elif strColName == c_strDBTblColNameUpdateTime:
            strColDataType = c_strDBTblColDataTypeUpdateTime
            intDataLen = c_intDBTblColDataLenUpdateTime
            intDataScale = 0
            blnColNullable = False
            blnColPrmKey = True
            blnColAutoIncrement = False

    # <PyCmt: ReFmt Col Info.>
    strColDataType = strColDataType.lower()
    if strColDataType == c_strMySQLDataTypeInt:
        strColNumFmt = c_strNumFmtInt
        strSQLColDft = c_strNumberDBNumDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmplt
        strSQLColSelt = c_strSQLColSeltTmpltNum
        strSQLColUpd = c_strSQLColUpdApdTmpltNum if blnUpdApd else c_strSQLColUpdTmplt
        if blnValBlkSkip: intDataLen = 0
    elif strColDataType == c_strMySQLDataTypeFloat:
        if intDataScale > 0:
            strColNumFmt = c_strNumFmtDecimal + '0' * (intDataScale - 1)
            strDataLen = str(intDataLen) + '.' + str(intDataScale)
        else:
            strColNumFmt = c_strNumFmtInt
        strSQLColDft = c_strNumberDBNumDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmplt
        strSQLColSelt = c_strSQLColSeltTmpltNum
        strSQLColUpd = c_strSQLColUpdApdTmpltNum if blnUpdApd else c_strSQLColUpdTmplt
    elif strColDataType == c_strMySQLDataTypeDecimal:
        if intDataScale > 0:
            strColNumFmt = c_strNumFmtDecimal + '0' * len(intDataScale)-1
            strDataLen = str(intDataLen) + '.' + str(intDataScale)
        else:
            strColNumFmt = c_strNumFmtInt
        strSQLColDft = c_strNumberDBNumDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmpltNumChr
        strSQLColSelt = c_strSQLColSeltTmpltNum
        strSQLColUpd = c_strSQLColUpdApdTmpltNum if blnUpdApd else c_strSQLColUpdTmplt
    elif strColDataType == c_strMySQLDataTypeBool:
        strColNumFmt = c_strNumFmtBool
        strSQLColDft = c_strNumFmtBoolDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmplt
        strSQLColSelt = c_strSQLColSeltTmpltNum
        strSQLColUpd = c_strSQLColUpdApdTmpltBool if blnUpdApd else c_strSQLColUpdTmplt
    elif strColDataType == c_strMySQLDataTypeDateTime:
        strColNumFmt = c_strNumFmtDateTime
        strSQLColDft = c_strValDBDateTimeDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmplt
        strSQLColSelt = c_strSQLColSeltTmpltDate
        strSQLColUpd = c_strSQLColUpdTmplt
    elif strColDataType == c_strMySQLDataTypeDate:
        strColNumFmt = c_strNumFmtDate1
        strSQLColDft = c_strValDateDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmplt
        strSQLColSelt = c_strSQLColSeltTmpltDate
        strSQLColUpd = c_strSQLColUpdTmplt
    elif strColDataType in [c_strMySQLDataTypeVarChar, c_strDataTypeStr]:
        strColDataType = c_strMySQLDataTypeVarChar
        strDataLen = str(intDataLen)
        strColNumFmt = c_strNumFmtStr
        strSQLColDft = c_strValStrDft
        strSQLColTblCrtDataLen = c_strTblCrtDataLenTmpltNumChr
        strSQLColSelt = c_strSQLColSeltTmpltText
        strSQLColUpd = c_strSQLColUpdApdTmpltText if blnUpdApd else c_strSQLColUpdTmplt

    # <PyCmt: Fill Col Info. into dictColSchema>
    dictColSchema['strColDataType'] = strColDataType
    dictColSchema['intDataLen'] = intDataLen
    # <PyCmt: ColNullable Fill Into dictColSchema>
    strColNullable= (c_strTblCrtNullableTmplt if not bool(blnColNullable) else '' )
    dictColSchema['blnColNullable']=blnColNullable
    dictColSchema['strColNullable'] = strColNullable

    # <PyCmt: ColPrmKey Fill Into dictColSchema>
    dictColSchema['blnColPrmKey'] = blnColPrmKey

    # <PyCmt: ColAutoIncrement Fill Into dictColSchema>
    strColAutoIncrement= (c_strTblCrtAutoIncrementTmplt if bool(blnColAutoIncrement) else '' )
    dictColSchema['blnColAutoIncrement'] = blnColAutoIncrement
    dictColSchema['strColAutoIncrement'] = strColAutoIncrement

    # <PyCmt: Col NumFmt, ValueDft Fill Into dictColSchema>
    dictColSchema['strColNumFmt'] = strColNumFmt
    dictColSchema['strSQLColDft'] = strSQLColDft

    # <PyCmt: ColDataLen Fill Into dictColSchema>
    strSQLColTblCrtDataLenRun = strSQLColTblCrtDataLen
    strSQLColTblCrtDataLenRun = strSQLColTblCrtDataLenRun.replace('<DataLen>', strDataLen)
    dictColSchema['strSQLColTblCrtDataLenRun'] = strSQLColTblCrtDataLenRun

    # <PyCmt: Col Create Table SQL Fill Into dictColSchema>
    dictColSchema['strSQLColSchema']=c_strTblColSchemaTmplt
    strSQLColSchemaRun=c_strTblColSchemaTmplt
    strSQLColSchemaRun = strSQLColSchemaRun.replace('<DataType>', strColDataType)
    strSQLColSchemaRun = strSQLColSchemaRun.replace('<DataLenStr>', strSQLColTblCrtDataLenRun)
    dictColSchema['strSQLColSchemaRun'] = strSQLColSchemaRun

    dictColSchema['strSQLColTblCrt'] = c_strTblCrtColTmplt
    strSQLColTblCrtRun = c_strTblCrtColTmplt
    strSQLColTblCrtRun = strSQLColTblCrtRun.replace('<ColName>', strColName)
    strSQLColTblCrtRun = strSQLColTblCrtRun.replace('<DataType>', strColDataType)
    strSQLColTblCrtRun = strSQLColTblCrtRun.replace('<DataLenStr>', strSQLColTblCrtDataLenRun)
    strSQLColTblCrtRun = strSQLColTblCrtRun.replace('<NullableStr>', strColNullable)
    strSQLColTblCrtRun = strSQLColTblCrtRun.replace("<AutoIncrementSrt>", strColAutoIncrement)
    dictColSchema['strSQLColTblCrtRun'] = strSQLColTblCrtRun

    # <PyCmt: Col Select SQL Fill Into dictColSchema>
    dictColSchema['strSQLColSelt'] = strSQLColSelt
    strSQLColSeltRun = strSQLColSelt
    strSQLColSeltRun = strSQLColSeltRun.replace('<ColName>', strColName)
    strSQLColSeltRun = strSQLColSeltRun.replace('<ColValueDefault>', strSQLColDft)
    strSQLColSeltRun = strSQLColSeltRun.replace('<ColNameAlias>', strColName)
    dictColSchema['strSQLColSeltRun'] = strSQLColSeltRun

    # <PyCmt: Col Update SQL Fill Into dictColSchema>
    dictColSchema['strSQLColUpd'] = strSQLColUpd
    dictColSchema['strSQLColUpdRun'] = ''
    strSQLColUpdRun:str = strSQLColUpd
    strSQLColUpdRun = strSQLColUpdRun.replace('<ColName>', strColName)

    # <PyCmt: if strColValue User Inputted, Base on strColDataType Convert strColValue to strColValueRun>
    dictColSchema['strColValue'] = strColValue
    dictColSchema['strColValueRun'] = ''
    dictColSchema['strErrMsg'] = ''

    blnResult, strErrMsg, strColValueRun = \
        fnDBColStrValueCvrt(
            strColValue=strColValue,
            strColDataType=strColDataType,
            blnValBlkSkip = blnValBlkSkip,
            blnErrRtn = blnErrRtn
        )
    if not blnResult:
        strFuncName = 'EHDBApply.fnDBColSngSchemaDictCvrt'
        dictColSchema['strErrMsg'] = strErrMsg
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                dictColSchema=dictColSchema
            )
    dictColSchema['strColValueRun'] = strColValueRun
    if (strColDataType in [c_strMySQLDataTypeVarChar, c_strDataTypeStr] and
            len(strColValue)> intDataLen):
        strErrMsg=('ColName: {0}, ColValue: \'{1}\', Len={2}, Over Collen({3})!'.
                   format(strColName, strColValue, len(strColValue), intDataLen))
        strFuncName = "EHDBApply.fnDBColSngSchemaDictCvrt"
        dictColSchema["strErrMsg"] = strErrMsg
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                dictColSchema=dictColSchema
            )
    # <PyCmt: Replace strSQLColUpdRun strSQL as New strColValue >
    strSQLColUpdRun = strSQLColUpdRun.replace("<ColValue>", strColValueRun)
    dictColSchema["strSQLColUpdRun"] = strSQLColUpdRun
    return True,strErrMsg, dictColSchema

def fnDBColStrValueCvrt(
        strColValue:str,
        strColDataType:str,
        blnValBlkSkip:bool = False,
        blnErrRtn = False
) -> (str, str):
    # <PyFunc: fnDBColStrValueCvrt>
    #   Desc: Convert strColValue to SQL Execution format
    #       Convert strColValue Format for SQL INSERT
    #   Remark:
    #       numeric: 'strColValue'
    #       bool: 'strColValue'
    #       str, varchar: 'strColValue'
    #       datetime, time: 'fnStrDateCvt(strRun=strCOlValue)'
    # </PyFunc: fnDBColStrValueCvrt>
    blnResult = True
    strErrMsg = ''
    try:
        if strColDataType == c_strMySQLDataTypeInt:
            strColValue=strColValue.strip()
            if len(strColValue)==0:
                strColValue = '0'
            elif c_strDecimalPoint in strColValue:
                strColValue=strColValue.split(c_strDecimalPoint)[0]
            strColValue = int(strColValue)
        elif strColDataType in [c_strMySQLDataTypeFloat, c_strMySQLDataTypeDecimal]:
            if len(strColValue) == 0: strColValue = '0'
            strColValue = float(strColValue)
        elif strColDataType == c_strMySQLDataTypeBool:
            strColValue = ( True if strColValue.lower()=='true' else False )
        elif strColDataType in [c_strMySQLDataTypeVarChar, c_strDataTypeStr]:
            pass
        elif strColDataType in c_lstMySQLDataTypeDateTime:
            if blnValBlkSkip and len(strColValue)==0:
                blnResult = True
            else:
                blnResult, strErrMsg, strColValue = EHDate.fnStrDateCvt(strRun=strColValue, blnErrRtn=blnErrRtn)
    except Exception as Err:
        blnResult = False
        if not strColDataType in c_lstMySQLDataTypeDateTime:
            strErrMsg = 'strColValue: {0} Convert Error!'.format(strColValue) + \
                'Err: {0}'.format(Err)
    finally:
        if not blnResult:
            strFuncName = 'EHDBApply.fnDBColValueCvrt'
            return \
                EHDebug.fnErrRtn(
                    blnResult=False,
                    strErrMsg=strErrMsg,
                    strFuncName=strFuncName,
                    blnErrRtn=blnErrRtn,
                    blnLog=False,
                    strColValue=''
                )

    # <PyCmt: strColValue Insert Format>
    strColValue=str(strColValue)
    if strColDataType == c_strMySQLDataTypeInt:
        strColValue = ''.join(['\'', strColValue, '\''])
    elif strColDataType in [c_strMySQLDataTypeFloat, c_strMySQLDataTypeDecimal]:
        strColValue = ''.join(['\'', strColValue, '\''])
    elif strColDataType == c_strMySQLDataTypeBool:
        strColValue = ''.join(['\'', strColValue, '\''])
    elif strColDataType in [c_strMySQLDataTypeVarChar, c_strDataTypeStr]:
        strColValue = ''.join(['\'', strColValue, '\''])
    elif strColDataType in [c_strMySQLDataTypeDateTime, c_strMySQLDataTypeDate]:
        strColValue = ''.join(['\'', strColValue, '\''])
    return True, strErrMsg, strColValue

def fnDBColSchemaCmp(
    lstColSchemaSrc,
    strTblNameTrg,
    strSectName='',
    strDBName=''
)->(bool, str, dict, list):
    # <PyFunc: fnDBColSchemaCmp>
    #    Desc: Compare 2 DBColSchema
    #    Use By:
    #    Noticed:
    #    Parameter:
    #        lstColSchemaSrc: Source lstDBColSchema
    #        strTblNameTrg: Target DBTbl Name, get lstDBColSchema from Database
    #    Option:
    #        strSectName: Indicated DB Cfg SectName
    #        strDBName: Indicated DBName
    #    Return:
    #       1. blnResult:bool: Compare result
    #       2. strErrMsg:str
    #       3. dictColCmp:dict: Compare Result Dict
    #       4. lstColSchemaTrg:list: Target lstDBColSchema
    #       5. lstColNameNew
    # </PyFunc: fnDBColSchemaCmp>

    # <PyCmt: setup Fixed Dict>
    lstColSchemaCmpResult=['ColNameDiff', 'ColNotIncd', 'ColMiss',
        'ColDataType', 'ColDataTypeResult',
        'ColDataLen', 'ColDataLenResult',
        'ColDataScale', 'ColDataScaleResult' ]
    dictColCmp=EHArray.EHFixElmDict(lstElmKey=lstColSchemaCmpResult)

    lstColNameSrc=[]
    for lstRow in lstColSchemaSrc:
        lstColNameSrc.append(lstRow[c_intTblColSchemaColName])

    blnResult, strErrMsg, lstColSchemaTrg, lstColNameTrg = \
        fnDBColSchemaGet(
            strSectName = strSectName,
            strDBName = strDBName,
            strTblName = strTblNameTrg,
            blnValBlkSkip = True
        )
    if not blnResult: return False, strErrMsg, None, None

    lstColNameNotIncd=[]
    # <PyCmt: lstColSchemaTrg will be Database Col Schema>
    lstColNameLowCSrc=list(map(str.lower, lstColNameSrc))
    for strColNameTrg in lstColNameTrg:
        strColNameLowCTrg = strColNameTrg.lower()
        if not strColNameLowCTrg in lstColNameLowCSrc:
            lstColNameNotIncd.append(strColNameTrg)
    dictColCmp['ColNotIncd'] = lstColNameNotIncd

    lstColNameMiss=[]
    # <PyCmt: lstColSchemaSrc will be Txt Colname>
    lstColNameLowCTrg = list(map(str.lower, lstColNameTrg))
    for strColNameSrc in lstColNameSrc:
        strColNameLowCSrc = strColNameSrc.lower()
        if not strColNameLowCSrc in lstColNameLowCTrg:
            lstColNameMiss.append(strColNameSrc)
    dictColCmp['ColMiss'] = lstColNameMiss

    if len(lstColNameSrc)>0 and len(lstColNameTrg)>0 :
        lstColSchemaIntersection=lstColNameSrc + lstColNameTrg
        lstColSchemaIntersection=list(set(lstColSchemaIntersection))

        lstColDataType = []
        lstColDataTypeRslt = []
        lstColDataLen = []
        lstColDataLenRslt = []
        lstColDataScale = []
        lstColDataScaleRslt = []
        for strColName in lstColSchemaIntersection:
            intColIndexSrc=-1
            intColIndexTrg=-1
            if strColName in lstColNameSrc: intColIndexSrc=lstColNameSrc.index(strColName)
            if strColName in lstColNameTrg: intColIndexTrg=lstColNameTrg.index(strColName)
            if intColIndexSrc>=0 and intColIndexTrg>=0:
                strColDataTypeSrc=lstColSchemaSrc[intColIndexSrc][c_intTblColSchemaColDataType]
                strColDataTypeTrg=lstColSchemaTrg[intColIndexTrg][c_intTblColSchemaColDataType]
                if strColDataTypeSrc!= strColDataTypeTrg:
                    strDataTypeDiff=''.\
                        join(['ColName: ', strColName, ', Src: ', strColDataTypeSrc, ', Trg: ', strColDataTypeTrg])
                    lstColDataType.append(strColName)
                    lstColDataTypeRslt.append(strDataTypeDiff)

                if not strColDataTypeTrg in c_lstMySQLDataTypeDateTime:
                    intDataLenSrc=int(lstColSchemaSrc[intColIndexSrc][c_intTblColSchemaColDataLen])
                    intDataLenTrg=int(lstColSchemaTrg[intColIndexTrg][c_intTblColSchemaColDataLen])
                    if intDataLenSrc!= intDataLenTrg:
                        strDataLenDiff=''.\
                            join(['ColName: ', strColName,
                                  ', Src: ', str(intDataLenSrc),
                                  ', Trg: ', str(intDataLenTrg)])
                        lstColDataLen.append(strColName)
                        lstColDataLenRslt.append(strDataLenDiff)
                    intDataScaleSrc=int(lstColSchemaSrc[intColIndexSrc][c_intTblColSchemaColDataScale])
                    intDataScaleTrg=int(lstColSchemaSrc[intColIndexTrg][c_intTblColSchemaColDataScale])
                    if intDataScaleSrc!= intDataScaleTrg:
                        strDataScaleDiff=''.\
                            join(['ColName: ', strColName,
                                  'Src: ', str(intDataScaleSrc),
                                  'Trg: ', str(intDataScaleTrg)])
                        lstColDataScale.append(strColName)
                        lstColDataScaleRslt.append(strDataScaleDiff)
        dictColCmp['ColDataScale'] = lstColDataScale
        dictColCmp["ColDataScaleResult"] = lstColDataScaleRslt
        dictColCmp['ColDataLen'] = lstColDataLen
        dictColCmp["ColDataLenResult"] = lstColDataLenRslt
        dictColCmp['ColDataType'] = lstColDataType
        dictColCmp["ColDataTypeResult"] = lstColDataTypeRslt

        dictColCmp['ColNameDiff'] = \
            list(set( lstColNameNotIncd + lstColNameMiss + lstColDataType + lstColDataLen+ lstColDataScale ))
    else:
        dictColCmp['ColNameDiff'] = \
            list(set( lstColNameNotIncd + lstColNameMiss))
    return True, strErrMsg, dictColCmp, lstColSchemaTrg
def fnDBColSysColNameAppend(
        lstColName,
    lstColValue = None,
    blnUqeNoApd = False,
    dateRun = None
)->(list, list):
    if dateRun is None: dateRun = EHDate.fnNow()
    lstColNameRun=lstColName.copy()
    lstColValueRun=lstColValue.copy()
    for strSysColName in c_lstDBSysColName:
        blnApd = False
        intColIndex = 0
        if not strSysColName in lstColNameRun:
            if strSysColName == c_strDBTblColNameUqeNo:
                if blnUqeNoApd:
                    intColIndex = 0
                    lstColNameRun.insert(intColIndex, strSysColName)
                    blnApd = True
            else:
                intColIndex=len(lstColNameRun)
                lstColNameRun.append(strSysColName)
                blnApd = True
            if blnApd and not lstColValueRun is None:
                strColValue=''
                if strSysColName == c_strDBTblColNameUqeNo:
                    strColValue=''
                elif strSysColName == c_strDBTblColNameDeleted:
                    strColValue='N'
                elif strSysColName == c_strDBTblColNameLastVer:
                    strColValue='Y'
                elif strSysColName == c_strDBTblColNameUploader:
                    strColValue=clsEHUsrMgt.p_strUSRID
                elif strSysColName == c_strDBTblColNameUpdateTime:
                    strColValue=EHDate.fnDateToStr(dateRun=dateRun, blnDBDate=True)
                lstColValueRun.insert(intColIndex, strColValue)
    return lstColNameRun, lstColValueRun

def fnDBColSysColNameRemove(
    lstColName,
    lstColValue = None,
    blnUqeNoRmv = True
)->(list, list):
    lstColNameRun=lstColName.copy()
    lstColValueRun=lstColValue.copy()
    for strSysColName in c_lstDBSysColName:
        if strSysColName in lstColNameRun:
            if not blnUqeNoRmv or strSysColName.upper() == c_strDBTblColNameUqeNo.upper():
                intColIndex = lstColNameRun.index(strSysColName)
                lstColNameRun.pop(intColIndex)
                if not lstColValueRun is None: lstColValueRun.pop(intColIndex)
    return lstColNameRun, lstColValueRun

def fnDBColSysColValReplace(
    lstColName:list,
    lstColValue:list,
    dateRun:datetime = None
)->list:
    strDateRun=EHDate.fnDateToStr(dateRun=dateRun)
    for strSysColName in c_lstDBSysColName:
        if strSysColName in lstColName:
            intColIndex = lstColName.index(strSysColName)
            if strSysColName == c_strDBTblColNameDeleted:
                lstColValue[intColIndex]=c_strDBTblColValDftDeleted
            elif strSysColName == c_strDBTblColNameLastVer:
                lstColValue[intColIndex]=c_strDBTblColValDftLastVer
            if strSysColName == c_strDBTblColNameUploader:
                lstColValue[intColIndex]=c_strDBTblColValDftUploader
            if strSysColName == c_strDBTblColNameUpdateTime:
                lstColValue[intColIndex]=c_strDBTblColValDftUpdateTime

            lstColValue[intColIndex]=lstColValue[intColIndex].replace('<Uploader>', clsEHUsrMgt.p_strUSRID)
            lstColValue[intColIndex]=lstColValue[intColIndex].replace('<UpdateTime>', strDateRun)
    return lstColValue
# </PyRegion: DBCol>

# <PyRegion: DBTbl>
def fnDBTblEnum(
        strSectName = '',
        strDBName = '',
        strTblName = '',
        blnSysTblShow = True
)->(list | None, list | None):
    # <PyFunc: fnDBTblEnum>
    # Desc: Get All DB Table Info
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #       strSectName= INI Config Section Name
    #       strTblName= DB TableName
    #       blnSysTblShow= Sys Table Show or Not, only MS Access Available
    #   Remark:
    #       TblSchema:
    #       1. DBName
    #       2. Table Name
    #       3. ObjName
    #   Return: 1. Table Name List, if specific strTblName, only show the dedicated or None
    #       2. Show Tbl Schema['DBName', 'TblName', 'TblType']
    # </PyFunc: fnDBTblEnum>
    udtCNN = EHDB.fnDBCNNGet(strSectName = strSectName, strDBName = strDBName )
    if udtCNN is None:
        strErrMsg='SectName: {}, strDBName: {} Connection Error!'.format(strSectName, strDBName)
        strFuncName = 'EHDBApply.fnDBTblEnum'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return None, None
    objCursor = udtCNN.objCursor
    if objCursor is None: return None, None
    blnDBTableNameLowCase = \
        EHDB.fnDBCNNGet(
            strSectName=strSectName,
            strDBName = strDBName,
            strAttrName=EHDB.c_strINIAttrNameDBTblNameLCase
        )
    if blnDBTableNameLowCase: strTblName = strTblName.lower()

    lstTblSchema = []
    lstTblName = []
    for rowRun in objCursor.tables():
        lstTblSchemaRun = []
        if rowRun[c_intDBTblEnumColPosTblName] == strTblName:
            lstTblSchema = []
            lstTblSchema.append(rowRun[c_intDBTblEnumColPosDBName])
            lstTblSchema.append(rowRun[c_intDBTblEnumColPosTblName])
            lstTblSchema.append(rowRun[c_intDBTblEnumColPosObjType])
            lstTblName.append(rowRun[c_intDBTblEnumColPosTblName])
            return lstTblName, lstTblSchema
        elif len(strTblName) == 0:
            if not blnSysTblShow and \
                udtCNN.udeDBType == EHUDE.udeDBType.udeDBTypeAccess and \
                (rowRun[c_intDBTblEnumColPosTblName][0:2] == 'MS' or
                 rowRun[c_intDBTblEnumColPosTblName][0:1] == '~'):
                pass
            else:
                lstTblSchemaRun.append(rowRun[c_intDBTblEnumColPosDBName])
                lstTblSchemaRun.append(rowRun[c_intDBTblEnumColPosTblName])
                lstTblSchemaRun.append(rowRun[c_intDBTblEnumColPosObjType])
                lstTblName.append(rowRun[c_intDBTblEnumColPosTblName])
            if len(lstTblSchemaRun) > 0: lstTblSchema.append(lstTblSchemaRun)
    if len(lstTblName)==0:
        lstTblName = None
        lstTblSchema = None
    return lstTblName, lstTblSchema

def fnDBTblCreate(
        strTblName:str ,
        lstColSchema:list ,
        strSectName:str = '',
        strDBName:str = '',
        blnCleanUp:bool = False,
        blnTmpTbl:bool = False,
        blnErrRtn:bool = False
) -> (bool, str):
    # <PyFunc: fnDBTblCreate>
    # Desc: Create DB Table
    #   Use By:
    #   Noticed:
    #       lstColSchema will load by 'fnDBColSngSchemaDictCvrt' Convert to dictColSchema
    #   Parameter:
    #       strTblName: Table Name
    #       lstColSchema: Table Col Schema, it may co-work with 'fnDBColSchemaCvrt'(dict->list)
    #   Option:
    #       strSectName= INI Config Section Name
    #       strDBName= DB Name
    #       blnCleanUp= if Table Existed, Clean it up
    #       blnTmpTbl=
    #   Remark: lstColSchema Fmt
    #       0. strColPos [Optional]
    #       1. strColName
    #       2. strDataType [int; float, decimal, bool, varchar, str, datetime, date]
    #       3. intDataLen
    #       4. intDataScale [decimal Only]
    #       5. strPrimaryKey [true or others]
    #       6. strColNullable [true or others]
    # </PyFunc: fnDBTblCreate>

    # <PyCmt: Check Tbl Existing>
    lstTblName, lstTblSchema = \
        fnDBTblEnum(
            strSectName=strSectName,
            strDBName=strDBName,
            strTblName=strTblName
        )
    if not lstTblName is None:
        # <PyCmt: DB Table Dropping>
        if blnCleanUp:
            blnResult = \
                fnDBTblDrop(
                    strTblName=strTblName,
                    strSectName=strSectName,
                    blnDataChk= not blnCleanUp,
                    blnErrRtn= True
                )
            strErrMsg = "DB Tbl: {}, Drop Fail!".format(strTblName)
            strFuncName = "EHDBApply.fnDBTblCreate"
            return \
                EHDebug.fnErrRtn(
                    blnResult=blnResult,
                    strErrMsg=strErrMsg,
                    strFuncName=strFuncName,
                    blnErrRtn=blnErrRtn,
                )
        else:
            strErrMsg = "DB Tbl: {}, Existed!".format(strTblName)
            strFuncName = "EHDBApply.fnDBTblCreate"
            return \
                EHDebug.fnErrRtn(
                    blnResult=False,
                    strErrMsg=strErrMsg,
                    strFuncName=strFuncName,
                    blnErrRtn=blnErrRtn,
                    blnLog=False,

                )
    # </PyCmt: Check Tbl Existing>

    # <PyCmt: Check lstColSchema>
    if lstColSchema is None or len(lstColSchema) == 0:
        strErrMsg = 'lstColSchema Empty!'
        strFuncName = 'EHDBApply.fnDBTblCreate'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                blnLog=False,

            )

    lstColName:list = []
    blnUqeNo:bool = False
    lstColNamePrmKey:list = []
    lstSQLColTblCrt:list = []
    lstErrMsg:list = []
    for rowColSchema in lstColSchema:
        if len(rowColSchema[c_intTblColSchemaColSQLColErrMsg])>0:
            lstErrMsg.append(rowColSchema[c_intTblColSchemaColSQLColErrMsg])
        else:
            strColName:str = rowColSchema[c_intTblColSchemaColName]
            if strColName==c_strDBTblColNameUqeNo: blnUqeNo=True
            # <PyCmt: Convert Single Col Schema to Dict>
            blnResult, strErrMsg, dictColSchema =  \
                fnDBColSngSchemaDictCvrt(
                    strColName=strColName,
                    lstColSchema=rowColSchema,
                    blnValBlkSkip=True,
                    blnErrRtn=True
                )
            if not blnResult:
                strFuncName = 'EHDBApply.fnDBTblCreate'
                strErrMsg=': '.join([strFuncName, strErrMsg])
                lstErrMsg.append(strErrMsg)
            else:
                blnColPrmKey = dictColSchema['blnColPrmKey']
                if blnColPrmKey: lstColNamePrmKey.append(strColName)
                strSQLColTblCrt = dictColSchema['strSQLColTblCrtRun']
                lstSQLColTblCrt.append(strSQLColTblCrt)
                lstColName.append(strColName)

    if len(lstErrMsg) > 0:
        strErrMsg = c_strNewLine.join(lstErrMsg)
        strFuncName = 'EHDBApply.fnDBTblCreate'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                blnLog=False,

            )

    if blnTmpTbl:
        strSQLTypeTblCrt = EHSQLAnaly.c_strSQLCREATETEMPTABLEKeyword
    else:
        strSQLTypeTblCrt = EHSQLAnaly.c_strSQLCREATETABLEKeyword

    # <PyCmt: lstSQLColTblCrt join with ','(c_strSQLSplitor)>
    strSQLColTblCrt:str = c_strSQLSplitor.join(lstSQLColTblCrt)

    strUqeNo:str = c_strTblCrtUniqueNoTmplt if blnUqeNo else ''
    strUqeNo=strUqeNo.replace('<UqeNo>', c_strDBTblColNameUqeNo)
    strPrmKey:str = c_strTblCrtPrimaryKeyTmplt if len(lstColNamePrmKey) > 0 else ''
    strPrmKey = strPrmKey.replace('<PrmKeyCol>', c_strSQLSplitor.join(lstColNamePrmKey))

    strSQLRun = c_strTblCreateTmplt
    strSQLRun = strSQLRun.replace('<CreateTbl>', strSQLTypeTblCrt)
    strSQLRun = strSQLRun.replace('<TblName>', strTblName)
    strSQLRun = strSQLRun.replace('<SQLColTblCrt>', strSQLColTblCrt)
    strSQLRun = strSQLRun.replace('<AutoIncrementSrt>', '')
    strSQLRun = strSQLRun.replace('<PrmKeyStr>', strPrmKey)
    strSQLRun = strSQLRun.replace('<UqeNoStr>', strUqeNo)

    blnResult, strErrMsg, lstInsertID = \
        EHDB.fnDBRSTGet(
            strSQLRun = strSQLRun,
            strSectName = strSectName,
            strDBName = strDBName,
            blnExec = True,
            blnErrRtn = blnErrRtn
        )

    strFuncName='EHDBApply.fnDBTblCreate'
    return \
        EHDebug.fnErrRtn(
            blnResult=blnResult,
            strErrMsg=strErrMsg,
            strFuncName=strFuncName,
            blnErrRtn=blnErrRtn
        )

def fnDBTblDrop(
        strTblName:str ,
        strSectName:str = '',
        blnDataChk:bool = True,
        blnErrRtn:bool = False
) -> (bool, str):
    # <PyFunc: fnDBTblDrop>
    #   Desc: Create DB Table
    #   Use By:
    #   Noticed:
    #   Parameter:
    #       strTblName: Table Name
    #   Option:
    #       strSectName= INI Config Section Name
    #       blnDataChk= if Table Record Existed
    #       blnForce= Force Drop Table
    # </PyFunc: fnDBTblDrop>
    
    
    lstTblName, lstTblSchema = fnDBTblEnum(strSectName=strSectName, strTblName=strTblName)
    if lstTblName is None: return True

    if blnDataChk:
        strSQL = "SELECT COUNT(*) FROM <TblName>"
        strSQLRun = strSQL
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        blnResult, strErrMsg, rowDataChk = (
            EHDB.fnDBRSTGet(strSQLRun=strSQLRun, strSectName=strSectName))
        if not blnResult: return False, strErrMsg

        if not rowDataChk is None:
            strErrMsg='DB Table: {} has data!'.format(strTblName)
            strFuncName='EHDBApply.fnDBTblDrop'
            return \
                EHDebug.fnErrRtn(
                    blnResult=False,
                    strErrMsg=strErrMsg,
                    strFuncName=strFuncName,
                    blnErrRtn=blnErrRtn
                )
        else:
            blnResult = True
    else:
        blnResult = True

    if blnResult:
        strSQL = 'DROP TABLE <TblName>'
        strSQLRun = strSQL
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        EHDB.fnExecSQL(strSQL=strSQLRun, strSectName=strSectName)
        strErrMsg='DB Table: {} Dropped!'.format(strTblName)
        strFuncName='EHDBApply.fnDBTblDrop'
        return \
            EHDebug.fnErrRtn(
                blnResult=blnResult,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                blnLog=blnErrRtn
            )
    return blnResult

# <PyDebug: >
def fnDBTblChk(
        strTblName:str,
        dictTblSchema:dict, 
        strSectName:str = '',
        blnReBud:bool = False
):
    # <PyFunc: >
    #   Desc: Check DB Table Existed or Create it
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #   Option:
    #      strSectName= INI Config Section Name
    #      blnReBud= Rebuild Table
    # </PyFunc: >
    lstDBTblName = None
    if blnReBud:
        blnResult = \
            fnDBTblDrop(
                strTblName=strTblName,
                strSectName=strSectName,
                blnDataChk=False
            )
    else:
        lstDBTblName, lstDBTbl = \
            fnDBTblEnum(
                strSectName=strSectName,
                strTblName=strTblName
            )

    if lstDBTblName is None :
        lstColSchema, lstColSchemaSQL = \
            fnDBColSchemaCvrt(dictTblSchema=dictTblSchema)
        blnResult = \
            fnDBTblCreate(
                strTblName=strTblName,
                strSectName=strSectName,
                lstColSchema=lstColSchema
            )
    else:
        blnResult = True
    return blnResult

def fnDBTblNullRpl(
        strTblName,
        strSectName='',
) -> (bool, str, list | None):
    # <PyFunc: fnDBTblNullRpl>
    #   Desc: Replace All Cols of User indicated Table, replace NULL to Blank ''
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #   Option:
    #      strSectName= INI Config Section Name
    #   Return: ColName List with NULL replaced 
    # </PyFunc: fnDBTblNullRpl>
    c_strSQLUpdateNull = 'UPDATE <TblName> SET <ColName>=\'\' WHERE <ColName> IS NULL'

    blnResult, strErrMsg, lstColSchemaTrg, lstColNameTrg = \
        fnDBColSchemaGet(
            strSectName=strSectName,
            strTblName=strTblName
        )
    if not blnResult: return False, strErrMsg, None
    udtCNN = EHDB.fnDBCNNGet(strSectName=strSectName)
    objCursor = udtCNN.objCursor

    lstColName = []
    for rowRun in lstColSchema:
        strSQLRun = c_strSQLUpdateNull
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        strSQLRun = strSQLRun.replace('<ColName>', rowRun[c_intTblColSchemaColName])
        objCursor.execute(strSQLRun)
        objCursor.commit()
        lstColName.append(rowRun[c_intTblColSchemaColName])
    return True, '', lstColName

def fnDBTblCmp(
        strTblSrc,
        strTblTrg,
        strSectName='',
        lstColNameSrcUsr=None,
        lstColNameTrgUsr=None,
        strCriteriaSrc='',
        strCriteriaTrg=''
)->(bool, str, pyodbc.Row | None):
    # <PyFunc: fnDBTblCmp>
    #   Desc: DB Table Data Compare, it can Compare 2 Table Data
    #       Using by SELECT User Defined Col (lstColNameSrcUsr, lstColNameTrgUsr),
    #       And GROUP BY User Defined Col,
    #       And HAVING COUNT(*)<>2
    #   Use By:
    #   Noticed:
    #   Parameter:
    #       strTblSrc: Source Table Name
    #       strTblTrg: Target Table Name
    #   Option:
    #       strSectName= INI Config Section Name
    #       lstColNameSrcUsr= Source Table User Defined Col Name List
    #       lstColNameTrgUsr= Target Table User Defined Col Name List
    #       strCriteriaSrc= Source Table Criteria
    #       strCriteriaTrg= Target Table Criteria
    # </PyFunc: fnDBTblCmp>

    if c_blnEHDebugMode: print('fnDBTblCmp')
    blnResult, strErrMsg, lstColSchemaSrc, lstDBColNameSrc = \
        fnDBColSchemaGet(
            strSectName=strSectName,
            strTblName=strTblSrc,
            blnSysDftColElm=True
        )
    if not blnResult: return False, strErrMsg, None
    if lstColNameSrcUsr is None and blnResult: lstColNameSrcUsr = lstDBColNameSrc
    lstSQLColSeltSrc = []
    for strColNameRun in lstColNameSrcUsr:
        if strColNameRun in lstDBColNameSrc:
            blnResult, strErrMsg, dictColSchema = \
                fnDBColSngSchemaDictCvrt(
                    strColName=strColNameRun,
                    lstColSchema=lstColSchemaSrc,
                    blnErrRtn = True
                )
            if not blnResult:
                strErrMsg = 'SourceTable: {} ColSchema Convert to Dict Fail!'.format(strTblSrc)
                strFuncName = 'EHDBApply.fnDBTblCmp'
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
                return None
            strSQLColRun = dictColSchema['strSQLColSeltRun']
            lstSQLColSeltSrc.append(strSQLColRun)

    blnResult, strErrMsg, lstColSchemaTrg, lstDBColNameTrg = \
        fnDBColSchemaGet(
            strSectName=strSectName,
            strTblName=strTblTrg,
            blnSysDftColElm=True
        )
    if not blnResult: return False, strErrMsg, None
    if lstColNameTrgUsr is None and blnResult: lstColNameTrgUsr = lstDBColNameTrg
    lstSQLColSeltTrg = []
    for strColNameRun in lstColNameTrgUsr:
        if strColNameRun in lstDBColNameTrg:
            blnResult, strErrMsg, dictColSchema  = \
                fnDBColSngSchemaDictCvrt(
                    strColName=strColNameRun,
                    lstColSchema=lstColSchemaTrg,
                    blnErrRtn = True
                )
            if not blnResult:
                strErrMsg = 'TargetTable: {} ColSchema Convert to Dict Fail!'.format(strTblTrg)
                strFuncName = 'EHDBApply.fnDBTblCmp'
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
                return None
            strSQLColRun = dictColSchema['strSQLColSeltRun']
            lstSQLColSeltTrg.append(strSQLColRun)

    c_strSQLTblCmp = \
        'SELECT ' + \
        'MIN(TblName) AS TblName, ' + \
        'MIN(<UqeNoColName>) AS <UqeNoColName>, ' + \
        '<ColNameCollSrc> ' + \
        'FROM ' + \
        '(' + \
        '<TblCmpStrSubSrc> ' + \
        'UNION ALL ' + \
        '<TblCmpStrSubTrg> ' + \
        ') Tmp ' + \
        'GROUP BY <ColNameCollSrc> ' + \
        'HAVING COUNT(*)<>2 ' + \
        'ORDER BY TblName, <ColNameCollSrc> '

    c_strSQLTblCmpSub = \
        'SELECT ' + \
        '\'<DataType>\' AS TblName, ' + \
        '<UqeNoColName> AS <UqeNoColName>, ' + \
        '<ColNameColl> ' + \
        'FROM ' + \
        '<TblName> ' + \
        '<WHEREStr>' + \
        '<CriteriaStr>'

    strSQLRunSrc = c_strSQLTblCmpSub
    strSQLRunSrc = strSQLRunSrc.replace('<DataType>', 'Source')
    strSQLRunSrc = strSQLRunSrc.replace('<UqeNoColName>', c_strDBTblColNameUqeNo)
    strSQLRunSrc = strSQLRunSrc.replace('<ColNameColl>', EHSymbolDef.c_strSQLSplitor.join(lstSQLColSeltSrc))
    strSQLRunSrc = strSQLRunSrc.replace('<TblName>', strTblSrc)
    strSQLRunSrc = strSQLRunSrc.replace('<WHEREStr>', ('WHERE ' if len(strCriteriaSrc) > 0 else ''))
    strSQLRunSrc = strSQLRunSrc.replace('<CriteriaStr>', (strCriteriaSrc if len(strCriteriaSrc) > 0 else ''))

    strSQLRunTrg = c_strSQLTblCmpSub
    strSQLRunTrg = strSQLRunTrg.replace('<DataType>', 'Target')
    strSQLRunTrg = strSQLRunTrg.replace('<UqeNoColName>', c_strDBTblColNameUqeNo)
    strSQLRunTrg = strSQLRunTrg.replace('<ColNameColl>', EHSymbolDef.c_strSQLSplitor.join(lstSQLColSeltTrg))
    strSQLRunTrg = strSQLRunTrg.replace('<TblName>', strTblTrg)
    strSQLRunTrg = strSQLRunTrg.replace('<WHEREStr>', ('WHERE ' if len(strCriteriaTrg) > 0 else ''))
    strSQLRunTrg = strSQLRunTrg.replace('<CriteriaStr>', (strCriteriaTrg if len(strCriteriaTrg) > 0 else ''))

    strSQLRun = c_strSQLTblCmp
    strSQLRun = strSQLRun.replace('<UqeNoColName>', c_strDBTblColNameUqeNo)
    strSQLRun = strSQLRun.replace('<ColNameCollSrc>', EHSymbolDef.c_strSQLSplitor.join(lstDBColNameSrc))
    strSQLRun = strSQLRun.replace('<TblCmpStrSubSrc>', strSQLRunSrc)
    strSQLRun = strSQLRun.replace('<TblCmpStrSubTrg>', strSQLRunTrg)

    if c_blnEHDebugMode:
        EHMsg.fnMsgPrt('EHDBApply.fnDBTblCmp.strSQLRun: {}'.format(strSQLRun))
    blnResult, strErrMsg, rowTblCmp = (
        EHDB.fnDBRSTGet(strSQLRun=strSQLRun, strSectName=strSectName))
    strFuncName = 'EHDBApply.fnDBTblCmp'
    return \
        EHDebug.fnErrRtn(
            blnResult=blnResult,
            strErrMsg=strErrMsg,
            strFuncName=strFuncName,
            rowTblCmp=rowTblCmp
        )
# </PyRegion: DBTbl>

# <PyRegion: DBRST>
def fnDBRSTFieldNameGet(
        RST,
        lstElmCol=''
) -> list:
    # <PyFunc: >
    #   Desc: Get RST Field Name
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      RST= DB RST Only!
    #   Option:
    #      lstElmCol= Eliminate Col Name List
    #   Return: RST Field Name List
    # </PyFunc: >
    if RST is None: return None

    lstRSTFldName = []
    lstRSTFldNameSkip = []
    for RSTFld in RST.Fields:
        strRSTFldName = RSTFld.name
        if strRSTFldName in lstElmCol:
            lstRSTFldNameSkip.append(strRSTFldName)
        else:
            lstRSTFldName.append(strRSTFldName)
    return lstRSTFldName

def fnDBRSTInsert(
        strTblName,
        strSectName='',
        strDBName='',
        lstColName=None,
        lstColValue=None,
        lstUqeNo=None,
        blnColSchemaChk=True,
        lstColSchema=None,
        blnErrRtn=False,
        intRowRef=0,
        dateRun=None
) -> ( bool, str, list):
    # <PyFunc: fnDBRSTInsert>
    #   Desc: Insert data into DB
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #   Option:
    #      strSectName= INI Config Section Name
    #      lstColName= Insert ColName
    #      lstColValue= Insert ColValue
    #      lstUqeNo= Unique No List
    #      blnColSchemaChk= Check Column Schema
    #      lstColSchema= Column Schema List
    #      blnErrRtn= Error Return or not, if True, return Error Message String
    #      intRowRef= Excel Sheet Run Row, for ErrMsg Show up
    #      dateRun= for insert DB UploadTime Col
    # </PyFunc: fnDBRSTInsert>
    blnResult = False
    if lstColSchema is None:
        # <PyCmt: if parameter lstColSchema is None, get it from DB>
        blnResult, strErrMsg, lstColSchema, lstDBColName = \
            fnDBColSchemaGet(
                strTblName = strTblName,
                strSectName = strSectName,
                lstColNameCollUser = lstColName,
                blnErrRtn = blnErrRtn
            )
        if not blnResult: return False, strErrMsg, None

    if lstColName is None:
        lstColName = []
        for lstRow in lstColSchema:
            lstColName.append(lstRow[c_intTblColSchemaColName])

    blnInsertSelt = False
    if not lstUqeNo is None:
        # <PyCmt: if UniqueNo List Not pass in, then using INSERT INTO, SELECT >
        blnInsertSelt = True
    elif not isinstance(lstColName, list) or \
            not isinstance(lstColValue, list):
        strErrMsg = (('Row: {}, ' if intRowRef > 0 else '').format(intRowRef) +
            'lstColName({0}) or lstColValue({1}) Type Error!'.format(type(lstColName), type(lstColValue)))
        strFuncName = 'EHDBApply.fnDBRSTInsert'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                lstInsertedID=None
            )
    elif len(lstColName) != len(lstColValue):
        strErrMsg = ('Row: {}, ' if intRowRef > 0 else '').format(intRowRef) + \
            'lstColName({0}) or lstColValue({1}) Qty Mismatch!'.format(lstColName, lstColValue)
        strFuncName = 'EHDBApply.fnDBRSTInsert'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                lstInsertedID=None
            )

    lstColNameInsert = []
    lstColValueInsert = []
    if blnInsertSelt:
        lstColNameInsert = lstColName
        if c_strDBTblColNameUqeNo in lstColNameInsert:
            lstColNameInsert.remove(c_strDBTblColNameUqeNo)
    elif blnColSchemaChk:
        lstErrMsg=[]
        lstColName, lstColValue = \
            fnDBColSysColNameRemove(lstColName=lstColName, lstColValue=lstColValue)
        lstColValue=fnDBColSysColValReplace(lstColName=lstColName, lstColValue=lstColValue)
        for strColName in lstColName:
            intColIndex= lstColName.index(strColName)
            strColValue = lstColValue[intColIndex]
            blnResult, strErrMsg, dictColSchema  = \
                fnDBColSngSchemaDictCvrt(
                    strColName=strColName,
                    lstColSchema=lstColSchema,
                    strColValue=strColValue,
                    blnErrRtn = True
                )
            strColValue = dictColSchema["strColValueRun"]
            if not blnResult:
                strFuncName = "EHDBApply.fnDBRSTInsert"
                strErrMsg = dictColSchema['strErrMsg']
                strErrMsg = ('Row: {}, ' if intRowRef > 0 else '').format(intRowRef) + strErrMsg
                if blnErrRtn:
                    lstErrMsg.append(strErrMsg)
                else:
                    return EHDebug.fnErrRtn(
                        blnResult=False,
                        strErrMsg=strErrMsg,
                        strFuncName=strFuncName,
                        blnErrRtn=blnErrRtn,
                        lstInsertedID=None
                    )
            lstColNameInsert.append(strColName)
            lstColValueInsert.append(strColValue)
        # <PyCmt: Record DataType Error, return ErrMsg String>

        strErrMsg = c_strNewLine.join(lstErrMsg)
        strFuncName = 'EHDBApply.fnDBRSTInsert'
        if len(lstErrMsg)>0:
            return EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                lstInsertedID=None,
            )
    else:
        lstColNameInsert = lstColName
        lstColValueInsert = lstColValue

    lstErrMsg = []
    if blnInsertSelt:
        strSQL = 'INSERT INTO <EHDBName><TblName> '
        strSQL = strSQL + \
                 '(<ColName>) '
        strSQL = strSQL + \
                 'SELECT ' + \
                 '<ColName> '
        strSQL = strSQL + \
                 'FROM ' + \
                 '<TblName> '
        strSQL = strSQL + \
                 'WHERE ' + \
                 '<CrtaStr> '
        blnResult, dateRun = EHDate.fnDateChk(dateRun=dateRun, blnErrRtn=blnErrRtn)
        if not blnResult:
            strErrMsg = 'dateRun: {} Convert Error'.format(dateRun)
            strFuncName = 'EHDBApply.fnDBRSTInsert'
            return EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                blnErrRtn=blnErrRtn,
                lstInsertedID=None,
            )
        strDateRun=EHDate.fnDateToStr(dateRun=dateRun, blnDBDate=True)

        lstInsertedID = []
        for intUqeNoRun in lstUqeNo:
            strColUpdRun = c_strSQLUqeNoCrta  # c_strSQLUqeNoCrta='<UqeNoColName>=\'<UqeNoColValue>\' '
            strColUpdRun = strColUpdRun.replace('<UqeNoColName>', c_strDBTblColNameUqeNo)
            strColUpdRun = strColUpdRun.replace('<UqeNoColValue>', str(intUqeNoRun))
            strSQLRun = strSQL
            strSQLRun = strSQLRun.replace('<TblName>', strTblName)
            strSQLRun = strSQLRun.replace('<ColName>', c_strSQLSplitor.join(lstColNameInsert))
            strSQLRun = strSQLRun.replace(''.join(['\'<',c_strDBTblColNameUpdateTime,'\'>']), strDateRun)
            strSQLRun = strSQLRun.replace('<CrtaStr>', strColUpdRun)
            blnResult, strErrMsg, lstInsertedIDRun = \
                EHDB.fnDBRSTGet(
                    strSQLRun = strSQLRun,
                    strSectName = strSectName,
                    strDBName = strDBName,
                    blnExec=True,
                    blnErrRtn = blnErrRtn
                )
            if not blnResult:
                lstErrMsg.append(strErrMsg)
            else:
                lstInsertedID.append(lstInsertedIDRun)
        if len(lstErrMsg)>0:
            blnResult = False
            strErrMsg = c_strNewLine.join(lstErrMsg)
            return False, strErrMsg, None
        else:
            return blnResult, '', lstInsertedID
    else:
        strSQL = 'INSERT INTO <EHDBName><TbName> ' + \
                 '(<ColName>) ' + \
                 'VALUES(<ColValue>)'
        strSQLRun = strSQL
        strSQLRun = strSQLRun.replace('<TbName>', strTblName)
        strSQLRun = strSQLRun.replace('<ColName>', c_strSQLSplitor.join(lstColNameInsert))
        strSQLRun = strSQLRun.replace('<ColValue>', c_strSQLSplitor.join(lstColValueInsert))
        blnResult, strErrMsg, lstInsertedID = \
            EHDB.fnDBRSTGet(
                strSQLRun = strSQLRun,
                strSectName = strSectName,
                strDBName = strDBName,
                blnExec=True,
                blnErrRtn = blnErrRtn
            )
    return blnResult, strErrMsg, lstInsertedID

def fnDBRSTUpdate(
        strTblName: str,
        strCriteria:str,
        lstColName:list,
        lstColValue:list,
        strSectName:str = '',
        strDBName:str = '',
        lstValueApdColColl:list = None,
        strOrdBy:str = '',
        intTopRec:int = 0,
        blnDirUpd:bool = False,
        blnErrRtn:bool = False,
        intRowRef:int = 0,
        dateRun:datetime.datetime = None
) -> (bool, str, list):
    # <PyFunc: fnDBRSTUpdate>
    #   Desc: Update DB Table Recordset
    #      1. Get UniqueNo which match Criteria
    #      2. Update Old Record, LastVer='N'
    #      3. Insert New Record, by lstColName, lstColValue
    #      4. if blnDirUpd=True, Update Recordset Directly
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #      strCriteria= Update Criteria
    #      lstColName= Insert ColName
    #      lstColValue= Insert ColValue
    #   Option:
    #      strSectName= INI Config Section Name
    #      lstValueApdColColl= Update Value with Append ColName and Value
    #      strOrdBy= work with intTopRec, Order By ColName
    #      intTopRec= work with strOrdBy, Only Update Top Record Count
    #      blnDirUpd= Update Recordset Directly
    #      dateRun= for insert DB UploadTime Col
    # </PyFunc: fnDBRSTUpdate>
    blnResult = False
    if len(lstColName) != len(lstColValue):
        strErrMsg = \
            'Update lstColName, lstColValue Qty Mismatch!' + \
            'lstColName({}): {}, lstColValue({}): {}'.format(len(lstColName), lstColName, len(lstColValue), lstColValue)
        strFuncName = 'EHDBApply.fnDBRSTUpdate'
        if blnErrRtn: return blnResult, strErrMsg
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return blnResult, strErrMsg

    blnResult, strErrMsg, lstColSchema, lstDBColName = \
        fnDBColSchemaGet(
            strTblName = strTblName,
            strSectName = strSectName,
            strDBName = strDBName,
            lstColNameCollUser=lstColName,
            blnErrRtn=True
        )
    if not blnResult: return False, strErrMsg, None

    lstColUpd = []
    lstColValueRun=[]
    lstErrMsg = []
    intRun = 0
    for strColName in lstColName:
        strColValue = lstColValue[intRun]
        strColUpdRun=''
        if blnDirUpd:
            strColUpdRun = c_strSQLColUpdTmplt
            strColUpdRun = strColUpdRun.replace('<ColName>', strColName)
            strColUpdRun = strColUpdRun.replace('<ColValue>', strColValue)
            strColUpdRun = strColUpdRun.replace('<CriteriaStr>', strCriteria)
            strColUpdRun = strColUpdRun.replace('<OrderByStr>', strOrdBy)
            strColUpdRun = strColUpdRun.replace('<TopRecCount>', intTopRec)
        else:
            if strColValue is None:
                pass
            elif len(strColValue)>=2:
                if strColValue[0] == '\'' and strColValue[-1] == '\'':
                    strColValue = strColValue[1:-1]
            blnResult, strErrMsg, dictColSchema = \
                fnDBColSngSchemaDictCvrt(
                    strColName = strColName,
                    lstColSchema = lstColSchema,
                    strColValue = strColValue,
                    lstValueApdColColl = lstValueApdColColl,
                    blnErrRtn = True
                )
            if not blnResult:
                strErrMsg = ('Row: {}, ' if intRowRef > 0 else '').format(intRowRef) + strErrMsg
                lstErrMsg.append(strErrMsg)
            else:
                strColValue = dictColSchema['strColValueRun']
                strColUpdRun = dictColSchema['strSQLColUpdRun']
        lstColUpd.append(strColUpdRun)
        lstColValueRun.append(strColValue)
        intRun += 1
        strErrMsg = c_strNewLine.join(lstErrMsg)
        strFuncName = 'EHDBApply.fnDBRSTUpdate'
        if len(strErrMsg)>0:
            if blnErrRtn: return strErrMsg, blnResult
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
            return blnResult, c_strNewLine.join(strErrMsg)

    if blnDirUpd:
        # <PyCmt: blnDirUpd=True, Update Recordset Directly>
        strSQLUpdDir = 'UPDATE ' + \
                       '<TblName> ' + \
                       'SET ' + \
                       '<ColNameValue> ' + \
                       'WHERE ' + \
                       '<CriteriaStr> '
        if len(strOrdBy) > 0:
            strSQLUpdDir = strSQLUpdDir + \
                           'ORDER BY ' + \
                           '<OrderByStr> '
        if intTopRec > 0:
            strSQLUpdDir = strSQLUpdDir + \
                           'LIMIT ' + \
                           '<TopRecCount> '

        strSQLRun = strSQLUpdDir
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        strSQLRun = strSQLRun.replace('<ColNameValue>', c_strSQLSplitor.join(lstColUpd))
        blnResult, strErrMsg, lstInsertedID = \
            EHDB.fnDBRSTGet(
                strSQLRun=strSQLRun,
                strSectName=strSectName,
                strDBName=strDBName,
                blnExec=True,
                blnErrRtn = blnErrRtn
            )
        return blnResult, lstInsertedID, strErrMsg
    else:
        # <PyCmt: Get UniqueNo which match Criteria>
        lstUqeNo = \
            fnDBRSTUqeNoGet(
                strTblName=strTblName,
                strCtra=strCriteria,
                strSectName=strSectName,
                strDBName=strDBName,
                strOrdBy=strOrdBy,
                intTopRec=intTopRec
            )
        # </PyCmt: Get UniqueNo which match Criteria>
        if len(lstUqeNo)==0:
            blnResult, dateRun = EHDate.fnDateChk(dateRun=dateRun, blnErrRtn=blnErrRtn)
            if not blnResult:
                strErrMsg = 'intRowRef: {}, dateRun Convert Error!'.format(intRowRef)
                strFuncName = 'EHDBApply.fnDBRSTUpdate'
                if blnErrRtn: return blnResult, strErrMsg
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
                return blnResult, strErrMsg

            blnResult, strErrMsg, lstInsertID = \
                fnDBRSTInsert(
                    strTblName = strTblName,
                    strSectName = strSectName,
                    strDBName = strDBName,
                    lstColName = lstColName,
                    lstColValue = lstColValueRun,
                    blnColSchemaChk = False,
                    lstColSchema = lstColSchema,
                    blnErrRtn = blnErrRtn,
                    intRowRef = intRowRef,
                    dateRun = dateRun
                )
            return blnResult, strErrMsg, lstInsertID
        # <PyCmt: Get Inserted UniqueNo>
        blnResult, strErrMsg, lstUqnNoInsert = \
            fnDBRSTInsert(
                strTblName=strTblName,
                strSectName=strSectName,
                lstUqeNo=lstUqeNo
            )
        # </PyCmt: Get Inserted UniqueNo>
        # <PyCmt: blnDirUpd=False, Update Recordset via UniqueNo>
        strSQLUpdUqeNo = \
            'UPDATE <TblName> ' + \
            'SET <ColUpdColl> ' + \
            'WHERE ' + \
            '<UquNoColName> IN (<UqeNoColl>)'
        # </PyCmt: blnDirUpd=False, Update Recordset via UniqueNo>

        # <PyCmt: Update Old Record, LastVer='N' >
        strSQLRun = strSQLUpdUqeNo
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        strSQLRun = strSQLRun.replace('<ColUpdColl>', 'LastVer=\'N\' ')
        strSQLRun = strSQLRun.replace('<UquNoColName>', c_strDBTblColNameUqeNo)
        #   <PyCmt: UquNo List Join Process>
        strUqeNoJoin = c_strSQLValueBracketSymbol + c_strSQLSplitor + c_strSQLValueBracketSymbol
        strUqeNoRun = ''.join([c_strSQLValueBracketSymbol, strUqeNoJoin.join([str(strUqeNo) for strUqeNo in lstUqeNo]),
                               c_strSQLValueBracketSymbol])
        strSQLRun = strSQLRun.replace('<UqeNoColl>', strUqeNoRun)
        blnResult, strErrMsg, lstInsertedID = \
            EHDB.fnDBRSTGet(
                strSQLRun=strSQLRun,
                strSectName=strSectName,
                blnExec=True,
                blnErrRtn = True
            )
        if not blnResult:
            strErrMsg = 'intRowRef: {}, Update Old Record Fail!'.format(intRowRef)
            strFuncName = 'EHDBApply.fnDBRSTUpdate'
            return \
                EHDebug.fnErrRtn(
                    blnResult=False,
                    strErrMsg=strErrMsg,
                    strFuncName=strFuncName,
                    blnErrRtn=blnErrRtn,
                    blnLog=False,
                    lstInsertID=None
                )
        # </PyCmt: Update Old Record, LastVer='N' >

        # <PyCmt: Update New Record, Col: Uploader, UpdateTime >
        strColUpdColl = \
            '<UploaderCol>=\'<UploaderValue>\' ' + \
            ', <UpdateTimeCol>=\'<UpdateTimeValue>\' '
        strColUpdCollRun = strColUpdColl
        strColUpdCollRun = strColUpdCollRun.replace('<UploaderCol>', c_strDBTblColNameUploader)
        strColUpdCollRun = strColUpdCollRun.replace('<UploaderValue>', os.environ['USERNAME'])
        strColUpdCollRun = strColUpdCollRun.replace('<UpdateTimeCol>', c_strDBTblColNameUpdateTime)
        strColUpdCollRun = strColUpdCollRun.replace('<UpdateTimeValue>',
            EHDate.fnDateToStr(dateRun=dateRun, blnDBDate=True) )

        # <PyCmt: lstColUpd Combine>
        lstColUpd.append(strColUpdCollRun)
        strColUpdCollRun = c_strSQLSplitor.join(lstColUpd)
        # </PyCmt: lstColUpd Combine>

        strSQLRun = strSQLUpdUqeNo
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        strSQLRun = strSQLRun.replace('<ColUpdColl>', strColUpdCollRun)
        strSQLRun = strSQLRun.replace('<UquNoColName>', c_strDBTblColNameUqeNo)
        #   <PyCmt: UquNo List Join Process>
        strUqeNoJoin = c_strSQLValueBracketSymbol + c_strSQLSplitor + c_strSQLValueBracketSymbol
        strUqeNoRun = ''.join(
            [c_strSQLValueBracketSymbol, strUqeNoJoin.join([str(strUqeNo) for strUqeNo in lstUqnNoInsert]),
             c_strSQLValueBracketSymbol])
        strSQLRun = strSQLRun.replace('<UqeNoColl>', strUqeNoRun)
        blnResult, strErrMsg, lstInsertedID = \
            EHDB.fnDBRSTGet(
                strSQLRun=strSQLRun,
                strSectName=strSectName,
                blnExec=True,
                blnErrRtn = True
            )
        if not blnResult:
            strErrMsg = 'intRowRef: {}, Update New Record Fail!'.format(intRowRef)
            strFuncName = 'EHDBApply.fnDBRSTUpdate'
            return \
                EHDebug.fnErrRtn(
                    blnErrRtn=blnErrRtn,
                    blnResult=blnResult,
                    strErrMsg=strErrMsg,
                    strFuncName=strFuncName,
                    lstInsertedID=None
                )
        return blnResult, lstInsertedID
        # </PyCmt: Update New Record, Col: Uploader, UpdateTime >

def fnDBRSTDelete(
        strTblName,
        strCriteria='',
        strSectName='',
        strDBName=''
)->(bool, str):
    # <PyFunc: fnDBRSTDelete>
    #   Desc: Delete DB Table Recordset
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #   Option:
    #      strCriteria= Delete Criteria
    #      strSectName= INI Config Section Name
    #      strDBName= DB Name
    # </PyFunc: fnDBRSTDelete>
    strSQL = 'DELETE FROM <EHDBName><TblName> '
    if len(strCriteria) > 0:
        strSQL = strSQL + \
                 'WHERE ' + \
                    '<CtraStr> '
    strSQLRun = strSQL
    strSQLRun = strSQLRun.replace('<TblName>', strTblName)
    strSQLRun = strSQLRun.replace('<CtraStr>', strCriteria)
    blnResult, strErrMsg, lstInsertedID = \
        EHDB.fnDBRSTGet(
            strSQLRun=strSQLRun,
            strSectName=strSectName,
            strDBName=strDBName,
            blnExec=True
        )
    return blnResult, strErrMsg

def fnDBRSTUqeNoGet(
        strTblName,
        strCtra,
        strSectName='',
        strDBName='',
        strOrdBy='',
        intTopRec=0
) -> (bool, str, pyodbc.Row) :
    # <PyFunc: fnDBRSTUqeNoGet>
    #   Desc: Get UniqueNo which match Criteria
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #      strCtra= Get UniqueNo Criteria
    #   Option:
    #      strSectName= INI Config Section Name
    #      strOrdBy= work with intTopRec, Order By ColName
    #      intTopRec= work with strOrdBy, Only Update Top Record Count
    #   Return:
    #      lstUqeNo= UniqueNo List
    # </PyFunc: fnDBRSTUqeNoGet>
    strSQL = \
        'SELECT ' + \
        "<UqeNoCol> " + \
        'FROM ' + \
        '<EHDBName><TblName> ' + \
        'WHERE ' + \
        '<CtraStr> '
    if len(strOrdBy) > 0:
        strSQL = \
            'ORDER BY ' + \
            '<OrdByStr> '
    if intTopRec > 0:
        strSQL = \
            'LIMIT ' + \
            '<TopRec> '
    strSQLRun = strSQL
    strSQLRun = strSQLRun.replace('<UqeNoCol>', c_strDBTblColNameUqeNo)
    strSQLRun = strSQLRun.replace('<TblName>', strTblName)
    strSQLRun = strSQLRun.replace('<CtraStr>', strCtra)
    strSQLRun = strSQLRun.replace('<OrdByStr>', strOrdBy)
    strSQLRun = strSQLRun.replace('<TopRec>', str(intTopRec))
    blnResult, strErrMsg, rowUqeNo = \
        EHDB.fnDBRSTGet(
            strSQLRun=strSQLRun,
            strSectName=strSectName,
            strDBName=strDBName
        )

    strErrMsg = "rowUqeNo: {}".format(rowUqeNo)
    strFuncName = "EHDBApply.fnDBRSTUqeNoGet"
    return \
        EHDebug.fnErrRtn(
            blnResult=blnResult,
            strErrMsg=strErrMsg,
            strFuncName=strFuncName,
            rowUqeNo=rowUqeNo
        )

def fnDBRSTExistCheck(
        strTblName:str,
        strCriteria:str,
        strSectName:str = '',
        strOrdBy:str = '',
        intTopRec:int = 0
) -> (bool, str, pyodbc.Row):
    # <PyFunc: >
    #   Desc: Insert data into DB
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #      lstColName= Insert ColName
    #      lstColValue= Insert ColValue
    #   Option:
    #      strSectName= INI Config Section Name
    #      intRowRef= Excel Sheet Run Row, for ErrMsg Show up
    #   Return: 
    # </PyFunc: >

    strSQL = 'SELECT ' + \
             '<UqeNoColName> '
    strSQL = strSQL + \
             "FROM " + \
             "<EHDBName><TBlName> "
    strSQL = strSQL + \
             "WHERE " + \
             "<Crta> "
    if len(strOrdBy)>0:
        strSQL = strSQL + \
            "ORDER BY " + \
                 "<OrderByStr> "
    if intTopRec > 0:
        strSQL = strSQL + \
            "LIMIT " + \
                "<TopRecCount> "
    strSQLRun = strSQL
    strSQLRun = strSQLRun.replace('<UqeNoColName>', c_strDBTblColNameUqeNo)
    strSQLRun = strSQLRun.replace('<TBlName>', strTblName)
    strSQLRun = strSQLRun.replace('<Crta>', strCriteria)
    strSQLRun = strSQLRun.replace('<OrderByStr>', strOrdBy if len(strOrdBy) > 0 else '')
    strSQLRun = strSQLRun.replace('<TopRecCount>', intTopRec)

    blnResult, strErrMsg, rowRun = \
        EHDB.fnDBRSTGet(
            strSQLRun=strSQLRun,
            strSectName=strSectName
        )

    strFuncName = "EHDBApply.fnDBRSTExistCheck"
    return \
        EHDebug.fnErrRtn(
            blnResult=blnResult,
            strErrMsg=strErrMsg,
            strFuncName=strFuncName,
            rowRun=rowRun
        )

def fnDBRSTDupliRmv(
        strTblName,
        strSectName='',
        strDBName=''
)->bool:
    # <PyFunc: >
    #   Desc: Compare DB Table Record, and Delete via UniqueNo
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #   Option:
    #      strSectName= INI Config Section Name
    #   Return:
    # </PyFunc: >
    blnResult, strErrMsg, lstColSchema, lstDBColName = \
        fnDBColSchemaGet(
            strTblName=strTblName,
            strSectName=strSectName,
            strDBName=strDBName
        )
    if not blnResult: return False

    if not c_strDBTblColNameUqeNo in lstDBColName:
        return None
    strSQL = 'DELETE ' + \
             'Table1 '
    strSQL = strSQL + \
             'FROM ' + \
             '<TblName> Table1 ' + \
             'JOIN <TblName> Table2 '
    strSQL = strSQL + \
             'ON ' + \
             'Table1.<UqeNoColName> < Table2.<UqeNoColName> ' + \
             '<ColCrta>'
    strColCrtaTbl1 = ('Table1.' + (c_strSQLSplitor + 'Table1.').join(lstDBColName)).split(c_strSQLSplitor)
    strColCrtaTbl2 = ('Table2.' + (c_strSQLSplitor + 'Table2.').join(lstDBColName)).split(c_strSQLSplitor)
    strColCrtaTbl = ['='.join(strRun) for strRun in zip(strColCrtaTbl1, strColCrtaTbl2)]
    strColCrtaTbl=' AND '.join(strColCrtaTbl)
    strSQLRun = strSQL
    strSQLRun = strSQLRun.replace('<TblName>', strTblName)
    strSQLRun = strSQLRun.replace('<UqeNoColName>', c_strDBTblColNameUqeNo)
    strSQLRun = strSQLRun.replace('<ColCrta>', 'AND ' + strColCrtaTbl)
    return EHDB.fnExecSQL(strSQL=strSQLRun)

def fnDBRSTValueGet(
        strSQLRun='',
        strTblName='',
        strSectName='',
        strDBName='',
        lstColName=None,
        blnColNameUserSeqOnly=False,
        lstElmCol=None,
        blnSysDftColElm=False,
        blnColUqeNoGet=False,
        strCriteria='',
        intTopRec=0,
        blnDistinct=False,
        strOrderBy="",
        blnValueListTrans=False,
        blnCombineToStr=False,
        blnErrRtn=False
)-> (bool, str, pyodbc.Row | str | None) :
    # <PyFunc: fnDBRSTValueGet >
    #   Desc: Get DB Value
    #   Use By:
    #   Noticed: Must with strSQLRun or strTblName
    #   Parameter:
    #   Option:
    #      strSQLRun= SQL string
    #      strTblName= DB Table Name
    #      strSectName= INI Config Section Name
    #      lstColName= Select ColName List
    #      blnColNameUserSeqOnly= Only Select User Seq ColName
    #      lstElmCol= Eliminated ColName List
    #      blnSysDftColElm= Eliminate System Default Col[UniqueNo, Deleted, LastVer, Uploader, UpdateTime]
    #      blnColUqeNoGet= Get UniqueNo Col
    #      strCriteria= Select Criteria
    #      intTopRec= Select Top Record Count
    #      blnDistinct= Get DISTINCT Records
    #      strOrderBy= Get ORDER BY Records
    #      blnValueListTrans= Transpose Result List
    #      blnCombineToStr= Combine Result List to String
    #   Return:
    #       1. blnResult:bool
    #       2. strErrMsg:str
    # </PyFunc: fnDBRSTValueGet >
    if len(strSQLRun) == 0 and len(strTblName) == 0: return False, '', None

    lstElmCol = \
        fnDBColElmGet(
            lstElmCol=lstElmCol,
            blnSysDftColElm=blnSysDftColElm,
            blnUqeNoGet=blnColUqeNoGet
        )
    if len(strTblName) > 0:
        strSQLRun = ''
        blnResult, strErrMsg, lstColSchema, lstDBColName = \
            fnDBColSchemaGet(
                strSQLRun=strSQLRun,
                strTblName=strTblName,
                strSectName=strSectName,
                strDBName=strDBName,
                lstColNameCollUser=lstColName,
                blnColNameUserSeqOnly=blnColNameUserSeqOnly,
                lstElmCol=lstElmCol,
                blnErrRtn=True
            )
        if not blnResult: return False, strErrMsg

        lstSQLCol=[]
        for lstRow in lstColSchema:
            lstSQLCol.append(lstRow[c_intTblColSchemaColSQLColSelt])

        if not lstSQLCol is None:
            if isinstance(lstSQLCol, (list, tuple)):
                strSQLColColl = ', '.join(lstSQLCol)
            else:
                strSQLColColl = lstSQLCol
            strSQL = "SELECT " + \
                     "<Distinct>" + \
                     "<TopRec>" + \
                     "<ColNameColl> "
            strSQL = strSQL + \
                     "FROM " + \
                     "<EHDBName><TbName> "
            if len(strCriteria) > 0:
                strSQL = strSQL + \
                         "WHERE " + \
                         "<CriteriaStr>"
            if len(strOrderBy) > 0:
                strSQL = strSQL + \
                         "ORDER BY " + \
                         "<OrderByStr>"
            strSQLRun = strSQL
            strSQLRun = strSQLRun.replace('<Distinct>', EHSQLAnaly.c_strSQLDISTINCTKeyword if blnDistinct else '')
            strSQLRun = strSQLRun.replace('<TopRec>', (
                (EHSQLAnaly.c_strSQLTOPKeyword + str(intTopRec) + ' ') if intTopRec > 0 else ''))
            strSQLRun = strSQLRun.replace('<ColNameColl>', strSQLColColl)
            strSQLRun = strSQLRun.replace('<TbName>', strTblName)
            strSQLRun = strSQLRun.replace('<CriteriaStr>', strCriteria)
            strSQLRun = strSQLRun.replace('<OrderByStr>', strOrderBy)

    blnResult, strErrMsg, lstDBRow = \
        EHDB.fnDBRSTGet(
            strSQLRun=strSQLRun,
            strSectName=strSectName,
            strDBName=strDBName,
            blnErrRtn=True
        )

    if not blnResult:
        strFuncName = 'EHDBApply.fnDBRSTValueGet'
        return EHDebug.fnErrRtn(
            blnResult=False,
            strErrMsg=strErrMsg,
            strFuncName=strFuncName,
            lstDBRow=None
        )

    if blnCombineToStr:
        lstRowColl = []
        for lstRow in lstDBRow:
            if len(lstRow)==1:
                strColColl=lstRow
            else:
                strColColl = c_strAttrSplitor.join(lstRow)
            lstRowColl.append(strColColl)
        return True, strErrMsg, c_strLineSplitor.join(lstRowColl)
    elif blnValueListTrans:
        lstDBRow=EHArray.fnArrayZIPTranspose(lstRun=lstDBRow)
        return True, strErrMsg, lstDBRow
    else:
        return True, strErrMsg, lstDBRow
# </PyRegion: DBValue>
# <PyRegion: SQL Process>
def fnSQLCrtaJoin(
    lstColName,
    lstColValue,
    lstColNameKey = None,
    blnColWithSysDft = False,
    blnErrRtn = False
)->(bool, str | None):
    # <PyFunc: fnSQLCrtaJoin>
    #   Desc: Join SQL Criteria
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      lstColName= SQL Column Name List
    #      lstColValue= SQL Column Value List
    #   Return:
    #      strSQLCrt= SQL Criteria String and Result
    # </PyFunc: fnSQLCrtaJoin>
    blnResult = False
    if len(lstColName)!= len(lstColValue):
        strErrMsg = \
            'Error: Column Name and Value List Length Not Match' + \
            c_strNewLine +'ColName({}): {}, ColValue({}): {}'.\
                format(len(lstColName), lstColName, len(lstColValue), lstColValue)
        strFuncName = 'EHDBApply.fnSQLCrtaJoin'
        if blnErrRtn: return False, strErrMsg
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return blnResult, strErrMsg
    strJoinPrefix = '='+c_strSQLValueBracketSymbol
    strJoinSuffix = c_strSQLValueBracketSymbol

    if lstColNameKey is None:
        lstJoin = [''.join([strColName, strJoinPrefix, strColValue, strJoinSuffix ]) \
           for strColName, strColValue in zip(lstColName, lstColValue)]
    else:
        lstJoin = [''.join([strColName, strJoinPrefix, strColValue, strJoinSuffix]) \
           for strColName, strColValue in zip(lstColName, lstColValue) if strColName in lstColNameKey]

    if blnColWithSysDft:
        if not c_strDBTblColNameDeleted in lstColName: lstJoin.append(c_strDBTblColNameDeleted + '<>\'Y\'')
        if not c_strDBTblColNameLastVer in lstColName: lstJoin.append(c_strDBTblColNameLastVer + '=\'Y\'')

    strJoin=' AND '.join(lstJoin)

    blnResult = True
    return blnResult, strJoin
# </PyRegion: SQL Process>