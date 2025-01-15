# EHSQLAnaly.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import EHArray
import EHSymbolDef
import EHUDE
import EHMsg

import EHDB
import EHRegExp
import EHStr
from EHUDE import udeDBType

# <PyDecl: Symbol Define & UDE import >
c_strNewLine = EHSymbolDef.c_strNewLine # '\n'

c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor
c_strSQLBracketLeft=EHSymbolDef.c_strSQLBracketLeft
c_strSQLBracketRight=EHSymbolDef.c_strSQLBracketRight
c_strSQLSplitor=EHSymbolDef.c_strSQLSplitor
c_strSQLSelectColFuncSplitor=EHSymbolDef.c_strSQLSelectColFuncSplitor
c_strSQLValueBracketSymbol=EHSymbolDef.c_strSQLValueBracketSymbol
# </PyDecl: Symbol Define & UDE import >

#<PyDecl: Select>
c_strSQLSELECTKeyword = 'SELECT '
c_strSQLSelectColKeyword= 'SelectCol'
c_strSQLTOPKeyword= ' TOP '
c_strSQLLIMITKeyword = ' LIMIT '
c_strSQLDISTINCTKeyword = ' DISTINCT '

#<PyDecl: From>
c_strSQLFROMKeyword = ' FROM '
c_strSQLJOINKeyword= ' JOIN '
c_lstSQLJOINKeywordColl= \
    [
        ' LEFT JOIN ' ,
        ' RIGHT JOIN ' ,
        ' INNER JOIN ' ,
        ' OUTER JOIN ' ,
        ' CROSS JOIN ' ,
        c_strSQLJOINKeyword
    ]
c_strSQLONKeyword= ' ON '

#<PyDecl: SubQuery>
c_strSQLSubQueryKeyword= 'SubQuery'
c_strSQLSelectSubQueryTmpReplace= '<SQLSubQueryStr>'

c_strSQLSelectFuncMySQLIFNULL= 'IFNULL('
c_strSQLSelectFuncMySQLIIF= 'IF('
c_strSQLSelectFuncMySQLTRIM= 'TRIM('

c_strSQLSelectFuncMSSQLISNULL= 'ISNULL('
c_strSQLSelectFuncMSSQLIIF= 'IIF('
c_strSQLSelectFuncMSSQLTRIM= 'LTRIM(RTRIM('

c_strSQLSelectFuncAS= ' AS '

#<PyDecl: Where>
c_strSQLWHEREKeyword= ' WHERE '
c_strSQLANDKeyword= ' AND '
c_strSQLORKeyword= ' OR '
c_strSQLLIKEKeyword= ' REGEXP '
c_strSQLMySQLREGEXPKeyword= ' REGEXP '

#<PyDecl: GROUP/ORDER/HAVING>
c_strSQLGROUPKeyword= ' GROUP BY '
c_strSQLORDERKeyword= ' ORDER BY '
c_strSQLHAVINGKeyword= ' HAVING '

#<PyDecl: UNION>
c_strSQLUNIONKeyword= ' UNION '
c_strSQLUNIONALLKeyword= ' UNION ALL '
c_strSQLINTERSECTKeyword= ' INTERSECT '

#<PyDecl: Delete>
c_strSQLDELETEKeyword= 'DELETE '

#<PyDecl: Update>
c_strSQLUPDATEKeyword= 'UPDATE '
c_strSQLSETKeyword= ' SET '

#<PyDecl: Alter>
c_strSQLALTERKeyword= 'ALTER TABLE '
c_strSQLALTERKeywordRENAME= ' RENAME TO '
c_strSQLALTERKeywordADD= ' ADD '
c_strSQLALTERKeywordCHANGE= ' CHANGE '
c_strSQLALTERKeywordMODIFY= ' MODIFY '
c_strSQLALTERKeywordDROP= ' DROP '

#<PyDecl: Insert>
c_strSQLINSERTKeyword= 'INSERT INTO '
c_strSQLVALUESKeyword= 'VALUES'

#<PyDecl: Show Tables>
c_strSQLSHOWTABLESKeyword= 'SHOW TABLES '

#<PyDecl: Show Columns>
c_strSQLSHOWCOLUMNSKeyword= 'SHOW COLUMNS FROM '

#<PyDecl: Describe Table>
c_strSQLDESCRIBEKeyword= 'DESCRIBE '

#<PyDecl: Create>
c_strSQLCREATESCHEMAKeyword= 'CREATE SCHEMA '
c_strSQLDEFAULTCHARSETKeyword= 'DEFAULT CHARACTER SET '
c_strSQLCOLLATEKeyword= 'COLLATE '
c_strSQLCREATETEMPTABLEKeyword= 'CREATE TEMPORARY TABLE '
c_strSQLCREATETABLEKeyword= 'CREATE TABLE '

#<PyDecl: Create Index>
c_strSQLCREATEINDEXKeyword= 'CREATE INDEX '

#<PyDecl: Drop Table>
c_strSQLDROPTABLEKeyword= 'DROP TABLE '

#<PyDecl: Drop Index>
c_strSQLDROPINDEXKeyword= 'DROP INDEX '

#<PyDecl: With>
c_strSQLWITHKeyword= 'WITH '

#<PyDecl: Call>
c_strSQLCALLKeyword= 'CALL '

p_lstSQLKeyWordColl = \
    [
        c_strSQLSELECTKeyword ,
        c_strSQLDELETEKeyword ,
        c_strSQLUPDATEKeyword ,
        c_strSQLALTERKeyword ,
        c_strSQLINSERTKeyword ,
        c_strSQLSHOWTABLESKeyword ,
        c_strSQLSHOWCOLUMNSKeyword ,
        c_strSQLDESCRIBEKeyword ,
        c_strSQLCREATESCHEMAKeyword ,
        c_strSQLCREATETEMPTABLEKeyword ,
        c_strSQLCREATESCHEMAKeyword ,
        c_strSQLCREATETABLEKeyword ,
        c_strSQLCREATEINDEXKeyword ,
        c_strSQLDROPTABLEKeyword ,
        c_strSQLDROPINDEXKeyword ,
        c_strSQLWITHKeyword ,
        c_strSQLCALLKeyword
    ]

p_lstSQLKeyWordLimitColl= \
    [
        c_strSQLTOPKeyword ,
        c_strSQLLIMITKeyword ,
        c_strSQLDISTINCTKeyword
    ]

p_lstSQLKeyWordFuncColl = \
    [
        c_strSQLSelectFuncMySQLIFNULL ,
        c_strSQLSelectFuncMySQLIIF ,
        c_strSQLSelectFuncMySQLTRIM ,
        c_strSQLSelectFuncMSSQLISNULL ,
        c_strSQLSelectFuncMSSQLIIF ,
        c_strSQLSelectFuncMSSQLTRIM
    ]

p_strSQLKeyWordOperColl = \
    [
        c_strSQLANDKeyword ,
        c_strSQLORKeyword ,
        c_strSQLMySQLREGEXPKeyword
    ]

p_strSQLKeywordGroupColl = \
    [
        c_strSQLGROUPKeyword ,
        c_strSQLORDERKeyword ,
        c_strSQLHAVINGKeyword
    ]

c_lstSQLAnalyKeywordCollBySeq = [
    'strSQLWith'
    , 'strSQLWithSelectSub'
    , 'strSQLSelect'
    , 'strSQLLimit'
    , 'strSQLDistinct'
    , 'strSQLDelete'
    , 'strSQLUpdate'
    , 'strSQLAlter'
    , 'strSQLInsert'
    , 'strSQLShowTables'
    , 'strSQLShowColumns'
    , 'strSQLDescribe'
    , 'strSQLCreateSchema'
    , 'strSQLCreateTable'
    , 'strSQLCreateIndex'
    , 'strSQLDropTable'
    , 'strSQLDropIndex'
    , 'strSQLColName'
    , 'strSQLIndexName'
    , 'strSQLIndexON'
    , 'strSQLFrom'
    , 'strSQLTables'
    , 'strSQLJoin'
    , 'strSQLOn'
    , 'strSQLSchemaCharSet'
    , 'strSQLSchemaCollate'
    , 'strSQLSet'
    , 'strSQLColNameValue'
    , 'strSQLWhere'
    , 'strSQLLike'
    , 'strSQLGroup'
    , 'strSQLOrder'
    , 'strSQLHaving'
    , 'strSQLAlterAction'
    , 'strSQLTableNameNew'
    , 'strSQLColNameSub'
    , 'strSQLColValue'
    , 'strSQLSelectSub'
    , 'strSQLCall'
    , 'strSQL'
]
        
