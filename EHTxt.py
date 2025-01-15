# EHTxt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import xlwings as xw
import EHXW

import EHSymbolDef
import EHDate
import EHMsg
import EHSysMgt
import EHFile
import EHArray
import EHDBApply

# <PyDecl: Symbol Define & UDE import >
c_strNewLine = EHSymbolDef.c_strNewLine #'\n'
c_strTab = EHSymbolDef.c_strTab #'\t'

c_strAttrSplitor = EHSymbolDef.c_strAttrSplitor # ';'
c_strSQLSplitor = EHSymbolDef.c_strSQLSplitor # ', '
c_strSQLValueBracketSymbol = EHSymbolDef.c_strSQLValueBracketSymbol # '\''
c_strAttrValueSplitor = EHSymbolDef.c_strAttrValueSplitor # '::'

c_strTxtImpSymbFilePath = EHSymbolDef.c_strTxtImpSymbFilePath # '\'
c_strTxtImpHeaderSymbPrefix = EHSymbolDef.c_strTxtImpHeaderSymbPrefix # '#'
c_strTxtImpHeaderSymbValSplitor = EHSymbolDef.c_strTxtImpHeaderSymbValSplitor # ':'
c_strTxtImpHeaderSplitor = EHSymbolDef.c_strTxtImpHeaderSplitor # ','

c_strTxtImpDataSplitor = EHSymbolDef.c_strTxtImpDataSplitor # '<;>'
# </PyDecl: Symbol Define & UDE import >

c_strTxtImpPrefix = EHSysMgt.c_strTxtImpPrefix
c_strTxtFileNameTmp =  c_strTxtImpPrefix + 'TxtImpEx.txt'
c_strTxtImpParaDBName = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DBName'
c_strTxtImpParaDBTblName = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DBTblName'
c_strTxtImpParaDBTblCreate = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DBTblCreate|Y;N'
c_strTxtImpParaDBTblCreateOnly = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DBTblCreateOnly|Y;N'
c_strTxtImpParaDBTblRebuild = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DBTblRebuild|Y;N'
c_strTxtImpParaDBTblWithSysDftCol = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DBTblWithSysDftCol|Y;N'
c_strTxtImpParaDataDel = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DataDel|Y;N'
c_strTxtImpParaDataUpd = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DataUpd|Y;N'
c_strTxtImpParaDataApd = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'DataApd|Y;N'
c_strTxtImpParaColName = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'ColName'
c_strTxtImpParaColSchema = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'ColSchema|[MySQLColSchema]'
c_strTxtImpParaColNameKey = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'ColNameKey'
c_strTxtImpParaHeaderEnd = c_strTxtImpHeaderSymbPrefix + c_strTxtImpPrefix + 'HeaderEnd'

c_lstTxtImpPara= \
    [
        c_strTxtImpParaDBName,
        c_strTxtImpParaDBTblName,
        c_strTxtImpParaDBTblCreate,
        c_strTxtImpParaDBTblCreateOnly,
        c_strTxtImpParaDBTblRebuild,
        c_strTxtImpParaDBTblWithSysDftCol,
        c_strTxtImpParaDataDel,
        c_strTxtImpParaDataUpd,
        c_strTxtImpParaDataApd,
        c_strTxtImpParaColName,
        c_strTxtImpParaColSchema,
        c_strTxtImpParaColNameKey
    ]

p_blnXWMode=EHXW.p_blnXWMode
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHTxt.py !')
# </PyDecl: RunTime>
# <PyRegion: Txt File Oper>
def fnTxtOper(
        strFilePath:str,
        lstReadLines:list = None,
        intFromLine: int = -1,
        blnWrite:bool = False,
        intWriteLine:int = -1,
        strMsgWrite:str = '',
        blnOverWrite:bool = False
)->(str| bool, int):
    # <PyFunc: >
    #   Desc: Txt File Operate Function
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strFilePath= Txt File Path
    #   Option:
    #      lstReadLines= User indicated Read Line List
    #      intFromLine= User indicated Read From Line
    #      blnWrite= Write Mode
    #      strMsgWrite= Message To Write
    #      blnOverWrite= Clear File Before Write
    #   Return: 
    #       strMsg= Read or Write Message
    #       intLineCount= Line Count
    # </PyFunc: >
    strFilePathRun=EHFile.fnFileExist(strFileName=strFilePath)
    if len(strFilePathRun)==0 and not blnWrite:
        strErrMsg='File Not Exist!: {}'.format(strFilePath)
        strFuncName='EHTxtFile.fnTxtOper'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return None

    if blnOverWrite:
        strOperType = 'w+'
    elif blnWrite:
        strOperType = 'a+'
    else:
        strOperType = 'r'

    with open(strFilePath, strOperType) as OpenFile:
        if strOperType == 'w+':
            OpenFile.write(strMsgWrite)
            return True, -1
        OpenFile.seek(0)
        lstRead = []
        intLineCount:int = 0
        for intLineNo, strLine in enumerate(OpenFile):
            if strOperType == 'r':
                if not lstReadLines is None :
                    if intLineNo in lstReadLines: lstRead.append(strLine)
                elif intFromLine >= 0:
                    if intLineNo >= intFromLine: lstRead.append(strLine)
                else:
                    lstRead.append(strLine)
            elif strOperType == 'a+':
                if 0 <= intWriteLine != intLineNo:
                    lstRead.append(strLine)
                else:
                    strMsgWrite=''.join([strMsgWrite, c_strNewLine])
                    strMsgWrite=strMsgWrite.replace(c_strNewLine + c_strNewLine, c_strNewLine)
                    lstRead.append(strMsgWrite)
            intLineCount = intLineNo
        strRead=''.join(lstRead)
        if intWriteLine >= 0:
            fnTxtOper(
                strFilePath=strFilePath,
                strMsgWrite = strRead,
                blnOverWrite= True
            )
        elif strOperType != 'r':
            OpenFile.write(strMsgWrite)
        strMsg=strRead if strOperType == 'r' else strMsgWrite
        return strMsg, intLineCount
