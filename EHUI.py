# EHUI.py
# <PyDecl: Module Init, Setup DebugMode>
import datetime

import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import EHSymbolDef
# <PyDecl: Symbol Define & UDE import >
c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor # ';'
c_strNewLine = EHSymbolDef.c_strNewLine # '\n'
# </PyDecl: Symbol Define & UDE import >

import EHPyMdl
import EHMsg
import EHPyQt
import EHPyFunc

c_strEHUIMdlName:str=__name__

c_strCommonEHQtFomGen: str = "EHQtFomGen"

c_strEHPyQtMdlName:str='EHPyQt'
# <PyCmt: c_strPyQtObjParaDict, For Filter from EHPyQtClsObj>
c_strPyQtObjParaDict:str='dictObjPara'
c_strPyQtObjUDEPfx:str= 'ude'
c_strPyQtObjBoolPfx:str= 'bln'

c_strPyQtObjParaDictName:str='strName'
c_strPyQtObjParaDictObjName:str='strObjName'
c_strPyQtObjParaDictObjParent:str='objParent'

c_lstBoxTreeObjAddedTitleRow:list=['ItemKey', 'Name', 'ObjType']
c_intTreeLstColItemKey:int=0
c_intTreeLstColObjName:int=1
c_intTreeLstColObjType:int=2

c_intEHPyQtObjItmKeyCreatedItmKey:int=0
c_intEHPyQtObjItmKeyCreatedObjName:int=1

    # <PyCmt: Object Attr>
c_strObjAttrName: str = 'ObjAttr'
c_strKeywordLayout: str = 'LayoutType'
c_strQtKeywordLayout: str = 'Layout'
    # </PyCmt: Object Attr>

# <PyCmt: RunTime>
    # <PyCmt: Static Object >
QWin:EHPyQt.QWin =None
QFrmObjAddBoxTree:EHPyQt.QBoxTree =None
QFrmObjAddObjPickCmb:EHPyQt.QBoxCmb=None
QFrmObjAddObjPickBtnAdd:EHPyQt.QBtn=None
QFrmObjAttr:EHPyQt.QFrm =None
    # </PyCmt: Static Object >

    # <PyCmt: Variable Declare>
# <PyCmt: s_dictEHPyQtObj contain all object dict para of EHPyQt >
s_dictEHPyQtObj:dict={}
# <PyCmt: s_dictEHPyQtObjParam contained RunningTime Obj Attrib>
s_dictEHPyQtObjParam:dict={}
s_lstEHPyQtObjItmKeyCreated:list=[]
s_lstEHPyQtObjNameCreated:list=[]

# <PyCmt: TreeItem Selected>
s_itmTreeSeltd:EHPyQt.QBoxTree.selectedItems=None
s_intTreeSeltdRow:int=-1


# <PyCmt: s_lstPyDataType=EHPyFunc.udePyDataType Collection>
s_lstPyDataType:list=None
# <PyCmt: s_lstEHPyQtUdeColl=EHPyQt.fnEHPyQtClsGet UDE Collection>
s_lstEHPyQtUdeColl:list = None
    # </PyCmt: Variable Declare>
# </PyCmt: RunTime>

def fnEHPyQtObjTypeGet()->dict:
    # <PyFunc: fnEHPyQtObjTypeGet>
    #    Desc: Get All Obj Type from EHPyQt and fill into lstObjTypeName
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
    # </PyFunc: fnEHPyQtObjTypeGet>
    import sys

    # <PyCmt: Get Container Type from EHPyQt: QGroupBox;QFrame;QScrollArea;QDockWidget
    c_strContainerColl=EHPyQt.c_strContainerColl
    mdlRun=EHPyMdl.fnMdlLoad(strMdlName = c_strEHPyQtMdlName)
    lstEHPyQtObjName=dir(mdlRun)
    lstEHPyQtObjTypeNameContainer:list=[]
    lstEHPyQtObjTypeName:list=[]
    for strObjName in lstEHPyQtObjName:
        # <PyCmt: get all obj from EHPyQt start with c_strPyQtObjParaDict(dictObjPara))>
        if strObjName[: len(c_strPyQtObjParaDict)] == c_strPyQtObjParaDict:
            dictObjPara:dict=sys.modules[c_strEHPyQtMdlName].__getattribute__(strObjName)
            strObjTypeName=dictObjPara[c_strPyQtObjParaDictObjName]
            s_dictEHPyQtObj[strObjTypeName]=dictObjPara

            if c_strAttrSplitor+strObjTypeName+c_strAttrSplitor in \
                c_strAttrSplitor+c_strContainerColl+c_strContainerColl:
                lstEHPyQtObjTypeNameContainer.append(strObjTypeName)
            else:
                lstEHPyQtObjTypeName.append(strObjTypeName)
    return  lstEHPyQtObjTypeNameContainer, lstEHPyQtObjTypeName

