# EHSNMgt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import datetime

import EHSysMgt
import EHSymbolDef
import EHDate
import EHArray
import EHStr
import EHDB
import EHDBApply

#<PyDecl: Symbol Config>
c_strAttrSplitor = EHSymbolDef.c_strAttrSplitor
c_strSQLSplitor = EHSymbolDef.c_strSQLSplitor
c_strSQLValueBracketSymbol = EHSymbolDef.c_strSQLValueBracketSymbol
c_strAttrValueSplitor = EHSymbolDef.c_strAttrValueSplitor
#</PyDecl: Symbol Config>

#<PyDecl: SNMgt SerialNo Func>
c_strSNTmplt='<DocType><YrChar><MonthChar><DayWKChar><SNChar>'
c_intSNLenMax=20

c_intYearBase=2000
c_lstDateScpYrNum=[0, 9]
c_lstDateScpYrChr=['A', 'Z']
c_intChrLenYr=1

c_lstDateScpMthNum=[1, 9]
c_lstDateScpMthChr=['A', 'C']
c_intChrLenMth=1

c_intChrLenDayWK=3

c_intChrLenSN=3
c_blnSNCntFrmZero=False
#</PyDecl: SNMgt SerialNo Func>

#<PyDecl: SNMgt DBTable Func>
c_strDBTblNameSN= EHSysMgt.c_strSysDBTblPrefix + 'SNMgt'
c_strDBColNameTblName ='TblName'
c_strDBColNameSNColName ='SNColName'
c_strDBColNameSNTmplt ='SNTmplt'
c_strDBColNameSNVal ='SNVal'

c_dictTblSchemaSNMgt= \
    {
        EHDBApply.c_strDBTblColNameUqeNo: EHDBApply.c_strMySQLDataTypeInt,
        c_strDBColNameTblName: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
        c_strDBColNameSNColName: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
        c_strDBColNameSNTmplt: EHDBApply.c_strMySQLDataTypeVarChar + '(30)',
        c_strDBColNameSNVal: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
        EHDBApply.c_strDBTblColNameDeleted: EHDBApply.c_strMySQLDataTypeVarChar + '(1)',
        EHDBApply.c_strDBTblColNameLastVer: EHDBApply.c_strMySQLDataTypeVarChar + '(1)',
        EHDBApply.c_strDBTblColNameUploader: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
        EHDBApply.c_strDBTblColNameUpdateTime: EHDBApply.c_strMySQLDataTypeDateTime
    }
#</PyDecl: SNMgt DBTable Func>
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHSNMgt.py !')
# </PyDecl: RunTime>

#<PyRegion: SNMgt DBTable Func>
def fnSNTblChk(blnReBud=False)->bool:
    # <PyFunc: >
    #   Desc: Check the DB Tbl[c_dictTblSchemaSNMgt] Exist or Not,
    #       if not exist, Create AS [c_dictTblSchemaSNMgt]
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strTblName= DB TableName
    #      lstColName= Insert ColName
    #      lstColValue= Insert ColValue
    #   Option:
    #      strSectName= INI Config Section Name
    #   Return:
    # </PyFunc: >
    blnResult= \
        EHDBApply.fnDBTblChk(
            strTblName=c_strDBTblNameSN,
            dictTblSchema=c_dictTblSchemaSNMgt,
            blnReBud=blnReBud
        )
    return blnResult
#</PyRegion: SNMgt DBTable Func>


# <PyRegion: DB Col SN Analysis>
def fnSNFloatMaxGetExample():
    lstRtn = \
        fnSNDBColFloatMaxGet(
            strTblName='mdimgtrans_projitem',
            strDBName='spec',
            strColName='ProjNo'
        )
    print('lstRtn: ', lstRtn)
