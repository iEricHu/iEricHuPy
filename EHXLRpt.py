# EHXLRpt.py
# <PyDecl: Module Init, Setup DebugMode>
import pyodbc

import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

# <PyDev: >
#  1. SpecialCol Develop
#  2.
#  3.
#  4.
#  5.
#  6.
#  7.
#  8.
#  9.
# 10.
# </PyDev: >

import xlwings as xw
import xlwings.constants as xwcnst
from datetime import datetime

import EHPyFunc
import EHStr
import EHSymbolDef
import EHDate
import EHMsg
import EHRegExp
import EHDBApply
import EHXLObj
import EHXLApp
import EHXLSht
import EHXW

#<PyDecl: Symbol Config>
c_strNewLine = EHSymbolDef.c_strNewLine # '\n'

c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor # ';'
c_strShtCfgvalueSymbol = EHSymbolDef.c_strAttrValueSplitor # '::'
c_strShtCfgLineBreakSymbol=EHSymbolDef.c_strLineSplitor # '&;'
#</PyDecl: Symbol Config>

#<PyDecl: Report>
c_intReportGenButtonTopRow = 1
c_intReportGenButtonLeftCol = 2
c_strReportGenButtonNameGetData = "GetData"
c_strReportGenButtonNameUpload = "Upload"
c_strReportGenButtonNameDelete = "Delete"
c_strReportGenButtonFuncName = "fnExcelReportBtnCall"
c_intReportGenUploadStatusCol = 1
c_strReportGenUploadStatus = "UploadStatus"

c_strReportGenWaitUpload = "Wait Upload"
c_strReportGenWaitDelete = "Wait Delete"
c_strReportGenUploaded = "Uploaded"
c_strReportGenDeleted = "Deleted"
c_strReportGenUploadError = "Upload Error"
c_strReportGenDeleteError = "Delete Error"

c_lngColorNone = 16777215
c_lngColorLightBlueTitleRow = 16764057
c_lngColorLightLightBlue = 16772300
c_lngColorLightRed = 16764159
c_lngColorLightOrange = 10079487
c_lngColorLightYellow = 13434879
c_lngColorLightGreen = 13434828
c_lngColorLightBlue = 16764006

c_lngTitleRowColorDefault = c_lngColorLightBlueTitleRow
c_lngTitleRowColorLightLightBlue = c_lngColorLightLightBlue
c_lngTitleRowColorLightGreen = c_lngColorLightGreen
c_lngTitleRowColorHighLight = c_lngColorLightYellow

c_strTitleRowNewLineReplace = EHSymbolDef.c_strNewLine #'\n'

c_intSheetProtectPasswordLen = 10
#</PyDecl: Report>

#<PyDecl: ShtCfg>
c_strShtCfgTitleSymbol = EHSymbolDef.c_strValueAppendSymbol # '#'

c_dblShapeAltTextLenLimit = 5242870

c_blnShtCfgAttrAppend  = True
c_lngShtCfgShpTop  = 0
c_lngShtCfgShpLeft = 0
c_lngShtCfgShpWidth = 0
c_lngShtCfgShpHeight = 0
c_intShtCfgShapePlacement=xwcnst.Placement.xlFreeFloating
c_blnShtCfgShapeVisible=False
c_intShtCfgShapePrintObject=False
c_lngShtCfgShapeInteriorColor = xwcnst.RgbColor.rgbWhite
c_lngShtCfgShapeBorderColor = xwcnst.RgbColor.rgbWhite

c_strShtCfgTitle = "ShtCfg"
c_strShtCfgCmbBxName = "CmbBxName"
c_strShpCfgAltStrTitle = "<TitleSymbol><TitleStr><TitleSymbol>"
c_strShpCfgAltStrItem = "<AttrName><ValueSymbol><AttrValue>"

c_strShtCfgShtName='SheetName'
c_strShtCfgTitleRow='TitleRow'
c_strShtCfgTitleCol='TitleCol'
c_strShtCfgDelAvail='DeleteAvail'
c_strShtCfgUploadAvail='UploadAvail'
c_strShtCfgUploadStatusCol='UploadStatusCol'
c_strShtCfgUqeNoCol='UqeNoCol'
c_strShtCfgKeyColName='KeyColName'
c_lstShtCfgKeyColPos='KeyColPos'
c_strShtCfgValueColName='valueColName'
c_strShtCfgValueColPos='valueColPos'
c_strShtCfgColSchema="ColSchema"
c_strShtCfgShtProtect="SheetProtect"
c_strShtCfgShtProtectPassword="SheetProtectPassword"
c_strShtCfgShtDeactDel="SheetDeactDel"
c_strShtCfgShtDeactDelQry="SheetDeactDelQry"
c_strShtCfgAuthDept="AuthDept"
c_strShtCfgAuthGrade="AuthGrade"
c_strShtCfgClassName="ClassName"
c_strShtCfgSpecialColObjName="SpecialColObjName"
c_strShtCfgSpecialCol="SpecialCol"

