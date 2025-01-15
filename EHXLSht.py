# EHXLSht.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import xlwings as xw
import xlwings.constants as xwcnst

import EHSymbolDef
import EHMsg

import EHXW
import EHRegExp
import EHXLRpt
import EHDBApply
import EHPyFunc

#Range
#clsEHXW.p_wbXWWB.app.selection
#clsEHXW.p_shtAct.api.Columns(1)
#clsEHXW.p_objApp.selection.api.EntireRow.SpecialCells(xwcnst.CellType.xlCellTypeConstants).EntireRow

#Range Info
#clsEHXW.p_shtAct.cells.api.SpecialCells(11).Address
#intTitleRow=shtRun.cells(1, intColMax).end('down').Row
#intColMax = clsEHXW.p_shtAct.cells.api.SpecialCells(11).Column

#Range Action
#clsEHXW.p_shtAct.api.Rows(10).Select()
#FindArea=clsEHXW.p_shtAct.api.Columns(5).Find('abc').Address
#clsEHXW.p_shtAct.activate()
#clsEHXW.p_shtAct.cells(1,1).api.Select()
#clsEHXW.p_shtAct.cells(1, 1).value = '\n'


c_strFontNameDefault='Times New Roman'
c_intFontSizeDefault=10

c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor
c_strAttrValueSplitor=EHSymbolDef.c_strAttrValueSplitor
c_strValueAppendSymbol=EHSymbolDef.c_strValueAppendSymbol

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHXLSht.py !')
# </PyDecl: RunTime>

# <PyRegion: Excel WorkSheet Info>
def fnEHXWClass()->object:
    return EHXW.EHXWClass()
def fnShtRowsCount()->int:
    # <PyFunc: >
    #   Desc: Get Excel WorkSheet Rows Count[1048576]
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    clsEHXWRun=fnEHXWClass()
    return clsEHXWRun.p_shtAct.cells.rows.count

def fnShtColsCount()->int:
    # <PyFunc: >
    #   Desc: Get Excel WorkSheet Cols Count[16384]
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    clsEHXWRun = fnEHXWClass()
    return clsEHXWRun.p_shtAct.cells.columns.count

def fnShtEndRow(shtRun, intColDect=0):
    # <PyFunc: >
    #   Desc: get Excel WorkSheet Last Cell Row
    #   Use By:
    #   Noticed:
    #       if intColDect>0, it will find the last row of data in the column
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    if intColDect>0:
        return shtRun.cells(fnShtRowsCount(),intColDect).end('up').row
    else:
        return fnRngLastCell(shtRun=shtRun).Row

def fnShtEndCol(shtRun):
    # <PyFunc: >
    #   Desc: Get Excel WorkSheet Last Cell Column
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    return fnRngLastCell(shtRun=shtRun).Column
# </PyRegion: Excel WorkSheet Info>
# <PyRegion: Excel WorkSheet Range Object>
def fnRngRowsAll(
    shtRun:xw.Sheet = None
)->xw.RangeRows :
    if shtRun is None:
        clsEHXWRun = fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct
    return shtRun.cells.rows

def fnRngColsAll(
    shtRun:xw.Sheet = None
)->xw.RangeColumns  :
    if shtRun is None:
        clsEHXWRun = fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct
    return shtRun.cells.columns

def fnRngGet(
    intRowStart:int=None,
    intRowEnd:int=None,
    intColStart:int=None,
    intColEnd:int=None,
    shtRun:xw.Sheet = None
)->xw.Range:
    # <PyCmt: xlwings range method will be>
    # Range Type
    # 1. shtRun.range(10,10): Row:10, Col:10
    # 2. shtRun.range('10:20'): Row: from 10 to 20
    # 3. shrRun.range('A:C'): Col: A to C
    # 4. shtRun.range('10:20,3:5'): Row: from 10 to 20 and 3 to 5
    # 4. shtRun.range('10:20,3:5,A:C,h:i'): Row: from 10 to 20, 3 to 5, Col:A to C, H to I
    # Cells Type
    # 1. shtRun.cells[9, 9]: Row:10, Col:10 (start with 0)
    # 2. shtRun.cells[0:10, 20:30]:
    #       Row: 1 to 10, Col: 21 to 30
    if shtRun is None:
        clsEHXWRun = fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct
    return shtRun.cells[intRowStart:intRowEnd, intColStart:intColEnd]