def fnQtFomMdl():
    # <PyFunc: fnQtFomMdl>
    #    Desc: Generate 'EH Form Model Generator' window
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
    # </PyFunc: fnQtFomMdl>

    lstEHPyQtObjTypeNameContainer, lstEHPyQtObjTypeName = \
        fnEHPyQtObjTypeGet()

    # <PyCmt: MainWindow>
    strWinTitle:str = 'EH Form Model Generator'
    global QWin
    QWin= \
        EHPyQt.QWin(
            strName = c_strCommonEHQtFomGen,
            strTitle =  strWinTitle,
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeH
        )
    QWgetCentral:QtWidgets.QWidget=QWin.QWgetCentral

    # <PyCmt: Object Added Frame>
    QFrmObjAdd:QtWidgets.QFrame = \
        EHPyQt.QFrm(
            objParent = QWgetCentral,
            strName = c_strCommonEHQtFomGen+'ObjAddFrm',
            strToolTip = 'Object Add',
            udeFrmSizePolicyH = EHPyQt.udeQtSizePolicy.udeQtSizePolicyMin,
            udeFrmSizePolicyV = EHPyQt.udeQtSizePolicy.udeQtSizePolicyMin,
            intFrmLineWidth=1
        )

    # <PyCmt: Object Added Frame Layout>
    QFrmObjAddVLayout:QtWidgets.QVBoxLayout = \
        EHPyQt.QLayout(
            objParent = QFrmObjAdd,
            strName=c_strCommonEHQtFomGen+'ObjAddLayout',
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeV
        )

    # <PyCmt: Object Added Frame SubLayout: TemplateNo>
    QFrmTempNoHLayout:QtWidgets.QHBoxLayout = \
        EHPyQt.QLayout(
            objParent = QFrmObjAdd,
            strName=c_strCommonEHQtFomGen+'FrmTempNoHLayout',
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeH
        )
    QFrmTempNoLbl:QtWidgets.QLabel = \
        EHPyQt.QLbl(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmTempNoLbl',
            objLayoutInd = QFrmTempNoHLayout,
            strText = 'TempNo: '
        )
    QFrmTempNoEditLn:QtWidgets.QLineEdit = \
        EHPyQt.QEditLn(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmTempNoEditLn',
            objLayoutInd = QFrmTempNoHLayout,
            strText = '',
            blnReadOnly = True
        )

    # <PyCmt: Object Added Label>
    QFrmObjAddLbl:QtWidgets.QLabel = \
        EHPyQt.QLbl(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmObjAddLbl',
            strText = 'ObjAdded: '
        )

    # <PyCmt: Object Added TreeWidget>
    global QFrmObjAddBoxTree
    lstItem = fnFrmObjAddTreeItmDft()
    QFrmObjAddBoxTree = \
        EHPyQt.QBoxTree(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmObjAddBoxTree',
            lstTitleRow = c_lstBoxTreeObjAddedTitleRow,
            intColCount = len(lstItem[0]),
            lstItem=lstItem,
            udeSizePolicyH =
                EHPyQt.udeQtSizePolicy.udeQtSizePolicyMin ,
            udeSizePolicyV =
                EHPyQt.udeQtSizePolicy.udeQtSizePolicyMin,
            strMethItemClick = c_strEHUIMdlName + ".fnFrmObjAddTreeItmSelt"
        )

    # <PyCmt: Object Add Control Widget>
    QFrmObjAddObjPickHLayout:QtWidgets.QHBoxLayout = \
        EHPyQt.QLayout(
            objParent = QFrmObjAdd,
            strName=c_strCommonEHQtFomGen+'ObjAddObjPickHLayout',
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeH
        )
    QFrmObjAddLbl:QtWidgets.QLabel = \
        EHPyQt.QLbl(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmObjAddObjPickLbl',
            objLayoutInd = QFrmObjAddObjPickHLayout,
            strText = 'ObjType: '
        )

    lstEHPyQtObjTypeNameColl=\
        ['']+ \
        lstEHPyQtObjTypeNameContainer + \
        lstEHPyQtObjTypeName
    global QFrmObjAddObjPickCmb
    QFrmObjAddObjPickCmb = \
        EHPyQt.QBoxCmb(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmObjAddObjPickCmb',
            objLayoutInd = QFrmObjAddObjPickHLayout,
            blnEditable= False,
            strToolTip = 'ObjType',
            lstItem = sorted(lstEHPyQtObjTypeNameColl),
            strValue = '',
            blnEnable = False,
            strMethTextChg = c_strEHUIMdlName+'.fnFrmObjAddCmbChg'
        )
    global QFrmObjAddObjPickBtnAdd
    QFrmObjAddObjPickBtnAdd = \
        EHPyQt.QBtn(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmObjAddObjPickBtnAdd',
            objLayoutInd = QFrmObjAddObjPickHLayout,
            strCaption = 'Add',
            blnEnable = False,
            strMethClick=c_strEHUIMdlName+'.fnFrmObjAddBtnObjAdd'
        )
    QFrmObjAddObjPickBtnRmv:QtWidgets.QPushButton = \
        EHPyQt.QBtn(
            objParent = QFrmObjAdd,
            strName = c_strCommonEHQtFomGen+'FrmObjAddObjPickBtnRmv',
            objLayoutInd = QFrmObjAddObjPickHLayout,
            strCaption = 'Remove',
            strMethClick=c_strEHUIMdlName+'.fnObjAddFrmObjPickRmv'
        )

    # <PyCmt: QWin Right Side Layout>
    QRLayout:QtWidgets.QVBoxLayout = \
        EHPyQt.QLayout(
            objParent = QWgetCentral,
            strName=c_strCommonEHQtFomGen+'RLayout',
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeV
        )

    # <PyCmt: Object Attribute Frame>
    global QFrmObjAttr
    QFrmObjAttr = \
        EHPyQt.QFrm(
            objParent = QWgetCentral,
            strName = c_strCommonEHQtFomGen + 'ObjAttrFrm',
            objLayoutInd = QRLayout,
            strToolTip = 'Object Attribute',
            udeFrmSizePolicyH = EHPyQt.udeQtSizePolicy.udeQtSizePolicyMin,
            udeFrmSizePolicyV = EHPyQt.udeQtSizePolicy.udeQtSizePolicyMin,
            intFrmLineWidth = 1
        )

    # <PyCmt: Object Attribute Frame Layout>
    QFrmObjAttrLayout:QtWidgets.QFormLayout  = \
        EHPyQt.QLayout(
            objParent = QFrmObjAttr,
            strName=c_strCommonEHQtFomGen+'ObjAttrLayout',
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeF
        )

    # <PyCmt: WinGen Btn Set>
    QWinGenHLayout:QtWidgets.QHBoxLayout = \
        EHPyQt.QLayout(
            objParent = QWgetCentral,
            strName=c_strCommonEHQtFomGen+'WinGenHLayout',
            udeLayoutType = EHPyQt.udeQtLayoutType.udeQtLayoutTypeH,
            objLayoutInd=QRLayout
        )
    QWinGenBtn:QtWidgets.QPushButton = \
        EHPyQt.QBtn(
            objParent = QWgetCentral,
            strName = c_strCommonEHQtFomGen+'WinGenBtn',
            objLayoutInd = QWinGenHLayout,
            strCaption = 'WinGen',
            strMethClick = c_strEHUIMdlName + ".fnQtFomWinGen"
        )
    QWinGenBtnWrite:QtWidgets.QPushButton = \
        EHPyQt.QBtn(
            objParent = QWgetCentral,
            strName = c_strCommonEHQtFomGen+'WinGenBtnWrite',
            objLayoutInd = QWinGenHLayout,
            strCaption = 'Write',
            blnEnable = False,
            strMethClick = c_strEHUIMdlName + ".fnQtFomWinGenWrite"
        )
    QWinGenBtnCancel:QtWidgets.QPushButton = \
        EHPyQt.QBtn(
            objParent = QWgetCentral,
            strName = c_strCommonEHQtFomGen+'WinGenBtnCancel',
            objLayoutInd = QWinGenHLayout,
            strCaption = 'Cancel',
            strMethClick = c_strEHUIMdlName + ".fnQtFomWinGenCancel"
        )

    QWin.fnWinShow()