# </PyRegion: Txt File Oper>
# <PyRegion: Excel Range to Txt File>
def fnTxtXLRngToTxt(
        rngRun:xw.Range = None,
        strFilePath:str = ''
)->str:
    # <PyFunc: >
    #   Desc: Excel Range Data To Txt File
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #      shtRun= Excel Worksheet Object
    #      strXLRng= Excel Range
    #      strFilePath= Txt File Path
    #   Return:
    #       strFilePath= Txt File Path
    # </PyFunc: >
    import EHXLSht
    if rngRun is None: rngRun = EHXLSht.fnRngSeltRng()
    shtRun=rngRun.sheet
    strFilePath = fnTxtFilePath(strFilePath=strFilePath)
    if len(strFilePath)==0:
        strErrMsg='Txt File Path Not Exist!'
        strFuncName='EHTxtFile.fnTxtXLRngToTxt'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return None

    rngFirstCell = EHXLSht.fnRngFirstCell(shtRun)
    EHXLSht.fnRngLastCellReset(shtRun)
    rngLastCell = EHXLSht.fnRngLastCell(shtRun)
    intRowCount = rngLastCell.row - rngFirstCell.row + 1
    intColCount = rngLastCell.column - rngFirstCell.column + 1

    blnResult = False
    intRowStart = rngRun.row
    intColStart = rngRun.column
    intColEnd = rngRun.column + rngRun.columns.count - 1
    intRowEnd = rngRun.row + rngRun.rows.count - 1
    lstColName = None
    strColName = ''
    strColSchema = ''
    if rngRun.row!=rngFirstCell.row or rngRun.column!=rngFirstCell.column or \
        rngRun.rows.count!=intRowCount or rngRun.columns.count!=intColCount:
        strMsg = 'Selected Range is partial, ' + \
            c_strNewLine + 'Current: Range({}, {}) to Range({}, {}), '.\
                 format(
                    rngRun.row, rngRun.column,
                    rngRun.row+rngRun.rows.count-1, rngRun.column+rngRun.columns.count-1) + \
            c_strNewLine + 'Expand: Range({}, {}) to Range({}, {}), '.\
                 format(rngFirstCell.row, rngFirstCell.column, rngLastCell.row, rngLastCell.column) + \
            c_strNewLine + 'do you want to switch to full range? (Y/N)'
        strCaption = 'Range Area Changing Confirmation'
        blnResult = EHMsg.fnDlgOpt( strMsg=strMsg, strCaption=strCaption)
        if blnResult:
            EHXLSht.fnRngLastCellReset(shtRun)
            rngLastCell = EHXLSht.fnRngLastCell(shtRun)
            rngRun = shtRun.range(rngFirstCell, rngLastCell)
            blnResult, lstColName, tupAddr = EHXLSht.fnRngHeaderGuess(rngRun=rngRun)
            intRowStart=tupAddr[0]
            intColStart=tupAddr[1]
            intColEnd=tupAddr[2]
            intRowEnd=rngRun.row+rngRun.rows.count-1
            rngRun=shtRun.range(shtRun.cells(intRowStart, intColStart), shtRun.cells(intRowEnd, intColEnd))
        else:
            blnResult, lstColName, tupAddr = EHXLSht.fnRngHeaderGuess(rngRun=rngRun)
            intRowStart=tupAddr[0]
            intColStart=tupAddr[1]
            intColEnd=tupAddr[2]
            intRowEnd=rngRun.row+rngRun.rows.count-1

        if c_blnEHDebugMode:
            print('Area Expand Done!: {}'.format(rngRun.address))

    tupData = \
        EHXLSht.fnRngSeltValLstGet(
            shtRun=shtRun,
            intRowStart=intRowStart + (1 if blnResult else 0),
            intRowEnd=intRowEnd,
            intColStart=intColStart,
            intColEnd=intColEnd
        )
    if c_blnEHDebugMode:
        print("Range Data!: {}".format(tupData))

    lstColSchema= \
        EHXLSht.fnRngColSchemaGet(
            tupData=tupData,
            lstColName=lstColName if blnResult else None
        )
    if not lstColName is None: strColName = c_strAttrSplitor.join(lstColName)
    if not lstColSchema is None: strColSchema = c_strAttrSplitor.join(lstColSchema)
    if c_blnEHDebugMode:
        print("fnRngColSchemaGet, lstColName: {}, lstColSchema: {}".format(lstColName, lstColSchema))

    strDBTblName:str = EHFile.fnFileNameOnly(strFilePath = strFilePath)
    strFilePath = \
        fnTxtDBImpFileCreate(
            strFilePath = strFilePath,
            strDBName = '',
            strDBTblName = strDBTblName,
            strDBTblCreate = '',
            strDBTblCreateOnly = '',
            strDBTblRebuild = '',
            strDBTblWithSysDftCol = '',
            strDataDel = '',
            strDataUpd = '',
            strDataApd = '',
            strColName = strColName,
            strColSchema = strColSchema,
            strDataWrite = tupData
        )
    if c_blnEHDebugMode:
        print("fnTxtDBImpFileCreate: {}".format(strFilePath))

    return strFilePath
