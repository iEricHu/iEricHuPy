# EHXLObj.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import xlwings as xw
import xlwings.constants as xwcnst

import EHMsg
import EHXLRpt

c_strBtnFuncAttrName="BtnFuncAttr"

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHXLObj.py !')

udeXLObjShpType=xwcnst.FormControl
rgbWhite=xwcnst.RgbColor.rgbWhite
# </PyDecl: RunTime>
def XLObjShpCreate(
        shtRun:xw.Sheet,
        strShpName:str,
        strBtnFuncName:str='',
        blnShpDel:bool=False,
        udeXLObjShpTypeRun:udeXLObjShpType=udeXLObjShpType.xlLabel,
        lngShpTop:int=0,
        lngShpLeft:int=0,
        lngShpWidth:int=0,
        lngShpHeight:int=0,
        blnAutoPos:bool=False,
        strShpStr:str='',
        strShpAltStr:str='',
        xlShpPlacement:int=xwcnst.Placement.xlFreeFloating,
        blnShpVisible:bool=True,
        blnShpPrintObj:bool=True,
        strShpFontName:str='',
        intShpFontSize:int=10,
        blnShpAutoSize:bool=True,
        lngShpFontColorIndex:int=0,
        lngShpInteriorColor:xwcnst.RgbColor=rgbWhite,
        lngShpBorderColor:xwcnst.RgbColor= rgbWhite
)->xw.Shape:
    shpRun:xw.Shape=None
    shpRun= \
        fnXLObjShpDetect(
            shtRun=shtRun,
            strShpName=strShpName,
            blnDel=blnShpDel
        )
    if blnShpDel: return None
    try:
        varCtrlType=shpRun.ShapeRange.Item(1).FormControlType
    except Exception:
        varCtrlType=None

    if not shpRun is None:
        if varCtrlType!=udeXLObjShpTypeRun:
            shpRun.delete()
            shpRun=None

    if shpRun is None:
        if udeXLObjShpTypeRun==udeXLObjShpType.xlEditBox:
            strMsg='Can not create EditBox!'
            strFuncName='EHXLObj.XLObjShpCreate'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
            return None
        shpRun=\
            shtRun.shapes.api.AddFormControl(
                udeXLObjShpTypeRun,
                lngShpTop,
                lngShpLeft,
                lngShpWidth,
                lngShpHeight
            ).OLEFormat.Object

    shpRun.Name=strShpName
    if udeXLObjShpTypeRun == udeXLObjShpType.xlButtonControl:
        # xlButtonControl: AutoSize, Caption, DefaultButton, Font(Bold, Color, ColorIndex,Name), OnAction
        shpRun.api.AutoSize=blnShpAutoSize
        shpRun.api.Caption=strShpName
        shpRun.api.OnAction = \
            '\'' + shtRun.workbook.Name + '\'!' & EHXLRpt.c_strReportGenButtonFuncName
        EHXLRpt.fnShtCfgOper(
            shtRun=shtRun,
            strAttrName=c_strBtnFuncAttrName,
            strAttrValue=strBtnFuncName
        )
        if shpRun.api.TopLeftCell.Rows.RpwHeight<shpRun.Height:
            shpRun.api.TopLeftCell.Rows.RpwHeight = shpRun.Height
        if len(strShpFontName)>0: shpRun.font.name=strShpFontName
        if len(intShpFontSize) > 0: shpRun.font.size = intShpFontSize
        if lngShpFontColorIndex!=0: shpRun.font.api.ColorIndex=lngShpFontColorIndex
        if blnAutoPos:
            lngMaxLeft = 0
            lngMinTop = 99999
            lngMaxLeftBtnWidth=0
            for btnRun in shtRun.Buttons:
                if btnRun.Name!=btnDect.Name:
                    if btnRun.Left > lngMaxLeft:
                        lngMaxLeft=btnRun.Left
                        lngMaxLeftBtnWidth=btnRun.Width
                    if btnRun.Top < lngMinTop:
                        lngMinTop =btnRun.Top
            if lngMaxLeft>0:
                shpRun.left=lngMaxLeft+lngMaxLeftBtnWidth
                shpRun.top=lngMinTop
            else:
                shpRun.left=shtRun.cells(1,2).Left
                shpRun.top=0
        else:
            shpRun.left = shtRun.cells(1, 2).Left
            shpRun.top = 0

    elif udeXLObjShpTypeRun==udeXLObjShpType.xlCheckBox:
        # xlCheckBox: Caption, OnAction, Text, Value(Y/N)
        shpRun.caption=strShpName
        shpRun.text = strShpStr
    elif udeXLObjShpTypeRun==udeXLObjShpType.xlDropDown:
        # xlDropDown: ListIndex, ListCount, OnAction, Value
        pass
    elif udeXLObjShpTypeRun==udeXLObjShpType.xlGroupBox:
        # xlGroupBox: Caption, OnAction, Text
        shpRun.caption=strShpName
        shpRun.text=strShpStr
    elif udeXLObjShpTypeRun==udeXLObjShpType.xlLabel:
        # xlLabel: Caption, OnAction, Text
        # shpRun.caption=strShpName # <PyDebug: Error>
        shpRun.Caption=strShpName
        shpRun.Text=strShpStr
    elif udeXLObjShpTypeRun==udeXLObjShpType.xlListBox:
        # xlListBox: ListIndex, ListCount, OnAction, Value
        pass
    elif udeXLObjShpTypeRun==udeXLObjShpType.xlOptionButton:
        # xlOptionButton: Caption, GroupBox, OnAction, Text, Value(Y/N)
        shpRun.caption=strShpName
        shpRun.text = strShpStr

    shpRun.ShapeRange.AlternativeText=strShpAltStr
    shpRun.Placement = xlShpPlacement
    shpRun.Visible = blnShpVisible
    shpRun.PrintObject = blnShpPrintObj
    # shpRun.Interior.Color = lngShpInteriorColor # <PyDebug: Error>
    # shpRun.Border.Color = lngShpBorderColor # <PyDebug: Error>
    return shpRun

def fnXLObjShpDetect(
        shtRun,
        strShpName,
        blnDel=False,
        blnClean=False,
        fltBtnLeft:float =0
)->xw.Shape:
    for shpRun in shtRun.api.Shapes:
        if shpRun.Name == strShpName:
            shpRun=shpRun.OLEFormat.Object
            shpRun.Left=fltBtnLeft
            if blnDel:
                shpRun.Delete()
                return None
            elif blnClean:
                shpRun.ShapeRange.AlternativeText = ""
                return shpRun
            else:
                return shpRun
            break

def fnXLObjShpClean(
        shtRun:str,
        blnShtCfgShpSkip:bool = True,
        blnCmbBxObjSkip:bool = True
)->bool:
    blnDel: bool = False
    for shpRun in shtRun.api.Shapes:
        if shpRun.Name==EHXLRpt.c_strShtCfgTitle:
            if not blnShtCfgShpSkip:
                shpRun.Delete()
                blnDel=True
        elif shpRun.Name==EHXLRpt.c_strShtCfgCmbBxName:
            if not blnCmbBxObjSkip:
                shpRun.Delete()
                blnDel = True
        else:
            shpRun.Delete()
            blnDel = True
    return blnDel