def fnSNDBColFloatMaxGet(
        strTblName,
        strColName,
        strSectName='',
        strDBName=''
)->(bool, str, list):
    # <PyFunc: fnSNDBColFloatMaxGet>
    #    Desc: Analysis the DB Table Column[strColName] Content,
    #       1. Get All Col Contents,
    #       2. fnStrNumGet: Split All Col Contents by Numeric and Not AS [0], and ColPosNumPos AS [1],
    #       2.1 Ex: '20160524-01(SJ)'->[['20160524', 'X', '01', 'XXXX'], 2]
    #       3. EHArray.fnArrayTypeDistinct: Integer All Col Num/Non-Num Col Format, Remove Duplicated
    #       3.1 Ex: '8;-1;2;-4::2'
    #       4. fnSNTmpltGen: Generate SQL REGEXP Serial No Template,
    #       4.1 Ex: '^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][^0-9][0-9][0-9][^0-9][^0-9][^0-9][^0-9]$'
    #       5. MAX(<ColName>): Get the Column Max Value via SQL MAX(<ColName>)
    #       6. fnSNNoAdd: Add 1 to the Column Max Value Digit Section, and Return the New Serial No
    #    Use By:
    #    Noticed:
    #    Parameter:
    #        strTblName: Dedicate DB Table Name
    #        strColName: Dedicated SN ColName process
    #    Option:
    #        strSectName: DB Config Section Name
    #        strDBName: DB Name
    #    Return: Max Serial No +1 List
    # </PyFunc: fnSNDBColFloatMaxGet>
    strSQL = 'SELECT DISTINCT ' + \
        '<ColNameSel> '
    strSQL = strSQL + \
        'FROM ' + \
            '<EHDBName><TblName> '

    # <PyCmt: Get strColName Col All Contents From DBTbl>
    strSQLRun=strSQL
    strSQLRun = strSQLRun.replace('<ColNameSel>', strColName)
    strSQLRun = strSQLRun.replace('<TblName>', strTblName)
    blnResult, strErrMsg, rowColValue = \
        EHDB.fnDBRSTGet(
            strSQLRun=strSQLRun,
            strSectName=strSectName,
            strDBName=strDBName
        )
    if not blnResult:
        strFuncName = 'EHSNMgt.fnSNDBColFloatMaxGet'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
                lstSNMax=None
            )

    if c_blnEHDebugMode:
        print('strSQLRun: {}'.format(strSQLRun))
        print('rowColValue: {}'.format(rowColValue))

    # <PyCmt: All Col Contents split by Numeric and Not AS [0], and ColPosNumPos AS [1]>
    # <PyCmt: Ex: ['20160524-01(SJ)'->['20160524', 'X', '01', 'XXXX'], 2] >
    lstColNumSplit = \
        EHStr.fnStrNumGet(
            lstRun=rowColValue,
            strNotSplit='.'
        )
    if c_blnEHDebugMode:
        print('lstColNumSplit: {}'.format(lstColNumSplit))

    # <PyCmt: Integer All Col Num/Non-Num Col Format>
    lstColChrType = EHArray.fnArrayTypeDistinct(lstRun=lstColNumSplit)
    if c_blnEHDebugMode:
        print('lstColChrType: {}'.format(lstColChrType))
    lstSNTmplt = fnSNTmpltGen(varRun = lstColChrType)
    if c_blnEHDebugMode: print('lstSNTmplt: {}'.format(lstSNTmplt))

    strSQLCtrl =\
        'WHERE ' + \
            '<ColName> REGEXP \'<SNColTmplt>\''
    lstSNMax:list=[]
    intRun=0
    for strSNTmplt in lstSNTmplt:
        strSQLRun=strSQL + strSQLCtrl
        strSQLRun=strSQLRun.replace('<ColNameSel>', 'MAX(<ColName>)') # <PyCmt: Add SQL MAX Here>
        strSQLRun = strSQLRun.replace('<ColName>', strColName)
        strSQLRun = strSQLRun.replace('<TblName>', strTblName)
        strSQLRun = strSQLRun.replace('<SNColTmplt>', strSNTmplt)
        blnResult, strErrMsg, rowSNMax = \
            EHDB.fnDBRSTGet(
                strSQLRun = strSQLRun,
                strSectName = strSectName,
                strDBName = strDBName
            )
        strSNMax=rowSNMax[0]
        strColFmt = lstColChrType[intRun].split(c_strAttrValueSplitor)[0]
        if c_blnEHDebugMode:
            print('strColFmt: {}'.format(strColFmt))
        intColPosNumLast = lstColChrType[intRun].split(c_strAttrValueSplitor)[1]
        if c_blnEHDebugMode:
            print('intColPosNumLast: {}'.format(intColPosNumLast))
        strSNNew = fnSNNoAdd(strSNMax=strSNMax, strColFmt=strColFmt, intColPosNumLast=intColPosNumLast)
        if len(strSNNew)>0: lstSNMax.append(strSNNew)
        intRun+=1
    return lstSNMax