def fnFrmObjAddTreeItmSelt(objRun):
    # <PyFunc: fnFrmObjAddTreeItmSelt>
    #    Desc: User Select Tree Item, and setup FrmAttr Obj
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
    # </PyFunc: fnFrmObjAddTreeItmSelt>
    global s_itmTreeSeltd
    global s_intTreeSeltdRow

    blnChg, lstItmChgd=QFrmObjAttr.fnValueChgDet()
    if blnChg:
        # <PyCmt: Confirm Value Change Item Data Discard>
        strCaption='Value Change Discard Confirm'
        strMsg='ObjAttr: {} Value Changed!'.format(QFrmObjAddObjPickCmb.currentText()) + \
            '\n Discard Value?'
        if not EHMsg.fnDlgOpt(
            strMsg = strMsg,
            strTitle = strCaption,
            blnMsgOnly=False
        ):
            s_itmTreeSeltd.treeWidget().fnRowSelt(intRowSelt=s_intTreeSeltdRow)
            return
        else:
            for objValueChgDiscard in lstItmChgd:
                objValueChgDiscard.fnValueChgDiscard()
            QFrmObjAddObjPickCmb.fnValue('')
    else:
        QFrmObjAddObjPickCmb.fnValue('')


    # <PyCmt: Get Selected Item ObjName>
    s_itmTreeSeltd=objRun[0]
    s_intTreeSeltdRow=s_itmTreeSeltd.treeWidget().intRowSelt

    # <PyCmt: get ObjType from Selected Item, Col: c_intTreeLstColObjType>
    strObjType=objRun[0].text(c_intTreeLstColObjType)
    fnFrmObjAttrItmChg(
        strObjType = strObjType,
        strTreeItemName = objRun[0].text(c_intTreeLstColObjName)
    )
    QFrmObjAddObjPickCmb.fnEnable(True)