def fnRngCurReg()->xw.Range:
    # <PyFunc: >
    #   Desc: Get Excel Active Selection Current Region
    #   Use By:
    #   Noticed: if Selected Blank Cell, it will find next non-blank cell
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    clsEHXWRun = fnEHXWClass()
    rngRun = clsEHXWRun.p_objApp.selection.current_region
    if rngRun.count == 1 and len(rngRun.value)==0 :
        rngRun = \
            fnRngFind(
                strFind='*',
                shtRun=clsEHXW.p_shtAct,
                rngAfter=rngRun
            )
        rngRun = fnXWTypeCvrt(rngRun)
    return rngRun

def fnRngLastCell(shtRun=None)->xw.Range:
    # <PyFunc: >
    #   Desc: Get Excel WorkSheet Last Cell
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    if shtRun is None:
        clsEHXWRun=fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct
    rngRun=shtRun.cells.api.SpecialCells(xwcnst.CellType.xlCellTypeLastCell)
    rngRun = fnXWTypeCvrt(rngRun)
    return rngRun

def fnRngFirstCell(shtRun=None)->xw.Range:
    # <PyFunc: >
    #   Desc: get Excel WorkSheet First Non-Blank Cell via 'fnRngFind'
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    if shtRun is None:
        clsEHXWRun = fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct
    if len(shtRun.range(1,1).value)>0 :
        rngRun=shtRun.range(1,1)
    else:
        rngRun = \
            fnRngFind(
                strFind='*',
                shtRun=shtRun,
                rngAfter=shtRun.range(1,1)
            )
    rngRun = fnXWTypeCvrt(rngRun)
    return rngRun

def fnRngSeltGet()->xw.Range:
    # <PyFunc: >
    #   Desc: Get Excel Selection [Range; OLEObj; Chart; Picture]
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    clsEHXWRun=fnEHXWClass()
    return clsEHXWRun.p_objApp.selection

def fnRngSeltRng()->xw.Range:
    # <PyFunc: >
    #   Desc: Get Excel Selection, and Convert to Range
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #   Return:
    # </PyFunc: >
    clsEHXWRun=fnEHXWClass()
    rngSelt=clsEHXWRun.p_objApp.selection
    if isinstance(rngSelt, xw.Range):
        pass
    elif isinstance(rngSelt, (xw.Shape, xw.Picture)):
        rngSelt=rngSelt.TopLeftCell
    elif isinstance(rngSelt, xw.Chart):
        rngSelt = None
    else:
        rngSelt = None
    return rngSelt

def fnRngToRight(rngRun:xw.Range)->xw.Range:
    return rngRun.end('right')

def fnXWTypeCvrt(rngRun)->xw.Range:
    # <PyFunc: >
    #   Desc: Convert 'win32com.gen_py.Microsoft Excel Range' or 'xlwings._xlwindows.COMRetryObjectWrapper' to XW Range
    #   Use By:
    #   Noticed: rngRun Type will be
    #       1. class 'win32com.gen_py.00020813-0000-0000-C000-000000000046x0x1x9.Range'
    #       2. class 'xlwings._xlwindows.COMRetryObjectWrapper'
    #   Parameter:
    #      rngRun= User Input Range
    #   Option:
    #   Return: class 'xlwings.main.Range'
    # </PyFunc: >
    if not isinstance(rngRun, xw.Range):
        # <PyCmt: Check type(rngRun), type(rngRun).__name__, vars(rngRun) >
        import EHPyFunc
        if EHPyFunc.fnTypeName(rngRun) == 'Range':
            rngRun = xw.Range(rngRun.Address)
    return rngRun
# </PyRegion: Excel WorkSheet Range Object>