# </PyRegion: DB Col SN Analysis>

# <PyRegion: Serial No Management>
def fnSNNoAdd(
    strSNMax,
        strColFmt,
        intColPosNumLast,
        strSplitorElm:str = c_strAttrSplitor
):
    # <PyFunc: fnSNNoAdd>
    #    Desc: Depends on Column Format, Add 1 to the Column Max Value Digit Section,
    #       and Return the New Serial No
    #    Use By:
    #    Noticed: Analysis Like '8;-1;2;-4::2' ,
    #       Positive Num is digit char, Negative Num is Non-digit char,
    #       '::2' is Last digit position
    #    Parameter:
    #        strColFmt: the Serial No Content Format
    #        intColPosNumLast: Last Digit Section of the Serial No
    #        Para3:
    #    Option:
    #        OptPara1:
    #        OptPara2:
    #        OptPara3:
    #    Return:
    # </PyFunc: fnSNNoAdd>
    intColRun = 0
    intChrLenRun = 0

    strSNNew = ''
    for intChrLen in strColFmt.split(strSplitorElm):
        if intColRun == int(intColPosNumLast):
            intChrStart = intChrLenRun
            intChrEnd = intChrStart + abs(int(intChrLen))
            strSNOrig = strSNMax[intChrStart:intChrEnd]
            intSNNew = int(strSNOrig) + 1
            if len(str(intSNNew)) <= len(strSNOrig):
                strSNNew = str('0' * (len(strSNOrig) - len(str(intSNNew))) + str(intSNNew))
                strSNNew = strSNMax[:intChrStart] + strSNNew + strSNMax[intChrEnd:]
                break
        intChrLenRun = intChrLenRun + abs(int(intChrLen))
        intColRun += 1
    return strSNNew
def fnSerialNoTemplateGet(
        strSNTmplt='',
        strDocType='',
        varYr='',
        varMth='',
        varDayWK='',
        intChrLenSN=c_intChrLenSN,
        blnSQL=True
)->str:
    # <PyDebug: Wait Develop>
    if len(strSNTmplt)==0: strSNTmplt=c_strSNTmplt
    strSN=strSNTmplt
    if len(strDocType)>0: strSN=strSN.replace('<DocType>', strDocType)
    strSN = strSN.replace('<YrChar>',fnSNYrChrCvrt( varYr = varYr ))
    strSN = strSN.replace('<MonthChar>', fnSNMthChrCvrt( varMth = varMth ))
    strSN = strSN.replace('<DayWKChar>', EHDate.fnDayWKNoGet( strDate = varDayWK ))
    strSNChar='_' if blnSQL else '0'
    if c_blnSNCntFrmZero:
        strSNChar=strSNChar*intChrLenSN
    else:
        strSNChar=strSNChar*intChrLenSN-1+ strSNChar if blnSQL else '1'
    strSN = strSN.replace('<SNChar>', strSNChar)
    return strSN