# </PyRegion: Excel Range to Txt File>
# <PyRegion: Txt File Database Import Function>
def fnTxtDBImpFileCreate(
    strFilePath='',
    strDBName='',
    strDBTblName='',
    strDBTblCreate='',
    strDBTblCreateOnly='',
    strDBTblRebuild='',
    strDBTblWithSysDftCol='',
    strDataDel='',
    strDataUpd='',
    strDataApd='',
    strColName='',
    strColSchema='',
    strDataWrite=''
)->str:
    # <PyFunc: >
    #   Desc: Create Txt File Template for DB Import
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strFilePath= Txt File Path
    #      strDBName= 'DB Name' Parameter
    #      strDBTblName= 'DB Table Name' Parameter
    #      strDBTblCreate= 'DB Table Create' Parameter
    #      strDBTblCreateOnly= 'DB Table Create Only' Parameter [Y;N]
    #      strDBTblRebuild= 'DB Table Rebuild' Parameter [Y;N]
    #      strDBTblWithSysDftCol= 'DB Table With System Default Column' Parameter [Y;N]
    #      strDataDel= 'Data Delete' Parameter [Y;N]
    #      strDataUpd= 'Data Update' Parameter [Y;N]
    #      strDataApd= 'Data Append' Parameter [Y;N]
    #      strColName= 'Column Name' Parameter
    #      strColSchema= 'Column Schema' Parameter
    #      strMsgWrite= Message To Write
    #   Return: 
    #       strPath= Txt File Path
    # </PyFunc: >
    strFilePath=fnTxtFilePath(strFilePath=strFilePath)
    if len(strFilePath)==0:
        strErrMsg='Txt File Path Not Exist!'
        strFuncName='EHTxtFile.fnTxtDBImpFileCreate'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return None

    if len(strDBName)==0:
        import EHDB
        clsEHDB=EHDB.EHDBClass()
        strDBName = clsEHDB.p_strDBNameDft
    strDBTblName=strDBTblName.replace(' ', '')

    strHeader = \
        fnTxtDBImpFileHeaderCreate(
            strDBName = strDBName,
            strDBTblName = strDBTblName,
            strDBTblCreate = strDBTblCreate,
            strDBTblCreateOnly = strDBTblCreateOnly,
            strDBTblRebuild = strDBTblRebuild,
            strDBTblWithSysDftCol = strDBTblWithSysDftCol,
            strDataDel = strDataDel,
            strDataUpd = strDataUpd,
            strDataApd = strDataApd,
            strColName = strColName,
            strColSchema = strColSchema
        )
    strMsg=strHeader
    if isinstance(strDataWrite, (list, tuple)):
        strDataWrite=fnLstToTxt(tupRun=strDataWrite)
    if len(strDataWrite)>0:
        strMsg = c_strNewLine.join([strMsg, strDataWrite])

    fnTxtOper(
        strFilePath=strFilePath,
        blnWrite=True,
        strMsgWrite=strMsg,
        blnOverWrite=True
    )
    return strFilePath