# <PyRegion: Sheet Range Find>
def fnRngFind(
    strFind,
    shtRun = None,
    rngAfter = None,
    intRowFind = 0,
    intColFind = 0 ,
    blnPartial=False
)->xw.Range:
    # <PyFunc: >
    #   Desc: Find Excel WorkSheet Cells by 'strFind'
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strFind= Find String
    #   Option:
    #      shtRun= WorkSheet Object
    #      rngAfter= Start Search Range
    #      intRowFind= User Indicated Row
    #      intColFind= User Indicated Column    
    #   Return: 
    # </PyFunc: >
    if shtRun is None:
        clsEHXWRun = fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct

    if intRowFind>0:
        rngTrg=shtRun.rows(intRowFind)
        xlSrchOrd = xwcnst.SearchOrder.xlByColumns
    elif intColFind>0:
        rngTrg=shtRun.columns(intColFind)
        xlSrchOrd = xwcnst.SearchOrder.xlByRows
    else:
        rngTrg=shtRun.cells
        xlSrchOrd = xwcnst.SearchOrder.xlByColumns

    if not rngAfter is None:
        if rngAfter.count>1: raise RuntimeError('rngAfter.count>1')
        rngAfter=rngAfter.api

    if blnPartial:
        xlLookAt = xwcnst.LookAt.xlPart
    else:
        xlLookAt = xwcnst.LookAt.xlWhole

    rngRun= \
        rngTrg.api.Find(
            What=strFind,
            After=rngAfter,
            LookIn=xwcnst.FindLookIn.xlValues,
            LookAt=xlLookAt,
            SearchOrder=xlSrchOrd,
            SearchDirection=xwcnst.SearchDirection.xlNext,
            MatchCase=False,
            MatchByte=False
        )
    rngRun = fnXWTypeCvrt(rngRun)
    return rngRun

def fnRngTitleRowFind(shtRun)->int:
    # <PyFunc: >
    #   Desc: Get Excel WorkSheet Title Row from ShtCfg object or LastCol top1stCell
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      shtRun= WorkSheet Object
    #   Option:
    #   Return: 
    # </PyFunc: >
    intTitleRow=\
        EHXLRpt.fnShtCfgOper(
            shtRun=shtRun,
            strAttrName=EHXLRpt.c_strShtCfgTitleRow,
        )
    if intTitleRow == 0:
        intColEnd=fnShtEndCol(shtRun=shtRun)
        if len(shtRun.cells(1, intColEnd))>0:
            intTitleRow=1
        else:
            intTitleRow=shtRun.cells(1, intColEnd).end('down').row
    if intTitleRow == fnShtRowsCount():
        print('fnRngTitleRowFind.fnRngFind')
        rngRun = \
            fnRngFind(
                strFind='*',
                shtRun=shtRun,
                rngAfter=shtRun.cells(1,1),
                blnPartial=True
            )
        if not rngFind is None: intTitleRow = rngRun.Row
    return intTitleRow

def fnRngTitleRowColFind(
        strColName,
        shtRun=None,
        intTitleRow=0
)->int:
    # <PyFunc: >
    #   Desc: Find ColName in Excel WorkSheet Title Row
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strColName= User Indicated Column Name
    #   Option:
    #      shtRun= WorkSheet Object
    #      intTitleRow= User Indicated Title Row
    #   Return: 
    # </PyFunc: >
    if shtRun is None:
        clsEHXWRun = fnEHXWClass()
        shtRun=clsEHXWRun.p_shtAct
    if intTitleRow==0: intTitleRow=fnRngTitleRowFind(shtRun=shtRun)
    if intTitleRow==0: return None

    rngRun = \
        fnRngFind(
            strFind=strColName,
            shtRun=shtRun,
            rngAfter=shtRun.cells(1,1),
            intRowFind=intTitleRow
        )
    return rngRun.Column

def fnRngColPosFindLst(
        shtRun,
        lstColName,
        intRowRun = 0,
)->list:
    # <PyFunc: >
    #   Desc: Find List ColName in Excel WorkSheet Title Row
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      shtRun= WorkSheet Object
    #      strColName= User Indicated Column Name
    #   Option:
    #      intRowRun= User Indicated Row
    #   Return: Col Found List
    # </PyFunc: >
    if intRowRun==0: intRowRun=fnRngTitleRowFind(shtRun=shtRun)
    for strColNameRun in lstColName:
        if len(strColNameRun)==0:
            intColPos=0
        else:
            intColPos= \
                fnRngTitleRowColFind(
                    strColName=strColNameRun,
                    shtRun=shtRun,
                    intTitleRow=intRowRun
                )
        lstColPos.append( intColPos )
    return lstColPos

def fnRngRowGet(
        rngRun,
        intCol
)->xw.Range:
    # <PyFunc: >
    #   Desc: get Excel WorkSheet ColRange which Intersect with indicated Column
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      rngRun= User Indicated Range
    #      intCol= User Indicated Column
    #   Option:
    #   Return: 
    # </PyFunc: >
    if not isinstance(rngRun, (xw.Range,xw.Shape) ):
        return None
    if isinstance(rngRun, xw.Shape): rngRun = rngRun.TopLeftCell
    rngRowExp = rngRun.api.EntireRow.SpecialCells(xwcnst.CellType.xlCellTypeConstants).EntireRow
    rngCol = rngRun.sheet.api.Columns(intCol)
    rngRun = clsEHXW.p_objApp.api.Intersect(rngRowExp, rngCol)
    rngRun = fnXWTypeCvrt(rngRun)
    return rngRun