'''<PyCmt: dictSQLDstru>
'strSQLWith':#<PyCmt: Before 'strSQLWithSelectSub'>
'strSQLWithSelectSub':#<PyCmt: Before 'strSQLSelect'>
'strSQLSelect': #<PyCmt: [WITH]>
'strSQLLimit': '', 
'strSQLDistinct': '', 
 
'strSQLDelete': #<PyCmt: Before 'From', [DELETE]>
'strSQLUpdate': #<PyCmt: Before 'strSQLTables', [UPDATE]>
'strSQLAlter': #<PyCmt: Before 'strSQLTables', [ALTER]>
'strSQLInsert': #<PyCmt: Before 'strSQLTables', [INSERT]>
'strSQLShowTables': #<PyCmt: Before 'strSQLWhere' or 'strSQLLike', [SHOW TABLES]>
'strSQLShowColumns': #<PyCmt: Before 'strSQLFrom', [SHOW COLUMNS]>
'strSQLDescribe': #<PyCmt: Before 'strSQLTables', [DESCRIBE]>
'strSQLCreateTable': #<PyCmt: Before 'strSQLTables', [CREATE TABLE]>
'strSQLCreateIndex': #<PyCmt: Before 'strSQLIndexName', [CREATE INDEX]>
'strSQLDropTable': #<PyCmt: Before 'strSQLTables', [DROP TABLE]>
'strSQLDropIndex': #<PyCmt: Before 'strSQLIndexName', [DROP INDEX]>

'strSQLColName': #<PyCmt: Before 'strSQLFrom', [SELECT]>
'strSQLIndexName': #<PyCmt: Before 'strSQLTables', [CREATE INDEX, DROP INDEX]>
'strSQLIndexON': #<PyCmt: Before 'strSQLTables', After 'strSQLIndexName' [CREATE INDEX, DROP INDEX]>

'strSQLFrom': #<PyCmt: Before 'strSQLTables', [SELECT, DELETE, UPDATE, SHOW COLUMNS]>
'strSQLTables': #<PyCmt: Before 'strSQLJoin',
    #[SELECT, DELETE, UPDATE, ALTER, INSERT, DESCRIBE, CREATE TABLE, CREATE INDEX, DROP TABLE, DROP INDEX]>
'strSQLJoin': #<PyCmt: Before 'strSQLOn' [FROM]>
'strSQLOn': #<PyCmt: [JOIN]>
'strSQLWhere': #<PyCmt: [SELECT, DELETE, UPDATE, SHOW TABLES]>
'strSQLLike': #<PyCmt: [SHOW TABLES]>

'strSQLGroup': #<PyCmt: [SELECT]>
'strSQLOrder': #<PyCmt: After 'strSQLGroup', [SELECT]>
'strSQLHaving': #<PyCmt: After 'strSQLOrder', [SELECT]>

'strSQLSet': #<PyCmt: After 'strSQLUpdate', [UPDATE]>
'strSQLColNameValue': #<PyCmt: After 'strSQLSet', [UPDATE]>

'strSQLAlterAction': #<PyCmt: After 'strSQLAlter', [ALTER]>
'strSQLTableNameNew': #<PyCmt: After 'strSQLAlterAction', [ALTER]>

'strSQLColNameSub': #<PyCmt: After 'strSQLTables', [INSERT, CREATE TABLE]>
'strSQLColValue': #<PyCmt: After 'strSQLInsert', [INSERT]>
'strSQLSelectSub': #<PyCmt: After 'strSQLInsert', [INSERT]>

'strSQLCall': '', 
'strSQL': '' 
'''

#<PyDecl: EHSQLAnaly Global>
p_udeDBTypeRun=udeDBType.udeDBTypeNA
p_blnDBTableNameLowCase = False
#</PyDecl: EHSQLAnaly Global>
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHSQLAnaly.py !')
# </PyDecl: RunTime>
class EHSQLAnalyDist(dict):
    def __init__(self):
        dictRun={key: '' for key in c_lstSQLAnalyKeywordCollBySeq}
        super().__init__(dictRun)

    def __setitem__(self, key, value):
        if key in  c_lstSQLAnalyKeywordCollBySeq:
            super().__setitem__(key, value)
        else:
            raise ValueError('Key: \'{}\' Not in EHSQLAnalyDict'.format(key))

# dictSQLDstru = \
#     { \
#         'strSQLWith': '', \
#         'strSQLWithSelectSub': '', \
#         \
#         'strSQLSelect':'',
#         'strSQLLimit': '', \
#         'strSQLDistinct': '', \
#         \
#         'strSQLDelete': '', \
#         'strSQLUpdate': '', \
#         'strSQLAlter': '',  \
#         'strSQLInsert': '', \
#         'strSQLShowTables': '', \
#         'strSQLShowColumns': '', \
#         'strSQLDescribe': '', \
#         'strSQLCreateTable': '', \
#         'strSQLCreateIndex':'', \
#         'strSQLDropTable':'', \
#         'strSQLDropIndex': '', \
#         \
#         'strSQLColName': '', \
#         'strSQLIndexName': '', \
#         'strSQLIndexON': '', \
#         \
#         'strSQLFrom':'', \
#         'strSQLTables': '', \
#         'strSQLJoin': '', \
#         'strSQLOn': '', \
#         'strSQLWhere': '', \
#         'strSQLLike': '', \
#         \
#         'strSQLGroup':'', \
#         'strSQLOrder':'', \
#         'strSQLHaving':'', \
#         \
#         'strSQLSet':'', \
#         'strSQLColNameValue':'', \
#         \
#         'strSQLAlterAction':'', \
#         'strSQLTableNameNew':'', \
#         \
#         'strSQLColNameSub':'', \
#         'strSQLColValue':'', \
#         'strSQLSelectSub':'', \
#         \
#         'strSQLCall':'', \
#         \
#         'strSQL':'' \
#     }

c_strSQLSelectSubQueryTmpReplace = "<SQLSubQueryStr>"
c_strDBNameReplacement = "<EHDBName>"

class EHSQLAnalyDict(dict):
    def __init__(self):
        dictRun={key: '' for key in c_lstSQLAnalyKeywordCollBySeq}
        super().__init__(dictRun)

    def __setitem__(self, strKey, varValue):
        if strKey in self.keys():
            super().__setitem__(strKey, varValue)
        else:
            print('EHSQLAnalyDict without \"{}\" keyword'.format(strKey) )