def fnTxtDBImpFileHeaderCreate(
    strDBName='',
    strDBTblName='',
    strDBTblCreate='',
    strDBTblCreateOnly='',
    strDBTblRebuild='',
    strDBTblWithSysDftCol='',
    strDataDel='',
    strDataUpd='',
    strDataApd='',
    strColName='',
    strColSchema='',
    strColNameKey=''
):
    lstHeader=[]
    for strParaName in c_lstTxtImpPara:
        if strParaName==c_strTxtImpParaDBName:
            strParaName = (c_strTxtImpParaDBName if len(strDBName)==0 else c_strTxtImpParaDBName.split('|')[0])
            strValue=strDBName
        elif strParaName==c_strTxtImpParaDBTblName:
            strParaName = (c_strTxtImpParaDBTblName if len(strDBTblName)==0 else c_strTxtImpParaDBTblName.split('|')[0])
            strValue = strDBTblName
        elif strParaName==c_strTxtImpParaDBTblCreate:
            strParaName = \
                (c_strTxtImpParaDBTblCreate if len(strDBTblCreate)==0 else c_strTxtImpParaDBTblCreate.split('|')[1])
            strValue = strDBTblCreate
        elif strParaName==c_strTxtImpParaDBTblCreateOnly:
            strParaName = \
                (c_strTxtImpParaDBTblCreateOnly if len(strDBTblCreateOnly)==0
                    else c_strTxtImpParaDBTblCreateOnly.split('|')[1])
            strValue = strDBTblCreateOnly
        elif strParaName==c_strTxtImpParaDBTblRebuild:
            strParaName = \
                (c_strTxtImpParaDBTblRebuild if len(strDBTblRebuild)==0
                    else c_strTxtImpParaDBTblRebuild.split('|')[1])
            strValue = strDBTblRebuild
        elif strParaName==c_strTxtImpParaDBTblWithSysDftCol:
            strParaName = \
                (c_strTxtImpParaDBTblWithSysDftCol
                    if len(strDBTblWithSysDftCol)==0 else c_strTxtImpParaDBTblWithSysDftCol.split('|')[1])
            strValue = strDBTblWithSysDftCol
        elif strParaName==c_strTxtImpParaDataDel:
            strParaName = (c_strTxtImpParaDataDel if len(strDataDel)==0 else c_strTxtImpParaDataDel.split('|')[1])
            strValue = strDataDel
        elif strParaName==c_strTxtImpParaDataUpd:
            strParaName = (c_strTxtImpParaDataUpd if len(strDataUpd)==0 else c_strTxtImpParaDataUpd.split('|')[1])
            strValue = strDataUpd
        elif strParaName==c_strTxtImpParaDataApd:
            strParaName = (c_strTxtImpParaDataApd if len(strDataApd)==0 else c_strTxtImpParaDataApd.split('|')[1])
            strValue = strDataApd
        elif strParaName==c_strTxtImpParaColName:
            strValue = strColName
        elif strParaName==c_strTxtImpParaColSchema:
            strParaName =(c_strTxtImpParaColSchema if len(strColSchema)==0 else c_strTxtImpParaColSchema.split('|')[0])
            strValue = strColSchema
        elif strParaName==c_strTxtImpParaColNameKey:
            strValue = strColNameKey
        else:
            strValue = ''
        strHeaderRun = strParaName + c_strTxtImpHeaderSymbValSplitor + ' ' + strValue
        lstHeader.append(strHeaderRun)
    lstHeader.append(c_strTxtImpParaHeaderEnd)
    strHeader=c_strTxtImpHeaderSplitor.join(lstHeader)
    return strHeader

def fnLstToTxt(
    tupRun:tuple,
    strSplitor=c_strTxtImpDataSplitor
)->str:
    # <PyFunc: >
    #   Desc: Convert Tuple to Txt Data
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      tupRun= Tuple Data Input
    #   Option:
    #      strSplitor= Splitor for Data
    #   Return:
    # </PyFunc: >
    if not isinstance(tupRun, (tuple, list)): return ''
    lstData=[]
    for tupRow in tupRun:
        blnRowNone=all(elm is None for elm in tupRow)
        if not blnRowNone:
            strDataRow = strSplitor.join(map(str, tupRow))
            lstData.append(strDataRow)
    return c_strNewLine.join(lstData)