def fnRngColGet(
        rngRun,
        intRow
)->xw.Range:
    # <PyFunc: >
    #   Desc: get Excel WorkSheet RowRange which Intersect with indicated Row
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      rngRun= User Indicated Range
    #      intCol= User Indicated Row
    #   Option:
    #   Return: 
    # </PyFunc: >
    if not isinstance(rngRun, (xw.Range,xw.Shape) ):
        return None
    if instance(rngRun, xw.Shape): rngRun=rngRun.TopLeftCell
    rngColExp = rngRun.api.EntireColumn.SpecialCells(xwcnst.CellType.xlCellTypeConstants).EntireColumn
    rngRow = rngRun.sheet.api.Rows(intRow)
    rngRun = clsEHXW.p_objApp.api.Intersect(rngColExp, rngRow)
    rngRun = fnXWTypeCvrt(rngRun)
    return rngRun

def fnRngColLstGet(rngRun)->list:
    # <PyFunc: >
    #   Desc: Get Column Position into List
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      rngRun= User Indicated Range
    #   Option:
    #   Return: Column Position List
    # </PyFunc: >
    if not isinstance(rngRun, xw.Range): return None
    lstCol=[]
    for rngCell in rngRun:
        if not rngCell.column in lstCol: lstCol.append(rngCell.column)
    return lstCol
# </PyRegion: Sheet Range Find>


# <PyRegion: Excel WorkBook Operations>
def fnWBDetect(strWBName)->xw.Book:
    # <PyFunc: >
    #   Desc: Get Excel WorkBook From xlwings.p_objApp
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strWBName= WorkBook Name
    #   Option:
    #   Return:
    # </PyFunc: >
    wbResult=None
    clsEHXWRun=fnEHXWClass()
    for wbRun in clsEHXWRun.p_objApp.books:
        if ('*' in strWBName and EHRegExp.fnREMatch(strRun=wbRun.name, strPattern=strWBName)) or \
            wbRun.name==strWBName:
            wbResult=wbRun
            break
    return wbResult
# </PyRegion: Excel WorkBook Operations>