c_strShtCfgAttrInitColl= \
    c_strShtCfgShtName + c_strAttrSplitor + \
    c_strShtCfgTitleRow + c_strAttrSplitor + \
    c_strShtCfgDelAvail + c_strAttrSplitor + \
    c_strShtCfgUploadAvail + c_strAttrSplitor + \
    c_strShtCfgUploadStatusCol + c_strAttrSplitor + \
    c_strShtCfgUqeNoCol + c_strAttrSplitor + \
    c_strShtCfgKeyColName + c_strAttrSplitor + \
    c_lstShtCfgKeyColPos + c_strAttrSplitor + \
    c_strShtCfgValueColName + c_strAttrSplitor + \
    c_strShtCfgValueColPos + c_strAttrSplitor + \
    c_strShtCfgColSchema + c_strAttrSplitor + \
    c_strShtCfgShtProtect + c_strAttrSplitor + \
    c_strShtCfgShtProtectPassword + c_strAttrSplitor + \
    c_strShtCfgShtDeactDel + c_strAttrSplitor + \
    c_strShtCfgShtDeactDelQry + c_strAttrSplitor + \
    c_strShtCfgAuthDept + c_strAttrSplitor + \
    c_strShtCfgAuthGrade + c_strAttrSplitor + \
    c_strShtCfgClassName + c_strAttrSplitor + \
    c_strShtCfgSpecialCol
#</PyDecl: ShtCfg>

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHXLRpt.py !')

p_blnXWMode=EHXW.p_blnXWMode
def clsEHXW()->object:
    return EHXW.EHXWClass()

# </PyDecl: RunTime>