def fnTxtDBImpPreProc(strFilePath:str ='')->bool:
    # <PyFunc: fnTxtDBImpPreProc>
    #   Desc: Import Txt File to DB with TXT Header Judgement for Parameter
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strFilePath= Import Txt File Path
    #   Option:
    #   Return: 
    # </PyFunc: >    
    
    # <PyCmt: Show File Picker for Text File to Import>
    if len(strFilePath)==0:
        strFilePath=EHFile.fnFilePicker(strWinCap='Select Text File to Import', strWildcard='Text files (*.txt)|*.txt')
    if strFilePath is None: return None

    # <PyCmt: Setup LogPath>
    EHMsg.fnLogFilePath(strFilePath = strFilePath, blnSetRunning = True)

    # <PyCmt: Get Txt File 1st Line as Parameter>
    strPara, intLineCount= fnTxtOper(strFilePath=strFilePath, lstReadLines=[0])
    if c_strTxtImpParaHeaderEnd in strPara: strPara=strPara.split(c_strTxtImpParaHeaderEnd)[0]
    if strPara is None:
        strErrMsg='Config Header is Empty!'
        strFuncName='EHTxtFile.fnTxtDBImpPreProc'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return False

    # <PyCmt: Get A Txt File Import Fixed Element Dict>
    dictTxtImpPara = \
        EHArray.EHFixElmDict(
            lstElmKey=c_lstTxtImpPara,
            blnErrShow=False
        )

    # <PyCmt: Compare Parameter with 'c_lstTxtImpPara' and Set Dict Value>
    for strParaRun in strPara.split(c_strTxtImpHeaderSplitor):
        strParaNameRun=strParaRun
        strParaValueRun=''
        if c_strTxtImpHeaderSymbValSplitor in strParaRun:
            strParaValueRun = strParaRun.split(c_strTxtImpHeaderSymbValSplitor)[1].strip()
            strParaNameRun = strParaRun.split(c_strTxtImpHeaderSymbValSplitor)[0]
        strParaNameRun=strParaNameRun.strip()
        for strParaStd in c_lstTxtImpPara:
            strParaNameStd=strParaStd
            if '|' in strParaStd: strParaNameStd = strParaNameStd.split('|')[0]
            if strParaNameRun==strParaStd or strParaNameRun == strParaNameStd :
                # <PyCmt: if Para Std Name with Value Criteria, Filter Value Criteria>
                strDataTypeStd=dictTxtImpPara.get(strParaStd+'DataType','')
                if len(strDataTypeStd)>0:
                    if ''.join([';', strParaValueRun, ';']) in ''.join([';', strDataTypeStd, ';']):
                        dictTxtImpPara[strParaNameStd] = strParaValueRun
                else:
                    dictTxtImpPara[strParaNameStd] = strParaValueRun
                break

    if len(dictTxtImpPara[c_strTxtImpParaDBName])==0 or len(dictTxtImpPara[c_strTxtImpParaDBTblName])==0:
        strErrMsg='DBName or DBTblName is Empty!'
        strFuncName='EHTxtFile.fnTxtDBImpPreProc'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return False
    # elif not dictTxtImpPara[c_strTxtImpParaDBTblCreate.split('|')[0]]!='Y' and \
    #     dictTxtImpPara[c_strTxtImpParaDBTblCreateOnly.split('|')[0]]!='Y' and \
    #     not dictTxtImpPara[c_strTxtImpParaDataUpd.split('|')[0]] == 'Y' and \
    #     not dictTxtImpPara[c_strTxtImpParaDataApd.split('|')[0]] == 'Y':
    #     strErrMsg='No Operation Specified!'
    #     strFuncName='EHTxtFile.fnTxtDBImpPreProc'
    #     EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
    #     return False

    import EHDBApply
    # <PyCmt: Get Txt Import ColSchema and Convert to DB ColSchema>
    strColName=dictTxtImpPara[c_strTxtImpParaColName]
    strColDataType=dictTxtImpPara[c_strTxtImpParaColSchema.split('|')[0]]
    strColNameKey = dictTxtImpPara[c_strTxtImpParaColNameKey]
    blnColWithSysDft=dictTxtImpPara[c_strTxtImpParaDBTblWithSysDftCol.split('|')[0]]=='Y'

    # <PyCmt: Convert strColName and strColDataType to DB DictColSchema,
    #   Ex:
    #       dictColSchema['blnColNullable']
    #       dictColSchema['strColNullable']
    #       dictColSchema['blnColPrmKey']
    #       dictColSchema['blnAutoIncrement']
    #       dictColSchema['strColNumFmt']
    #       dictColSchema['strColDefault']
    #       dictColSchema['strSQLColTblCrtDataLen']
    #       dictColSchema['strSQLColTblCrtDataLenRun']
    #       dictColSchema['strSQLColTblCrt']
    #       dictColSchema['strSQLColTblCrtRun']
    #       dictColSchema['strSQLColSelt']
    #       dictColSchema['strSQLColSeltRun']
    #       dictColSchema['strSQLColUpd']
    #       dictColSchema['strSQLColUpdRun']
    #       dictColSchema['strColValue']
    #       dictColSchema['strColValueRun']
    #       dictColSchema['strErrMsg']
    #       dictColSchema['blnErr']

    dictColSchema = \
        EHDBApply.fnDBColStrSchemaDictCvrt(
            strColName=strColName,
            strColDataType=strColDataType,
            blnColWithSysDft=blnColWithSysDft
        )
    # <PyCmt: Load DictColSchema to Convert to lstColSchema and lstColSchemaSQL>

    blnResult, lstColSchema = EHDBApply.fnDBColDictSchemaCvrt(dictTblSchema = dictColSchema)
    if not blnResult:
        strFuncName='EHTxtFile.fnTxtDBImpPreProc'
        # <PyCmt: ErrMsg including in lstColSchema>
        EHMsg.fnMsgPrt(strMsg = lstColSchema, strFuncName = strFuncName, blnLog=True)
        return False

    strTblName:str = dictTxtImpPara[c_strTxtImpParaDBTblName]
    strDBName:str = dictTxtImpPara[c_strTxtImpParaDBName]
    blnTblCreate:bool = dictTxtImpPara[c_strTxtImpParaDBTblCreate.split('|')[0]]=='Y'
    blnTblCreateOnly:bool = dictTxtImpPara[c_strTxtImpParaDBTblCreateOnly.split('|')[0]]=='Y'
    blnTblRebuild:bool = dictTxtImpPara[c_strTxtImpParaDBTblRebuild.split('|')[0]]=='Y'
    blnDataDel:bool = dictTxtImpPara[c_strTxtImpParaDataDel.split('|')[0]]=='Y'
    blnDataUpd:bool = dictTxtImpPara[c_strTxtImpParaDataUpd.split('|')[0]]=='Y'
    blnDataApd:bool = dictTxtImpPara[c_strTxtImpParaDataApd.split('|')[0]]=='Y'

    blnTblExisted: bool = False
    lstTblName, lstTblSchema = \
        EHDBApply.fnDBTblEnum(
            strDBName=strDBName,
            strTblName=strTblName
        )
    if not lstTblName is None: blnTblExisted = True

    blnTblCreated: bool = False
    if blnTblExisted and not blnTblRebuild:
        pass
    elif blnTblCreate:
        # <PyCmt: Create Tabel with Data Schema>
        blnResult, strErrMsg = \
            EHDBApply.fnDBTblCreate(
                lstColSchema=lstColSchema,
                strTblName=strTblName,
                strDBName=strDBName,
                blnCleanUp=blnTblRebuild,
                blnErrRtn=True
            )
        if not blnResult:
            strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
            return False
        else:
            strMsg = 'Txt File Import, Table: {} Created!'.format(dictTxtImpPara[c_strTxtImpParaDBTblName])
            strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
            blnTblCreated=True
        lstColName=[]
        for lstColSchemaRun in lstColSchema:
            lstColName.append(lstColSchemaRun[EHDBApply.c_intTblColSchemaColName])
        strColName=c_strAttrSplitor.join(lstColName)
    else:
        lstTblName, lstTblSchema = EHDBApply.fnDBTblEnum(strDBName=strDBName,strTblName=strTblName)
        if lstTblName is None:
            strMsg = 'Table: {} Not Exist!'.format(dictTxtImpPara[c_strTxtImpParaDBTblName])
            strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
            return False

    # <PyCmt: Tbl Create Only>
    if blnTblCreateOnly:
        strMsg='Table Created Only!'
        strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return True

    # <PyCmt: Table Col Schema Check!>
    if blnTblExisted:
        blnResult, strErrMsg, dictColSchema, lstColSchemaTrg = \
            EHDBApply.fnDBColSchemaCmp(
                lstColSchemaSrc=lstColSchema,
                strTblNameTrg=strTblName,
                strDBName=strDBName
            )
        if not blnResult:
            strErrMsg = 'Txt File Import Function, Table Col Schema Check Fail!'
            strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
            return False
        elif len(dictColSchema['ColNameDiff'])>0:
            lstErrMsg = []
            strErrMsg=''
            for strKey, strValue in dictColSchema.items():
                if len(strValue)>0:
                    strErrMsgRun = '{}: {}'.format(strKey, strValue)
                    lstErrMsg.append(strErrMsgRun)
            if len(lstErrMsg)>0: strErrMsg = c_strNewLine.join(lstErrMsg)
            strErrMsg=\
                c_strNewLine.\
                    join(['Txt File Import Function, '
                          'Txt File and DB Tbl(\'{}\') Col Compare Mismatch!'.format(strTblName),
                    strErrMsg])
            strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'

            if len(dictColSchema['ColNotIncd'])>0:
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
                return False
            else:
                strMsg='Target DB Tbl: {} Col Mismatch with Source(Txt File Col Schema)!'.format(strTblName) +\
                    c_strNewLine + 'Load by Target(DB) ColSchema?'
                strMsg=c_strNewLine.join([strFuncName, strMsg])
                blnResult=EHMsg.fnDlgOpt(strMsg=strMsg, strCaption = "Load By DB Table ColSchema Confirmation")
            if blnResult:
                lstColName=[]
                lstColDataType=[]
                lstColSchema=lstColSchemaTrg
                for lstColSchemaRun in lstColSchema:
                    strColName=lstColSchemaRun[EHDBApply.c_intTblColSchemaColName]
                    lstColName.append(strColName)
                    blnResult, strErrMsg, dictColSchema = \
                        EHDBApply.fnDBColSngSchemaDictCvrt(
                            strColName = strColName,
                            lstColSchema=lstColSchema,
                            blnValBlkSkip = True
                        )
                    if blnResult:
                        strColDataType = dictColSchema['strSQLColSchemaRun']
                        lstColDataType.append(strColDataType)
                strColName = c_strAttrSplitor.join(lstColName)
                strColSchema = c_strAttrSplitor.join(lstColDataType)
                strHeader = fnTxtDBImpFileHeaderCreate(
                    strDBName=strDBName,
                    strDBTblName=strTblName,
                    strDBTblCreate='Y' if blnTblCreate else '',
                    strDBTblCreateOnly='Y' if blnTblCreateOnly else '',
                    strDBTblRebuild='Y' if blnTblRebuild else '',
                    strDBTblWithSysDftCol='Y' if blnColWithSysDft else '',
                    strDataDel='Y' if blnDataDel else '',
                    strDataUpd='Y' if blnDataUpd else '',
                    strDataApd='Y' if blnDataApd else '',
                    strColName=strColName,
                    strColSchema=strColSchema,
                )
                fnTxtOper(
                    strFilePath = strFilePath,
                    blnWrite = True,
                    intWriteLine = 0 ,
                    strMsgWrite = strHeader
                )
            else:
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
                return False
        else:
            lstColSchema=lstColSchemaTrg
            lstColName=[]
            for lstColSchemaRun in lstColSchema:
                lstColName.append(lstColSchemaRun[EHDBApply.c_intTblColSchemaColName])
            strColName=c_strAttrSplitor.join(lstColName)
    # <PyCmt: Start Import Data>
    if intLineCount <= 1:
        strMsg = 'Txt File Import, File Content Only Header!'
        strFuncName = 'EHTxtFile.fnTxtDBImpPreProc'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return False

    strData, intLineCount=fnTxtOper(strFilePath=strFilePath, intFromLine=1)
    blnResult, strErrMsg = \
        fnTxtDataImp(
            strTblName = dictTxtImpPara[c_strTxtImpParaDBTblName],
            strDBName = dictTxtImpPara[c_strTxtImpParaDBName],
            lstColSchema = lstColSchema,
            strColName = strColName,
            strDataPath = strFilePath,
            strData = strData,
            blnColWithSysDft = blnColWithSysDft,
            blnDataDel = blnDataDel,
            blnDataUpd = blnDataUpd,
            strColNameKey = strColNameKey,
            blnDataApd = blnDataApd,
            strLogPath = strFilePath,
            strSplitor = c_strTxtImpDataSplitor
        )
    # <PyCmt: Setup LogPath>
    EHMsg.fnLogFilePath(blnCleanDft = True)

    return blnResult