# <PyRegion: Excel WorkSheet Operations>
def fnShtDetect(
    strShtName:str,
    wbRun:xw.books=None,
    blnDel:bool=False,
    blnCleanUp:bool=True,
    strAftShtName:str='',
    sngRowHeight:float=0,
    blnAutoFitRow:bool=False,
    sngColWidth:float=0,
    blnAutoFitCol:bool=False,
    byteFontSize:int=10,
    sngZoomSize:int=100,
    blnDspZeros:bool=True,
    blnDspGridLine:bool=True,
    intTitleRow:int=0,
    intTitleCol:int=0,
    blnShtLock:bool=False,
    lngShtTabColorIndex:xwcnst.RgbColor = xwcnst.RgbColor.rgbWhite
)->(list|xw.Sheet, int):
    # <PyFunc: >
    #   Desc: Detect or Create Excel WorkSheet 
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      strShtName= WorkSheet Name
    #   Option:
    #      wbRun= WorkBook Object
    #      blnDel= Delete WorkSheet if Exist, if blnDel then return None
    #      blnCleanUp= Clean Up WorkSheet if Exist
    #      strAftShtName= Move shtRun After WorkSheet Name
    #      sngRowHeight= Setup Row Height
    #      blnAutoFitRow= Auto Fit Row Height   
    #      sngColWidth= Setup Column Width
    #      blnAutoFitCol= Auto Fit Column Width
    #      byteFontSize= Setup Cells Font Size
    #      sngZoomSize= Setup Excel Sheet Zoom Size
    #      blnDspZeros= Display Zeros
    #      blnDspGridLine= Display Grid Line
    #      intTitleRow= Setup Title Row with FreezePanes
    #      intTitleCol= Setup Title Col with FreezePanes
    #      blnShtLock= Lock WorkSheet Cells
    #      lngShtTabColorIndex= Setup Sheet Tab Color
    #      strSectName= INI Config Section Name
    #   Return:
    #       1. Sheet Object List
    #       2. Title Row
    # </PyFunc: >
    if wbRun is None:
        clsEHXWRun=fnEHXWClass()
        wbRun=clsEHXWRun.p_wbXWWB
    if intTitleRow==0: intTitleRow=3

    shtTmp:xw.Sheet=None
    lstSht=[]
    for shtRun in wbRun.sheets:
        if ('*' in strShtName and EHRegExp.fnREMatch(strRun=shtRun.name, strPattern=strShtName)) or \
            shtRun.name==strShtName:
            if blnDel:
                # <PyCmt: if blnDel, shtRun will be deleted and ExitFunc >
                if not shtRun.visible: shtRun.Visible=True
                if wbRun.sheets.count==1:
                    shtTmp=wbRun.sheets.add(name='tmp', after=wbRun.sheets(1) )
                    shtRun.delete()
            else:
                lstSht.append(shtRun)
    if blnDel: return None, 0

    if len(lstSht)==0:
        strShtName=strShtName.replace('*', '_')
        shtRun=wbRun.sheets.add(name=strShtName, before=wbRun.sheets(1).name)
        lstSht.append(shtRun)

    if not blnCleanUp: return lstSht, 0

    for shtRun in lstSht:
        # <PyCmt: AutoFilter Clean >
        fnAutoFilter(shtRun=shtRun, blnFilterClean=True)
        # <PyCmt: Cells Content Clean >
        fnRngRowsAll(shtRun=shtRun).hidden=False
        fnRngColsAll(shtRun=shtRun).hidden = False
        shtRun.cells.clear_contents()
        # <PyCmt: Sheet Tab Color Clean>
        shtRun.api.Tab.Color =lngShtTabColorIndex

        # <PyCmt: Setup Row Height >
        if blnAutoFitRow:
            shtRun.api.Rows.autofit()
        elif sngRowHeight>0:
            shtRun.api.Rows.RowHeight=sngRowHeight
        # <PyCmt: Setup Column Width >
        if blnAutoFitCol:
            shtRun.api.Columns.autofit()
        elif sngColWidth>0:
            shtRun.api.Columns.ColumnWidth=sngColWidth

        # <PyCmt: Setup Cells Format back to Default>
        Cells=shtRun.cells
        Cells.api.Font.Name=c_strFontNameDefault
        Cells.api.Font.Size=byteFontSize
        Cells.api.Font.ColorIndex=xwcnst.ColorIndex.xlColorIndexAutomatic
        Cells.api.Validation.Delete()
        Cells.api.ClearOutline()
        Cells.api.Locked=blnShtLock

        # <PyCmt: Setup FreezePanes >
        if intTitleRow > 0 or intTitleCol > 0:
            wbRun.activate()
            shtRun.activate()
            winAct=wbRun.app.api.ActiveWindow
            if not winAct is None:
                winAct.FreezePanes=False
                winAct.ScrollRow=1
                winAct.ScrollColumn = 1
                intFreezeRow=intTitleRow+1
                intFreezeCol=intTitleCol+1
                shtRun.cells(intFreezeRow, intFreezeCol).select()
                winAct.FreezePanes = True
                winAct.DisplayZeros=blnDspZeros
                winAct.DisplayGridlines=blnDspGridLine
                winAct.Zoom=sngZoomSize
                winAct.WindowState=xwcnst.WindowState.xlMaximized

        # <PyCmt: Setup shtRun Position >
        if len(strAftShtName)>0:
            for shtAft in wbRun.sheets:
                if shtAft==strAftShtName:
                    shtRun.api.Move(shtAft.api)
                    break
        else:
            shtRun.api.Move(wbRun.sheets(1).api)

    if not shtTmp is None: shtTmp.delete()
    if len(lstSht)==1:
        return lstSht[0], intTitleRow
    else:
        return lstSht, intTitleRow