def fnRptGen(
        strShtName,
        intTitleRow,
        lstTblColSchema,
        lstValue,
        lstColNameKey = None,
        lstColNameValue='',
        blnArrayTranspose=False,
        lstTitleColShow=None,
        intTitleCol=0,
        intColStart=1,
        strAftShtName='',
        lstColNotShow='',
        lstColNameCvrt='',
        blnDspZeros=False,
        blnAutoFilter=False,
        strGetDataFuncName='',
        strUploadFuncName='',
        intReportGenUploadStatusCol=0,
        intColUqeNo=-1,
        strDeleteFuncName='',
        blnSheetProtect=False,
        blnShtDeactDel=False,
        blnShtDeactDelQry=False,
        strAuthDept='*',
        intAuthGrade=0,
        dateRun=EHDate.c_dateDateZero ,
        intRowFilled=0,
        strSpecialCol=''
)->xw.Sheet:
    if dateRun==EHDate.c_dateDateZero: dateRun=datetime.now()

    clsEHXWRun=clsEHXW()
    shtRun, intTitleRow= \
        EHXLSht.fnShtDetect(
            strShtName=strShtName,
            wbRun=clsEHXWRun.p_wbXWWB,
            blnCleanUp=intRowFilled==0,
            strAftShtName=strAftShtName,
            blnDspZeros=blnDspZeros,
            intTitleRow=intTitleRow,
            intTitleCol=intTitleCol
        )
    blnUploadFunc = len(strUploadFuncName) > 0
    if blnUploadFunc and intReportGenUploadStatusCol == 0:
        intReportGenUploadStatusCol = c_intReportGenUploadStatusCol
    if intRowFilled==0:
        lstColFilled= \
            EHXLSht.fnRngTitleRowColFmt(
                shtRun = shtRun,
                lstColSchema = lstTblColSchema,
                lstColNameKey = lstColNameKey,
                lstColNameValue = lstColNameValue,
                intTitleRow=intTitleRow,
                intColUqeNo=intColUqeNo,
                intUpdStatusCol = intReportGenUploadStatusCol,
                lstColNameShow=lstTitleColShow,
                lstColNameNotShow=lstColNotShow,
                lstColNameCvrt=lstColNameCvrt,
                intColStart=intColStart
            )
    if not lstValue is None:
        intColRun = intColStart if intColStart > 0 else 1
        if blnUploadFunc and intColRun == c_intReportGenUploadStatusCol:
            if intColUqeNo < 0: intColRun = intColRun + 1
        intRowFill = intRowFilled + 2 if intRowFilled>0 else intTitleRow + 1
        intRowFilled= \
            fnRptArrayFill(
                shtRun=shtRun,
                rngTarget=shtRun.cells(intRowFill, intColRun),
                lstValue=lstValue,
                lstTblColSchema=lstTblColSchema,
                blnArrayTranspose=blnArrayTranspose,
                lstColNotShow=lstColNotShow
            )
        if intColUqeNo>0:
            rngRun= \
                shtRun.range(
                    shtRun.cells(intTitleRow+1, c_intReportGenUploadStatusCol), 
                    shtRun.cells(intRowFilled, c_intReportGenUploadStatusCol)
                )
            fnRptUpldStatOper(rngRun=rngRun)
    shtRun.cells(1,1).number_format ="MM/DD HH:MM"
    shtRun.cells(1, 1).value = dateRun
    if shtRun.cells(1, 1).value!=EHDate.fnNow():
        shtRun.cells(1, 1).api.Interior.Color=c_lngColorLightYellow

    fltBtnLeft=shtRun.cells(c_intReportGenButtonTopRow, c_intReportGenButtonLeftCol).left
    btnRun = \
        EHXLObj.fnXLObjShpDetect(
            shtRun=shtRun,
            strShpName=c_strReportGenButtonNameGetData,
            blnDel=len(strGetDataFuncName) == 0,
            fltBtnLeft = fltBtnLeft
        )
    if len(strGetDataFuncName) > 0: fltBtnLeft = btnRun.Left + btnRun.Width + 9

    btnRun = \
        EHXLObj.fnXLObjShpDetect(
            shtRun=shtRun,
            strShpName=c_strReportGenButtonNameDelete,
            blnDel=len(strDeleteFuncName) == 0,
            fltBtnLeft = fltBtnLeft
        )
    if len(strDeleteFuncName) > 0: fltBtnLeft = btnRun.Left + btnRun.Width + 9

    fnShtCfgShpInit(
        shtRun=shtRun,
        intShtCfgTitleRow=intTitleRow,
        intShtCfgTitleCol=intTitleCol,
        blnShtCfgDelAvail=len(strDeleteFuncName)>0,
        blnShtCfgUploadAvail=blnUploadFunc,
        intShtCfgUploadStatusCol=intReportGenUploadStatusCol,
        intShtCfgUqeNoCol=intColUqeNo,
        lstShtCfgColNameKey=lstColNameKey,
        lstShtCfgColNameValue=lstColNameValue,
        lstTblColSchema=lstTblColSchema,
        blnShtCfgShtProtect=blnSheetProtect,
        blnShtDeactDel=blnShtDeactDel,
        blnShtDeactDelQry=blnShtDeactDelQry,
        strAuthDept=strAuthDept,
        intAuthGrade=intAuthGrade,
        strSpecialCol=strSpecialCol
    )
    fnRptAutoFilter(shtRun=shtRun, intTitleRow=intTitleRow)
    #<PyDebug: p_blnSpecialColAvailable>

    if blnSheetProtect:
        strShtPwd=fnRptShtProtect(shtRun=shtRun)
        fnShtCfgOper(
            shtRun=shtRun,
            strAttrName=c_strShtCfgShtProtectPassword,
            strAttrValue=strShtPwd
        )
    return shtRun

def fnRptArrayFill(
        shtRun:xw.Sheet,
        rngTarget:xw.Range,
        lstValue:list,
        lstTblColSchema:list,
        blnArrayTranspose:bool=False,
        lstColNameFill:list='',
        lstColNotShow:list='',
        intColStart:int=1,
        strSplitor:str=c_strAttrSplitor
)->int | None:
    import EHArray

    if lstTblColSchema is None: return None
    if lstValue is None: return None
    if blnArrayTranspose:
        lstValue=\
            EHArray.fnArrayTranspose(lstRun=lstValue)
    if intColStart==0: intColStart=1

    intRowRun=rngTarget.row
    if len(lstColNameFill) > 0 or len(lstColNotShow) > 0:
        lstTitleRow=lstTblColSchema[EHDBApply.c_intTblColSchemaColName]
        lstTitleRow=\
            EHArray.fnArrayFilter(
                lstSource = lstTitleRow,
                lstFilter = lstColNameFill if len(lstColNameFill)>0 else lstColNotShow,
                blnInclude=len(lstColNameFill)>0,
                strSplitor = strSplitor
            )
        intRun = 0
        intColRun = intColStart
        for lstValueRow in lstValue:
            for strValue in lstValueRow:
                strColNameRun = lstTblColSchema[EHDBApply.c_intTblColSchemaColName][intRun]
                if not strColNameRun in lstColNotShow:
                    shtRun.cells(intRowRun, intColRun).value = strValue
                intColRun += 1
            intRun += 1
            intRowRun += 1
    else:
        intArrayDim=EHArray.fnArrayDimGet(lstValue)
        if intArrayDim==1:
            shtRun.cells(intRowRun, intColStart).resize(len(lstValue)).value = lstValue
        elif intArrayDim==2:
            shtRun.cells(intRowRun, intColStart).resize(len(lstValue), len(lstValue[0])).value=lstValue
        else:
            strErrMsg = 'lstValue Dim Over 2! lstValue: {}'.format(lstValue)
            strFuncName = 'EHXLRpt.fnRptArrayFill'
            EHMsg.fnMsgPrt(
                strMsg=strErrMsg,
                strFuncName=strFuncName,
                blnLog=True
            )
        intRowRun=intRowRun+len(lstValue)
    return intRowRun-1