def fnTxtDataImp(
    strTblName:str,
    strDBName:str,
    strColName:str,
    lstColSchema:list,
    strDataPath:str,
    strData:str,
    blnColWithSysDft:bool = False,
    blnDataDel:bool = False,
    blnDataUpd:bool = False,
    strColNameKey:str = '',
    blnDataApd:bool = False,
    strLogPath:str = '',
    strSplitor:str = c_strTxtImpDataSplitor
)->(bool, str):
    # <PyFunc: >
    #   Desc: Import strData to DB Table
    #   Use By:
    #   Noticed: Called by fnTxtDBImpPreProc
    #   Parameter:
    #      strTblName= DB TableName
    #      strDBName= DB Name
    #      lstColName= Insert ColName
    #      strData= Data to Import with strSplitor and c_strNewLine as Line Separator
    #      lstColSchema= DB Table ColSchema
    #      blnDataDel= Delete Data Before Import [Y/N]
    #      blnDataUpd= Update Data Into DB [Y/N]
    #      strColNameKey= Key Column Name for Update Operation
    #        if strDataUpd='Y' and strColNameKey='' then break Upload Operation
    #      strDataApd= Append Data Into DB [Y/N]
    #      strLogPath= Log File Path
    #   Option:
    #      strSectName= INI Config Section Name
    #   Return:
    # </PyFunc: >
    if blnDataUpd and len(strColNameKey)==0:
        strErrMsg = 'Indicated \'Update\' Operation, But No Key Column Specified!'
        strFuncName='EHTxtFile.fnTxtDataImp'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
            )

    dateRun = EHDate.fnNow()
    # <PyCmt: lstColName Remove All Space>
    lstColName=[strColName.strip().replace(' ','') for strColName in strColName.split(c_strAttrSplitor)]
    # <PyCmt: lstColNameKey Remove All Space>
    lstColNameKey = strColNameKey.split(strSplitor)
    lstColNameKey = [strColNameKey.replace(' ', '') for strColNameKey in lstColNameKey]

    if blnDataDel:
        # <PyCmt: c_strTxtImpParaDataDel >
        blnResult = \
            EHDBApply.fnDBRSTDelete(
                strTblName=strTblName,
                strDBName=strDBName
            )
        if not blnResult:
            strErrMsg = 'DB Table: {}, Delete Data Fail!'.format(strTblName)
            strFuncName='EHTxtFile.fnTxtDataImp'
            return EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
            )

    # <PyCmt: DataCol Count Compare with Col Count>
    lstErrMsg=[]
    intRowRun=2
    intRecInsertCnt=0
    for strDataLine in strData.split(c_strNewLine):
        lstColValue=strDataLine.split(strSplitor)
        if blnDataUpd:
            # <PyCmt: c_strTxtImpParaDataUpd >
            # <PyCmt: Get ColNameKey and Counter ColValue>
            blnResult, strCrta = \
                EHDBApply.fnSQLCrtaJoin(
                    lstColName=lstColName,
                    lstColValue=lstColValue,
                    lstColNameKey=lstColNameKey,
                    blnColWithSysDft = blnColWithSysDft,
                    blnErrRtn = True
                )
            if not blnResult:
                lstErrMsg.append(strCrta)
            else:
                # <PyCmt: c_strTxtImpParaDataApd >
                lstColNameValueUpd=None
                if blnDataApd:
                    lstColNameValueUpd = \
                        [lstColNameValueUpd for lstColNameValueUpd in lstColName
                            if not lstColNameValueUpd in lstColNameKey]
                if blnColWithSysDft:
                    lstColNameRun, lstColValueRun = \
                        EHDBApply.fnDBColSysColNameAppend(
                            lstColName=lstColName,
                            lstColValue=lstColValue,
                            blnUqeNoApd=False
                        )
                else:
                    lstColNameRun, lstColValueRun = lstColName, lstColValue
                blnResult, strErrMsg, lstInsertID = \
                    EHDBApply.fnDBRSTUpdate(
                        strTblName=strTblName,
                        strCriteria=strCrta,
                        lstColName=lstColNameRun,
                        lstColValue=lstColValueRun,
                        strDBName=strDBName,
                        lstValueApdColColl=lstColNameValueUpd,
                        blnErrRtn=True,
                        intRowRef=intRowRun,
                        dateRun=dateRun
                    )
                if not blnResult: lstErrMsg.append(strErrMsg)
        else:
            if blnColWithSysDft:
                lstColNameRun, lstColValueRun = \
                    EHDBApply.fnDBColSysColNameAppend(
                        lstColName=lstColName,
                        lstColValue=lstColValue,
                        blnUqeNoApd=False
                    )
            else:
                lstColNameRun, lstColValueRun = lstColName, lstColValue

            blnResult, strErrMsg, lstInsertID = \
                EHDBApply.fnDBRSTInsert(
                    strTblName=strTblName,
                    strDBName=strDBName,
                    lstColName=lstColNameRun,
                    lstColValue=lstColValueRun,
                    lstColSchema=lstColSchema,
                    blnErrRtn=True,
                    intRowRef=intRowRun,
                )
            if not blnResult:
                strErrMsg=''.join(['Row: {}, '.format(intRowRun),strErrMsg ])
                lstErrMsg.append(strErrMsg)
            else:
                intRecInsertCnt += 1
        intRowRun+=1
    if len(lstErrMsg)>0:
        strErrMsg = (c_strNewLine + c_strTab).join(lstErrMsg)
        strFuncName='EHTxt.fnTxtDataImp'
        return \
            EHDebug.fnErrRtn(
                blnResult=False,
                strErrMsg=strErrMsg,
                strFuncName=strFuncName,
            )
    strMsg='Total Records: {}, DB Table: {}, '.format(intRecInsertCnt, strTblName) + \
        'Txt File: \"{}\" Data Import!'.format(strDataPath)
    strFuncName='EHTxt.fnTxtDataImp'
    EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True, strLogPath=strLogPath )
    return True, ''