def fnSQLDstru(
        strSQL: str,
        udeDBTypeRun: EHUDE.udeDBType = EHUDE.udeDBType.udeDBTypeNA,
        blnDBTableNameLowCase: bool = None,
        blnSQLPrint: bool = False
)-> str:
    if strSQL is None: return None

    global p_udeDBTypeRun
    dictSQLDstru=EHSQLAnalyDict()
    if udeDBTypeRun!=EHUDE.udeDBType.udeDBTypeNA:
        p_udeDBTypeRun=udeDBTypeRun
    global p_blnDBTableNameLowCase
    if not blnDBTableNameLowCase is None:
        p_blnDBTableNameLowCase=blnDBTableNameLowCase

    #<PyCmt: strSQL Preprocess>
    strSQL=strSQL.strip()
    strSQL= \
        strSQL.replace(c_strSQLONKeyword + c_strSQLBracketLeft, c_strSQLONKeyword + ' ' + c_strSQLBracketLeft )
    strSQL = \
        strSQL.replace(c_strSQLBracketRight + c_strSQLSELECTKeyword, c_strSQLBracketRight + " " + c_strSQLSELECTKeyword)
    strSQL=strSQL.replace('  ',' ')
    # </PyCmt: strSQL Preprocess>

    #<PyCmt: strSQL Keyword Guess>
    strSQLType=fnSQLKeywordGuess(strSQL=strSQL)

    # <PyCmt: Subquery Process>
    strSubQueryResult= \
        fnSQLSubQueryProcess(
            strSQL=strSQL,
            blnSQLPrint=blnSQLPrint,
        )
    if not strSubQueryResult is None: return strSubQueryResult
    #<PyCmt: Union Process>
    strUNIONResult=fnSQLUNIONProcess(strSQL=strSQL)
    if not strUNIONResult is None: return strUNIONResult

    if strSQLType==c_strSQLSELECTKeyword:
        fnSQLSELECTStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLDELETEKeyword:
        fnSQLDELETEStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLUPDATEKeyword:
        fnSQLUPDATEStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLALTERKeyword:
        fnSQLALTERStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLINSERTKeyword:
        fnSQLINSERTStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLSHOWTABLESKeyword:
        fnSQLSHOWTABLESStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLSHOWCOLUMNSKeyword:
        fnSQLSHOWCOLUMNSStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLDESCRIBEKeyword:
        fnDESCRIBEStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLCREATESCHEMAKeyword:
        fnSQLCREATESCHEMAStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLCREATETEMPTABLEKeyword:
        fnSQLCREATETABLEStrProcess(strSQL=strSQL, strSQLType=strSQLType, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLCREATETABLEKeyword:
        fnSQLCREATETABLEStrProcess(strSQL=strSQL, strSQLType=strSQLType, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLCREATEINDEXKeyword:
        fnSQLCREATEINDEXStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLDROPTABLEKeyword:
        fnSQLDROPTABLEStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLDROPINDEXKeyword:
        fnSQLDROPINDEXStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLWITHKeyword:
        fnSQLWITHStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    elif strSQLType==c_strSQLCALLKeyword:
        fnSQLCALLStrProcess(strSQL=strSQL, dictSQLDstru=dictSQLDstru)
    else:
        strMsg = 'SQL Analysis Error!' \
            + c_strNewLine + 'Please Contact Program Designer!' \
            + c_strNewLine + 'strSQL: {}'.format( strSQL)
        strFuncName = 'EHSQLAnaly.fnSQLDstru'
        strTitle = "strSQLType Error!"
        EHMsg.fnMsgPrt(strMsg=strMsg, strTitle=strTitle, strFuncName=strFuncName, blnLog=True)
    strResult=fnSQLStrCombine(dictSQLDstru = dictSQLDstru)
    del dictSQLDstru
    if blnSQLPrint:
        strMsg='fnSQLDstru strResult:'+strResult
        EHMsg.fnMsgPrt(strMsg=strMsg, blnCmdPrint=True)
    return strResult

def fnSQLKeywordGuess(
        strSQL='',
        blnSubStr=False
)->str:
    if len(strSQL.strip())==0: return ''
    strSQL=strSQL.strip()

    strResult=''
    for strKeywordRun in p_lstSQLKeyWordColl:
        if strKeywordRun==c_strSQLSHOWTABLESKeyword and \
                strSQL.strip()==c_strSQLSHOWTABLESKeyword.strip():
            strResult=c_strSQLSHOWTABLESKeyword
            break
        elif strSQL[0:len(strKeywordRun)]==strKeywordRun:
            strResult = strKeywordRun
            break

    if len(strResult)==0 and blnSubStr:
        if c_strSQLJOINKeyword in strSQL or \
            c_strSQLONKeyword in strSLQRun:
            strResult=c_strSQLJOINKeyword
        else:
            strResult=c_strSQLSubQueryKeyword

    return strResult

def fnSQLSubQueryProcess(
        strSQL,
        blnSQLPrint=False
)->str:
    match p_udeDBTypeRun:
        case udeDBType.udeDBTypeMySQL:
            strPattern=r'\([\s]*?SELECT.*?FROM.*?\)'
        case udeDBType.udeDBTypeMSSQL:
            strPattern=r'\([\s]*?SELECT.*?FROM.*?\)'
        case _:
            return None

    lstRegExpMatch, lstRegExpSpan=\
        EHRegExp.fnRegExp(
            strPattern=strPattern,
            strRun=strSQL,
            blnMulti=True,
            blnBracketBalance=True
        )
    if lstRegExpMatch is None: return None

    lstSubQuery=[]
    for strMatch in lstRegExpMatch:
        blnBracketStatus, blnBracketSingle= \
             EHStr.fnStrBracketBalJudge(
                 strRun=strSQL,
                 strBracketLeft=EHSymbolDef.c_strSQLBracketLeft,
                 strBracketRight=EHSymbolDef.c_strSQLBracketRight
             )
        if not blnBracketStatus:
            strMatch= \
                fnStrBracketBalFind(
                    strRun=strSQL,
                    strBracketLeft=EHSymbolDef.c_strSQLBracketLeft,
                    strBracketRight=EHSymbolDef.c_strSQLBracketRight
                )
        strMatch=strMatch[1:len(strMatch)-1]

        strSubQuery=fnSQLDstru(strSQL=strMatch)
        lstSubQuery.append(strSubQuery)
        strSQL=strSQL.replace(strMatch, c_strSQLSelectSubQueryTmpReplace)

    strSQLResult=fnSQLDstru(strSQL=strSQL, blnSQLPrint=blnSQLPrint)
    for strSubQuery in lstSubQuery:
        strSQLResult=strSQLResult.replace(c_strSQLSelectSubQueryTmpReplace,strSubQuery,1)
    return strSQLResult

def fnSQLUNIONProcess(strSQL)->str:
    intUNIONALLPos = -1
    intUNIONPos=-1
    intINTERSECTPos = -1
    if c_strSQLUNIONALLKeyword in strSQL: intUNIONALLPos = strSQL.index(c_strSQLUNIONALLKeyword)
    if c_strSQLUNIONKeyword in strSQL: intUNIONPos=strSQL.index(c_strSQLUNIONKeyword)
    if c_strSQLINTERSECTKeyword in strSQL: intINTERSECTPos = strSQL.index(c_strSQLINTERSECTKeyword)

    if intUNIONALLPos<0 and intUNIONPos<0 and intINTERSECTPos<0: return None

    strSQLColl=''
    while intUNIONALLPos>0 or \
        intUNIONPos>0 or \
        intINTERSECTPos>0:
        intKeywordPos=\
            min(filter(lambda intPos: intPos>=0, [intUNIONALLPos, intUNIONPos, intINTERSECTPos]))

        strSectionKeyword=''
        if intUNIONALLPos>=0 and intUNIONALLPos==intKeywordPos:
            strSectionKeyword=c_strSQLUNIONALLKeyword
        elif intUNIONPos>=0 and intUNIONPos==intKeywordPos:
            strSectionKeyword=c_strSQLUNIONKeyword
        elif intINTERSECTPos>=0 and intINTERSECTPos == intKeywordPos:
            strSectionKeyword = c_strSQLINTERSECTKeyword

        strSQLSubRun=strSQL[:intKeywordPos]
        strSQLCollRun=fnSQLDstru(strSQL=strSQLSubRun)
        strSQLColl=strSQLColl+strSQLCollRun+strSectionKeyword
        strSQL=strSQL[intKeywordPos+len(strSectionKeyword):]

        intUNIONALLPos = -1
        intUNIONPos=-1
        intINTERSECTPos = -1
        if c_strSQLUNIONALLKeyword in strSQL: intUNIONALLPos = strSQL.index(c_strSQLUNIONALLKeyword)
        if c_strSQLUNIONKeyword in strSQL: intUNIONPos=strSQL.index(c_strSQLUNIONKeyword)
        if c_strSQLINTERSECTKeyword in strSQL: intINTERSECTPos = strSQL.index(c_strSQLINTERSECTKeyword)

    if len(strSQL)>0:
        strSQLCollRun=fnSQLDstru(strSQL=strSQL)
        strSQLColl=strSQLColl+strSQLCollRun
    return strSQLColl

def fnSQLSELECTStrProcess(
        strSQL,
        dictSQLDstru
):
    #<PyCmt: strSQLHaving>
    if len(dictSQLDstru['strSQLHaving'])>0:
        dictSQLDstru['strSQLHaving']= \
            dictSQLDstru['strSQLHaving']+strSQL
        return None
    strSQLResult, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLHAVINGKeyword
        )
    dictSQLDstru['strSQLHaving']=strSQLResult

    # <PyCmt: strSQLOrder>
    if len(dictSQLDstru['strSQLOrder'])>0:
        dictSQLDstru['strSQLOrder']= \
            dictSQLDstru['strSQLOrder']+strSQL
        return None
    strSQLResult, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLORDERKeyword
        )
    dictSQLDstru['strSQLOrder']=strSQLResult

    # <PyCmt: strSQLGroup>
    if len(dictSQLDstru['strSQLGroup'])>0:
        dictSQLDstru['strSQLGroup']= \
            dictSQLDstru['strSQLGroup']+strSQL
        return None
    strSQLResult, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLGROUPKeyword
        )
    dictSQLDstru['strSQLGroup'] = strSQLResult

    # <PyCmt: strSQLLimit>
    if len(dictSQLDstru['strSQLLimit'])>0:
        dictSQLDstru['strSQLLimit']= \
            dictSQLDstru['strSQLLimit']+strSQL
        return None
    if p_udeDBTypeRun==udeDBType.udeDBTypeMySQL:
        strSQLResult, strSQL =\
            fnSQLElementStrGet(
                strSQL=strSQL,
                strSQLType = c_strSQLLIMITKeyword,
            )
        dictSQLDstru['strSQLLimit'] =strSQLResult

    # <PyCmt: strSQLWhere>
    if len(dictSQLDstru['strSQLWhere'])>0:
        dictSQLDstru['strSQLWhere']= \
            dictSQLDstru['strSQLWhere']+strSQL
        return None

    strSQLResult, strSQL =\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLWHEREKeyword,
        )
    strWHERE=strSQLResult
    strWHERE=\
        fnSQLWHEREStrProcess(
            strSQL=strWHERE,
            strSQLType=c_strSQLWHEREKeyword
        )
    dictSQLDstru['strSQLWhere'] = strWHERE

    # <PyCmt: strJOIN>
    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLJOINKeyword
        )
    strJOIN= strSQLResult
    dictSQLDstru['strSQLJoin']=fnSQLJOINStrProcess(strSQL=strJOIN)

    # <PyCmt: strSQLTables, strSQLFrom>
    strTableName=''
    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLFROMKeyword,
            blnWithoutKeyword=True
        )
    if strSQLResult: strTableName=strSQLResult
    if len(strTableName)>0:
        dictSQLDstru['strSQLTables'] = fnSQLTableNameLcase(strTableName=strTableName)
        dictSQLDstru['strSQLFrom'] = c_strSQLFROMKeyword

    # <PyCmt: strSQLLimit>
    strSQLResult, strSQL =\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLTOPKeyword
        )
    if dictSQLDstru['strSQLLimit'] is None and not strSQLResult is None:
        dictSQLDstru['strSQLLimit'] = strSQLResult
    else:
        if c_blnEHDebugMode :
            strErrMsg = 'dictSQLDstru[\'strSQLLimit\']: {}, Existed!'.format(dictSQLDstru['strSQLLimit'])
            strFuncName = 'EHSQLAnaly.fnSQLSELECTStrProcess'
            EHMsg.fnMsgPrt(
                strMsg=strErrMsg,
                strFuncName=strFuncName,
                blnLog=True
            )

    # <PyCmt: strSQLDistinct>
    strSQLResult, strSQL= \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLDISTINCTKeyword,
            blnKeywordOnly=True
        )
    dictSQLDstru['strSQLDistinct'] =strSQLResult

    # <PyCmt: strSQLSelect, strSQLColName>
    strColName=''
    strSQLResult, strSQL= \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLSELECTKeyword,
            blnWithoutKeyword=True
        )
    if not strSQLResult is None: strColName=strSQLResult
    if len(strColName)>0:
        strColName=fnSQLNULLReplace(strSQL=strColName)
        strColName=fnSQLTRIMReplace(strSQL=strColName)
        dictSQLDstru['strSQLColName'] = strColName
    dictSQLDstru['strSQLSelect'] = c_strSQLSELECTKeyword