def fnFrmObjAttrItmChg(
    strObjType:str,
    strTreeItemName:str=''
):
    # <PyFunc: fnFrmObjAttrItmChg>
    #    Desc: Depend User Selected Tree Item, setup Attr Obj Type
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
    # </PyFunc: fnFrmObjAttrItmChg>
    QWin.setUpdatesEnabled(False)

    # <PyCmt: get Python Basic DataType>
    global s_lstPyDataType
    if s_lstPyDataType is None:
        s_lstPyDataType=EHPyFunc.fnPyDataType()[0] # lstDataTypeStr

    # <PyCmt: get EHPyQt udeClass>
    global s_lstEHPyQtUdeColl
    if s_lstEHPyQtUdeColl is None:
        s_lstEHPyQtUdeColl=EHPyQt.fnEHPyQtClsGet(c_strPyQtObjUDEPfx)

    # <PyCmt: ReInitFrmObjAttr>
    fnFrmObjAttrDft()
    if len(strObjType)==0: return

    # <PyCmt: get ObjRun Para Dict
    # 1. from EHPyQt: Object Attrib from Default EHPyQt Attrib Dict>
    # 2. from s_dictEHPyQtObjParam: Running Saved s_dictEHPyQtObjParam
    if len(strTreeItemName)>0:
        dictRun = s_dictEHPyQtObjParam[strTreeItemName]
    else:
        dictRun = s_dictEHPyQtObj[strObjType]

    strValue:str=''
    strMsg:str=''
    for intIndex, (strSubItmKey, objRun) in enumerate(dictRun.items()):
        ObjAttrLbl: QtWidgets.QLabel = \
            EHPyQt.QLbl(
                objParent=QFrmObjAttr,
                strName=c_strObjAttrName + "_Lbl_"+strSubItmKey,
                strText=strSubItmKey + ": ",
                strTag=strSubItmKey,
            )

        strObjDataType:str=''
        strValue=''
        if strSubItmKey==c_strPyQtObjParaDictObjParent and \
            len(strTreeItemName)==0 and \
            not s_itmTreeSeltd is None:
            strValue=s_itmTreeSeltd.text(c_intTreeLstColObjName)
            # <PyCmt: When strSubItmKey is 'pbjParent', make strValue as TreeItm Selected>
            objRun=strValue
            strObjDataType = type(objRun).__name__
        elif strTreeItemName in s_dictEHPyQtObjParam:
            if strSubItmKey in s_dictEHPyQtObjParam[strTreeItemName]:
                strValue=s_dictEHPyQtObjParam[strTreeItemName][strSubItmKey]

        if strSubItmKey[:len(c_strPyQtObjUDEPfx)] == c_strPyQtObjUDEPfx:
            strSubItmKeyRun:str=''
            if not strSubItmKey in s_lstEHPyQtUdeColl and \
             strSubItmKey[:-1] in s_lstEHPyQtUdeColl:
                strSubItmKeyRun=strSubItmKey[:-1]
            else:
                strSubItmKeyRun=strSubItmKey

            if strSubItmKeyRun in s_lstEHPyQtUdeColl:
                if len(strValue)==0 and hasattr(objRun,'name'):
                     strValue=objRun.name
                objRun= \
                    EHPyMdl.fnMdlEnumClsGet(
                        mdlRun=EHPyMdl.fnMdlLoad(strMdlName=c_strEHPyQtMdlName),
                        strClsName=strSubItmKeyRun
                    )
        elif strSubItmKey[:len(c_strPyQtObjBoolPfx)]==c_strPyQtObjBoolPfx:
            strValue = objRun
            strObjDataType=EHPyFunc.udePyDataType.udeDataTypeBool.value[0]
        elif not type(objRun).__name__ in s_lstPyDataType :
            # <PyCmt: objRun Type not in Python General Data Type>
            strErrMsg='DataType: {} not in PyDataType!'.format(type(objRun).__name__)
            EHMsg.fnDlgOpt(strMsg = strErrMsg)
        elif len(strValue)==0:
            strValue=objRun

        if len(strObjDataType)==0:strObjDataType = type(objRun).__name__
        if objRun is None:
            ObjAttrObj: QtWidgets.QLineEdit = \
                EHPyQt.QEditLn(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    strText = str(objRun),
                    strTag = strSubItmKey,
                    blnReadOnly = True
                )
        elif strObjDataType==EHPyFunc.udePyDataType.udeDataTypeStr.value[0]:
            if strSubItmKey==c_strPyQtObjParaDictName and \
                len(objRun)==0 and \
                len(strTreeItemName) > 0:
                objRun=strTreeItemName
            ObjAttrObj: QtWidgets.QLineEdit = \
                EHPyQt.QEditLn(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    strText=strValue,
                    strTag = strSubItmKey,
                    strMethEditFinished=c_strEHUIMdlName+'.fnFrmObjAttrWgetObjAttrChg'
                )
        elif strObjDataType==EHPyFunc.udePyDataType.udeDataTypeInt.value[0]:
            ObjAttrObj: QtWidgets.QLineEdit = \
                EHPyQt.QEditLn(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    strText = strValue,
                    strTag = strSubItmKey,
                    strMethEditFinished = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                )
        elif strObjDataType==EHPyFunc.udePyDataType.udeDataTypeFloat.value[0]:
            ObjAttrObj: QtWidgets.QLineEdit = \
                EHPyQt.QEditLn(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    strText = strValue,
                    strTag = strSubItmKey,
                    strMethEditFinished = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                )
        elif strObjDataType==EHPyFunc.udePyDataType.udeDataTypeBool.value[0]:
            ObjAttrObj: QtWidgets.QComboBox = \
                EHPyQt.QBoxCmb(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    lstItem = [True, False],
                    strValue=strValue,
                    strTag = strSubItmKey,
                    blnEditable = False,
                    strMethTextChg = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                )
        elif strObjDataType==EHPyFunc.udePyDataType.udeDataTypeList.value[0]:
            ObjAttrObj: QtWidgets.QComboBox = \
                EHPyQt.QBoxCmb(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    lstItem = objRun,
                    strValue = strValue,
                    strTag = strSubItmKey,
                    blnEditable = False,
                    strMethTextChg = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                )
        elif strObjDataType == EHPyFunc.udePyDataType.udeDataTypeDateTime.value[0]:
            if strSubItmKey=='dateRun':
                EHPyQt.QEditLn(
                    objParent=QFrmObjAttr,
                    strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                    strText = 'now()',
                    strTag = strSubItmKey,
                    strMethEditFinished = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                )
        elif strObjDataType==EHPyFunc.udePyDataType.udeDataTypeDate.value[0]:
            if strSubItmKey=='dateMin':
                ObjAttrObj:QDateTimeEdit  = \
                    EHPyQt.QEditDate(
                        objParent=QFrmObjAttr,
                        strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                        dateRun = EHPyQt.c_dateEditDateMin,
                        strTag = strSubItmKey,
                        strMethChg = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                    )
            elif strSubItmKey == 'dateMax':
                ObjAttrObj:QDateTimeEdit  = \
                    EHPyQt.QEditDate(
                        objParent=QFrmObjAttr,
                        strName=c_strObjAttrName + "_" + strObjDataType + "_" + strSubItmKey,
                        dateRun = EHPyQt.c_dateEditDateMax,
                        strTag = strSubItmKey,
                        strMethChg = c_strEHUIMdlName + '.fnFrmObjAttrWgetObjAttrChg'
                    )
        else:
            if len(strMsg)>0: strMsg=strMsg+'\n'
            strMsg='Object DataType: {} Not Support!'.format(strObjDataType)

    if len(strMsg) > 0:
        strMsg = strMsg + '\n\nPlease contact Program Designer!'
        EHMsg.fnMsgPrt(
            strMsg = strMsg,
            strTitle = 'Object DataType Error',
            strFuncName='EHUI.fnFrmObjAttrItmChg'
        )
    QWin.fnResize()
    QWin.setUpdatesEnabled(True)