def fnRngTitleRowColFmt(
    shtRun:xw.Sheet,
    lstColSchema:list,
    lstColNameKey:list=None,
    lstColNameValue:list=None,
    intTitleRow:int=0,
    intColUqeNo:int=0,
    intUpdStatusCol:int=0,
    lstColNameShow:list=None,
    lstColNameNotShow:list=None,
    lstColNameCvrt:list=None,
    intColStart:int=1,
    blnFontBold:bool=True,
    lstFillColor:bool=None,
    blnWithBorder:bool=False
)->list:
    # <PyFunc: >
    #   Desc: Setup Excel WorkSheet Title Row and Column Format
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      shtRun= WorkSheet Object
    #      lstColSchema= Column Schema List
    #   Option:
    #      intTitleRow= User Indicated Title Row
    #      intColUqeNo= User Indicated Unique No Column Position
    #      intUpdStatusCol= User Indicated Update Status Column Position
    #      lstColNameShow= User Indicated Title Array()
    #      lstColNameNotShow= Column Name Not Show
    #      lstColNameCvrt= Column Name Convert To
    #      intColStart= Start Column Position
    #      lstColNameKey= Key Column Name
    #      lstColNameValue= Value Column Name
    #      blnFontBold= Cell Font Bold
    #      lstFillColor= Cell Interior Fill Color List
    #      blnWithBorder= Cell With Border
    #   Return: Title Row Column Name Filled List
    # </PyFunc: >
    if intTitleRow<3: intTitleRow=3

    if lstColSchema is None:
            exit(1)
    lstColName:list=[]
    for lstRow in lstColSchema:
        lstColName.append(lstRow[EHDBApply.c_intTblColSchemaColName])

    lstColNameRun=[]
    if not lstColNameShow is None:
        for strColName in lstColName:
            if strColName in lstColNameShow:
                lstColNameRun.append(strColName)
    else:
        lstColNameRun=lstColName

    if len(lstColNameRun) > 0 and len(lstColNameCvrt) > 0:
        if len(strColNameOrig.split(strSplitor))!=len(lstColNameCvrt.split(strSplitor)):
            strMsg='Convert ColName  Qty Mismatch!'
            strFuncName='EHXLSht.fnXLShtTitleRowColFmtArray'
            strTitle = 'Table Head ColName Convert Fail'
            EHMsg.fnMsgPrt(strMsg=strMsg, strTitle=strTitle, strFuncName=strFuncName, blnLog=True)
            return None

    lstBorderItem=\
        [xwcnst.BordersIndex.xlEdgeBottom, xwcnst.BordersIndex.xlEdgeLeft,
         xwcnst.BordersIndex.xlEdgeRight, xwcnst.BordersIndex.xlEdgeTop]
    lstColFilled=[]
    if intColStart<=0: intColStart=1
    intColRun=intColStart
    # for lstRow in lstColSchema:
    intRun:int=0
    while intRun<len(lstColSchema):
        strColNameRun=lstColSchema[intRun][EHDBApply.c_intTblColSchemaColName]
        if strColNameRun == EHDBApply.c_strDBTblColNameUqeNo and \
            intColUqeNo>0:
            pass
        elif intColRun == intUpdStatusCol:
            strColNameRun = EHXLRpt.c_strReportGenUploadStatus
        elif len(lstColNameNotShow)>0 and not strColNameRun in lstColNameNotShow:
            strColNameRun=''
        elif len(lstColNameCvrt)>0 and not intColRun <= len(lstColNameCvrt):
            strColNameRun=''

        if len(strColNameRun)>0:
            shtRun.range(intTitleRow, intColRun).value=strColNameRun
            shtRun.range(intTitleRow, intColRun).font.bold=blnFontBold
            rngData:xw.Range= \
                shtRun.range(
                    shtRun.range(intTitleRow + 1, intColRun),
                    shtRun.range(fnShtRowsCount(), intColRun)
                )
            rngData.number_format = lstColSchema[intRun][EHDBApply.c_intTblColSchemaColNumFmt]

            rngTitleRowSngCell:xw.Range=shtRun.cells(intTitleRow, intColRun)
            rngTitleRowSngCell.value=strColNameRun
            rngTitleRowSngCell.font.bold = blnFontBold
            lstColFilled.append(strColNameRun)

            if not lstColNameKey is None and strColNameRun in lstColNameKey:
                rngTitleRowSngCell.Interior.Color = EHXLRpt.c_lngTitleRowColorLightLightBlue
            elif not lstColNameValue is None and strColNameRun in lstColNameValue:
                rngTitleRowSngCell.Interior.Color = EHXLRpt.c_lngTitleRowColorLightGreen
            else:
                if isinstance(lstFillColor, bool):
                    if lstFillColor: rngTitleRowCell.Interior.Color = EHXLRpt.c_lngTitleRowColorDefault
                elif isinstance(lstFillColor, int):
                    rngTitleRowCell.Interior.Color = lstFillColor
                elif isinstance(lstFillColor, list):
                    if intRun<len(lstFillColor):rngTitleRowCell.Interior.Color = lstFillColor[intRun]

            if blnWithBorder:
                for intBrdItem in lstBorderItem:
                    rngTitleRowCell.Borders(intBrdItem).Weight = xlThin
                    rngTitleRowCell.Borders(intBrdItem).ColorIndex = 0
                    rngTitleRowCell.Borders(intBrdItem).LineStyle = xlContinuous
            lstColFilled.append(strColNameRun)
            if intColRun != intUpdStatusCol: intRun+=1
            intColRun+=1
    return lstColFilled