def fnSQLSeltColSplit(strRun)->list:
    strPattern=r'(\s*?\w+?\s*?(,|$))'
    lstRegExpMatch, lstRegExpSpan = \
        EHRegExp.fnRegExp(
            strPattern=strPattern,
            strRun=strRun,
            blnMulti=True
        )
    lstSltColSplitResult=[]
    for strItem in lstRegExpMatch:
        strItemRun=strItem
        strItemRun=strItemRun.strip()
        if strItemRun[-1]==c_strSQLSplitor: strItemRun=strItemRun[:-1]
        lstSltColSplitResult.append(strItemRun)
    return lstSltColSplitResult

def fnSQLDELETEStrProcess(
        strSQL,
        dictSQLDstru
):
    # <PyCmt: strSQLWhere>
    strSQLResult, strSQL =\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLWHEREKeyword,
        )
    strWHERE=strSQLResult
    strWHERE=\
        fnSQLWHEREStrProcess(
            strSQL=strWHERE,
            strSQLType=c_strSQLWHEREKeyword
        )
    dictSQLDstru['strSQLWhere'] = strWHERE

    # <PyCmt: strJOIN>
    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLJOINKeyword
        )
    strJOIN= strSQLResult
    strJOIN=fnSQLJOINStrProcess(strSQL=strJOIN)
    dictSQLDstru['strSQLJoin']=strJOIN

    # <PyCmt: strSQLTables, strSQLFrom>
    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLFROMKeyword,
            blnWithoutKeyword=True
        )
    strTableName=strSQLResult
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)
    dictSQLDstru['strSQLTables'] = strTableName
    dictSQLDstru['strSQLFrom'] = c_strSQLFROMKeyword

    # <PyCmt: strSQLSelect, strSQLColName>
    strColName=''
    strSQLResult, strSQL= \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLDELETEKeyword,
            blnWithoutKeyword=True
        )
    if not strSQLResult is None: strColName=strSQLResult
    if len(strColName)>0:
        strColName=fnSQLNULLReplace(strSQL=strColName)
        strColName=fnSQLTRIMReplace(strSQL=strColName)
        dictSQLDstru['strSQLColName'] = strColName
    dictSQLDstru['strSQLDelete'] =c_strSQLDELETEKeyword

def fnSQLUPDATEStrProcess(
        strSQL,
        dictSQLDstru
):
    strSQLResult, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLWHEREKeyword
        )
    strWHERE=strSQLResult
    strWHERE=fnSQLWHEREStrProcess(strSQL=strWHERE)

    strSQLResult, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLSETKeyword,
            blnWithoutKeyword=True
        )
    strColNameValueRun=strSQLResult

    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLUPDATEKeyword,
            blnWithoutKeyword=True
        )
    strTableName=strSQLResult

    strTableNameColl=''
    for strTableName in strTableName.split(c_strSQLSplitor.strip()):
        strTableName = strTableName.strip()
        strTableName = fnSQLTableNameLcase(strTableName=strTableName)
        strTableNameColl = \
            strTableNameColl +\
            c_strSQLSplitor if len(strTableNameColl)>0 else "" +\
            ' ' + strTableName
    dictSQLDstru['strSQLUpdate'] = c_strSQLUPDATEKeyword
    dictSQLDstru['strSQLTables'] = strTableNameColl
    # dictSQLDstru['strSQLJoin'] = strJOIN
    dictSQLDstru['strSQLSet'] = c_strSQLSETKeyword
    dictSQLDstru['strSQLColNameValue'] = strColNameValueRun
    dictSQLDstru['strSQLWhere'] = strWHERE