def fnRptUpldStatOper(
        rngRun,
        strStatusRun=''
)->bool:
    rngUpldStat=EHXLSht.fnRngRowGet(rngRun=rngRun , intCol= c_intReportGenUploadStatusCol)
    for rngRun in rngUpldStat:
        if len(rngRun.value)==0:
            rngRun.value=strStatusRun
            intStrLen1 = len(strStatusRun)
        elif rngRun.value.isnumeric():
            rngRun.value=c_strReportGenUqeNo+rngRun.value
            intStrLen1 = 0
            intStrLen2 = len(rngRun.value)
        elif len(strStatusRun)==0:
            intStrLen1 = 0
            intStrLen2 = len(rngRun.value)
        elif c_strAttrSplitor in rngRun.value:
            intStrLen2 = len(rngRun.value) + 1
            rngRun.value = strStatusRun + c_strAttrSplitor + rngRun.value.split(c_strAttrSplitor)[1]
            intStrLen1 = len(strStatusRun)
        elif rngRun.value[:len(c_strReportGenUqeNo)]==c_strReportGenUqeNo:
            intStrLen2 = len(rngRun.value) + 1
            rngRun.value = strStatusRun + c_strAttrSplitor + rngRun.value
            intStrLen1 = len(strStatusRun)
        elif rngRun.value==strStatusRun:
            intStrLen1=len(rngRun.value)
        elif rngRun.value!=strStatusRun:
            rngRun.value = strStatusRun
            intStrLen1 = len(strStatusRun)
        else:
            strErrMsg='ChgCell Out Of Upload Status Rule Control!'
            strFuncName='EHXLRpt.fnRptUpldStatOper'
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName)
            return False
        return True

def fnRptShtProtect(
        shtRun,
        blnUnprotect=False,
        strPassword='',
        blnPwdRnd=False,
        blnProtectDrawObj=True,
        blnProtectContents=True,
        blnProtectScenarios=True
)->str:
    if not blnUnprotect and not shtRun.api.ProtectContents:
        if blnPwdRnd: strPassword = EHStr.fnChrRnd(intDigi=c_intSheetProtectPasswordLen)
        shtRun.api.Protect(
            Password=strPassword,
            DrawingObjects=blnProtectDrawObj,
            Contents=blnProtectContents,
            Scenarios=blnProtectScenarios
        )
        return strPassword
    elif blnUnprotect and sht.api.ProtectContents:
        try:
            shtRun.api.Unprotect(Password=strPassword)
            return strPassword
        except Exception as Err:
            strErrMsg='Sheet: {} Unprotect Fail!' + \
              c_strNewLine + 'Err:{}'.\
                format(shtRun.name, Err)
            strFuncName='EHXLRpt.fnRptShtProtect'
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName)
            return None

def fnRptAutoFilter(
        shtRun,
        intTitleRow=0,
        intColEnd=0,
        intRowDetectCol=0,
        blnAutoFilterCancel=False
)->bool:
    if intTitleRow==0: intTitleRow=EHXLSht.fnRngTitleRowFind(shtRun=shtRun)
    if intRowDetectCol==0:
        rngUsed=shtRun.used_range
        intRowEnd=rngUsed.row+rngUsed.rows.count
    else:
        intRowEnd=shtRun.cells(EHXLSht.fnShtRowsCount(), intRowDetectCol).end('up').Row
    if intColEnd==0: intColEnd=shtRun.cells(intTitleRow, EHXLSht.fnShtColsCount()).end('left').column

    if shtRun.api.AutoFilterMode:
        if blnAutoFilterCancel:
            shtRun.api.AutoFilterMode=False
        elif shtRun.api.AutoFilter.Range.Rows(1).Address!= \
            shtRun.range(shtRun.cells(intTitleRow, 1), shtRun.cells(intTitleRow, intColEnd)).address:
            shtRun.api.AutoFilterMode=False
    if not blnAutoFilterCancel:
        shtRun.range(
            shtRun.cells(intTitleRow, 1),
            shtRun.cells(intRowEnd, intColEnd)
        ).api.AutoFilter(Field=1, Criteria1='', VisibleDropDown=True)
        shtRun.api.ShowAllData()
    return True