# </PyRegion: Excel WorkSheet Operations>

# <PyRegion: Range Oper>
def fnRngLastCellReset(shtRun:xw.Sheet):
    return shtRun.used_range

def fnRngHeaderGuess(rngRun:xw.Range)->(bool, list, tuple):
    # <PyFunc: >
    #   Desc: Guess Header Row and Column Name from Range
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      rngRun= User Indicated Range
    #   Option:
    #   Return:
    #       blnHeader= Header Row or Not
    #       lstColName= Header Column Name List
    #           rngColStart= Start Column Range
    #           rngColEnd= End Column Range
    # </PyFunc: >
    clsEHXWRun=fnEHXWClass()
    shtRun: xw.main.Sheet = clsEHXWRun.p_wbXWWB.sheets(rngRun.sheet.name)

    intRowStart:int = rngRun.row
    intColStart:int = rngRun.column
    intColEnd:int = fnRngToRight(rngRun = rngRun).column

    if len(str(shtRun.cells(intRowStart, intColStart).value))==0:
        rngAft:xw.Range = shtRun.cells(intRowStart, intColStart)
        rngStart:xw.Range = \
            fnRngFind(
                strFind='*',
                shtRun=shtRun,
                rngAfter=rngAft
            )
        intRowStart:int = rngStart.row
        intColStart:int = rngStart.column
        intColEnd:int = fnRngToRight(rngRun = rngStart).column

    lstColName=[]
    blnHeader = True
    for rngCell in shtRun.range(shtRun.cells(intRowStart, intColStart),shtRun.cells(intRowStart, intColEnd)):
        strCellValue=str(rngCell.value)
        if strCellValue.isnumeric():
            blnHeader=False
        elif not strCellValue[0].isalpha():
            blnHeader=False
        strCellValue=strCellValue.replace(' ','')
        lstColName.append(strCellValue)
    return blnHeader, lstColName, (intRowStart, intColStart, intColEnd)

def fnRngSeltValLstGet(
    shtRun = None,
    intRowStart:int=0,
    intRowEnd:int=0,
    intColStart:int=0,
    intColEnd:int=0
)->tuple:
    # <PyFunc: >
    #   Desc: Get Indicated Range or Selected Range Value Into Tuple
    #   Use By:
    #   Noticed:
    #   Parameter:
    #   Option:
    #      shtRun= WorkSheet Object
    #      intRowStart= Start Row Position
    #      intRowEnd= End Row Position
    #      intColStart= Start Column Position
    #      intColEnd= End Column Position
    #   Return: Tuple with Range Value List
    # </PyFunc: >
    clsEHXWRun = fnEHXWClass()
    if shtRun is None: shtRun = clsEHXWRun.p_shtAct
    rngSelt = clsEHXWRun.p_objApp.selection
    if intRowStart == 0: intRowStart = rngFirst.row
    if intRowEnd == 0: intRowEnd = rngSelt.row + rngSelt.rows.Count-1
    if intColStart == 0: intColStart = rngFirst.column
    if intColEnd == 0: intColEnd = rngLast.column + rngSelt.columns.Count-1
 
    rngSelt=shtRun.range(shtRun.cells(intRowStart, intColStart), shtRun.cells(intRowEnd, intColEnd))
    import datetime
    # <PyCmt: Convert Selected Range Value Into List, which Empty Cell='', Date Cell Value=DateTime>
    lstRng=rngSelt.options(empty='', dates=datetime.datetime).value
    return lstRng

def fnRngColSchemaGet(
    tupData: tuple,
    lstColName:list
)->list:
    if tupData is None: return None
    if len(tupData)==0: return None
    import EHNum
    lstColSchema=EHNum.fnNumSchema(tupData=tupData, lstColName=lstColName)
    lstColSchemaJoin=[]
    for lstSchemaRow in lstColSchema:
        lstColSchemaJoin.append(''.join(lstSchemaRow))
    return lstColSchemaJoin