def fnSQLALTERStrProcess(
    strSQL,
        dictSQLDstru
):
    #<PyCmt: ALTER TABLE [RENAME, ADD, CHANGE, MODIFY, DROP]>'
    strTableNameNew = ''
    strKeyword = ''
    if c_strSQLALTERKeyword in strSQL and \
        c_strSQLALTERKeywordRENAME in strSQL:
        strSQLResult, strSQL = \
            fnSQLElementStrGet(
                strSQL=strSQL,
                strSQLType=c_strSQLALTERKeywordRENAME,
                blnWithoutKeyword=True
            )

        strSQLResult, strSQL = \
            fnSQLElementStrGet(
                strSQL=strSQL,
                strSQLType=c_strSQLALTERKeyword,
                blnWithoutKeyword=True
            )
        strTableNameNew = strSQLResult
    elif c_strSQLALTERKeyword in strSQL and  \
        c_strSQLALTERKeywordADD in strSQL:
        strKeyword = c_strSQLALTERKeywordADD
    elif c_strSQLALTERKeyword in strSQL and  \
        c_strSQLALTERKeywordCHANGE in strSQL:
        strKeyword = c_strSQLALTERKeywordCHANGE
    elif c_strSQLALTERKeyword in strSQL and  \
        c_strSQLALTERKeywordMODIFY in strSQL:
        strKeyword = c_strSQLALTERKeywordMODIFY
    elif c_strSQLALTERKeyword in strSQL and  \
        c_strSQLALTERKeywordDROP in strSQL:
        strKeyword = c_strSQLALTERKeywordDROP

    strTableName = ''
    strColName = ''
    if len(strKeyword)>0:
        strSQLResult, strSQL = \
            fnSQLElementStrGet(
                strSQL=strSQL,
                strSQLType=strKeyword,
                blnWithoutKeyword=True
            )
        strColName = strSQLResult

        strSQLResult, strSQL = \
            fnSQLElementStrGet(
                strSQL=strSQL,
                strSQLType=strKeyword,
                blnWithoutKeyword=True
            )
        strTableName = strSQLResult
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)
    strTableNameNew = fnSQLTableNameLcase(strTableName=strTableNameNew)
    dictSQLDstru['strSQLAlter'] = c_strSQLALTERKeyword
    dictSQLDstru['strSQLTables'] = strTableName
    dictSQLDstru['strSQLAlterAction'] = strKeyword
    dictSQLDstru['strSQLTableNameNew'] = strTableNameNew
    dictSQLDstru['strSQLColName'] = strColName

def fnSQLINSERTStrProcess(
        strSQL,
        dictSQLDstru
):
    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLSELECTKeyword
        )
    strSELECTSub = strSQLResult
    strSELECTSub = fnSQLDstru(strSQL=strSELECTSub)

    if c_strSQLVALUESKeyword in strSQL:
        strSQLResult, strSQL = \
            fnSQLElementStrGet(
                strSQL=strSQL,
                strSQLType=c_strSQLVALUESKeyword
            )
        strVALUES = strSQLResult
        strVALUES = fnSQLINSERTValueReplace(strSQL=strVALUES)
    else:
        strVALUES=''

    #<PyCmt: strColName Get>
    strColName=''
    if c_strSQLBracketLeft in strSQL and \
        c_strSQLBracketRight in strSQL:
        intBracketPosLeft=strSQL.find(c_strSQLBracketLeft)
        intBracketPosRight= strSQL.rfind(c_strSQLBracketRight)
        strColName=strSQL[intBracketPosLeft:intBracketPosRight+1]
        strSQL=strSQL[:intBracketPosLeft]

    #<PyCmt: INSERT INTO Keyword Get>
    strSQLResult, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLINSERTKeyword,
            blnWithoutKeyword=True
        )
    strTableName = strSQLResult
    strTableName=fnSQLTableNameLcase(strTableName=strTableName)
    dictSQLDstru['strSQLInsert'] = c_strSQLINSERTKeyword
    dictSQLDstru['strSQLTables'] = strTableName
    dictSQLDstru['strSQLColNameSub'] = strColName
    dictSQLDstru['strSQLColValue'] = strVALUES
    dictSQLDstru['strSQLSelectSub'] = strSELECTSub

def fnSQLINSERTValueReplace(strSQL)->str:
    strPattern=r'\'.*?\'(,|\)$)'
    lstRegExpMatch, lstRegExpSpan=\
        EHRegExp.fnRegExp(
            strPattern=strPattern,
            strRun=strSQL,
            blnMulti=True
        )
    if lstRegExpMatch is None: return strSQL
    strSQLNew=strSQL
    for strMatchItem in lstRegExpMatch:
        strReplace=strMatchItem.strip()
        if strReplace[:1]==c_strSQLValueBracketSymbol and \
            strReplace[-1:]==c_strSQLValueBracketSymbol:
            strReplace=strReplace[1:-1]
        if c_strSQLValueBracketSymbol in strReplace:
            strReplace = (
                strReplace.replace(
                    c_strSQLValueBracketSymbol,
                    c_strSQLValueBracketSymbol+c_strSQLValueBracketSymbol
                )
            )
        strReplace=c_strSQLValueBracketSymbol+strReplace+c_strSQLValueBracketSymbol
        strSQLNew=strSQLNew.replace(strMatchItem,strReplace)
    if p_udeDBTypeRun==udeDBType.udeDBTypeMySQL:strSQLNew=strSQLNew.replace('\\','\\\\')
    return strSQLNew

def fnSQLSHOWTABLESStrProcess(
        strSQL,
        dictSQLDstru
):
    strLIKE, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLLIKEKeyword
        )
    strWHERE, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLWHEREKeyword
        )
    strWHERE=\
        fnSQLTableNameLcase(
            strTableName=strWHERE,
            blnShowTableWHEREStr=True
        )
    dictSQLDstru['strSQLShowTables'] = c_strSQLSHOWTABLESKeyword
    dictSQLDstru['strSQLWhere'] = strWHERE
    dictSQLDstru['strSQLLike'] = strLIKE

def fnSQLSHOWCOLUMNSStrProcess(
        strSQL,
        dictSQLDstru
):
    strLIKE, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLLIKEKeyword
        )
    strTableName, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLSHOWCOLUMNSKeyword,
            blnWithoutKeyword=True
        )
    strTableName=fnSQLTableNameLcase(strTableName=strTableName)
    dictSQLDstru['strSQLShowColumns'] = c_strSQLSHOWCOLUMNSKeyword
    dictSQLDstru['strSQLTables'] = strTableName
    dictSQLDstru['strSQLLike'] = strLIKE

def fnDESCRIBEStrProcess(
        strSQL,
        dictSQLDstru
):
    strTableName, strSQL=\
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLDESCRIBEKeyword,
            blnWithoutKeyword=True
        )
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)
    dictSQLDstru['strSQLDescribe'] = c_strSQLDESCRIBEKeyword
    dictSQLDstru['strSQLTables'] = strTableName

def fnSQLCREATESCHEMAStrProcess(
        strSQL,
        dictSQLDstru
):
    # <PyCmt: [CREATE SCHEMA]>
    strCollate, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLCOLLATEKeyword
        )
    dictSQLDstru['strSQLSchemaCollate'] = strCollate

    strCharset, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLDEFAULTCHARSETKeyword
        )
    dictSQLDstru['strSQLSchemaCharSet'] = strCharset

    strSchema, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLCREATESCHEMAKeyword,
            blnWithoutKeyword=True
        )
    strSchema = strSchema.lower()
    dictSQLDstru['strSQLCreateSchema'] = c_strSQLCREATESCHEMAKeyword + strSchema

def fnSQLCREATETABLEStrProcess(
        strSQL,
        strSQLType,
        dictSQLDstru
):
    #<PyCmt: [CREATE TABLE, CREATE TEMP TABLE]>'
    intBracketPos=strSQL.find(c_strSQLBracketLeft)
    strColName=strSQL[intBracketPos:]
    strSQL=strSQL[:intBracketPos]

    strTableName, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=strSQLType,
            blnWithoutKeyword=True
        )
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)
    dictSQLDstru['strSQLCreateTable'] = strSQLType
    dictSQLDstru['strSQLTables'] = strTableName
    dictSQLDstru['strSQLColNameSub'] = strColName