def fnRptFilterOper(
        shtRun,
        lstFilterColArray,
        lstFilterValueArray=None,
        intTitleRow=0,
        intRowDetectCol=0,
        blnFilterModeOff=False,
        blnShowAllData=False
)->bool:
    if lstFilterValueArray is None:blnShowAllData=True
    if shtRun.api.AutoFilter is None:
        fnRptAutoFilter(
            shtRun=shtRun,
            intTitleRow=intTitleRow,
            intRowDetectCol=intRowDetectCol
        )
        return True

    # rngFilterTitle=\
    #     EHXLSht.fnRngRowGet( \
    #         rngRun=shtRun.api.AutoFilter.Range, \
    #         intRow=shtRun.api.AutoFilter.Range.Row \
    #     )
    lstFilterCol=EHXLSht.fnRngColLstGet(shtRun.api.AutoFilter.Range)
    intRun=0
    for intColRun in lstFilterCol:
        if intColRun in lstFilterColArray:
            shtRun.api.AutoFilter(
                Field=intRun+1,
                Criteria1=lstFilterValueArray[intRun],
                VisibleDropDown=True
            )
        intRun+=1

def fnRptSortAdd(
        shtRun,
        lstSortCol,
        intKeyCol=0,
        intTitleRow=0
):
    lstSortColOrig=[]
    lstSortOrdOrig=[]
    lstSortCustOrdOrig=[]
    for objSortField in shtRun.api.Sort.SortFields:
        lstSortColOrig.append(objSortField.Key.Column)
        lstSortOrdOrig.append(objSortField.Order)
        lstSortCustOrdOrig.append(objSortField.CustomOrder)

    blnResult = shtRun.api.Sort.SortFields.Clear
    if intTitleRow==0: intTitleRow=EHXLSht.fnRngTitleRowFind(shtRun=shtRun)
    intRowEnd=EHXLSht.fnShtEndRow(shtRun=shtRun, intColDect=intKeyCol)
    intColEnd=EHXLSht.fnShtEndCol(shtRun)
    for intSortCol in lstSortCol:
        rngSortRun = \
            shtRun.api.Range(
                shtRun.api.Cells(intTitleRow+1, intSortCol),
                shtRun.api.Cells(intRowEnd, intSortCol)
            )
        blnSortColOld=intSortCol in lstSortColOrig
        intSortOrdRun=0
        intSortCustOrdOrig=None
        if blnSortColOld:
            intSortOrdOrig=lstSortOrdOrig[lstSortColOrig.index(intSortCol)]
            if intSortOrdOrig==xwcnst.SortOrder.xlAscending:
                intSortOrdRun=xwcnst.SortOrder.xlDescending
            else:
                intSortOrdRun = xwcnst.SortOrder.xlAscending
            intSortCustOrdOrig = lstSortCustOrdOrig[lstSortColOrig.index(intSortCol)]
        else:
            intSortOrdRun = xwcnst.SortOrder.xlAscending

        shtRun.api.Sort.SortFields.Add(
            Key=rngSortRun,
            SortOn=xwcnst.SortOn.xlSortOnValues,
            Order=intSortOrdRun
        )
    rngSort=shtRun.api.Range(shtRun.api.Cells(intTitleRow, 1), shtRun.api.Cells(intRowEnd, intColEnd))
    shtRun.api.Sort.SetRange(rngSort)
    shtRun.api.Sort.Header=xwcnst.YesNoGuess.xlYes
    shtRun.api.Sort.MatchCase= False
    shtRun.api.Sort.Orientation = xwcnst.Constants.xlTopToBottom
    shtRun.api.Sort.Apply()
# </PyRegion: EHXLRpt>