def fnFrmObjAddTreeItmDft()->list:
    # <PyFunc: fnFrmObjAddTreeItmDft>
    #    Desc: Frame ObjAdd Tree Object Default Item setup
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
    # </PyFunc: fnFrmObjAddTreeItmDft>
    clsUdeObjName = EHPyQt.udeObjName
    dictObjParaQWin=EHPyQt.dictObjParaQWin
    dictObjParaQWget=EHPyQt.dictObjParaQWget
    dictObjParaQLayout=EHPyQt.dictObjParaQLayout
    lstTreeItem=[
        [
            '0',
            dictObjParaQWin[c_strPyQtObjParaDictName],
            dictObjParaQWin[c_strPyQtObjParaDictObjName]
        ],
        [
            '1',
            dictObjParaQWget[c_strPyQtObjParaDictName],
            dictObjParaQWget[c_strPyQtObjParaDictObjName]
        ],
        [
            '1.1',
            'QWgetLayoutDft',
            dictObjParaQLayout[c_strPyQtObjParaDictObjName]
        ]
    ]
    lstTreeItemParaDict=[]
    lstTreeItemParaDict.append(dictObjParaQWin.copy())
    lstTreeItemParaDict.append(dictObjParaQWget.copy())
    lstTreeItemParaDict.append(dictObjParaQLayout.copy())
    # <PyCmt: Get All UDE Obj Dict into s_lstEHPyQtUdeColl>
    global s_lstEHPyQtUdeColl
    if s_lstEHPyQtUdeColl is None: s_lstEHPyQtUdeColl=EHPyQt.fnEHPyQtClsGet(c_strPyQtObjUDEPfx)

    intRun=0
    for lstObjRow in lstTreeItem:
        strItmKey=lstObjRow[c_intTreeLstColItemKey]
        strObjName=lstObjRow[c_intTreeLstColObjName]
        dictTreeItemPara=lstTreeItemParaDict[intRun]
        for intIndex, (strSubItmKey, strValueRun) in enumerate(dictTreeItemPara.items()):
            strValue: str = ''
            strUDType: str = ''
            if hasattr(strValueRun, '__module__'):
                strUDType = strValueRun.__module__

            # <PyCmt: Convert objValue to String Type>
            if strSubItmKey==c_strPyQtObjParaDictName: # strName
                strValue = strObjName
            elif strSubItmKey==c_strPyQtObjParaDictObjParent: #ObjParent
                if strItmKey=='0':
                    pass
                else:
                    strValue=fnFrmObjAttrObjParentFind(strItmKey=strItmKey)
            elif len(strUDType) > 0:
                if hasattr(strValueRun, '__name__'):
                    strValue = strValueRun.__name__
                elif hasattr(strValueRun, 'name'):
                    strValue = str(strValueRun.name)
            elif strSubItmKey in s_lstEHPyQtUdeColl:
                strValue = str(strValueRun.name)
            if strValueRun is None and len(strValue)==0:
                strValue='None'
            elif len(strValue)==0:
                strValue = str(strValueRun)

            dictTreeItemPara[strSubItmKey]=strValue

        s_lstEHPyQtObjItmKeyCreated.append([strItmKey, strObjName])
        s_lstEHPyQtObjNameCreated.append(strObjName)
        s_dictEHPyQtObjParam[strObjName] = dictTreeItemPara
        intRun+=1
    return lstTreeItem