def fnSQLCREATEINDEXStrProcess(
        strSQL,
        dictSQLDstru
):
    intBracketPos=strSQL.find(c_strSQLBracketLeft)
    strColName=strSQL[intBracketPos+1:]
    strSQL=strSQL[:intBracketPos]

    strTableName = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLONKeyword,
            blnWithoutKeyword=True
        )
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)

    strINDEXName, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLCREATEINDEXKeyword,
            blnWithoutKeyword=True
        )
    strINDEXName = fnSQLTableNameLcase(strTableName=strINDEXName)
    dictSQLDstru['strSQLCreateIndex'] = c_strSQLCREATEINDEXKeyword
    dictSQLDstru['strSQLIndexName'] = strINDEXName
    dictSQLDstru['strSQLIndexON'] = c_strSQLONKeyword
    dictSQLDstru['strSQLTables'] = strTableName
    dictSQLDstru['strSQLColName'] = strColName

def fnSQLDROPTABLEStrProcess(
        strSQL,
        dictSQLDstru
):
    strTableName, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLDROPTABLEKeyword,
            blnWithoutKeyword=True
        )
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)
    dictSQLDstru['strSQLDropTable'] = c_strSQLDROPTABLEKeyword
    dictSQLDstru['strSQLTables'] = strTableName

def fnSQLDROPINDEXStrProcess(
        strSQL,
        dictSQLDstru
):
    strTableName = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLONKeyword,
            blnWithoutKeyword=True
        )
    strTableName = fnSQLTableNameLcase(strTableName=strTableName)

    strINDEXName, strSQL = \
        fnSQLElementStrGet(
            strSQL=strSQL,
            strSQLType=c_strSQLDROPINDEXKeyword,
            blnWithoutKeyword=True
        )
    strINDEXName = fnSQLTableNameLcase(strTableName=strINDEXName)
    dictSQLDstru['strSQLDropIndex'] = c_strSQLDROPINDEXKeyword
    dictSQLDstru['strSQLIndexName'] = strINDEXName
    dictSQLDstru['strSQLIndexON'] = c_strSQLONKeyword
    dictSQLDstru['strSQLTables'] = strTableName

def fnSQLWITHStrProcess(
        strSQL,
        dictSQLDstru
):
    intBracketPosLeft=strSQL.find(c_strSQLBracketLeft)
    strWITH=strSQL[:intBracketPosLeft]


    intBracketRight=strSQL.rfind(c_strSQLSELECTKeyword)
    intBracketRight = strSQL.rfind(c_strSQLBracketRight, intBracketRight)
    strSelectRun = strSQL[intBracketRight + 1:]
    strSelectRun = fnSQLDstru(strSQL=strSelectRun)

    strSelectSubRun=strSQL[intBracketPosLeft+1:intBracketRight]
    if strSelectSubRun != c_strSQLSelectSubQueryTmpReplace:
        strSelectSubRun = fnSQLDstru(strSQL=strSelectSubRun)
        strSelectSubRun =\
            c_strSQLBracketLeft+\
            strSelectSubRun+\
            c_strSQLBracketRight

    dictSQLDstru['strSQLWith'] = strWITH
    dictSQLDstru['strSQLWithSelectSub'] = strSelectSubRun
    dictSQLDstru['strSQLSelect'] = strSelectRun

def fnSQLCALLStrProcess(
        strSQL,
        dictSQLDstru
):
    dictSQLDstru['strSQLCall'] = strSQL

def fnSQLElementStrGet(
        strSQL,
        strSQLType,
        blnStrRev=False,
        blnWithoutKeyword=False,
        blnKeywordOnly=False,
        blnOrigStrCut=True
):
    bln2Para=False
    blnReplaceOrig=False
    if strSQLType==c_strSQLLIMITKeyword or \
        strSQLType==c_strSQLTOPKeyword:
        bln2Para = True
        blnReplaceOrig = True
    elif strSQLType==c_strSQLDISTINCTKeyword:
        blnReplaceOrig = True

    if strSQLType==c_strSQLJOINKeyword:
        intAnalyPos,strJOINMatch= \
            fnSQLJOINKeywordPosGet(
                strSQL=strSQL,
                blnJOINPosMin=not blnStrRev
            )
    elif blnStrRev:
        intAnalyPos = strSQL.rfind(strSQLType)
    elif strSQLType in strSQL:
        intAnalyPos = strSQL.find(strSQLType)
    else:
        intAnalyPos=-1

    if intAnalyPos>-1:
        if bln2Para:
            if " " in strSQL[intAnalyPos+len(strSQLType)+1:]:
                strSQLResult = strSQL[intAnalyPos:strSQL.find(' ', intAnalyPos+len(strSQLType)+1)]
            else:
                strSQLResult = strSQL[intAnalyPos:]
        elif blnKeywordOnly:
            strSQLResult = strSQL[intAnalyPos:intAnalyPos+len(strSQLType)]
        elif blnWithoutKeyword :
            strSQLResult = strSQL[intAnalyPos + len(strSQLType):]
        else:
            strSQLResult = strSQL[intAnalyPos:]

        if blnOrigStrCut:
            if blnReplaceOrig:
                strSQL = strSQL.replace(strSQLResult, " ")
            elif blnKeywordOnly:
                strSQL = strSQL[intAnalyPos + len(strSQLType):len(strSQL) - len(strSQLResult)]
            elif blnWithoutKeyword:
                strSQL = strSQL[:len(strSQL) - len(strSQLResult) - len(strSQLType)]
            else:
                strSQL = strSQL[:len(strSQL)-len(strSQLResult)]
    else:
        strSQLResult=None
    return strSQLResult, strSQL

def fnSQLJOINStrProcess(strSQL):
    if strSQL is None: return None
    blnSQLONExist=strSQL.rfind(c_strSQLONKeyword)>=0
    blnSQLJOINExist = strSQL.rfind(c_strSQLJOINKeyword)>=0
    lstJOIN=[]
    while blnSQLONExist or blnSQLJOINExist:
        strON=''
        strJOINTableName=''
        if blnSQLONExist:
            strSQLResult, strSQL= \
                fnSQLElementStrGet(
                    strSQL=strSQL,
                    strSQLType=c_strSQLONKeyword,
                    blnStrRev=True
                )
            strON=strSQLResult
            strON = \
                fnSQLWHEREStrProcess(
                    strSQL=strON,
                    strSQLType=c_strSQLONKeyword
                )
        if blnSQLJOINExist:
            strSQLResult, strSQL = \
                fnSQLElementStrGet(
                    strSQL=strSQL,
                    strSQLType=c_strSQLJOINKeyword,
                    blnStrRev=True
                )
            strJOINTableName=strSQLResult
            strJOINTableName =fnSQLTableNameLcase(strTableName=strJOINTableName)
        lstJOIN.append( strJOINTableName + strON )
        if len(strSQL)==0: break
        blnSQLONExist = strSQL.rfind(c_strSQLONKeyword) >= 0
        blnSQLJOINExist = strSQL.rfind(c_strSQLJOINKeyword) >= 0
    return ''.join(lstJOIN)

def fnSQLJOINKeywordPosGet(
        strSQL,
        blnJOINPosMin=False
):
    if strSQL is None: return None

    strJOINMatch=''
    intJOINPosRec=-1
    for strJOINRun in c_lstSQLJOINKeywordColl:
        if strJOINRun!=c_strSQLJOINKeyword and strJOINRun in strSQL:
            intJOINPos = strSQL.find(strJOINRun) if blnJOINPosMin else strSQL.rfind(strJOINRun)
            if blnJOINPosMin and \
                (intJOINPos < intJOINPosRec or intJOINPosRec<0):
                intJOINPosRec = intJOINPos
                strJOINMatch = strJOINRun
            elif not blnJOINPosMin and intJOINPos >= intJOINPosRec:
                intJOINPosRec = intJOINPos
                strJOINMatch = strJOINRun
    if c_strSQLJOINKeyword in strSQL:
        intJOINPos = strSQL.find(c_strSQLJOINKeyword) if blnJOINPosMin else strSQL.rfind(c_strSQLJOINKeyword)
        if blnJOINPosMin and \
                (intJOINPos < intJOINPosRec or intJOINPosRec < 0):
            intJOINPosRec = intJOINPos
            strJOINMatch = c_strSQLJOINKeyword
        elif not blnJOINPosMin and intJOINPos >= intJOINPosRec:
            intJOINPosRec = intJOINPos
            strJOINMatch = c_strSQLJOINKeyword
    return intJOINPosRec, strJOINMatch