#<PyRegion: ShtCfg>
def fnShtCfgShpInit(
        shtRun,
        intShtCfgTitleRow,
        intShtCfgTitleCol = 0,
        blnShtCfgDelAvail = False,
        blnShtCfgUploadAvail = False,
        intShtCfgUploadStatusCol = 1,
        intShtCfgUqeNoCol = -1,
        lstShtCfgColNameKey = '',
        lstShtCfgColPosKey = '',
        lstShtCfgColNameValue = '',
        lstShtCfgColPosValue = '',
        lstTblColSchema = None,
        blnShtCfgShtProtect = False,
        strSheetProtectPassword = '',
        blnShtDeactDel = False,
        blnShtDeactDelQry = True,
        strAuthDept  = '*',
        intAuthGrade = 0,
        strSpecialCol = '',
        strFuncName = '',
        strSplitor = c_strAttrSplitor
)->xw.Shape:
    shpShtCfg = EHXLObj.fnXLObjShpDetect(shtRun=shtRun, strShpName=c_strShtCfgTitle)
    strShpCfgAltStrTitleRun = c_strShpCfgAltStrTitle
    strShpCfgAltStrTitleRun = strShpCfgAltStrTitleRun.replace('<TitleSymbol>', c_strShtCfgTitleSymbol)
    strShpCfgAltStrTitleRun = strShpCfgAltStrTitleRun.replace('<TitleStr>', c_strShtCfgTitle)
    strShpCfgAltStrTitleRun = strShpCfgAltStrTitleRun.replace('<LineBreak>', c_strShtCfgLineBreakSymbol)

    if not lstShtCfgColNameKey is None:
        lstShtCfgColPosKey = \
            EHXLSht.fnRngColPosFindLst(
                shtRun=shtRun,
                lstColName=lstShtCfgColNameKey,
                intRowRun=intShtCfgTitleRow
            )

    if len(lstShtCfgColNameValue)>0 and len(lstShtCfgColPosValue)==0:
        lstShtCfgColPosValue = \
            EHXLSht.fnRngColPosFindLst(
                shtRun=shtRun,
                lstColName=lstShtCfgColNameValue,
                intRowRun=intShtCfgTitleRow
            )

    lstShtCfgAttr:list=[]
    lstColNumFmt:list=[]
    for strAttrRun in c_strShtCfgAttrInitColl.split(c_strAttrSplitor):
        blnFillValue = True
        strAttrValue = ''
        if len(strAttrRun)==0:
            pass
        else:
            if strAttrRun==c_strShtCfgShtName:
                strAttrValue = shtRun.name
            elif strAttrRun==c_strShtCfgTitleRow:
                strAttrValue = intShtCfgTitleRow
            elif strAttrRun == c_strShtCfgTitleCol:
                strAttrValue = intShtCfgTitleCol
            elif strAttrRun==c_strShtCfgDelAvail:
                strAttrValue = str(blnShtCfgDelAvail)
            elif strAttrRun==c_strShtCfgUploadAvail:
                strAttrValue = blnShtCfgUploadAvail
            elif strAttrRun==c_strShtCfgUploadStatusCol:
                strAttrValue = intShtCfgUploadStatusCol
            elif strAttrRun==c_strShtCfgUqeNoCol:
                strAttrValue = intShtCfgUqeNoCol
            elif strAttrRun==c_strShtCfgKeyColName and \
                not lstShtCfgColNameKey is None:
                strAttrValue = strSplitor.join(lstShtCfgColNameKey)
            elif strAttrRun==c_lstShtCfgKeyColPos and \
                not lstShtCfgColPosKey is None:
                strAttrValue = strSplitor.join(lstShtCfgColPosKey)
            elif strAttrRun==c_strShtCfgValueColName and \
                not lstShtCfgColNameValue is None:
                strAttrValue = strSplitor.join(lstShtCfgColNameValue)
            elif strAttrRun==c_strShtCfgValueColPos and \
                not lstShtCfgColPosValue is None:
                strAttrValue = strSplitor.join(lstShtCfgColPosValue)
            elif strAttrRun==c_strShtCfgColSchema and \
                not lstTblColSchema is None:
                for intRow in range(len(lstTblColSchema[0])):
                    lstColNumFmt.append(lstTblColSchema[intRow][EHDBApply.c_intTblColSchemaColNumFmt])
                strAttrValue=strSplitor.join(lstColNumFmt)
            elif strAttrRun==c_strShtCfgShtProtect:
                strAttrValue = str(blnShtCfgShtProtect)
            elif strAttrRun==c_strShtCfgShtProtectPassword:
                strAttrValue = strSheetProtectPassword
            elif strAttrRun==c_strShtCfgShtDeactDel:
                strAttrValue = str(blnShtDeactDel)
            elif strAttrRun==c_strShtCfgShtDeactDelQry:
                strAttrValue = str(blnShtDeactDelQry)
            elif strAttrRun==c_strShtCfgAuthDept:
                strAttrValue = strAuthDept
            elif strAttrRun==c_strShtCfgAuthGrade:
                strAttrValue = str(intAuthGrade)
            elif strAttrRun==c_strShtCfgClassName:
                strAttrValue = strFuncName
            elif strAttrRun==c_strShtCfgSpecialCol:
                blnFillValue = len(strSpecialCol) > 0
                strAttrValue = strSpecialCol
        if blnFillValue:
            strShtCfgAttr = c_strShpCfgAltStrItem
            strShtCfgAttr = strShtCfgAttr.replace('<AttrName>', strAttrRun)
            strShtCfgAttr = strShtCfgAttr.replace('<ValueSymbol>', c_strShtCfgvalueSymbol)
            strShtCfgAttr = strShtCfgAttr.replace('<AttrValue>', str(strAttrValue))
            lstShtCfgAttr.append(strShtCfgAttr)

    strShtCfgAttrTitle = c_strShpCfgAltStrTitle
    strShtCfgAttrTitle = strShtCfgAttrTitle.replace('<TitleSymbol>', c_strShtCfgTitleSymbol)
    strShtCfgAttrTitle = strShtCfgAttrTitle.replace('<TitleStr>', c_strShtCfgTitle)

    strShtCfgAttr=c_strShtCfgLineBreakSymbol.join([strShtCfgAttrTitle, c_strShtCfgLineBreakSymbol.join(lstShtCfgAttr)])

    shpRun= \
        EHXLObj.XLObjShpCreate(
            shtRun=shtRun,
            strShpName=c_strShtCfgTitle,
            lngShpTop=c_lngShtCfgShpTop,
            lngShpLeft=c_lngShtCfgShpLeft,
            lngShpWidth=c_lngShtCfgShpWidth,
            lngShpHeight=c_lngShtCfgShpHeight,
            strShpStr=strShtCfgAttr,
            xlShpPlacement=c_intShtCfgShapePlacement,
            blnShpVisible=c_blnShtCfgShapeVisible,
            blnShpPrintObj=c_intShtCfgShapePrintObject,
            lngShpInteriorColor=c_lngShtCfgShapeInteriorColor,
            lngShpBorderColor=c_lngShtCfgShapeBorderColor
        )
    return shpRun