# </PyeRegion: Range Oper>

# <PyRegion: AutoFilter Oper>
def fnAutoFilter(
    shtRun:xw.Sheet,
    rngRun:xw.Range=None,
    blnAutoFilter:bool=True,
    blnFilterClean:bool=False
):
    # <PyFunc: >
    #   Desc: Setup Excel WorkSheet AutoFilter or Clean Filter
    #   Use By:
    #   Noticed:
    #   Parameter:
    #      shtRun= WorkSheet Object
    #   Option:
    #      blnAutoFilter= Enable AutoFilter
    #      blnFilterClean= Clean Filter
    #   Return:
    # </PyFunc: >
    if not isinstance(shtRun, xw.Sheet): return None
    if rngRun is None:
        intRowLast=fnRngLastCell().row
        rngRun=shtRun.cells[:intRowLast, :]

    if shtRun.api.AutoFilterMode:
        if not blnAutoFilter :shtRun.cells.api.AutoFilterMode = False
    else:
        if blnAutoFilter and rngRun.rows.count>1:
            # <PyDebug: easy Msg>
            strMsg='rngRun: {}'.format(rngRun)
            import EHMsg
            EHMsg.fnMsgPrt(strMsg=strMsg)
            # </PyDebug: easy Msg>

            rngRun.api.AutoFilter(1)
    if blnFilterClean and shtRun.api.FilterMode: shtRun.cells.api.ShowAllData()

# </PyRegion: AutoFilter Oper>

# <PyRegion: XL Oper>
def fnXLAppReset(
    blnDisFunc:bool=False
):
    clsEHXWRun=fnEHXWClass()
    clsEHXWRun.p_objApp.api.EnableCancelKey  = xwcnst.EnableCancelKey.xlInterrupt
    clsEHXWRun.p_objApp.enable_events = not blnDisFunc
    clsEHXWRun.p_objApp.screen_updating = not blnDisFunc
    clsEHXWRun.p_objApp.display_alerts = not blnDisFunc
    if blnDisFunc:
        clsEHXWRun.p_objApp.calculation = 'manual'
    else:
        clsEHXWRun.p_objApp.calculation = 'automatic'
    clsEHXWRun.p_objApp.api.CalculateBeforeSave = not blnDisFunc
# </PyRegion: XL Oper>


# <PyRegion: EHXLSht Attrib>
def fnShtAttrGet(shtRun:xw.main.Sheet):
    print("dir(shtRun): {}".format(dir(shtRun)))
    # dir(shtRun):
    #   ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__'
    #       , '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__'
    #       , '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__'
    #       , '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'
    #       , 'activate', 'api', 'autofit', 'book', 'cells', 'charts', 'clear', 'clear_contents', 'clear_formats'
    #       , 'copy', 'delete', 'impl', 'index', 'name', 'names', 'page_setup', 'pictures', 'range', 'render_template'
    #       , 'select', 'shapes', 'tables', 'to_html', 'to_pdf', 'used_range', 'visible']
# </PyRegion: EHXLSht Attrib>
def fnRngAttrGet(rngRun:xw.Range):
    print("dir(rngRun.api): {}".format(dir(rngRun.api)))
    # dir(rngRun):
    #   ['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__'
    #       , '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__'
    #       , '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__'
    #       , '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'
    #       , '_impl', '_options'
    #       , 'add_hyperlink', 'address', 'api', 'autofill', 'autofit', 'characters', 'clear', 'clear_contents'
    #       , 'clear_formats', 'color', 'column', 'column_width', 'columns', 'copy', 'copy_picture', 'count'
    #       , 'current_region', 'delete', 'end', 'expand', 'font', 'formula', 'formula2', 'formula_array'
    #       , 'get_address', 'has_array', 'height', 'hyperlink', 'impl', 'insert', 'last_cell', 'left', 'merge'
    #       , 'merge_area', 'merge_cells', 'name', 'note', 'number_format', 'offset', 'options', 'paste', 'raw_value'
    #       , 'resize', 'row', 'row_height', 'rows', 'select', 'shape', 'sheet', 'size', 'table', 'to_pdf', 'to_png'
    #       , 'top', 'unmerge', 'value', 'width', 'wrap_text']