def fnSQLTableNameLcase(
        strTableName,
        blnShowTableWHEREStr=False
)->str:
    if p_udeDBTypeRun!=EHUDE.udeDBType.udeDBTypeMySQL: return strTableName
    if not p_blnDBTableNameLowCase:
        return strTableName
    elif len(strTableName)==0:
        return None

    if blnShowTableWHEREStr:
        lstRun=\
            EHStr.fnStrRegExpKeywordSplit(
                strRun=strTableName,
                strKeywordColl=c_strSQLValueBracketSymbol,
                blnDropSplitor=True
            )
        strTableNameColl=strTableName
        for strTableName in lstRun:
            strTableNameColl=strTableNameColl.replace(strTableName,strTableName.lower())
    else:
        lstTableName=[]
        strTableNameAlias=''
        for strTableNameSubRun in strTableName.split(c_strSQLSplitor.strip()):
            blnJOIN=False
            blnBracket=False
            if c_strSQLJOINKeyword in strTableNameSubRun:
                blnJOIN=True
                strTableNameSubRun, strJOIN = \
                    fnSQLElementStrGet(
                        strSQL=strTableNameSubRun,
                        strSQLType=c_strSQLJOINKeyword,
                        blnWithoutKeyword=True
                    )
            if strTableNameSubRun.strip()[0] == c_strSQLBracketLeft and \
                strTableNameSubRun.strip()[-1] == c_strSQLBracketRight:
                blnBracket=True
                strTableNameSubRun=strTableNameSubRun.strip()[1:-1]
            strTableNameSubRun=strTableNameSubRun.strip()
            if ' ' in strTableNameSubRun:
                strTableNameAlias = strTableNameSubRun.split(' ')[1]
                strTableNameSubRun = strTableNameSubRun.split(' ')[0]
            strTableNameSubRun = strTableNameSubRun.lower()
            strTableNameSubRun = strTableNameSubRun.replace(c_strDBNameReplacement.lower(), c_strDBNameReplacement)
            strTableNameSubRun = \
                strTableNameSubRun.replace(
                    c_strSQLSelectSubQueryTmpReplace.lower(),
                    c_strSQLSelectSubQueryTmpReplace
                )
            strTableNameSubRun = strTableNameSubRun+(' ' if len(strTableNameAlias) > 0 else '') + strTableNameAlias
            if blnBracket: strTableNameSubRun = c_strSQLBracketLeft + strTableNameSubRun + c_strSQLBracketRight
            strTableNameSubRun =  (c_strSQLJOINKeyword if blnJOIN else '') + strTableNameSubRun
            lstTableName.append(strTableNameSubRun)
        strTableNameColl=c_strSQLSplitor.join(lstTableName)
    return strTableNameColl

def fnSQLWHEREStrProcess(
        strSQL,
        strSQLType=c_strSQLWHEREKeyword,
)->str:
    if strSQL is None: return None
    strSQLRun=strSQL
    if p_udeDBTypeRun==udeDBType.udeDBTypeMySQL:
        strWildCardOrig = "*"
        strWildCardNew = "%"
    elif p_udeDBTypeRun==udeDBType.udeDBTypeMSSQL:
        strWildCardOrig = "*"
        strWildCardNew = "%"
    else:
        strWildCardOrig = "%"
        strWildCardNew = "*"

    if strSQLRun[:len(strSQLType)]==strSQLType:
        strSQLRun=strSQLRun[len(strSQLType):]
    lstWHERE=\
        EHStr.fnStrRegExpKeywordSplit(
            strRun=strSQLRun,
            strKeywordColl=c_strSQLANDKeyword + c_strAttrSplitor + c_strSQLORKeyword
        )
    if not lstWHERE is None:
        lstWhere=[]
        for strWhereSubRun in lstWHERE:
            if strWildCardOrig in strWhereSubRun and \
                not c_strSQLMySQLREGEXPKeyword in strWhereSubRun:
                strWhereSubRun=strWhereSubRun.replace(strWildCardOrig, strWildCardNew)
            lstWhere.append(strWhereSubRun)
        strWhereColl=''.join(lstWhere)
        strWhereColl=fnSQLNULLReplace(strWhereColl)
        strWhereColl=fnSQLTRIMReplace(strWhereColl)
        strSQL=strSQLType + strWhereColl
    return strSQL

def fnSQLWHERECrtaSplit(strRun)->list:
    strPattern=r'(^\s*?|OR\s+?|AND\s+?)'
    lstRegExpSplit = \
        EHRegExp.fnRegExp(
            strPattern=strPattern,
            strRun=strRun,
            blnSplit=True
        )
    lstWHERECrtaSplitResult=[]
    for strItem in lstRegExpSplit:
        strItemRun=strItem
        strItemRun=strItemRun.strip()
        if len(strItemRun)>0:
            if strItemRun.strip()!=c_strSQLORKeyword.strip() and \
                strItemRun.strip()!=c_strSQLANDKeyword.strip():
                strItemRun = strItemRun.strip()
                lstWHERECrtaSplitResult.append(strItemRun)
    return lstWHERECrtaSplitResult

def fnSQLOperGuess(strRun)->str:
    strPattern=r'(<>|>=|<=|=|>|<| LIKE )'
    objRegExpMatch = \
        EHRegExp.fnRegExp(
            strPattern=strPattern,
            strRun=strRun,
        )
    return str(objRegExpMatch)

def fnSQLNULLReplace(strSQL)->str:
    if p_udeDBTypeRun==udeDBType.udeDBTypeMySQL:
        strSQL=strSQL.replace(c_strSQLSelectFuncMSSQLIIF, c_strSQLSelectFuncMySQLIIF)
    elif p_udeDBTypeRun==udeDBType.udeDBTypeMSSQL:
        strSQL = strSQL.replace(c_strSQLSelectFuncMySQLIFNULL, c_strSQLSelectFuncMSSQLISNULL)
        strPattern=r'[^I]'+ c_strSQLSelectFuncMySQLIIF
        strNew=c_strSQLSelectFuncMSSQLIIF
        strSQL=\
            EHRegExp.fnREReplace(
                strRun=strSQL,
                strPattern=strPattern,
                strNew=strNew
            )
        if c_strSQLSelectFuncMSSQLIIF + c_strSQLSelectFuncMSSQLISNULL in strSQL:
            strSQL=fnSQLNULLRegExpReplace(strSQL, strReplaceType='IFISNULLtoISNULL')
    elif p_udeDBTypeRun == udeDBType.udeDBTypeAccess:
        strSQL = fnSQLNULLRegExpReplace(strSQL)
    # elif udeDBTypeRun == udeDBType.udeDBTypeOracle:
    return strSQL