def fnShtCfgOper(
        shtRun,
        strAttrName,
        strAttrValue=''
)->bool:
    shpShtCfg=EHXLObj.fnXLObjShpDetect(shtRun=shtRun, strShpName=c_strShtCfgTitle)
    if shpShtCfg is None: return 0
    blnShpCfgWrite=len(strAttrValue)>0

    strShtCfg=shpShtCfg.api.AlternativeText
    lstShtCfg=[]
    intShtCfg=0
    for strCfgItem in strShtCfg.split(c_strShtCfgLineBreakSymbol):
        if len(strCfgItem)==0:
            pass
        elif blnShpCfgWrite:
            if strCfgItem.split(c_strShtCfgvalueSymbol)[0]==strAttrName:
                lstShtCfg.append(c_strShtCfgvalueSymbol.join([strAttrName, strAttrValue]))
                blnShtCfgFound = True
            else:
                lstShtCfg.append(strCfgItem)
        elif strCfgItem.split(c_strShtCfgvalueSymbol)[0]==strAttrName:
            return strCfgItem.split(c_strShtCfgvalueSymbol)[1]
            blnShtCfgFound = True
            break

    if blnShpCfgWrite:
        if not c_blnShtCfgAttrAppend:
            strErrMsg='ShtCfg Attr Append Not Allow!'
            strFuncName='EHXLRpt.fnShtCfgOper'
            strTitle='ShtCfg Append Error'
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, strTitle=strTitle, blnLog=True)
            return False
        elif not blnShtCfgFound:
            lstShtCfg.append(c_strShtCfgvalueSymbol.join([strAttrName, strAttrValue]))
        strShtCfgColl=c_strShtCfgLineBreakSymbol.join(lstShtCfg)

        if len(strShtCfgColl)>c_dblShapeAltTextLenLimit:
            strErrMsg='AltText Len: {} exceed AltTextLen Limit!'.format(len(strShtCfgColl))
            strFuncName='EHXLRpt.fnShtCfgOper'
            strTitle='AlTextLen Error'
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, strTitle=strTitle, blnLog=True)
            return False
        else:
            pass
        shpShtCfg.api.AlternativeText = strShtCfgColl
        return True