def fnTxtFilePath(
    strFilePath:str='',
    blnFolderCreate:bool=False
)->str:
    # <PyFunc: >
    #   Desc: Check or Create FilePath and Return Txt File Path
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
    if len(strFilePath)==0:
            strFilePath = EHFile.fnFolderOS() + c_strTxtImpSymbFilePath + c_strTxtFileNameTmp
    strFilePath=EHFile.fnFileExist(strFileName=strFilePath, blnFileNameNew=True)
    strFolderPath = \
        EHFile.fnFolderChk(
            strFolderPath=EHFile.fnFolderParent(strFilePath=strFilePath),
            blnCreate=blnFolderCreate
        )
    if len(strFolderPath)==0: strFilePath = ''
    return strFilePath
# </PyRegion: Txt File Database Import Function>

# <PyRegion: Txt File Database Import Execution>
def fnTxtDBImpExec()->bool:
    strWinCap='Txt File Content Import to Database, Please Select Txt File for Import!'
    strFilePath = \
        EHFile.fnFilePicker(
            strWinCap=strWinCap,
            strWildcard="Text files (*.txt)|*.txt"
        )
    if strFilePath is None: return False

    blnResult:bool = fnTxtDBImpPreProc(strFilePath=strFilePath)
    return blnResult

def fnTxtDBImpTmpltCreate()->str:
    if not p_blnXWMode:
        strErrMsg = 'Txt File Import Only for Excel xlwings Mode!'
        strFuncName = 'EHTxt.fnTxtDBImpTmpltCreate'
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName,
            blnLog=True
        )
        return ''

    strWinCap='Excel Range to Txt File Import, Please Select Txt File for Create!'
    strFilePath=clsEHXW.p_strXWWBFilePath
    strFilePath=EHFile.fnFolderParent(strFilePath)
    strShtName=clsEHXW.p_shtAct.name

    strFilePath = \
        EHFile.fnFilePicker(
            strWinCap=strWinCap,
            strWildcard="Text files (*.txt)|*.txt",
            strDefaultDir = strFilePath,
            strFileName=strShtName,
            blnWrite = True
        )
    if strFilePath is None: return False
    fnTxtXLRngToTxt(
        rngRun=clsEHXW.p_objSel,
        strFilePath=strFilePath
    )
    strMsg = 'Txt File: \'{}\' Export Done!'.format(strFilePath)
    strFuncName = 'EHTxt.fnTxtDBImpTmpltCreate'
    EHMsg.fnMsgPrt(
        strMsg=strMsg,
        strFuncName=strFuncName,
        blnLog=True
    )
# </PyRegion: Txt File Database Import Execution>