def fnSQLNULLRegExpReplace(
        strSQL,
        strReplaceType='IFNULLtoIFISNULL'
)->str:
    strPattern = ''
    if strReplaceType=='IFISNULLtoISNULL':
        strPattern=\
            c_strSQLSelectFuncMSSQLIIF + r'\s*?' + \
            c_strSQLSelectFuncMSSQLISNULL + r'.*?' + c_strSQLBracketRight + \
            r',.*?' + \
            r',.*?' + c_strSQLBracketRight
    elif strReplaceType=='IFNULLtoIFISNULL':
        strPattern=\
            c_strSQLSelectFuncMySQLIFNULL + \
            r".*?,.*?" + \
            c_strSQLBracketRight
    strPattern = strPattern.replace(c_strSQLBracketLeft, '\\' + c_strSQLBracketLeft)
    strPattern = strPattern.replace(c_strSQLBracketRight, '\\' + c_strSQLBracketRight)

    lstRegExpMatch, lstRegExpSpan=\
        EHRegExp.fnRegExp(
            strRun=strSQL,
            strPattern=strPattern,
            blnMulti=True
        )
    if not lstRegExpMatch is None:
        for strRegExpMatchItem in lstRegExpMatch:
            blnBracketStatus, blnBracketSingle=\
                EHStr.fnStrBracketBalJudge(
                    strRun=strRegExpMatchItem,
                    strBracketLeft=c_strSQLBracketLeft,
                    strBracketRight=c_strSQLBracketRight
                )
            if not blnBracketStatus:
                strRegExpMatchItem=strRegExpMatchItem[1:]
                strRegExpMatchItem=\
                    fnStrBracketBalFind(
                        strRun=strRegExpMatchItem,
                        strBracketLeft=c_strSQLBracketLeft,
                        strBracketRight=c_strSQLBracketRight
                    )
            lstBracketSplit=\
                EHStr.fnStrBracketSplit(
                    strRun=strRegExpMatchItem,
                    strSplitor=c_strSQLSplitor,
                    strBracketLeft=c_strSQLBracketLeft,
                    strBracketRight=c_strSQLBracketRight
                )

            strNULLNew = ''
            if strReplaceType == 'IFISNULLtoISNULL':
                strValue = lstBracketSplit[0]
                strValue = strValue.split(c_strSQLBracketLeft)[1]
                strValue = strValue.split(c_strSQLBracketRight)[0]
                strValueTrue = lstBracketSplit[1]
                strNULLNew = \
                    c_strSQLSelectFuncMSSQLISNULL + \
                    strValue + \
                    c_strSQLSelectColFuncSplitor + \
                    strValueTrue +\
                    c_strSQLBracketRight
            elif strReplaceType == 'IFNULLtoIFISNULL':
                strValue = lstBracketSplit[0]
                strValueReplace = lstBracketSplit[1]
                strNULLNew = \
                    c_strSQLSelectFuncMSSQLIIF + \
                    c_strSQLSelectFuncMSSQLISNULL +\
                    strValue + \
                    c_strSQLBracketRight + \
                    c_strSQLSelectColFuncSplitor + \
                    strValueReplace +\
                    c_strSQLSelectColFuncSplitor +\
                    strValue +\
                    c_strSQLBracketRight
            strSQL=strSQL.replace(strRegExpMatchItem,strNULLNew,1)
    return strSQL

def fnSQLTRIMReplace(strSQL):
    strSQL=strSQL
    if p_udeDBTypeRun==udeDBType.udeDBTypeMySQL:
        strPattern = \
            r'[LR]' +\
            c_strSQLSelectFuncMySQLTRIM.replace(c_strSQLBracketLeft,"\\" + c_strSQLBracketLeft) + \
            r'. *?\)'
        strPatternSub = \
            r'[LR]' +\
            c_strSQLSelectFuncMySQLTRIM.replace(c_strSQLBracketLeft,"\\" + c_strSQLBracketLeft) + \
            r'. *?'
        strReplace = c_strSQLSelectFuncMySQLTRIM
        strAppend=''
    elif p_udeDBTypeRun == udeDBType.udeDBTypeMSSQL:
        strPattern = \
            r'([^LR]|^)' + \
            c_strSQLSelectFuncMySQLTRIM.replace(c_strSQLBracketLeft,"\\" + c_strSQLBracketLeft) +\
            r'. *?\)'
        strPatternSub = \
            r'([^LR]|^)' + \
            c_strSQLSelectFuncMySQLTRIM.replace(c_strSQLBracketLeft,"\\" + c_strSQLBracketLeft) +\
            r'. *?'
        strReplace = c_strSQLSelectFuncMSSQLTRIM
        strAppend=')'
    else:
        return strSQL

    lstRegExpMatch, lstRegExpSpan= \
        EHRegExp.fnRegExp(
            strRun=strSQL,
            strPattern=strPattern,
            blnMulti=True
        )
    if lstRegExpMatch is None:
        strSQLNew=strSQL
    else:
        intPosLast=0
        strSQLNew=''
        for lstRegExpSpanItem in lstRegExpSpan:
            intPosStart=lstRegExpSpanItem[0]
            intPosEnd=lstRegExpSpanItem[1]
            strTargetRun=strSQL[intPosStart:]
            strTargetRun=fnStrBracketBalFind(strTargetRun)
            strTargetRun=\
                fnSQLTRIMReplaceSub(
                    strSQL=strTargetRun,
                    strPattern=strPatternSub,
                    strReplace=strReplace,
                    strAppend=strAppend
                )
            strSQLNew= \
                strSQLNew \
                +strSQL[intPosLast:intPosStart+1] \
                +strTargetRun
            intPosLast=intPosEnd+ (1 if intPosLast==0 else 0)
        strSQLNew=\
            strSQLNew\
            +strSQL[intPosLast:]
    return strSQLNew

def fnSQLTRIMReplaceSub(
        strSQL,
        strPattern,
        strReplace,
        strAppend
)->str:
    lstRegExpMatch, lstRegExpSpan=\
        EHRegExp.fnRegExp(
            strRun=strSQL,
            strPattern=strPattern,
            blnMulti=True
        )
    intPosLast=0
    strSQLNew=''
    for lstRegExpSpanItem in lstRegExpSpan:
        intPosStart = lstRegExpSpanItem[0]
        intPosEnd = lstRegExpSpanItem[1]
        strSQLNew = \
            strSQLNew \
            + strSQL[intPosLast:intPosStart] \
            + strReplace
        strSQL=strSQL+strAppend
        intPosLast=intPosEnd
    strSQLNew = strSQLNew + strSQL[intPosLast:]
    return strSQLNew

def fnSQLStrCombine(dictSQLDstru)->str:
    EHArray.fnDictNoneRpl(dictRun=dictSQLDstru)
    if p_udeDBTypeRun==udeDBType.udeDBTypeMySQL:
        strSQLTOP=''
        strSQLLIMIT=dictSQLDstru['strSQLLimit']
    else:
        strSQLLIMIT=''
        strSQLTOP = dictSQLDstru['strSQLLimit'].replace(c_strSQLLIMITKeyword, c_strSQLTOPKeyword)

    dictSQLDstru['strSQL']= \
        dictSQLDstru['strSQLWith']+\
        dictSQLDstru['strSQLWithSelectSub']+\
        dictSQLDstru['strSQLSelect']+ \
        dictSQLDstru['strSQLDistinct'] + \
        strSQLTOP + \
        dictSQLDstru['strSQLDelete']+ \
        dictSQLDstru['strSQLUpdate'] + \
        dictSQLDstru['strSQLAlter'] + \
        dictSQLDstru['strSQLInsert'] + \
        dictSQLDstru['strSQLShowTables'] + \
        dictSQLDstru['strSQLShowColumns'] + \
        dictSQLDstru['strSQLDescribe'] + \
        dictSQLDstru['strSQLCreateSchema'] + \
        dictSQLDstru['strSQLCreateTable'] + \
        dictSQLDstru['strSQLCreateIndex'] + \
        dictSQLDstru['strSQLDropTable'] + \
        dictSQLDstru['strSQLDropIndex'] + \
        dictSQLDstru['strSQLColName'] + \
        dictSQLDstru['strSQLIndexName'] + \
        dictSQLDstru['strSQLIndexON'] + \
        dictSQLDstru['strSQLFrom']+ \
        dictSQLDstru['strSQLTables'] + \
        dictSQLDstru['strSQLJoin'] + \
        dictSQLDstru['strSQLOn'] + \
        dictSQLDstru['strSQLSchemaCharSet'] + \
        dictSQLDstru['strSQLSchemaCollate'] + \
        dictSQLDstru['strSQLSet'] + \
        dictSQLDstru['strSQLColNameValue'] + \
        dictSQLDstru['strSQLWhere'] + \
        dictSQLDstru['strSQLLike'] + \
        dictSQLDstru['strSQLGroup'] + \
        dictSQLDstru['strSQLOrder'] + \
        dictSQLDstru['strSQLHaving'] + \
        dictSQLDstru['strSQLAlterAction'] + \
        dictSQLDstru['strSQLTableNameNew'] + \
        dictSQLDstru['strSQLColNameSub'] + \
        dictSQLDstru['strSQLColValue'] + \
        dictSQLDstru['strSQLSelectSub'] + \
        dictSQLDstru['strSQLCall'] + \
        strSQLLIMIT
    return dictSQLDstru['strSQL']