def fnFrmObjAttrObjParentFind(
    strItmKey:str
)->str:
    if strItmKey=='1':
        strParentFind='0'
    else:
        c_strBoxTreeSplitor:str=EHPyQt.c_strBoxTreeSplitor
        strParentFind=c_strBoxTreeSplitor.join(strItmKey.split(c_strBoxTreeSplitor)[:-1])

    for lstEHPyQtObjItmKeyCreatedRow in s_lstEHPyQtObjItmKeyCreated:
        if lstEHPyQtObjItmKeyCreatedRow[c_intEHPyQtObjItmKeyCreatedItmKey]==strParentFind:
            return lstEHPyQtObjItmKeyCreatedRow[c_intEHPyQtObjItmKeyCreatedObjName]

def fnFrmObjAttrDft():
    # <PyFunc: fnFrmObjAttrDft>
    #    Desc: Destroy All Object of Container Object
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
    # </PyFunc: fnFrmObjAttrDft>
    EHPyQt.fnChildWidgetDestroy(objRun=QFrmObjAttr)

    # <PyCmt: ReCreate 'ObjAttr' Label>
    QFrmObjAttrLbl:QtWidgets.QLabel = \
        EHPyQt.QLbl(
            objParent = QFrmObjAttr,
            strName = c_strCommonEHQtFomGen+'ObjAttrLbl',
            strText = 'ObjAttr: ',
            udeSizePolicyV = EHPyQt.udeQtSizePolicy.udeQtSizePolicyMinExp
        )