def fnShtCfgChk(
        shtRun,
        blnShpReset=True,
        blnShpInvalidDel=False
)->bool:
    blnResult = True
    shpShtCfg=EHXLObj.fnXLObjShpDetect(shtRun=shtRun, strShpName=c_strShtCfgTitle)
    if shpShtCfg is None:
        strErrMsg='ShtCfg Object not found!'
        strFuncName='EHXLRpt.fnShtCfgChk'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        blnResult=False
        return blnResult

    lstErrMsg=[]    
    strErrMsg=fnShtCfgStrChk(shpShtCfg.api.AlternativeText)
    if shpShtCfg.api.Width!=c_lngShtCfgShpWidth:
        strErrMsg = 'ShtCfg Width Error!'
        if blnShpReset:
            shpShtCfg.Width=c_lngShtCfgShpWidth
        else:
            lstErrMsg.append(strErrMsg)
            blnResult = False
    if shpShtCfg.api.Width!=c_lngShtCfgShpHeight:
        strErrMsg = 'ShtCfg Height Error!'
        if blnShpReset:
            shpShtCfg.Height = c_lngShtCfgShpHeight
        else:
            lstErrMsg.append(strErrMsg)
            blnResult = False
    if shpShtCfg.api.Placement!=c_intShtCfgShapePlacement :
        strErrMsg = 'ShtCfg Placement Error!'
        if blnShpReset:
            shpShtCfg.Placement=c_intShtCfgShapePlacement
        else:
            lstErrMsg.append(strErrMsg)
            blnResult = False
    if shpShtCfg.api.Visible!=c_blnShtCfgShapeVisible :
        strErrMsg = 'ShtCfg Visible Error!'
        if blnShpReset:
            shpShtCfg.Visible=c_blnShtCfgShapeVisible
        else:
            lstErrMsg.append(strErrMsg)
            blnResult = False
    if shpShtCfg.api.DrawingObject.PrintObject!=c_intShtCfgShapePrintObject :
        strErrMsg =  'ShtCfg PrintObj Error!'
        if blnShpReset:
            shpShtCfg.DrawingObject.PrintObject=c_intShtCfgShapePrintObject
        else:
            lstErrMsg.append(strErrMsg)
            blnResult = False
    if not blnResult:
        strErrMsg=c_strNewLine.join(lstErrMsg)
        strFuncName='EHXLRpt.fnShtCfgChk'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
    return blnResult

def fnShtCfgStrChk(
        strRun,
        strSplitor=c_strShtCfgLineBreakSymbol
)->str:
    lstErrMsg=[]
    intLine=0
    for strItemChk in strRun.split(c_strShtCfgLineBreakSymbol):
        strErrMsg=''
        if len(strItemChk)==0:
            strErrMsg='ShtCfg Line: {} Error!'.format(intLine)
        elif c_strShtCfgvalueSymbol+c_strShtCfgLineBreakSymbol in strItemChk:
            pass
        elif EHRegExp.fnREMatch( strRun=strItemChkk, strPattern='*'+c_strShtCfgvalueSymbol+c_strShtCfgLineBreakSymbol):
            pass
        else:
            strErrMsg = 'ShtCfg Line: {} Error!'.format(intLine)

        if len(strErrMsg)>0: lstErrMsg.append(strErrMsg)
        intLine+=1
    return c_strNewLine.join(lstErrMsg)
#</PyRegion: ShtCfg>
# <PyRegion: EHXLRpt From SQL>
def fnRptSQLTbl(
    strShtName:str,
    intTitleRow:int,
    strTblName:str,
    strSectName:str='',
    strDBName:str='',
    strSQL:str=''
)->xw.Book:
    if len(strTblName)==0 and len(strSQL)==0:
        strErrMsg = 'Both strTblName and strSQL Empty!'
        strFuncName = 'EHXLRpt.fnRptSQLTbl'
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName,
            blnLog=True
        )
        return None

    if len(strSQL)==0:
        strSQL= \
            'SELECT ' + \
                '* ' + \
            'FROM ' + \
                '<TblName>'
        strSQLRun=strSQL
        strSQLRun=strSQLRun.replace('<TblName>', strTblName)
    else:
        strSQLRun=strSQL

    blnResult, strErrMsg, lstColSchema, lstColName= \
        EHDBApply.fnDBColSchemaGet(
            strTblName=strTblName,
            strDBName = strDBName,
            blnErrRtn = True
        )
    if not blnResult:
        strFuncName = 'EHXLRpt.fnRptSQL'
        EHMsg.fnMsgPrt(
            strMsg=strErrMsg,
            strFuncName=strFuncName,
            blnLog=True
        )

    EHXLSht.fnXLAppReset(blnDisFunc=True)
    blnResult, strErrMsg, lstTblContent=\
        EHDBApply.fnDBRSTValueGet(
            strSQLRun=strSQLRun,
            strSectName=strSectName,
            strDBName=strDBName
        )
    if not blnResult: return None

    fnRptGen(
        strShtName=strShtName,
        intTitleRow = intTitleRow,
        lstTblColSchema=lstColSchema,
        lstValue = lstTblContent
    )
    EHXLSht.fnXLAppReset()