def fnSNTmpltGen(
    varRun,
    strSplitorElm:str = c_strAttrSplitor, 
    strSplitorPos:str = c_strAttrValueSplitor
):
    if varRun is None: return None
    cp_strRegNum='[0-9]'
    cp_strRegNotNum = '[^0-9]'
    if isinstance(varRun, str):
        lstRun=[varRun]
    else:
        lstRun=varRun
    lstRtn=[]
    for strSub in lstRun:
        strColFmt=strSub.split(strSplitorPos)[0]
        strReg=''
        for intChrLen in strColFmt.split(strSplitorElm):
            intChrLen=int(intChrLen)
            strReg=strReg + \
                   (cp_strRegNum if intChrLen>0 else cp_strRegNotNum)*abs(intChrLen)
        if blnSntSmybAdd : strReg='^'+strReg+'$'
        lstRtn.append(strReg)
    return lstRtn

def fnDBSerialNoMgtInsert():
    pass

def fnSNDateSngChrScp(blnTypeYr=True, blnOrd=True)->list:
    if blnTypeYr:
        lstDateScpNum = c_lstDateScpYrNum
        lstDateScpChr = c_lstDateScpYrChr
    else:
        lstDateScpNum = c_lstDateScpMthNum
        lstDateScpChr = c_lstDateScpMthChr

    lstChrScp=[]
    if not lstDateScpNum is None:
        lstChrScp=[intChr for intChr in range(ord(str(lstDateScpNum[0])), ord(str(lstDateScpNum[-1])) + 1)]
    if not lstDateScpChr is None:
        lstChrScp = lstChrScp + [intChr for intChr in range(ord(lstDateScpChr[0]), ord(lstDateScpChr[-1]) + 1)]
    if blnOrd:
        return lstChrScp
    else:
        return [chr(chrRun) for chrRun in lstChrScp]

def fnSNYrChrCvrt(varYr = '', intChrLen = c_intChrLenYr):
    # <PyCmt: Convert Year to indicated Len Char>
    dateRun = EHDate.fnNow()

    if len(str(varYr))==0: varYr=dateRun.year
    if isinstance(varYr, int):
        lstSngChrScp = fnSNDateSngChrScp()
        if intChrLen==1:
            intYrRun = int(str(varYr)[-2:])
            intChrRun=(intYrRun % len(lstSngChrScp))
            return chr(lstSngChrScp[intChrRun])
        elif intChrLen==2:
            intYrRun = int(str(varYr)[-2:])
            return intYrRun
        elif intChrLen==4:
            return varYr + (c_intYearBase if varYr < c_intYearBase else 0)
        else:
            return None
    elif isinstance(varYr, str):
        lstSngChrScp = fnSNDateSngChrScp(blnOrd=False)
        if len(varYr)==1:
            if not varYr in lstSngChrScp: return None
            intYrLoop=(dateRun.year-c_intYearBase) // len(lstSngChrScp)
            return c_intYearBase+(intYrLoop*len(lstSngChrScp)-1)+lstSngChrScp.index(varYr)
        elif len(varYr) == 2:
            return int(varYr) + c_intYearBase
        elif len(varYr) == 4:
            return int(varYr)
        else:
            return None

def fnSNMthChrCvrt(varMth='', intChrLen=c_intChrLenMth):
    dateRun = EHDate.fnNow()

    if len(str(varMth))==0: varMth=dateRun.month
    if len(str(varMth))>2: return None
    if isinstance(varMth, int):
        lstSngChrScp = fnSNDateSngChrScp(blnTypeYr=False)
        intMth=varMth
        if intChrLen==1:
            return chr(lstSngChrScp[intMth])
        elif intChrLen==2:
            return intMth
        else:
            return None
    elif isinstance(varMth, str):
        lstSngChrScp = fnSNDateSngChrScp(blnTypeYr=False, blnOrd=False)
        if len(varMth)==1:
            if varMth in lstSngChrScp:
                return lstSngChrScp.index(varMth)+1
            else:
                return None
        elif len(varMth) == 2:
            return int(varMth)
        else:
            return None
# </PyRegion: Serial No Management>