def fnFrmObjAddCmbChg(objRun):
    # <PyFunc: fnFrmObjAddCmbChg>
    #    Desc: FrmObjAdd ObjAddCmb Item Changed Process
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
    # </PyFunc: fnFrmObjAddCmbChg>
    global s_itmTreeSeltd
    global s_intTreeSeltdRow

    # <PyCmt: objRun represent QBoxCmb object>
    blnChg, lstItmChgd=QFrmObjAttr.fnValueChgDet()
    if blnChg:
        strCaption='Value Change Discard Confirm'
        strMsg='ObjAttr: {} Value Changed!'.format(QFrmObjAddObjPickCmb.currentText()) + \
            '\n Discard Value?'
        if not EHMsg.fnDlgOpt(
            strMsg = strMsg,
            strTitle = strCaption,
            blnMsgOnly=False
        ):
            s_itmTreeSeltd.treeWidget().fnRowSelt(intRowSelt = s_intTreeSeltdRow)
            return
        else:
            for objValueChgDiscard in lstItmChgd:
                objValueChgDiscard.fnValueChgDiscard()

    fnFrmObjAttrItmChg(strObjType = objRun.strValue)
    QFrmObjAddObjPickBtnAdd.fnEnable(len(objRun.strValue)>0)

def fnFrmObjAddBtnObjAdd():
    # <PyFunc: fnFrmObjAddBtnObjAdd>
    #    Desc: When User Pick ObjType From CmbBox and Click 'Add' Btn
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
    # </PyFunc: fnFrmObjAddBtnObjAdd>
    if len(QFrmObjAddObjPickCmb.currentText())==0:
        EHMsg.fnDlgOpt(
                strMsg='No Object Type Selected!',
                strTitle='Object Type Selection Error'
            )
        return
    if len(QFrmObjAddBoxTree.selectedItems())==0:
        EHMsg.fnDlgOpt(
            strMsg='No Item Selected!',
            strTitle='Tree Widget Selection Error'
        )
        return

    # <PyCmt: TreeWidget Item Info. Get>
    itmParent=QFrmObjAddBoxTree.selectedItems()[0]
    strKey=QFrmObjAddBoxTree.fnTreeKeyMaxGet(itmParent=itmParent)

    # <PyCmt: ObjAttrFrm Info.>
    dictObjAttr=fnQtFomObjAttrGet(QFrmObjAttr)
    if len(dictObjAttr[c_strPyQtObjParaDictName])==0:
        EHMsg.fnDlgOpt(
            strMsg='Object Name Empty!',
            strTitle='Object Config Error'
        )
        return
    # <PyCmt: Add Item into s_dictEHPyQtObjParam>
    s_dictEHPyQtObjParam[dictObjAttr[c_strPyQtObjParaDictName]]=dictObjAttr

    lstItm:list = [strKey, dictObjAttr[c_strPyQtObjParaDictName], QFrmObjAddObjPickCmb.currentText()]
    QFrmObjAddBoxTree.fnItemAdd(
        itmParent = itmParent,
        lstItm = lstItm
    )

    # <PyCmt: Set Object in QFrmObjAttr value as Default>
    blnChg, lstItmChgd = \
        EHPyQt.fnWgetValueChgDet(wgetRun = QFrmObjAttr)
    if blnChg:
        for objValueSet in lstItmChgd:
            objValueSet.fnValueSetDft()

    QFrmObjAddObjPickCmb.fnValueSetDft(strValue='')
    QFrmObjAddObjPickBtnAdd.fnEnable(False)

def fnFrmObjAttrWgetObjAttrChg(objRun):
    # <PyFunc: fnFrmObjAttrWgetObjAttrChg>
    #    Desc: FrmObjAttr, ObjAttr Changed Process
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
    # </PyFunc: fnFrmObjAttrWgetObjAttrChg>
    if len(QFrmObjAddObjPickCmb)==0 and s_itmTreeSeltd:
        strObjName = s_itmTreeSeltd.text(c_intTreeLstColObjName)
        # <PyCmt: objRun.strTag Means ObjAttrName>
        s_dictEHPyQtObjParam[strObjName][objRun.strTag] = objRun.strValue
        objRun.fnValueSetDft()

def fnQtFomWinGen():
    # <PyFunc: fnQtFomWinGen>
    #    Desc:
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
    # </PyFunc: fnQtFomWinGen>

    QApp=EHPyQt.QApp()
    QWinFomGet=None
    QWgetCentralRun=None
    for intIndex, strObjName in enumerate(s_dictEHPyQtObjParam):
        dictRun=s_dictEHPyQtObjParam[strObjName]
        if dictRun[c_strPyQtObjParaDictObjName]==EHPyQt.udeObjName.udeObjNameWin.value:
            QWinFomGet=EHPyQt.QWin(**dictRun)
        elif dictRun[c_strPyQtObjParaDictObjName]==EHPyQt.udeObjName.udeObjNameQWget.value:
            dictRun['objParent']=QWinFomGet
            QWgetCentralRun=EHPyQt.QWgetCentral(**dictRun)
        elif dictRun[c_strPyQtObjParaDictObjName]==EHPyQt.udeObjName.udeObjNameLayout.value:
            dictRun['objParent'] = QwgetCentralRun
            objRun = EHPyQt.QLayout(**dictRun)
        else:
            print('Debug')
    QWinFomGet.fnWinShow()


def fnQtFomWinGenWrite():
    pass

def fnQtFomWinGenCancel():
    QWin.fnWinClose()

def fnQtFomObjAttrGet(
    objRun:EHPyQt.QWget,
    dictObjAttr:dict=None,
    intLayer:int=0
)->dict:
    # <PyFunc: fnQtFomObjAttrGet>
    #    Desc: Get Obj Attrib from FrmObjAttr Widget
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
    # </PyFunc: fnQtFomObjAttrGet>
    if dictObjAttr is None: dictObjAttr={}
    if hasattr(objRun, "strTag"):
        if len(objRun.strTag)>0 :
            dictObjAttr[objRun.strTag]=objRun.strValue
    for intRun in range(len(objRun.children())):
        dictObjAttr= \
            fnQtFomObjAttrGet(
                objRun=objRun.children()[intRun],
                dictObjAttr=dictObjAttr,
                intLayer=intLayer+1
            )
    return dictObjAttr

def fnQWinChildEnum(objRun:EHPyQt.QWget, intLayer:int=0):
    if str(objRun.__module__)==c_strEHPyQtMdlName:
        if hasattr(objRun,c_strPyQtObjParaDictName):
            print('{}{}'.format('  '*intLayer,objRun.strName))
    for intRun in range(len(objRun.children())):
        fnQWinChildEnum(objRun=objRun.children()[intRun], intLayer=intLayer+1)