# EHPyQt.py
# <PyDebug:Wait Develop>
    # Alignment


    # ToolBox
    # Tab Widget
    # Stacked Widget
    # MDI

    # Scroll Bar
    # Slider

    # Progress Bar
    # Horizontal Line
    # Vertical Line

# </PyDebug:Wait Develop>
# <PyDecl:Module Init, Setup DebugMode>
# EHPyQt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import EHSymbolDef
# <PyDecl: Symbol Define & UDE import >
c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor
c_strNewLine = EHSymbolDef.c_strNewLine # '\n'
# </PyDecl: Symbol Define & UDE import >

import EHArray
import EHDate
import EHPyMdl

import sys
import datetime
from datetime import date
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from PyQt6.QtCore import QRect, Qt
# <PyDecl:Symbol Define & UDE import >
from enum import Enum

class udeObjName(Enum):
    udeObjNameWin:str="QMainWindow"
    udeObjNameQWget:str='QWidget'
    udeObjNameLayout:str='QLayout'
    udeObjNameBoxGrp:str="QGroupBox"    # Container
    udeObjNameFrm:str="QFrame"          # Container
    udeObjNameScrArea:str="QScrollArea" # Container
    udeObjNameDock:str="QDockWidget"    # Container
    udeObjNameLbl:str='QLabel'
    udeObjNameEditLn:str='QLineEdit'
    udeObjNameEditTxt:str='QPlainTextEdit'
    udeObjNameEditDate:str="QDateTimeEdit"
    udeObjNameBtn:str='QPushButton'
    udeObjNameBtnTool:str="QToolButton"
    udeObjNameBtnRadio:str="QRadioButton"
    udeObjNameBoxChk:str='QCheckBox'
    udeObjNameBoxSpin:str='QSpinBox'
    udeObjNameBoxCmb:str='QComboBox'
    udeObjNameBoxLst:str="QListWidget"
    udeObjNameBoxTree:str="QTreeWidget"
    udeObjNameBoxTbl:str="QTableWidget"

c_strContainerColl: str=\
    udeObjName.udeObjNameBoxGrp.value + \
    c_strAttrSplitor + udeObjName.udeObjNameFrm.value + \
    c_strAttrSplitor + udeObjName.udeObjNameScrArea.value + \
    c_strAttrSplitor + udeObjName.udeObjNameDock.value

# <PyCmt:QMainWindow; QWin>
class udeScrSizeType(Enum):
    udeScrSizeTypeW:int=1
    udeScrSizeTypeH:int=2

class udeWinPosType(Enum):
    udeWinPosTypeC:int=1
    udeWinPosType0:int=2

class udeSizeMode(Enum):
    udeWinSizeModeFit:int=1
    udeWinSizeModeFull:int=2
    udeWinSizeModeFix:int=3

class udeQtSizePolicy(Enum):
    udeQtSizePolicyPrefer=QtWidgets.QSizePolicy.Policy.Preferred
    udeQtSizePolicyMin=QtWidgets.QSizePolicy.Policy.Minimum
    udeQtSizePolicyMax=QtWidgets.QSizePolicy.Policy.Maximum
    udeQtSizePolicyExp=QtWidgets.QSizePolicy.Policy.Expanding
    udeQtSizePolicyFix=QtWidgets.QSizePolicy.Policy.Fixed
    udeQtSizePolicyMinExp=QtWidgets.QSizePolicy.Policy.MinimumExpanding
    udeQtSizePolicyIgnore=QtWidgets.QSizePolicy.Policy.Ignored

class udeQtLayoutType(Enum):
    udeQtLayoutTypeNA=None
    udeQtLayoutTypeV:QtWidgets.QLayout=QtWidgets.QVBoxLayout # Vertical
    udeQtLayoutTypeH:QtWidgets.QLayout=QtWidgets.QHBoxLayout # Horizontal
    udeQtLayoutTypeG:QtWidgets.QLayout=QtWidgets.QGridLayout # Grid
    udeQtLayoutTypeS:QtWidgets.QLayout=QtWidgets.QStackedLayout # Stacked
    udeQtLayoutTypeF:QtWidgets.QLayout=QtWidgets.QFormLayout # Form;two-column format
    udeQtLayoutTypeB:QtWidgets.QLayout=QtWidgets.QBoxLayout # Box
    udeQtLayoutTypeQ:QtWidgets.QLayout=QtWidgets.QSplitter # Splitter

class udeQtLayoutRoleType(Enum):
    udeQtLayoutRoleTypeNone = None
    udeQtLayoutRoleTypeSpan=QtWidgets.QFormLayout.ItemRole.SpanningRole
    udeQtLayoutRoleTypeLabel=QtWidgets.QFormLayout.ItemRole.LabelRole
    udeQtLayoutRoleTypeField=QtWidgets.QFormLayout.ItemRole.FieldRole

c_strWinName:str='EHQWin'
c_strWinObjName:str=udeObjName.udeObjNameWin.value
c_strWinTitle:str='EHQWin'
c_udeWinLayout:udeQtLayoutType=udeQtLayoutType.udeQtLayoutTypeH
c_udeWinPosType=udeWinPosType.udeWinPosTypeC
c_intWinPosX:int=0
c_intWinPosY:int=0
c_udeWinSizeMode:udeSizeMode=udeSizeMode.udeWinSizeModeFit
c_udeWinSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeWinSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_intWinWidth:int=0
c_intWinHeight:int=0
c_blnWinAlwaysOnTop:bool=False
c_blnWinVisible:bool=True
c_strWinStyleSheet:str=''
# </PyCmt:QMainWindow; QWin>

# <PyCmt: QWidget>
class udeQtAlignment(Enum):
    udeQtAlignmentLeft=QtCore.Qt.AlignmentFlag.AlignLeft
    udeQtAlignmentRight=QtCore.Qt.AlignmentFlag.AlignRight
    udeQtAlignmentHCenter=QtCore.Qt.AlignmentFlag.AlignHCenter
    udeQtAlignmentJustify=QtCore.Qt.AlignmentFlag.AlignJustify
    udeQtAlignmentTop=QtCore.Qt.AlignmentFlag.AlignTop
    udeQtAlignmentBottom=QtCore.Qt.AlignmentFlag.AlignBottom
    udeQtAlignmentVCenter=QtCore.Qt.AlignmentFlag.AlignVCenter

class udeQtFrmShp(Enum):
    udeQtFrmShpNo=QtWidgets.QLabel.Shape.NoFrame
    udeQtFrmShpBox=QtWidgets.QLabel.Shape.Box
    udeQtFrmShpPanel=QtWidgets.QLabel.Shape.Panel
    udeQtFrmShpWinPanel=QtWidgets.QLabel.Shape.WinPanel
    udeQtFrmShpHLine=QtWidgets.QLabel.Shape.HLine
    udeQtFrmShpVLine=QtWidgets.QLabel.Shape.VLine
    udeQtFrmShpStyledPanel=QtWidgets.QLabel.Shape.StyledPanel

class udeQtTextInterAction(Enum):
    udeQtTextInterActionNo=QtCore.Qt.TextInteractionFlag.NoTextInteraction
    udeQtTextInterActionTextSelectableByKeyboard=QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard
    udeQtTextInterActionTextSelectableByMouse=QtCore.Qt.TextInteractionFlag.TextSelectableByMouse
# </PyCmt:QWidget>

# <PyCmt:QWgetCentral>
c_strQWgetName:str='QWgetCentral'
c_strQWgetObjName:str=udeObjName.udeObjNameQWget.value
c_objQWgetLayoutInd:QtWidgets.QLayout=None
c_strQWgetTag:str=''
c_strQWgetStyleSheet:str=''
# </PyCmt:QWgetCentral>

# <PyCmt:QLayout>
class udeQtLayoutSizeConstraint(Enum):
    udeQtLayoutSizeConstraintDft=QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
    udeQtLayoutSizeConstraintNo=QtWidgets.QLayout.SizeConstraint.SetNoConstraint
    udeQtLayoutSizeConstraintMin=QtWidgets.QLayout.SizeConstraint.SetMinimumSize
    udeQtLayoutSizeConstraintMax=QtWidgets.QLayout.SizeConstraint.SetMaximumSize
    udeQtLayoutSizeConstraintFix=QtWidgets.QLayout.SizeConstraint.SetFixedSize
    udeQtLayoutSizeConstraintMinMax=QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize

c_udeLayoutObjName:str=udeObjName.udeObjNameLayout.value
c_udeLayoutType:udeQtLayoutType=udeQtLayoutType.udeQtLayoutTypeV
c_objLayoutInd:QtWidgets.QLayout=None
c_strLayoutTag:str=''
c_udeLayoutSizeConstraint=udeQtLayoutSizeConstraint.udeQtLayoutSizeConstraintMin
c_udeLayoutAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_udeLayoutAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
# </PyCmt:QLayout>

#<PyCmt:QGroupBox; QBoxGrp>
c_strBoxGrpObjName:str=udeObjName.udeObjNameBoxGrp.value
c_objBoxGrpLayoutInd:QtWidgets.QLayout=None
c_strBoxGrpTitle:str=''
c_strBoxGrpTag:str=''
c_blnBoxGrpVisible:bool=True
c_blnBoxGrpEnable:bool=True
c_blnBoxGrpChkable:bool=False
c_strBoxGrpToolTip:str=''
c_udeBoxGrpSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxGrpSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxGrpAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
c_udeBoxGrpAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_strBoxGrpStyleSheet:str=''
#/<PyCmt:QGroupBox; QBoxGrp>

# <PyCmt:QFrame; QFrm>
c_strFrmObjName:str=udeObjName.udeObjNameFrm.value
c_objFrmLayoutInd:QtWidgets.QLayout=None
c_blnFrmVisible:bool=True
c_blnFrmEnable:bool=True
c_strFrmTag:str=''
c_strFrmToolTip:str=''
c_intFrmPosX:int=0
c_intFrmPosY:int=0
c_udeFrmSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeFrmSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_intFrmWidth:int=0
c_intFrmHeight:int=0
c_udeFrmFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpPanel
c_intFrmLineWidth:int=1
c_strFrmStyleSheet:str=''
# </PyCmt:QFrame; QFrm>

# <PyCmt:QScrollArea; QScrArea>
class udeQtScrollBarPolicy(Enum):
    udeQtScrollBarPolicyNone=QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
    udeQtScrollBarPolicyOn=QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn
    udeQtScrollBarPolicyOff=QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    udeQtScrollBarPolicyAsNeed=QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded

c_strScrAreaObjName:str=udeObjName.udeObjNameScrArea.value
c_objScrAreaLayoutInd:QtWidgets.QLayout=None
c_blnScrAreaVisible:bool=True
c_blnScrAreaEnable:bool=True
c_strScrAreaTag:str=''
c_strScrAreaToolTip:str=''
c_intScrAreaPosX:int=0
c_intScrAreaPosY:int=0
c_udeScrAreaSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeScrAreaSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_intScrAreaWidth:int=0
c_intScrAreaHeight:int=0
c_udeScrAreaFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpPanel
c_intScrAreaFrmLineWidth:int=1
c_udeScrAreaScrollBarPolicyH:udeQtScrollBarPolicy=udeQtScrollBarPolicy.udeQtScrollBarPolicyOn
c_udeScrAreaScrollBarPolicyV:udeQtScrollBarPolicy=udeQtScrollBarPolicy.udeQtScrollBarPolicyOn
c_udeScrAreaAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
c_udeScrAreaAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_strScrAreaStyleSheet:str=''
# </PyCmt:QScrollArea; QScrArea>

# <PyCmt:QDockWidget; QDock>
class udeQtDockArea(Enum):
    udeQtDockAreaTop=QtCore.Qt.DockWidgetArea.TopDockWidgetArea
    udeQtDockAreaBottom=QtCore.Qt.DockWidgetArea.BottomDockWidgetArea
    udeQtDockAreaLeft=QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
    udeQtDockAreaRight=QtCore.Qt.DockWidgetArea.RightDockWidgetArea

c_strDockObjName:str=udeObjName.udeObjNameDock.value
c_objDockLayoutInd:QtWidgets.QLayout=None
c_strDockTitle:str=''
c_strDockTag:str=''
c_blnDockVisible:bool=True
c_blnDockEnable:bool=True
c_blnDockClosable:bool=True
c_blnDockMovable:bool=True
c_blnDockFloatable:bool=True
c_blnDockDockAreaTop:bool=True
c_blnDockDockAreaBottom:bool=True
c_blnDockDockAreaLeft:bool=True
c_blnDockDockAreaRight:bool=True
c_udeDockArea:udeQtDockArea=udeQtDockArea.udeQtDockAreaLeft
c_intDockWidth:int=0
c_intDockHeight:int=0
c_udeDockSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeDockSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_strDockToolTip:str=''
c_strDockStyleSheet:str=''
# <PyCmt:QDockWidget; QDock>

# <PyCmt:QLabel; QLbl>
c_strLblObjName:str=udeObjName.udeObjNameLbl.value
c_objLblLayoutInd:QtWidgets.QLayout=None
c_strLblText:str=''
c_strLblTag:str=''
c_blnLblVisible:bool=True
c_blnLblWordWrap:bool=False
c_intLblIndent:int=0
c_udeLblTextInterAction:udeQtTextInterAction=udeQtTextInterAction.udeQtTextInterActionTextSelectableByMouse
c_blnLblAutoSize:bool=True
c_udeLblFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpNo
c_udeLblLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeLabel
c_udeLblSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeLblSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeLblAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
c_udeLblAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_strLblStyleSheet:str=''
# </PyCmt:QLabel; QLbl>

# <PyCmt:QLineEdit; QEditLn>
c_strEditLnObjName:str=udeObjName.udeObjNameEditLn.value
c_objEditLnLayoutInd:QtWidgets.QLayout=None
c_strEditLnText:str=''
c_strEditLnTag:str=''
c_blnEditLnVisible:bool=True
c_blnEditLnEnable:bool=True
c_blnEditLnReadOnly:bool=False
c_blnEditLnPwd:bool=False
c_intEditLnLenMax:int=0
c_strEditLnToolTip:str=''
c_udeEditLnLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeEditLnSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeEditLnSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyFix
c_udeEditLnAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
c_udeEditLnAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_strEditLnStyleSheet:str=''
# </PyCmt:QLineEdit; QEditLn>

# <PyCmt:QPlainTextEdit; QEditTxt>
c_strEditTxtObjName:str=udeObjName.udeObjNameEditTxt.value
c_objEditTxtLayoutInd:QtWidgets.QLayout=None
c_strEditTxtText:str=''
c_strEditTxtTag:str=''
c_blnEditTxtVisible:bool=True
c_blnEditTxtEnable:bool=True
c_blnEditTxtReadOnly:bool=False
c_blnEditTxtSizeGrip:bool=False
c_intEditTxtHeight:int=22
c_strEditTxtToolTip:str=''
c_udeEditTxtLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeEditTxtSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeEditTxtSizePolicyV=udeQtSizePolicy.udeQtSizePolicyMin
c_udeEditTxtFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpStyledPanel
c_strEditTxtStyleSheet:str=''
# </PyCmt:QPlainTextEdit; QEditTxt>

# <PyCmt:QDateTimeEdit; QEditDate>
c_strEditDateObjName:str=udeObjName.udeObjNameEditDate.value
c_objEditDateLayoutInd:QtWidgets.QLayout=None
c_dateEditDateRun:date=datetime.datetime.now()
c_dateEditDateMin:date=datetime.date(1900, 1, 1)
c_dateEditDateMax:date=datetime.date(2100, 1, 1)
c_strEditDateTag:str=''
c_blnEditDateDateTimeMode:bool=False
c_blnEditDateVisible:bool=True
c_blnEditDateEnable:bool=True
c_blnEditDateReadOnly:bool=False
c_strEditDateToolTip:str=''
c_udeEditDateLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeEditDateSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeEditDateSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeEditDateAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
c_udeEditDateAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_strEditDateStyleSheet:str=''
c_strEditDateMethChg:str=''
# </PyCmt:QDateTimeEdit; QEditDate>

# <PyCmt:QPushButton; QBtn>
c_strBtnObjName:str=udeObjName.udeObjNameBtn.value
c_objBtnLayoutInd:QtWidgets.QLayout=None
c_strBtnCaption:str=''
c_blnBtnValue:bool=False
c_strBtnTag:str=''
c_blnBtnVisible:bool=True
c_blnBtnEnable:bool=True
c_blnBtnChkable:bool=False
c_blnBtnAutoFft:bool=False
c_blnBtnFlat:bool=False
c_strBtnToolTip:str=''
c_udeBtnLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBtnSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBtnSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_strBtnStyleSheet:str=''
c_strBtnMethClick:str=''
# </PyCmt:QPushButton; QBtn>

# <PyCmt:QToolButton; QBtnTool>
class udeQtToolButtonPopupMode(Enum):
    udeQtToolButtonPopupModeNone=''
    udeQtToolButtonPopupModeDelayed=QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup
    udeQtToolButtonPopupModeMenu=QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup
    udeQtToolButtonPopupModeInstant=QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup

class udeQtToolButtonArrowType(Enum):
    udeQtToolButtonArrowTypeNoArrow=QtCore.Qt.ArrowType.NoArrow
    udeQtToolButtonArrowTypeUpArrow=QtCore.Qt.ArrowType.UpArrow
    udeQtToolButtonArrowTypeDownArrow=QtCore.Qt.ArrowType.DownArrow
    udeQtToolButtonArrowTypeLeftArrow=QtCore.Qt.ArrowType.LeftArrow
    udeQtToolButtonArrowTypeRightArrow=QtCore.Qt.ArrowType.RightArrow

c_strBtnToolObjName:str=udeObjName.udeObjNameBtnTool.value
c_objBtnToolLayoutInd:QtWidgets.QLayout=None
c_strBtnToolCaption:str='...'
c_blnBtnToolValue:bool=False
c_strBtnToolTag:str=''
c_blnBtnToolVisible:bool=True
c_blnBtnToolEnable:bool=True
c_blnBtnToolChkable:bool=False
c_strBtnToolToolTip:str=''
c_udeBtnToolLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBtnToolPopupMode:udeQtToolButtonPopupMode=udeQtToolButtonPopupMode.udeQtToolButtonPopupModeDelayed
c_udeBtnToolArrowType:udeQtToolButtonArrowType=udeQtToolButtonArrowType.udeQtToolButtonArrowTypeNoArrow
c_udeSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_strBtnToolStyleSheet:str=''
c_strBtnToolMethClick:str=''
# </PyCmt:QToolButton; QBtnTool>
    
# <PyCmt:QRadioButton; QBtnRadio>
c_strBtnRadioObjName:str=udeObjName.udeObjNameBtnRadio.value
c_objBtnRadioLayoutInd:QtWidgets.QLayout=None
c_strBtnRadioCaption:str=''
c_blnBtnRadioValue:bool=False
c_strBoxRadioTag:str=''
c_blnBtnRadioVisible:bool=True
c_blnBtnRadioEnable:bool=True
c_blnBtnRadioChkable:bool=False
c_strBtnRadioToolTip:str=''
c_udeBtnRadioLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBtnRadioSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBtnRadioSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_strBtnRadioStyleSheet:str=''
c_strBtnRadioMethClick:str=''
# </PyCmt:QRadioButton; QBtnRadio>

# <PyCmt:QCheckBox; QBoxChk>
c_strBoxChkObjName:str=udeObjName.udeObjNameBoxChk.value
c_objBoxChkLayoutInd:QtWidgets.QLayout=None
c_strBoxCkhCaption:str=''
c_blnBoxChkValue:bool=False
c_strBoxChkTag:str=''
c_blnBoxChkVisible:bool=True
c_blnBoxChkEnable:bool=True
c_blnBoxChkChkable:bool=False
c_strBoxChkToolTip:str=''
c_udeBoxChkLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBoxChkSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxChkSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_strBoxChkStyleSheet:str=''
c_strBoxChkMethStateChg:str=''
# </PyCmt:QCheckBox; QBoxChk>

# <PyCmt:QSpinBox; QBoxSpin>
c_strBoxSpinObjName:str=udeObjName.udeObjNameBoxSpin.value
c_objBoxSpinLayoutInd:QtWidgets.QLayout=None
c_intBoxSpinValue:int=0
c_intBoxSpinValueMin:int=0
c_intBoxSpinValueMax:int=999999999
c_strBoxSpinTag:str=''
c_blnBoxSpinVisible:bool=True
c_blnBoxSpinEnable:bool=True
c_strBoxSpinToolTip:str=''
c_udeBoxSpinLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBoxSpinSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxSpinSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxSpinAlignmentH:udeQtAlignment=udeQtAlignment.udeQtAlignmentLeft
c_udeBoxSpinAlignmentV:udeQtAlignment=udeQtAlignment.udeQtAlignmentTop
c_strBoxSpinStyleSheet:str=''
c_strBoxSpinMethValueChg:str=''
# </PyCmt:QSpinBox; QBoxSpin>

# <PyCmt:QComboBox; QBoxCmb>
c_strBoxCmbObjName:str=udeObjName.udeObjNameBoxCmb.value
c_objBoxCmbLayoutInd:QtWidgets.QLayout=None
c_lstBoxCmbItem:list=None
c_strBoxCmbValue:str=''
c_strBoxCmbTag:str=''
c_blnBoxCmbVisible:bool=True
c_blnBoxCmbEnable:bool=True
c_blnBoxCmbEditable:bool=True
c_strBoxCmbToolTip:str=''
c_udeBoxCmbLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBoxCmbSizePolicyH=udeQtSizePolicy.udeQtSizePolicyMinExp
c_udeBoxCmbSizePolicyV=udeQtSizePolicy.udeQtSizePolicyExp
c_strBoxCmbStyleSheet:str=''
c_strBoxCmbMethIndexChg:str=''
c_strBoxCmbMethTextChg:str=''
# </PyCmt:QComboBox; QBoxCmb>

#<PyCmt:QListWidget; QBoxLst>
c_strBoxLstObjName:str=udeObjName.udeObjNameBoxLst.value
c_objBoxLstLayoutInd:QtWidgets.QLayout=None
c_lstBoxLstItem:list=None
c_strBoxLstValue:str=''
c_strBoxLstTag:str=''
c_blnBoxLstVisible:bool=True
c_blnBoxLstEnable:bool=True
c_blnBoxLstSeltRect:bool=True
c_strBoxLstToolTip:str=''
c_udeBoxLstLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBoxLstSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxLstSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxLstFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpStyledPanel
c_strBoxLstStyleSheet:str=''
c_strBoxLstMethItmChg:str=''
 #</PyCmt:QListWidget; QBoxLst>

#<PyCmt:QTreeWidget; QBoxTree>
class udeQtBoxTreeDragDropMode(Enum):
    udeQtBoxTreeDragDropModeNone=QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop
    udeQtBoxTreeDragDropModeDrag=QtWidgets.QAbstractItemView.DragDropMode.DragOnly
    udeQtBoxTreeDragDropModeDrop=QtWidgets.QAbstractItemView.DragDropMode.DragOnly
    udeQtBoxTreeDragDropModeDragDrop=QtWidgets.QAbstractItemView.DragDropMode.DragDrop

class udeQtBoxTreeSeltMode(Enum):
    udeQtBoxTreeSeltModeNone=QtWidgets.QAbstractItemView.SelectionMode.NoSelection
    udeQtBoxTreeSeltModeSgn=QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
    udeQtBoxTreeSeltModeMulti=QtWidgets.QAbstractItemView.SelectionMode.MultiSelection
    udeQtBoxTreeSeltModeExt=QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection
    udeQtBoxTreeSeltModeCont=QtWidgets.QAbstractItemView.SelectionMode.ContiguousSelection

class udeQtTextElideMode(Enum):
    udeQtTextElideModeNone=QtCore.Qt.TextElideMode.ElideNone
    udeQtTextElideModeElideLeft=QtCore.Qt.TextElideMode.ElideLeft
    udeQtTextElideModeElideRight=QtCore.Qt.TextElideMode.ElideRight
    udeQtTextElideModeElideMid=QtCore.Qt.TextElideMode.ElideMiddle

c_strBoxTreeObjName:str=udeObjName.udeObjNameBoxTree.value
c_objBoxTreeLayoutInd:QtWidgets.QLayout=None
c_lstBoxTreeTitleRow:list=None
c_intBoxTreeRowCount:int=-1
c_intBoxTreeColCount:int=-1
c_intBoxTreeColKey:int=0
c_lstBoxTreeItem:list=None
c_blnBoxTreeSortingEnabled:bool=False
c_blnBoxTreeDblClick:bool=True
c_blnBoxTreeKeyPress:bool=False
c_blnBoxTreeDragEnable:bool=False
c_udeBoxTreeDragDropMode:udeQtBoxTreeDragDropMode=udeQtBoxTreeDragDropMode.udeQtBoxTreeDragDropModeNone
c_blnBoxTreeRowColor:bool=False
c_udeBoxTreeSeltMode:udeQtBoxTreeSeltMode=udeQtBoxTreeSeltMode.udeQtBoxTreeSeltModeSgn
c_udeBoxTreeTextElideMode:udeQtTextElideMode=udeQtTextElideMode.udeQtTextElideModeElideRight
c_intBoxTreeIndentation:int=10
c_blnBoxTreeHeaderVisible:bool=True
c_intBoxTreeRowSelt:int=0
c_strBoxTreeTag:str=''
c_blnBoxTreeVisible:bool=True
c_blnBoxTreeEnable:bool=True
c_strBoxTreeToolTip:str=''
c_udeBoxTreeLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBoxTreeSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxTreeSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_blnBoxTreeMinSizeCol:bool=True
c_udeBoxTreeFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpStyledPanel
c_strBoxTreeStyleSheet:str=''

c_strBoxTreeSplitor:str='.'
#</PyCmt:QTreeWidget; QBoxTree>

# <PyCmt:QTableWidget; QBoxTbl>
class udeQtBoxTblSeltMode(Enum):
    udeQtBoxTblSeltModeNone=QtWidgets.QAbstractItemView.SelectionMode.NoSelection
    udeQtBoxTblSeltModeSingle=QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
    udeQtBoxTblSeltModeMulti=QtWidgets.QAbstractItemView.SelectionMode.MultiSelection
    udeQtBoxTblSeltModeExt=QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection
    udeQtBoxTblSeltModeCont=QtWidgets.QAbstractItemView.SelectionMode.ContiguousSelection

c_strBoxTblObjName:str=udeObjName.udeObjNameBoxTbl.value
c_objBoxTblLayoutInd:QtWidgets.QLayout=None
c_lstBoxTblTitleRow:list=None
c_lstBoxTblTitleCol:list=None
c_intBoxTblRowCount:int=-1
c_intBoxTblColCount:int=-1
c_lstBoxTblItem:list=None
c_intBoxTblSeltRow:int=-1
c_strBoxTblTag:str=''
c_blnBoxTblVisible:bool=True
c_blnBoxTblEnable:bool=True
c_udeBoxTblSeltMode:udeQtBoxTblSeltMode=udeQtBoxTblSeltMode.udeQtBoxTblSeltModeSingle
c_strBoxTblToolTip:str=''
c_udeBoxTblLayoutRoleType:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeField
c_udeBoxTblSizePolicyH:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxTblSizePolicyV:udeQtSizePolicy=udeQtSizePolicy.udeQtSizePolicyMin
c_udeBoxTblFrmShp:udeQtFrmShp=udeQtFrmShp.udeQtFrmShpStyledPanel
c_strBoxTblStyleSheet:str=''
# </PyCmt:QTableWidget; QBoxTbl>

dictObjParaQWin:dict=\
    {
        'objParent':None,
        'strName':c_strWinName,
        'strObjName':c_strWinObjName,
        'strTitle':c_strWinTitle,
        'udeQtLayoutType':c_udeWinLayout,
        'udeWinPosType':c_udeWinPosType,
        'intPosX':c_intWinPosX,
        'intPosY':c_intWinPosY,
        'udeSizeMode':c_udeWinSizeMode,
        'udeQtSizePolicyH':c_udeWinSizePolicyH,
        'udeQtSizePolicyV':c_udeWinSizePolicyV,
        'intWidth':c_intWinWidth,
        'intHeight':c_intWinHeight,
        'blnAlwaysOnTop':c_blnWinAlwaysOnTop,
        'blnVisible':c_blnWinVisible,
        'strStyleSheet':c_strWinStyleSheet
    }
dictObjParaQWget:dict=\
    {
        'objParent':None,
        'strName':c_strQWgetName,
        'strObjName':c_strQWgetObjName,
        'objLayoutInd':c_objQWgetLayoutInd,
        'strTag':c_strQWgetTag,
        'strStyleSheet':c_strQWgetStyleSheet
    }
dictObjParaQLayout:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_udeLayoutObjName,
        'udeQtLayoutType':c_udeLayoutType,
        'objLayoutInd':c_objLayoutInd,
        'strTag': c_strLayoutTag,
        'udeQtLayoutSizeConstraint':c_udeLayoutSizeConstraint,
        'udeQtAlignmentH':c_udeLayoutAlignmentH,
        'udeQtAlignmentV':c_udeLayoutAlignmentV
    }
dictObjParaQBoxGrp:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxGrpObjName,
        'objLayoutInd':c_objBoxGrpLayoutInd,
        'strTitle':c_strBoxGrpTitle,
        'strTag': c_strBoxGrpTag,
        'blnVisible':c_blnBoxGrpVisible,
        'blnEnable':c_blnBoxGrpEnable,
        'blnChkable':c_blnBoxGrpChkable,
        'strToolTip':c_strBoxGrpToolTip,
        'udeQtSizePolicyH':c_udeBoxGrpSizePolicyH.value,
        'udeQtSizePolicyV':c_udeBoxGrpSizePolicyV.value,
        'udeQtAlignmentH':c_udeBoxGrpAlignmentH.value,
        'udeQtAlignmentV':c_udeBoxGrpAlignmentV.value,
        'strStyleSheet':c_strBoxGrpStyleSheet
    }
dictObjParaQFrm:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strFrmObjName,
        'objLayoutInd':c_objFrmLayoutInd,
        'blnVisible':c_blnFrmVisible,
        'blnEnable':c_blnFrmEnable,
        'strTag': c_strFrmTag,
        'strToolTip':c_strFrmToolTip,
        'c_intFrmPosX':c_intFrmPosX,
        'c_intFrmPosY':c_intFrmPosY,
        'udeFrmSizePolicyH':c_udeFrmSizePolicyH.value,
        'udeFrmSizePolicyV':c_udeFrmSizePolicyV.value,
        'c_intFrmWidth':c_intFrmWidth,
        'c_intFrmHeight':c_intFrmHeight,
        'udeFrmShp':c_udeFrmFrmShp.value,
        'intFrmLineWidth':c_intFrmLineWidth,
        'strStyleSheet':c_strFrmStyleSheet
    }
dictObjParaQScrArea:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strScrAreaObjName,
        'objLayoutInd':c_objScrAreaLayoutInd,
        'blnVisible':c_blnScrAreaVisible,
        'blnEnable':c_blnScrAreaEnable,
        'strTag': c_strScrAreaTag,
        'strToolTip':c_strScrAreaToolTip,
        'ScrAreaPosX':c_intScrAreaPosX,
        'ScrAreaPosY':c_intScrAreaPosY,
        'udeFrmSizePolicyH':c_udeScrAreaSizePolicyH.value,
        'udeFrmSizePolicyV':c_udeScrAreaSizePolicyV.value,
        'intWidth':c_intScrAreaWidth,
        'intHeight':c_intScrAreaHeight,
        'udeFrmShp':c_udeScrAreaFrmShp.value,
        'intFrmLineWidth':c_intScrAreaFrmLineWidth,
        'udeScrollBarPolicyH':c_udeScrAreaScrollBarPolicyH.value,
        'udeScrollBarPolicyV':c_udeScrAreaScrollBarPolicyV.value    ,
        'udeQtAlignmentH':c_udeScrAreaAlignmentH.value,
        'udeQtAlignmentV':c_udeScrAreaAlignmentV.value,
        'strStyleSheet':c_strScrAreaStyleSheet
    }
dictObjParaQDock:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strDockObjName,
        'objLayoutInd':c_objDockLayoutInd,
        'strTitle':c_strDockTitle,
        'strTag': c_strDockTag,
        'blnVisible':c_blnDockVisible,
        'blnEnable':c_blnDockEnable,
        'blnClosable':c_blnDockClosable,
        'blnMovable':c_blnDockMovable,
        'blnFloatable':c_blnDockFloatable,
        'blnDockAreaTop':c_blnDockDockAreaTop,
        'blnDockAreaBottom':c_blnDockDockAreaBottom,
        'blnDockAreaLeft':c_blnDockDockAreaLeft,
        'blnDockAreaRight':c_blnDockDockAreaRight,
        'udeDockArea':c_udeDockArea.value,
        'udeQtSizePolicyH':c_udeDockSizePolicyH.value,
        'udeQtSizePolicyV':c_udeDockSizePolicyV.value,
        'intWidth':c_intDockWidth,
        'intHeight':c_intDockHeight,
        'strToolTip':c_strDockToolTip,
        'strStyleSheet':c_strDockStyleSheet
    }
dictObjParaQLbl:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strLblObjName,
        'objLayoutInd':c_objLblLayoutInd,
        'strText':c_strLblText,
        'strTag': c_strLblTag,
        'blnVisible':c_blnLblVisible,
        'blnWordWrap':c_blnLblWordWrap,
        'intIndent':c_intLblIndent,
        'udeLblTextInterAction':c_udeLblTextInterAction.value,
        'blnAutoSize':c_blnLblAutoSize,
        'udeFrmShp':c_udeLblFrmShp.value,
        'udeQtSizePolicyH':c_udeLblSizePolicyH.value,
        'udeQtSizePolicyV':c_udeLblSizePolicyV.value,
        'udeQtAlignmentH':c_udeLblAlignmentH.value,
        'udeQtAlignmentV':c_udeLblAlignmentV.value,
        'strStyleSheet':c_strLblStyleSheet
    }
dictObjParaQEditLn:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strEditLnObjName,
        'strText':c_strEditLnText,
        'strTag': c_strEditLnTag,
        'blnVisible':c_blnEditLnVisible,
        'blnEnable':c_blnEditLnEnable,
        'blnReadOnly':c_blnEditLnReadOnly,
        'blnPwd':c_blnEditLnPwd,
        'intLenMax':c_intEditLnLenMax,
        'strToolTip':c_strEditLnToolTip,
        'udeQtSizePolicyH':c_udeEditLnSizePolicyH.value,
        'udeQtSizePolicyV':c_udeEditLnSizePolicyV.value,
        'udeQtAlignmentH':c_udeEditLnAlignmentH.value,
        'udeQtAlignmentV':c_udeEditLnAlignmentV.value,
        'strStyleSheet':c_strEditLnStyleSheet
    }
dictObjParaQEditTxt:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strEditTxtObjName,
        'objLayoutInd':c_objEditTxtLayoutInd,
        'strText':c_strEditTxtText,
        'strTag': c_strEditTxtTag,
        'blnVisible':c_blnEditTxtVisible,
        'blnEnable':c_blnEditTxtEnable,
        'blnReadOnly':c_blnEditTxtReadOnly,
        'blnSizeGrip':c_blnEditTxtSizeGrip,
        'strToolTip':c_strEditTxtToolTip,
        'udeQtSizePolicyH':c_udeEditTxtSizePolicyH.value,
        'udeQtSizePolicyV':c_udeEditTxtSizePolicyV.value,
        'udeFrmShp':c_udeEditTxtFrmShp.value,
        'strStyleSheet':c_strEditTxtStyleSheet
}
dictObjParaQEditDate:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strEditDateObjName,
        'objLayoutInd':c_objEditDateLayoutInd,
        'dateRun':c_dateEditDateRun,
        'dateMin':c_dateEditDateMin,
        'dateMax':c_dateEditDateMax,
        'strTag': c_strEditDateTag,
        'blnDateTimeMode':c_blnEditDateDateTimeMode,
        'blnVisible':c_blnEditDateVisible,
        'blnEnable':c_blnEditDateEnable,
        'blnReadOnly':c_blnEditDateReadOnly,
        'strToolTip':c_strEditDateToolTip,
        'udeQtSizePolicyH':c_udeEditDateSizePolicyH.value,
        'udeQtSizePolicyV':c_udeEditDateSizePolicyV.value,
        'udeQtAlignmentH':c_udeEditDateAlignmentH.value,
        'udeQtAlignmentV':c_udeEditDateAlignmentV.value,
        'strStyleSheet':c_strEditDateStyleSheet
    }
dictObjParaQBtn:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBtnObjName,
        'objLayoutInd':c_objBtnLayoutInd,
        'strCaption':c_strBtnCaption,
        'strTag': c_strBtnTag,
        'blnVisible':c_blnBtnVisible,
        'blnEnable':c_blnBtnEnable,
        'blnAutoDft':c_blnBtnAutoFft,
        'blnFlat':c_blnBtnFlat,
        'strToolTip':c_strBtnToolTip,
        'udePolicyH':c_udeBtnSizePolicyH.value,
        'udePolicyV':c_udeBtnSizePolicyV.value,
        'strStyleSheet':c_strBtnStyleSheet
    }
dictObjParaQBtnTool:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBtnToolObjName,
        'objLayoutInd':c_objBtnToolLayoutInd,
        'strCaption':c_strBtnToolCaption,
        'strTag': c_strBtnTag,
        'blnVisible':c_blnBtnToolVisible,
        'blnEnable':c_blnBtnToolEnable,
        'blnChkable':c_blnBtnToolChkable,
        'strToolTip':c_strBtnToolToolTip,
        'udePopupMode':c_udeBtnToolPopupMode.value,
        'udeArrowType':c_udeBtnToolArrowType.value,
        'udeQtSizePolicyH':c_udeSizePolicyH.value,
        'udeQtSizePolicyV':c_udeSizePolicyV.value,
        'strStyleSheet':c_strBtnToolStyleSheet
    }
dictObjParaQBtnRadio:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBtnRadioObjName,
        'objLayoutInd':c_objBtnRadioLayoutInd,
        'strCaption':c_strBtnRadioCaption,
        'blnValue':c_blnBtnRadioValue,
        'strTag': c_strBoxRadioTag,
        'blnVisible':c_blnBtnRadioVisible,
        'blnEnable':c_blnBtnRadioEnable,
        'blnChkable':c_blnBtnRadioChkable,
        'strToolTip':c_strBtnRadioToolTip,
        'udeQtSizePolicyH':c_udeSizePolicyH.value,
        'udeQtSizePolicyV':c_udeSizePolicyV.value,
        'strStyleSheet':c_strBtnRadioStyleSheet
    }
dictObjParaQBoxChk:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxChkObjName,
        'objLayoutInd':c_objBoxChkLayoutInd,
        'strCaption':c_strBoxCkhCaption,
        'blnValue':c_blnBoxChkValue,
        'strTag': c_strBoxChkTag,
        'blnVisible':c_blnBoxChkVisible,
        'blnEnable':c_blnBoxChkEnable,
        'blnChkable':c_blnBoxChkChkable,
        'strToolTip':c_strBoxChkToolTip,
        'udeQtSizePolicyH':c_udeBoxChkSizePolicyH,
        'udeQtSizePolicyV':c_udeBoxChkSizePolicyV,
        'strStyleSheet':c_strBoxChkStyleSheet
    }
dictObjParaQBoxSpin:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxSpinObjName,
        'objLayoutInd':c_objBoxSpinLayoutInd,
        'intValue':c_intBoxSpinValue,
        'intValueMin':c_intBoxSpinValueMin,
        'intValueMax':c_intBoxSpinValueMax,
        'strTag': c_strBoxSpinTag,
        'blnVisible':c_blnBoxSpinVisible,
        'blnEnable':c_blnBoxSpinEnable,
        'strToolTip':c_strBoxSpinToolTip,
        'udeQtSizePolicyH':c_udeBoxSpinSizePolicyH.value,
        'udeQtSizePolicyV':c_udeBoxSpinSizePolicyV.value,
        'udeQtAlignmentH':c_udeBoxSpinAlignmentH.value,
        'udeQtAlignmentV':c_udeBoxSpinAlignmentV.value,
        'strStyleSheet':c_strBoxSpinStyleSheet
    }
dictObjParaQBoxCmb:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxCmbObjName,
        'objLayoutInd':c_objBoxCmbLayoutInd,
        'lstItem':c_lstBoxCmbItem,
        'strValue':c_strBoxCmbValue,
        'strTag': c_strBoxCmbTag,
        'blnVisible':c_blnBoxCmbVisible,
        'blnEnable':c_blnBoxCmbEnable,
        'blnEditable':c_blnBoxCmbEditable,
        'strToolTip':c_strBoxCmbToolTip,
        'udeQtSizePolicyH':c_udeBoxCmbSizePolicyH,
        'udeQtSizePolicyV':c_udeBoxCmbSizePolicyV,
        'strStyleSheet':c_strBoxCmbStyleSheet
    }
dictObjParaQBoxLst:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxLstObjName,
        'objLayoutInd':c_objBoxLstLayoutInd,
        'lstItem':c_lstBoxLstItem,
        'strValue':c_strBoxLstValue,
        'strTag': c_strBoxLstTag,
        'blnVisible':c_blnBoxLstVisible,
        'blnEnable':c_blnBoxLstEnable,
        'blnSeltRect':c_blnBoxLstSeltRect,
        'strToolTip':c_strBoxLstToolTip,
        'udeQtSizePolicyH':c_udeBoxLstSizePolicyH.value,
        'udeQtSizePolicyV':c_udeBoxLstSizePolicyV.value,
        'udeFrmShp':c_udeBoxLstFrmShp.value,
        'strStyleSheet':c_strBoxLstStyleSheet
    }
dictObjParaQBoxTree:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxTreeObjName,
        'objLayoutInd':c_objBoxTreeLayoutInd,
        'lstTitleRow':c_lstBoxTreeTitleRow,
        'intRowCount':c_intBoxTreeRowCount,
        'intColCount':c_intBoxTreeColCount,
        'lstItem':c_lstBoxTreeItem,
        'blnSortingEnabled':c_blnBoxTreeSortingEnabled,
        'blnEditDblClick':c_blnBoxTreeDblClick,
        'blnEditKeyPress':c_blnBoxTreeKeyPress,
        'blnDragEnable':c_blnBoxTreeDragEnable,
        'udeDragDropMode':c_udeBoxTreeDragDropMode.value,
        'blnRowColor':c_blnBoxTreeRowColor,
        'udeSeltMode':c_udeBoxTreeSeltMode.value,
        'udeTextElideMode':c_udeBoxTreeTextElideMode.value,
        'intIndentation':c_intBoxTreeIndentation,
        'blnHeaderVisible':c_blnBoxTreeHeaderVisible,
        'intRowSelt':c_intBoxTreeRowSelt,
        'strTag': c_strBoxTreeTag,
        'blnVisible':c_blnBoxTreeVisible,
        'blnEnable':c_blnBoxTreeEnable,
        'strToolTip':c_strBoxTreeToolTip,
        'udeQtSizePolicyH':c_udeBoxTreeSizePolicyH.value,
        'udeQtSizePolicyV':c_udeBoxTreeSizePolicyV.value,
        'blnMinSizeCol':c_blnBoxTreeMinSizeCol,
        'udeFrmShp':c_udeBoxTreeFrmShp.value,
        'strStyleSheet':c_strBoxTreeStyleSheet
    }
dictObjParaQBoxTbl:dict=\
    {
        'objParent':None,
        'strName':'',
        'strObjName':c_strBoxTblObjName,
        'objLayoutInd':c_objBoxTblLayoutInd,
        'lstTitleRow':c_lstBoxTblTitleRow,
        'lstTitleCol':c_lstBoxTblTitleCol,
        'intRowCount':c_intBoxTblRowCount,
        'intColCount':c_intBoxTblColCount,
        'lstItem':c_lstBoxTblItem,
        'intSeltRow':c_intBoxTblSeltRow,
        'strTag': c_strBoxTblTag,
        'blnVisible':c_blnBoxTblVisible,
        'blnEnable':c_blnBoxTblEnable,
        'udeSeltMode':c_udeBoxTblSeltMode.value,
        'strToolTip':c_strBoxTblToolTip,
        'udeQtSizePolicyH':c_udeBoxTblSizePolicyH.value,
        'udeQtSizePolicyV':c_udeBoxTblSizePolicyV.value,
        'udeFrmShp':c_udeBoxTblFrmShp.value,
        'strStyleSheet':c_strBoxTblStyleSheet
    }
# </PyDecl:Symbol Define & UDE import >
# <PyCmt: RunTime>
s_lstEHPyQtUdeColl:list=[]
# </PyCmt: RunTime>
# <PyCmt:QApp>
class QApp(object):
    _instance = None

    def __new__(cls):
        # <PyCmt: QApp only allow one instance in RunTime>
        if not cls._instance:
            cls._instance = QtWidgets.QApplication(sys.argv)
        return cls._instance
# </PyCmt:QApp>

# <PyCmt:QWget>
class QWget(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args)
# </PyCmt:QWget>

# <PyCmt:QWin>
class QWin(QtWidgets.QMainWindow):
    # <PyCmt:QWidget & QLayout Notice>
    # 1. it has to add a QWidget for QMainWindow
    # 2. if Add QLayout for QMainWindow, the Parent of Layout have to be the QWidget
    def __init__(
        self,
        objParent:object=None,
        strName:str=c_strWinName,
        strObjName:str=c_strWinObjName,
        strTitle:str=c_strWinTitle,
        udeLayoutType:udeQtLayoutType=c_udeWinLayout,
        udeWinPosType=c_udeWinPosType,
        intPosX:int=c_intWinPosX,
        intPosY:int=c_intWinPosY,
        udeSizeMode=c_udeWinSizeMode,
        udeSizePolicyH:udeQtSizePolicy=c_udeWinSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeWinSizePolicyV,
        intWidth:int=c_intWinWidth,
        intHeight:int=c_intWinHeight,
        blnAlwaysOnTop:bool=c_blnWinAlwaysOnTop,
        blnVisible:bool=c_blnWinVisible,
        strStyleSheet:str=c_strWinStyleSheet
    ):
        self.QApp=QApp()
        super().__init__()

        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.strTitle=strTitle
        self.udeLayoutType=udeLayoutType
        self.udeWinPosType=udeWinPosType
        self.intPosX=intPosX
        self.intPosY=intPosY
        self.udeSizeMode=udeSizeMode
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.intWidth=intWidth
        self.intHeight=intHeight
        self.blnAlwaysOnTop=blnAlwaysOnTop
        self.blnVisible=blnVisible
        self.strStyleSheet=strStyleSheet

        self.fnName(strName)
        self.fnTitle(strTitle)

        # <PyCmt:QMainWindow needs to assign QWidget>
        self.QWgetCentral=None
        self.fnWinQWget(strName='QWinQCentralWget')
        self.layout=None
        self.objLayout = None
        self.fnLayout(self.udeLayoutType)

        self.fnPos(
            udeWinPosType=self.udeWinPosType,
            intPosX=self.intPosX,
            intPosY=self.intPosY
        )

        self.fnSize(
            udeSizeMode=self.udeSizeMode,
            udeSizePolicyH=self.udeSizePolicyH,
            udeSizePolicyV=self.udeSizePolicyV,
            intWidth=self.intWidth,
            intHeight=self.intHeight
        )
        self.fnWinAlwaysOnTop(self.blnAlwaysOnTop)
        self.fnStyleSheet(self.strStyleSheet)
        # self.fnWinVisible()

    def fnWinQWget(self, strName):
        self.QWgetCentral=\
            QWgetCentral(
                objParent=self,
                strName=strName
            )
        self.setCentralWidget(self.QWgetCentral)

    def fnName(self,strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnTitle(self, strTitle:str=c_strWinTitle):
        self.strTitle=strTitle
        self.setWindowTitle(strTitle)

    def fnLayout(
        self,
        udeLayoutType:udeQtLayoutType
    ):
        #<PyCmt:self.QWgetCentral.layout objParent must be self.QWgetCentral>
        self.QWgetCentral.layout=\
            QLayout(
                objParent=self.QWgetCentral,
                strName=self.strName+udeObjName.udeObjNameLayout.value,
                udeLayoutType=udeLayoutType,
                udeLayoutSizeConstraint=udeQtLayoutSizeConstraint.udeQtLayoutSizeConstraintMin
            ).layout
        self.layout = self.QWgetCentral.layout

        if udeLayoutType==udeQtLayoutType.udeQtLayoutTypeS:
            self.QWgetCentral.layout.setContentsMargins(0,0,0,0)
            self.QWgetCentral.layout.setSpacing(0)
            self.QWgetCentral.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    def fnPos(
        self,
        udeWinPosType:udeWinPosType,
        intPosX:int,
        intPosY:int
    ):
        udeWinPosType=fnStrValueCvrt(udeWinPosType)
        if udeWinPosType is None: udeWinPosType=c_udeWinPosType

        if udeWinPosType==udeWinPosType.udeWinPosTypeC:
            self.fnCenter(self)
        elif udeWinPosType==udeWinPosType.udeWinPosType0:
            self.move(0, 0)
        else:
            self.move(intPosX, intPosY)
        self.intPosX=self.x()
        self.intPosY=self.y()

    @staticmethod
    def fnCenter(window):
        CenterPos=window.screen().availableGeometry().center()
        # frmScrRng=window.frameGeometry()
        # frmScrRng.moveCenter(CenterPos)
        # window.move(CenterPos - QtCore.QPoint(int(frmScrRng.width()/2), int(frmScrRng.height()/2)))
        window.adjustSize()
        window.move(CenterPos - window.rect().center())

    def fnSize(
        self,
        udeSizeMode:udeSizeMode,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy,
        intWidth:int,
        intHeight:int
    ):
        udeSizeMode=fnStrValueCvrt(udeSizeMode)
        if udeSizeMode is None: udeSizeMode=c_udeWinSizeMode

        udeSizePolicyH=fnStrValueCvrt(udeSizePolicyH)
        if udeSizePolicyH is None: udeSizePolicyH = c_udeWinSizePolicyH

        udeSizePolicyV=fnStrValueCvrt(udeSizePolicyV)
        if udeSizePolicyV is None: udeSizePolicyV = c_udeWinSizePolicyV

        if udeSizeMode==udeSizeMode.udeWinSizeModeFull:
            intWidth=fnScrnSize()
            intHeight=fnScrnSize(udeScrSizeType.udeScrSizeTypeH)
            self.resize(intWidth, intHeight)

        elif udeSizeMode==udeSizeMode.udeWinSizeModeFit:
            self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

        elif udeSizeMode==udeSizeMode.udeWinSizeModeFix:
            self.resize(intWidth, intHeight)
            self.setFixedSize(intWidth, intHeight)

        scrRun = self.screen()
        AvailGeometry = scrRun.availableGeometry()
        intWidthMax = AvailGeometry.width()
        intHeightMax = AvailGeometry.height()
        self.setMaximumSize(intWidthMax, intHeightMax)

        self.intWidth=intWidth
        self.intHeight=intHeight

    def fnResize(self):
        self.QWgetCentral.adjustSize()
        self.adjustSize()
        self.fnCenter(self)

    def fnWinAlwaysOnTop(self, blnAlwaysOnTop:bool):
        self.blnAlwaysOnTop=blnAlwaysOnTop
        if blnAlwaysOnTop:
            self.setWindowFlags(
                self.windowFlags() |
                QtCore.Qt.WindowType.WindowStaysOnTopHint
            )

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnWinVisible(self, blnVisible:bool):
        if blnVisible:
            self.show()
        else:
            self.hide()
        self.blnVisible=self.isVisible()

    def fnWinWgetAdd(
        self,
        lstQtWget:list,
        lstRow:list=None,
        lstCol:list=None
    ):
        if isinstance(self.layout, QtWidgets.QGridLayout) and \
            (lstRow is None or lstCol is None):
            import EHMsg
            EHMsg.fnMsgPrt(
                strMsg=
                    'fnWinWgetAdd:udeQtLayoutType.udeQtLayoutTypeG need ' + \
                        'lstRow and lstCol !'
            )
            return False

        for QtWget in lstQtWget:
            # QWin.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea , QtEditLn1)

            strTypeName=QtWget.__class__.__bases__[0].__name__
            if strTypeName==udeObjName.udeObjNameDock.value:
                # if QtWget.udeDockArea.value==QtCore.Qt.DockWidgetArea.LeftDockWidgetArea:
                #     print('ok')
                self.addDockWidget(QtWget.udeDockArea.value, QtWget)
            else:
                self.QWgetCentral.layout.addWidget(QtWget)

        return True

    def fnWinShow(self):
        self.fnSize(
            udeSizeMode=self.udeSizeMode,
            udeSizePolicyH=self.udeSizePolicyH,
            udeSizePolicyV=self.udeSizePolicyV,
            intWidth=self.intWidth,
            intHeight=self.intHeight
        )
        self.show()
        self.QApp.exec()

    def fnWinClose(self):
        self.close()

    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        super().resizeEvent(event)
        for QtWget in self.findChildren(QtWidgets.QWidget):
            QtWget.adjustSize()
        self.adjustSize()
        self.updateGeometry()
        self.move( self.screen().availableGeometry().center() - self.rect().center())

    def closeEvent(self, event:QtGui.QCloseEvent) -> None:
        event.accept()

    def keyPressEvent(self, event):
        keyASCII=event.key()
        if keyASCII==QtCore.Qt.Key.Key_Escape:
            self.fnWinClose()

def fnScrnSize(
    udeScrSizeType:udeScrSizeType=udeScrSizeType.udeScrSizeTypeW
)->int:
    if udeScrSizeType==udeScrSizeType.udeScrSizeTypeW:
        return QtGui.QGuiApplication.primaryScreen().availableSize().width()
    elif udeScrSizeType==udeScrSizeType.udeScrSizeTypeH:
        return QtGui.QGuiApplication.primaryScreen().availableSize().height()
# </PyCmt:QWin>

# <PyCmt:QWgetCentral>
class QWgetCentral(QtWidgets.QWidget):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strQWgetObjName,
        objLayoutInd:QtWidgets.QLayout=c_objQWgetLayoutInd,
        strTag: str = c_strQWgetTag,
        strStyleSheet:str=c_strQWgetStyleSheet
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        # <PyCmt:QWgetCentral should with Layout>
        # <PyCmt:When QWgetCentral Assign for QWin,
        #   fnLayout will assign a layout for QWgetCentral>
        self.layout=None
        self.strTag = strTag
        self.strStyleSheet=strStyleSheet
        self.lstChgDetSub = []

        self.fnQWgetParent(self.objParent)
        self.fnQWgetName(self.strName)
        self.fnStyleSheet(self.strStyleSheet)

    def fnQWgetParent(self,objParent):
        self.objParent=objParent
        if isinstance(self.objParent, QtWidgets.QMainWindow):
            self.objParent.setCentralWidget(self)
        elif not self.objLayoutInd is None:
            self.objLayoutInd.addWidget(self)
        else:
            self.objParent.addWidget(self)
    def fnQWgetName(self,strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnSubValueChgDet(
        self,
        blnChg:bool,
        lstItmChgd:list
    ):
        blnChg, lstItmChgd = \
            fnWgetValueChgDet(
                wgetRun=self,
                blnChg=blnChg,
                lstItmChgd=lstItmChgd
            )
        return blnChg, lstItmChgd
# </PyCmt:QCentralWget>

# <PyCmt:QLayout; QLayout>
class QLayout(QtWidgets.QLayout):
    # <PyCmt:QLayout Notice>
    # 1. QtLayout not the actual QLayout Object, the QtLayout.layout will be
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_udeLayoutObjName,
        udeLayoutType:udeQtLayoutType=c_udeLayoutType,
        objLayoutInd: QtWidgets.QLayout=c_objLayoutInd,
        strTag: str = c_strLayoutTag,
        udeLayoutSizeConstraint=c_udeLayoutSizeConstraint,
        udeAlignmentH:udeQtAlignment=c_udeLayoutAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeLayoutAlignmentV,
    ):
        self.itemColl=[]

        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.udeLayoutType=udeLayoutType
        self.objLayoutInd=objLayoutInd
        # <PyCmt:self.layout represent current running layout>
        self.layout=None
        self.strTag = strTag
        self.udeLayoutRoleTypeLast:udeQtLayoutRoleType=udeQtLayoutRoleType.udeQtLayoutRoleTypeNone
        self.udeLayoutSizeConstraint=udeLayoutSizeConstraint
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV

        self.fnLayoutSetup(self.udeLayoutType)
        self.fnLayoutParent(self.objParent)
        self.fnName(self.strName)
        self.fnLayoutSizeConstraint(self.udeLayoutSizeConstraint)
        self.fnAlignment(self.udeAlignmentH, self.udeAlignmentH)

    def fnLayoutSetup(self, udeLayoutType):
        udeLayoutType = fnStrValueCvrt(udeLayoutType)
        if udeLayoutType is None: udeLayoutType=c_udeLayoutType.value()
        self.layout=fnStrValueCvrt(udeLayoutType)

    def fnLayoutParent(self, objParent):
        if not objParent is None:
            self.objParent=objParent
            self.objLayoutInd = fnStrValueCvrt(self.objLayoutInd)
            if not self.objLayoutInd is None:
                self.addAsChildLayout(objMotherLayout=self.objLayoutInd.layout)
            elif self.objParent.layout is None:
                self.objParent.layout=self.layout
                if hasattr(self.objParent,'objLayout'):
                    self.objParent.objLayout=self
                # <PyCmt:QLayout for QMainWindow or QFrame,
                #   it have to self.objParent.setLayout(self.layout)>'
                self.objParent.setLayout(self.layout)
            elif isinstance(self.objParent.layout, udeQtLayoutType.udeQtLayoutTypeS.value):
                QWgetRun= \
                    QWgetCentral(
                        objParent=self.objParent,
                        strName = 'StackedLayoutSub',
                        objLayoutInd=self.objParent.layout
                    )
                QWgetRun.setSizePolicy(
                    QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                    QtWidgets.QSizePolicy.Policy.MinimumExpanding
                )
                QWgetRun.layout=self.layout
                QWgetRun.objLayout=self
                QWgetRun.setLayout(self.layout)

                self.objParent.QWgetCentral=QWgetRun
                QWgetRun.setParent(self.objParent)
                QWgetRun.adjustSize()
                self.objParent.layout.addWidget(QWgetRun)
            else:
                # <PyCmt:SubLayout>
                # self.objParent.layout.addLayout(self.layout)
                self.addAsChildLayout(objMotherLayout=self.objParent.layout)

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnLayoutSizeConstraint(self, udeLayoutSizeConstraint):
        udeLayoutSizeConstraint=fnStrValueCvrt(udeLayoutSizeConstraint)
        self.udeLayoutSizeConstraint=udeLayoutSizeConstraint
        if not self.udeLayoutSizeConstraint is None:
            self.layout.setSizeConstraint(self.udeLayoutSizeConstraint.value)

    def fnAlignment(self, udeAlignmentH, udeAlignmentV):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        if self.udeLayoutType==udeQtLayoutType.udeQtLayoutTypeH:
            self.layout.setAlignment(udeAlignmentH.value)
        elif self.udeLayoutType==udeQtLayoutType.udeQtLayoutTypeV:
            self.layout.setAlignment(udeAlignmentV.value)
        # self.setAlignment(udeAlignmentH.value)
        # self.setAlignment(udeAlignmentV.value)

    def sizeHint(self) -> QtCore.QSize:
        # return QtCore.QSize(self.objParent.width(), self.objParent.height())
        return QtCore.QSize()

    def addItem(self, item):
        self.itemColl.append(item)

    def count(self):
        return len(self.itemColl)

    def itemAt(self, index):
        if index < len(self.itemColl):
            return self.itemColl[index]
        else:
            return None

    def takeAt(self, index):
        if index < len(self.itemColl):
            return self.itemColl.pop(index)
        else:
            return None

    def addWidget(self, Wget:QtWidgets.QWidget) -> None:
        if Wget is not None:
            if isinstance(self.layout, QtWidgets.QGridLayout):
                self.layout.addWidget(Wget, 0, 0)  # specify row and column
            else:
                self.layout.addWidget(Wget)
            Wget.adjustSize()

    def addAsChildLayout(self, objMotherLayout:QtWidgets.QLayout):
        # objMotherLayout.addLayout(self.layout)
        objMotherLayout.addLayout(self.layout)

    def addStretch(self, intStretch=0):
        for intRun in range(intStretch):
            self.addItem(
                QtWidgets.QSpacerItem(
                    0,
                    0,
                    QtWidgets.QSizePolicy.Policy.Expanding,
                    QtWidgets.QSizePolicy.Policy.Expanding
                )
            )
# </PyCmt:QtLayout; QLayout>

# <PyCmt:QGroupBox; QBoxGrp>
class QBoxGrp(QtWidgets.QGroupBox):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBoxGrpObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBoxGrpLayoutInd,
        strTitle:str=c_strBoxGrpTitle,
        strTag: str = c_strBoxGrpTag,
        blnVisible:bool=c_blnBoxGrpVisible,
        blnEnable:bool=c_blnBoxGrpEnable,
        blnChkable:bool=c_blnBoxGrpChkable,
        strToolTip:str=c_strBoxGrpToolTip,
        udeSizePolicyH:udeQtSizePolicy=c_udeBoxGrpSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBoxGrpSizePolicyV,
        udeAlignmentH:udeQtAlignment=c_udeBoxGrpAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeBoxGrpAlignmentV,
        strStyleSheet:str=c_strBoxGrpStyleSheet
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        # <PyCmt:QBoxGrp should with Layout>
        self.layout=None
        self.objLayout = None
        self.QWgetCentral=None
        self.strTitle=strTitle
        self.strTag=strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnChkable=blnChkable
        self.strToolTip=strToolTip
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        self.strStyleSheet=strStyleSheet
        self.lstChgDetSub=[]

        self.fnParent(self.objParent)
        self.fnName(self.strName)
        self.fnTitle(self.strTitle)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnChkable(self.blnChkable)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnAlignment(self.udeAlignmentH, self.udeAlignmentV)
        self.fnStyleSheet(self.strStyleSheet)

    def fnParent(self, objParent):
        fnParentSet(objRun=self, objParent = objParent)

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnTitle(self, strTitle:str):
        self.setTitle(strTitle)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnChkable(self, blnChkable:bool):
        self.blnChkable=blnChkable
        self.setCheckable(blnChkable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy,
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

    def fnAlignment(
        self,
        udeAlignmentH:udeQtAlignment,
        udeAlignmentV:udeQtAlignment
    ):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV = udeAlignmentV
        self.setAlignment(udeAlignmentH.value)
        self.setAlignment(udeAlignmentV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnValueChgDet(
        self,
        blnChg:bool=False,
        lstItmChgd:list = None
    ):
        blnChg, lstItmChgd = \
            fnWgetValueChgDet(
                wgetRun = self,
                blnChg = blnChg,
                lstItmChgd = lstItmChgd
            )
        return blnChg, lstItmChgd
# </PyCmt:QGroupBox; QBoxGrp>

# <PyCmt:QFrame; QFrm>
class QFrm(QtWidgets.QFrame):
    # <PyCmt:QLayout Notice>
    # 1. if more than 1 Frame add QLayout, each Frame needs to add QLayout
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strFrmObjName,
        objLayoutInd:QtWidgets.QLayout=c_objFrmLayoutInd,
        blnVisible:bool=c_blnFrmVisible,
        blnEnable:bool=c_blnFrmEnable,
        strTag: str = c_strFrmTag,
        strToolTip:str=c_strFrmToolTip,
        intPosX:int=c_intFrmPosX,
        intPosY:int=c_intFrmPosY,
        udeFrmSizePolicyH:udeQtSizePolicy=c_udeFrmSizePolicyH,
        udeFrmSizePolicyV:udeQtSizePolicy=c_udeFrmSizePolicyV,
        intWidth:int=c_intFrmWidth,
        intHeight:int=c_intFrmHeight,
        udeFrmShp:udeQtFrmShp=c_udeFrmFrmShp,
        intFrmLineWidth:int=c_intFrmLineWidth,
        strStyleSheet:str=c_strFrmStyleSheet
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        # <PyCmt:QFrame should with Layout>
        self.layout=None
        self.objLayout = None
        self.QWgetCentral=None
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.strTag = strTag
        self.strToolTip=strToolTip
        self.intPosX=intPosX
        self.intPosY=intPosY
        self.udeFrmSizePolicyH=udeFrmSizePolicyH
        self.udeFrmSizePolicyV=udeFrmSizePolicyV
        self.intWidth=intWidth
        self.intHeight=intHeight
        self.udeFrmShp=udeFrmShp
        self.intFrmLineWidth=intFrmLineWidth
        self.strStyleSheet=strStyleSheet
        self.lstChgDetSub = []

        self.fnParent(self.objParent)
        self.fnName(self.strName)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnToolTip(self.strToolTip)
        self.fnPos(
            self.intPosX,
            self.intPosY
        )
        self.fnSizePolicy(
            self.udeFrmSizePolicyH,
            self.udeFrmSizePolicyV,
            self.intWidth,
            self.intHeight,
        )
        self.fnFrmShp(
            udeFrmShp=self.udeFrmShp,
            intFrmLineWidth=self.intFrmLineWidth
        )
        self.fnStyleSheet(self.strStyleSheet)
    def fnParent(self, objParent):
        fnParentSet(objRun = self, objParent = objParent)

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnPos(self, intPosX:int, intPosY:int):
        self.intPosX=intPosX
        self.intPosY=intPosY
        self.move(intPosX, intPosY)

    def fnSizePolicy(
        self,
        udeFrmSizePolicyH:udeQtSizePolicy,
        udeFrmSizePolicyV:udeQtSizePolicy,
        intWidth:int,
        intHeight:int,
    ):
        self.udeFrmSizePolicyH=udeFrmSizePolicyH
        self.udeFrmSizePolicyV=udeFrmSizePolicyV
        if self.udeFrmSizePolicyH==udeQtSizePolicy.udeQtSizePolicyFix:
            self.setFixedWidth(intWidth)
        if self.udeFrmSizePolicyV==udeQtSizePolicy.udeQtSizePolicyFix:
            self.setFixedHeight(intHeight)
        self.setSizePolicy(udeFrmSizePolicyH.value, udeFrmSizePolicyV.value)


    def fnFrmShp(
        self,
        udeFrmShp:udeQtFrmShp,
        intFrmLineWidth:int
    ):
        self.udeFrmShp=udeFrmShp
        self.intFrmLineWidth=intFrmLineWidth

        self.setFrameShape(udeFrmShp.value)
        # self.setFrameStyle(QtWidgets.QFrame.Shape.Panel)
        self.setLineWidth(intFrmLineWidth)
        self.setMidLineWidth(intFrmLineWidth)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnValueChgDet(
        self,
        blnChg:bool=False,
        lstItmChgd:list = None
    ):
        blnChg, lstItmChgd = \
            fnWgetValueChgDet(
                wgetRun = self,
                blnChg = blnChg,
                lstItmChgd = lstItmChgd
            )
        return blnChg, lstItmChgd
# </PyCmt:QFrame; QFrm>

# <PyCmt:Scroll Area; QScrArea>
class QScrArea(QtWidgets.QScrollArea):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strScrAreaObjName,
        objLayoutInd:QtWidgets.QLayout=c_objScrAreaLayoutInd,
        blnVisible:bool=c_blnScrAreaVisible,
        blnEnable:bool=c_blnScrAreaEnable,
        strTag: str = c_strScrAreaTag,
        strToolTip:str=c_strScrAreaToolTip,
        intPosX:int=c_intScrAreaPosX,
        intPosY:int=c_intScrAreaPosY,
        udeSizePolicyH:udeQtSizePolicy=c_udeScrAreaSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeScrAreaSizePolicyV,
        intWidth:int=c_intScrAreaWidth,
        intHeight:int=c_intScrAreaHeight,
        udeFrmShp:udeQtFrmShp=c_udeScrAreaFrmShp,
        intFrmLineWidth:int=c_intScrAreaFrmLineWidth,
        udeScrollBarPolicyH:udeQtScrollBarPolicy=c_udeScrAreaScrollBarPolicyH,
        udeScrollBarPolicyV:udeQtScrollBarPolicy=c_udeScrAreaScrollBarPolicyV,
        udeAlignmentH:udeQtAlignment=c_udeScrAreaAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeScrAreaAlignmentV,
        strStyleSheet:str=c_strScrAreaStyleSheet
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        # <PyCmt:QScrArea should with Layout>
        self.layout=None
        self.objLayout = None
        self.QWgetCentral=None
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.strTag = strTag
        self.strToolTip=strToolTip
        self.intPosX=intPosX
        self.intPosY=intPosY
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.intWidth=intWidth
        self.intHeight=intHeight
        self.udeFrmShp=udeFrmShp
        self.intFrmLineWidth=intFrmLineWidth
        self.udeScrollBarPolicyH=udeScrollBarPolicyH
        self.udeScrollBarPolicyV=udeScrollBarPolicyV
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        self.strStyleSheet=strStyleSheet
        self.lstChgDetSub=[]

        self.fnParent(self.objParent)
        self.fnName(self.strName)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnToolTip(self.strToolTip)
        self.fnPos(self.intPosX, self.intPosY)
        self.fnSizePolicy(
            self.udeSizePolicyH,
            self.udeSizePolicyV,
            self.intWidth,
            self.intHeight,
        )
        self.fnFrmShp(self.udeFrmShp, self.intFrmLineWidth)
        self.fnScrollBarPolicy(
            self.udeScrollBarPolicyH, self.udeScrollBarPolicyV
        )
        self.fnAlignment(self.udeAlignmentH,self.udeAlignmentV)
        self.fnStyleSheet(self.strStyleSheet)

    def fnParent(self, objParent):
        fnParentSet(objRun=self, objParent = objParent)

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnPos(self, intPosX:int, intPosY:int):
        self.intPosX=intPosX
        self.intPosY=intPosY

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy,
        intWidth:int,
        intHeight:int,
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        if self.udeSizePolicyH==udeQtSizePolicy.udeQtSizePolicyFix:
            self.setFixedWidth(intWidth)
        if self.udeSizePolicyV==udeQtSizePolicy.udeQtSizePolicyFix:
            self.setFixedHeight(intHeight)
        self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

    def fnFrmShp(
        self,
        udeFrmShp:udeQtFrmShp,
        intFrmLineWidth:int
    ):
        self.udeFrmShp=udeFrmShp
        self.intFrmLineWidth=intFrmLineWidth

        self.setFrameShape(udeFrmShp.value)
        # self.setFrameStyle(QtWidgets.QScrollArea.Shape.Panel)
        self.setLineWidth(intFrmLineWidth)
        self.setMidLineWidth(intFrmLineWidth)

    def fnScrollBarPolicy(
        self,
        udeScrollBarPolicyH:udeQtSizePolicy,
        udeScrollBarPolicyV:udeQtScrollBarPolicy,
    ):
        self.udeScrollBarPolicyH=udeScrollBarPolicyH
        self.udeScrollBarPolicyV=udeScrollBarPolicyV
        self.setHorizontalScrollBarPolicy(udeScrollBarPolicyH.value)
        self.setVerticalScrollBarPolicy(udeScrollBarPolicyV.value)

    def fnAlignment(
        self,
        udeAlignmentH:udeQtAlignment,
        udeAlignmentV:udeQtAlignment
    ):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV = udeAlignmentV
        self.setAlignment(udeAlignmentH.value)
        self.setAlignment(udeAlignmentV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnSubValueChgDet(
        self,
        blnChg:bool=False,
        lstItmChgd:list = None
    ):
        blnChg, lstItmChgd = \
            fnWgetValueChgDet(
                wgetRun = self,
                blnChg = blnChg,
                lstItmChgd = lstItmChgd
            )
        return blnChg, lstItmChgd
# </PyCmt:Scroll Area; QScrArea>

# <PyCmt:QDockWidget; QDock>
class QDock(QtWidgets.QDockWidget):
    # <PyCmt:QDock Notice>
    # 1. if root is QMainWindow, QDock.objParent have to be QMainWindow>
    # 2. if root is QWidget, QWidget can contain QDock
    # 3. if root is QWidget, QWidget.layout can contain QDock
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strDockObjName,
        objLayoutInd:QtWidgets.QLayout=c_objDockLayoutInd,
        strTitle:str=c_strDockTitle,
        strTag: str = c_strDockTag,
        blnVisible:bool=c_blnDockVisible,
        blnEnable:bool=c_blnDockEnable,
        blnClosable:bool=c_blnDockClosable,
        blnMovable:bool=c_blnDockMovable,
        blnFloatable:bool=c_blnDockFloatable,
        blnDockAreaTop:bool=c_blnDockDockAreaTop,
        blnDockAreaBottom:bool=c_blnDockDockAreaBottom,
        blnDockAreaLeft:bool=c_blnDockDockAreaLeft,
        blnDockAreaRight:bool=c_blnDockDockAreaRight,
        udeDockArea:udeQtDockArea=c_udeDockArea,
        udeSizePolicyH:udeQtSizePolicy=c_udeDockSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeDockSizePolicyV,
        intWidth:int=c_intDockWidth,
        intHeight:int=c_intDockHeight,
        strToolTip:str=c_strDockToolTip,
        strStyleSheet:str=c_strDockStyleSheet
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        # <PyCmt:QDock should with Layout>
        self.layout=None
        self.objLayout = None
        self.QWgetCentral=None
        self.strTitle=strTitle
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnClosable=blnClosable
        self.blnMovable=blnMovable
        self.blnFloatable=blnFloatable
        self.blnDockAreaTop=blnDockAreaTop
        self.blnDockAreaBottom=blnDockAreaBottom
        self.blnDockAreaLeft=blnDockAreaLeft
        self.blnDockAreaRight=blnDockAreaRight
        self.udeDockArea=udeDockArea
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.intWidth=intWidth
        self.intHeight=intHeight
        self.strToolTip=strToolTip
        self.strStyleSheet = strStyleSheet
        self.lstChgDetSub=[]

        self.fnParent(self.objParent)
        self.fnName(self.strName)
        self.fnTitle(self.strTitle)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnClosable(self.blnClosable)
        self.fnMovable(self.blnMovable)
        self.fnFloatable(self.blnFloatable)
        self.fnDockArea(
            self.blnDockAreaTop,
            self.blnDockAreaBottom,
            self.blnDockAreaLeft,
            self.blnDockAreaRight
        )
        self.fnSize(self.intWidth, self.intHeight)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnStyleSheet(self.strStyleSheet)

    def fnParent(self, objParent):
        if objParent is not None:
            self.objParent=objParent
            self.setParent(self.objParent)
            if isinstance(self.objParent, QtWidgets.QMainWindow):
                featDockArea=QtCore.Qt.DockWidgetArea.NoDockWidgetArea
                if blnDockAreaTop:
                    featDockArea |= QtCore.Qt.DockWidgetArea.TopDockWidgetArea
                if blnDockAreaBottom:
                    featDockArea |= QtCore.Qt.DockWidgetArea.BottomDockWidgetArea
                if blnDockAreaLeft:
                    featDockArea |= QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
                if blnDockAreaRight:
                    featDockArea |= QtCore.Qt.DockWidgetArea.RightDockWidgetArea
                self.objParent.addDockWidget(self, featDockArea)
            elif not self.objLayoutInd is None:
                self.objLayoutInd.addWidget(self)
            elif not self.objParent.layout is None:
                self.objParent.layout.addWidget(self)
            elif isinstance(self.objParent, QtWidgets.QWidget):
                self.objParent.addWidget(self)

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnTitle(self, strTitle:str):
        self.strTitle=strTitle
        self.setWindowTitle(strTitle)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnClosable(self, blnClosable:bool):
        self.blnClosable=blnClosable
        featFeaturesCurr=self.features()
        featClosable=QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable
        if blnClosable !=bool(featFeaturesCurr.value & featClosable.value):
            self.setFeatures(featFeaturesCurr & ~featClosable)

    def fnMovable(self, blnMovable:bool):
        self.blnMovable=blnMovable
        featFeaturesCurr=self.features()
        featMovable=QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable
        if blnMovable !=bool(featFeaturesCurr.value & featMovable.value):
            self.setFeatures(featFeaturesCurr & ~featMovable)

    def fnFloatable(self, blnFloatable:bool):
        self.blnFloatable=blnFloatable
        featFeaturesCurr=self.features()
        featMovable=QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable
        if blnFloatable !=bool(featFeaturesCurr.value & featMovable.value):
            self.setFeatures(featFeaturesCurr & ~featMovable)

    def fnDockArea(
        self,
        blnDockAreaTop:bool,
        blnDockAreaBottom:bool,
        blnDockAreaLeft:bool,
        blnDockAreaRight:bool
    ):
        self.blnDockAreaTop=blnDockAreaTop
        self.blnDockAreaBottom=blnDockAreaBottom
        self.blnDockAreaLeft=blnDockAreaLeft
        self.blnDockAreaRight=blnDockAreaRight

        featDockArea=QtCore.Qt.DockWidgetArea.NoDockWidgetArea
        if blnDockAreaTop:
            featDockArea |= QtCore.Qt.DockWidgetArea.TopDockWidgetArea
        if blnDockAreaBottom:
            featDockArea |= QtCore.Qt.DockWidgetArea.BottomDockWidgetArea
        if blnDockAreaLeft:
            featDockArea |= QtCore.Qt.DockWidgetArea.LeftDockWidgetArea
        if blnDockAreaRight:
            featDockArea |= QtCore.Qt.DockWidgetArea.RightDockWidgetArea
        self.setAllowedAreas(featDockArea)

    def fnSize(self, intWidth:int, intHeight:int):
        self.intWidth=intWidth
        self.intHeight=intHeight
        if intWidth>0 or intHeight>0:
            self.fnSizePolicy(
                udeSizePolicyH=udeQtSizePolicy.udeQtSizePolicyFix,
                udeSizePolicyV=udeQtSizePolicy.udeQtSizePolicyFix
            )
        # self.setMinimumSize(intWidth, intHeight)
        if self.intWidth>0:self.setMinimumWidth(self.intWidth)
        if self.intHeight>0:self.setMinimumHeight(self.intHeight)
    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(self.udeSizePolicyH.value, self.udeSizePolicyV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnValueChgDet(
        self,
        blnChg:bool=False,
        lstItmChgd:list = None
    ):
        blnChg, lstItmChgd = \
            fnWgetValueChgDet(
                wgetRun = self,
                blnChg = blnChg,
                lstItmChgd = lstItmChgd
            )
        return blnChg, lstItmChgd
# </PyCmt:QDock>

# <PyCmt:Container Widget>
def fnContainerItemDel(objRun):
    for intRun in range(len(objRun.children())):
        itemRun=objRun.children()[intRun]
        if itemRun:itemRun.deleteLater()
# <PyCmt:Container Widget>

# <PyCmt:QtLabel; QLbl>
class QLbl(QtWidgets.QLabel):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strLblObjName,
        objLayoutInd:QtWidgets.QLayout=c_objLblLayoutInd,
        strText=c_strLblText,
        strTag: str = c_strLblTag,
        blnVisible=c_blnLblVisible,
        blnWordWrap:bool=c_blnLblWordWrap,
        intIndent:int=c_intLblIndent,
        udeQtTextInterAction:udeQtTextInterAction=c_udeLblTextInterAction,
        blnAutoSize:bool=c_blnLblAutoSize,
        udeFrmShp: udeQtFrmShp=c_udeLblFrmShp,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeLblLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeLblSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeLblSizePolicyV,
        udeAlignmentH:udeQtAlignment=c_udeScrAreaAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeScrAreaAlignmentV,
        strStyleSheet:str=c_strLblStyleSheet
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strText=strText
        self.strValue=self.strText
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnWordWrap=blnWordWrap
        self.intIndent=intIndent
        self.udeQtTextInterAction=udeQtTextInterAction
        self.blnAutoSize=blnAutoSize
        self.udeFrmShp=udeFrmShp
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        self.strStyleSheet=strStyleSheet

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnText(self.strText)
        self.fnVisible(self.blnVisible)
        self.fnWordWrap(self.blnWordWrap)
        self.fnIndent(self.intIndent)
        self.fnTextInterAction(self.udeQtTextInterAction)
        self.fnAutoSize(self.blnAutoSize)
        self.fnFrmShp(self.udeFrmShp)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnAlignment(self.udeAlignmentH,self.udeAlignmentV)
        self.fnStyleSheet(self.strStyleSheet)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnText(self, strText:str):
        self.strText=strText
        self.setText(strText)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnWordWrap(self, blnWordWrap:bool):
        self.setWordWrap(blnWordWrap)

    def fnIndent(self, intIndent:int):
        self.setIndent(intIndent)

    def fnTextInterAction(self,udeQtTextInterAction:udeQtTextInterAction):
        self.setTextInteractionFlags(udeQtTextInterAction.value)

    def fnAutoSize(self, blnAutoSize:bool):
        self.blnAutoSize=blnAutoSize
        if blnAutoSize: self.adjustSize()

    def fnFrmShp(self, udeFrmShp:udeQtFrmShp):
        self.setFrameShape(udeFrmShp.value)
        # self.setStyleSheet("border:1px solid black;")

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy
    ):
        if self.blnAutoSize:
            udeSizePolicyH=udeQtSizePolicy.udeQtSizePolicyMin
            udeSizePolicyV=udeQtSizePolicy.udeQtSizePolicyMin
        else:
            if udeSizePolicyV==udeQtSizePolicy.udeQtSizePolicyFix:
                self.setFixedHeight(20)

        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value,udeSizePolicyV.value)
        self.adjustSize()

    def fnAlignment(
        self,
        udeAlignmentH:udeQtAlignment,
        udeAlignmentV:udeQtAlignment
    ):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV = udeAlignmentV
        self.setAlignment(udeAlignmentH.value)
        self.setAlignment(udeAlignmentV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)
# </PyCmt:QLabel; QLbl>

# <PyCmt:QLineEdit; QEditLn>
class QEditLn(QtWidgets.QLineEdit):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strEditLnObjName,
        objLayoutInd:QtWidgets.QLayout=c_objEditLnLayoutInd,
        strText:str=c_strEditLnText,
        strTag: str = c_strEditLnTag,
        blnVisible:bool=c_blnEditLnVisible,
        blnEnable:bool=c_blnEditLnEnable,
        blnReadOnly:bool=c_blnEditLnReadOnly,
        blnPwd:bool=c_blnEditLnPwd,
        intLenMax:int=c_intEditLnLenMax,
        strToolTip:str=c_strEditLnToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeEditLnLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeEditLnSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeEditLnSizePolicyV,
        udeAlignmentH:udeQtAlignment=c_udeEditLnAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeEditLnAlignmentV,
        strStyleSheet:str=c_strEditLnStyleSheet,
        strMethTextChg:str='',
        strMethEditFinished:str=''
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strText=str(strText)
        self.strTextOrig=str(strText)
        self.strValue=str(strText)
        self.strValueOrig=str(strText)
        self.strTag = strTag
        self.blnChg=False
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnReadOnly=blnReadOnly
        self.blnPwd=blnPwd
        self.intLenMax=intLenMax
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        self.strToolTip=strToolTip
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.strStyleSheet=strStyleSheet

        self.strMethTextChg=strMethTextChg
        self.strMethEditFinished=strMethEditFinished

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnText(self.strText)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnReadOnly(self.blnReadOnly)
        self.fnPwd(self.blnPwd)
        self.fnLenMax(self.intLenMax)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnAlignment(self.udeAlignmentH,self.udeAlignmentV)
        self.fnStyleSheet(self.strStyleSheet)

        self.textChanged.connect(self.evtTextChanged)
        self.editingFinished.connect(self.evtEditFinished)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnText(self, strText:str):
        self.strText=strText
        self.setText(strText)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnReadOnly(self, blnReadOnly:bool):
        self.blnReadOnly=blnReadOnly
        self.setReadOnly(blnReadOnly)

    def fnPwd(self, blnPwd:bool):
        self.blnPwd=blnPwd
        self.setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password if blnPwd
                else QtWidgets.QLineEdit.EchoMode.Normal
        )

    def fnLenMax(self, intLenMax:int):
        if intLenMax>0:
            self.intLenMax=intLenMax
            self.setMaxLength(intLenMax)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value,udeSizePolicyV.value)

    def fnAlignment(
        self,
        udeAlignmentH:udeQtAlignment,
        udeAlignmentV:udeQtAlignment
    ):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV = udeAlignmentV
        self.setAlignment(udeAlignmentH.value)
        self.setAlignment(udeAlignmentV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtTextChanged(self):
        self.strText=self.text()
        self.strValue=self.strText
        self.blnChg=self.text()!=self.strTextOrig
        EHPyMdl.fnMdlFuncCall(self.strMethTextChg, self)

    def evtEditFinished(self):
        if self.isModified():
            EHPyMdl.fnMdlFuncCall(self.strMethEditFinished, self)
        self.setModified(False)

    def fnValueChgDet(self):
        self.blnChg=self.text()!=self.strTextOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.strText = strValue
            self.strValue = strValue
        self.strTextOrig=self.strText
        self.strValueOrig=self.strValue
        self.blnChg=False

    def fnValueChgDiscard(self):
        self.setText(self.strTextOrig)
        self.strText=self.strTextOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QLineEdit; QEditLn>

# <PyCmt:QPlainTextEdit; QEditTxt>
class QEditTxt(QtWidgets.QPlainTextEdit):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strEditTxtObjName,
        objLayoutInd:QtWidgets.QLayout=c_objEditTxtLayoutInd,
        strText:str=c_strEditTxtText,
        strTag: str = c_strEditTxtTag,
        blnVisible:bool=c_blnEditTxtVisible,
        blnEnable:bool=c_blnEditTxtEnable,
        blnReadOnly:bool=c_blnEditTxtReadOnly,
        blnSizeGrip:bool=c_blnEditTxtSizeGrip,
        strToolTip:str=c_strEditTxtToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeEditTxtLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeEditTxtSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeEditTxtSizePolicyV,
        udeFrmShp:udeQtFrmShp=c_udeEditTxtFrmShp,
        strStyleSheet:str=c_strFrmStyleSheet,
        strMethTextChg: str = '',
    ):
        super(QEditTxt, self).__init__(None)
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strText=str(strText)
        self.strTextOrig=str(strText)
        self.strValue=str(strText)
        self.strValueOrig = str(strText)
        self.strTag = strTag
        self.blnChg=False
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnReadOnly=blnReadOnly
        self.blnSizeGrip=blnSizeGrip
        self.SizeGrip=None
        self.strToolTip=strToolTip
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeFrmShp=udeFrmShp
        self.strStyleSheet=strStyleSheet
        self.strMethTextChg=strMethTextChg

        self.start_pos=None
        self.start_geometry=None
        self.resizing = False

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnText(self.strText)

        self.fnSizeGrip(self.blnSizeGrip)

        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnReadOnly(self.blnReadOnly)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnFrmShp(self.udeFrmShp)
        self.fnStyleSheet(self.strStyleSheet)

        self.textChanged.connect(self.evtTextChg)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnText(self, strText:str):
        self.strText=strText
        self.setPlainText(strText)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnReadOnly(self, blnReadOnly:bool):
        self.blnReadOnly=blnReadOnly
        self.setReadOnly(blnReadOnly)
        
    def fnSizeGrip(self, blnSizeGrip):
        if blnSizeGrip:
            self.setMinimumHeight(c_intEditTxtHeight)
            self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            self.SizeGrip=QtWidgets.QSizeGrip(self)
            self.SizeGrip.setFixedSize(16,16)
            self.setWindowFlags(Qt.WindowType.SubWindow)

            self.SizeGrip.installEventFilter(self)
            self.installEventFilter(self)
            
    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy
    ):
        if udeSizePolicyV==udeQtSizePolicy.udeQtSizePolicyFix:
            self.setFixedHeight(c_intEditTxtHeight)
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value,udeSizePolicyV.value)
        self.adjustSize()

    def fnFrmShp(self, udeQtFrmShp:udeQtFrmShp):
        self.setFrameShape(udeQtFrmShp.value)
        # self.setStyleSheet("border:1px solid black;")

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtTextChg(self):
        self.strText=self.toPlainText()
        self.strValue=self.strText
        self.blnChg=self.toPlainText()!=self.strTextOrig
        EHPyMdl.fnMdlFuncCall(self.strMethTextChg)

    def fnValueChgDet(self):
        self.blnChg=self.toPlainText()!=self.strTextOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.strText = strValue
            self.strValue = strValue
        self.strTextOrig=self.strText
        self.strValueOrig=self.strValue
        self.blnChg=False

    def fnValueChgDiscard(self):
        self.setPlainText(text=self.strTextOrig)
        self.strText=self.strTextOrig
        self.strValue=self.strValueOrig
        self.blnChg = False

    def evtEventFilter(self, objRun, event):
        # Always raise to top when interacting
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.raise_()

        # Handle size grip resizing
        if objRun == self.SizeGrip:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.resizing = True
                    self.start_pos = event.globalPosition().toPoint()
                    self.start_geometry = self.geometry()
                    self.raise_()
                    return True

            elif event.type() == QEvent.Type.MouseMove and self.resizing:
                delta = event.globalPosition().toPoint() - self.start_pos
                new_width = self.start_geometry.width() + delta.x()
                new_height = self.start_geometry.height() + delta.y()
                self.resize(max(50, new_width), max(50, new_height))
                return True

            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.resizing = False
                return True
        else:
            self.resizing = False
        return super().eventFilter(objRun, event)

    def mousePressEvent(self, event):
        super(QEditTxt, self).mousePressEvent(event)
        self.raise_()

    def resizeEvent(self, event):
        if self.blnSizeGrip:
        # Position the size grip in the bottom-right corner
            self.SizeGrip.move(self.width() - self.SizeGrip.width(), self.height() - self.SizeGrip.height())
            self.raise_()
            super(QEditTxt, self).resizeEvent(event)

# </PyCmt:QPlainTextEdit; QEditTxt>

# <PyCmt:QDateTimeEdit; QEditDate>
class QEditDate(QtWidgets.QDateTimeEdit):
    import datetime
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strEditDateObjName,
        objLayoutInd:QtWidgets.QLayout=c_objEditDateLayoutInd,
        dateRun:datetime.date=c_dateEditDateRun,
        dateMin:datetime.date=c_dateEditDateMin,
        dateMax:datetime.date=c_dateEditDateMax,
        strTag: str = c_strEditDateTag,
        blnDateTimeMode:bool=c_blnEditDateDateTimeMode,
        blnVisible:bool=c_blnEditDateVisible,
        blnEnable:bool=c_blnEditDateEnable,
        blnReadOnly:bool=c_blnEditDateReadOnly,
        strToolTip:str=c_strEditDateToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeEditDateLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeEditDateSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeEditDateSizePolicyV,
        udeAlignmentH:udeQtAlignment=c_udeEditDateAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeEditDateAlignmentV,
        strStyleSheet:str=c_strEditDateStyleSheet,
        strMethChg:str=c_strEditDateMethChg
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.dateRun=dateRun
        self.dateOrig=dateRun
        self.dateMin=dateMin
        self.dateMax=dateMax
        self.strValue=dateRun.strftime('%Y/%m/%d %H:%M:%S')
        self.strValueOrig=self.strValue
        self.blnChg=False
        self.strTag = strTag
        self.blnDateTimeMode=blnDateTimeMode
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnReadOnly=blnReadOnly
        self.strToolTip=strToolTip
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        self.strStyleSheet=strStyleSheet
        self.strMethChg=strMethChg

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnDate(self.dateRun)
        self.fnDateMin(self.dateMin)
        self.fnDateMax(self.dateMax)
        self.fnDateTimeMode(self.blnDateTimeMode)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnReadOnly(self.blnReadOnly)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnAlignment(self.udeAlignmentH,self.udeAlignmentV)
        self.fnStyleSheet(self.strStyleSheet)

        self.dateTimeChanged.connect(self.evtValueChg)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnDate(self, dateRun:datetime.date):
        self.dateRun=dateRun
        self.setDate(dateRun)

    def fnDateMin(self, dateMin:datetime.date):
        self.dateMin=dateMin
        self.setMinimumDate(dateMin)

    def fnDateMax(self, dateMax:datetime.date):
        self.dateMax=dateMax
        self.setMaximumDate(dateMax)

    def fnDateTimeMode(self, blnDateTimeMode:bool):
        self.blnDateTimeMode=blnDateTimeMode
        if blnDateTimeMode:
            self.setDisplayFormat('yyyy/MM/dd AP hh:mm')
        else:
            self.setDisplayFormat('yyyy/MM/dd')

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnReadOnly(self, blnReadOnly:bool):
        self.blnReadOnly=blnReadOnly
        self.setReadOnly(blnReadOnly)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

    def fnAlignment(
        self,
        udeAlignmentH:udeQtAlignment,
        udeAlignmentV:udeQtAlignment
    ):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV = udeAlignmentV
        self.setAlignment(udeAlignmentH.value)
        self.setAlignment(udeAlignmentV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtValueChg(self):
        self.dateRun=self.date().toPyDate()
        self.strValue=self.dateRun.strftime('%Y/%m/%d %H:%M:%S')
        self.blnChg=self.dateRun!=self.dateOrig
        EHPyMdl.fnMdlFuncCall(self.strMethChg, self)

    def fnValueChgDet(self):
        self.blnChg=self.dateRun!=self.dateOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            blnDate, dateRun=EHDate.fnDateChk(dateRun:=strValue)
            self.dateRun = dateRun
            self.strValue = strValue
        self.dateOrig=self.dateRun
        self.strValueOrig=self.strValue
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setTime(self.dateOrig)
        self.dateRun=self.dateOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QDateTimeEdit; QEditDate>

# <PyCmt:QPushButton; QBtn>
class QBtn(QtWidgets.QPushButton):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBtnObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBtnLayoutInd,
        strCaption:str=c_strBtnCaption,
        blnValue:bool=c_blnBtnValue,
        strTag: str = c_strBtnTag,
        blnVisible:bool=c_blnBtnVisible,
        blnEnable:bool=c_blnBtnEnable,
        blnAutoDft:bool=c_blnBtnAutoFft,
        blnFlat:bool=c_blnBtnFlat,
        strToolTip:str=c_strBtnToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBtnLayoutRoleType,
        udePolicyH:udeQtSizePolicy=c_udeBtnSizePolicyH,
        udePolicyV:udeQtSizePolicy=c_udeBtnSizePolicyV,
        strStyleSheet:str=c_strBtnStyleSheet,
        strMethClick:str=c_strBtnMethClick
    ):
        super().__init__()

        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strCaption=strCaption
        self.blnValue=bool(blnValue)
        self.blnValueOrig=bool(blnValue)
        self.strValue=str(blnValue)
        self.strValueOrig = str(blnValue)
        self.blnChg=False
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnAutoDft=blnAutoDft
        self.blnFlat=blnFlat
        self.strToolTip=strToolTip
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udePolicyH=udePolicyH
        self.udePolicyV=udePolicyV
        self.strStyleSheet=strStyleSheet
        self.strMethClick=strMethClick

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnCaption(self.strCaption)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnAutoDft(self.blnAutoDft)
        self.fnFlat(self.blnFlat)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udePolicyH, self.udePolicyV)
        self.fnStyleSheet(self.strStyleSheet)

        self.clicked.connect(self.evtClick)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnCaption(self, strCaption:str):
        self.strCaption=strCaption
        self.setText(strCaption)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable:bool):
        self.blnEnable=blnEnable
        self.setDisabled(not blnEnable)
        # self.setEnabled(blnEnable)

    def fnAutoDft(self, blnAutoDft:bool):
        self.blnAutoDft=blnAutoDft
        self.setAutoDefault(blnAutoDft)

    def fnFlat(self, blnFlat:bool):
        self.blnFlat=blnFlat
        self.setFlat(blnFlat)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udePolicyH:udeQtSizePolicy,
        udePolicyV:udeQtSizePolicy):
        self.udePolicyH=udePolicyH
        self.udePolicyV=udePolicyV
        self.setSizePolicy(udePolicyH.value, udePolicyV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtClick(self):
        self.blnValue=self.isChecked()
        self.strValue=str(self.blnValue)
        self.blnChg=self.blnValue!=self.blnValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethClick)

    def fnValueChgDet(self):
        self.blnChg=self.isChecked()!=self.blnValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.blnValue = bool(strValue)
            self.strValue = strValue
        self.blnValueOrig=self.blnValue
        self.strValueOrig=str(self.strValue)
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setChecked(self.blnValueOrig)
        self.blnValue=self.blnValueOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QPushButton; QBtn>

# <PyCmt:QToolButton; QBtnTool>
class QBtnTool(QtWidgets.QToolButton):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBtnToolObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBtnToolLayoutInd,
        strCaption:str=c_strBtnToolCaption,
        blnValue:bool=c_blnBtnToolValue,
        strTag: str = c_strBtnToolTag,
        blnVisible:bool=c_blnBtnToolVisible,
        blnEnable:bool=c_blnBtnToolEnable,
        blnChkable:bool=c_blnBtnToolChkable,
        strToolTip:str=c_strBtnToolToolTip,
        udeLayoutRoleType: udeQtLayoutRoleType = c_udeBtnToolLayoutRoleType,
        udePopupMode:udeQtToolButtonPopupMode=c_udeBtnToolPopupMode,
        udeArrowType:udeQtToolButtonArrowType=c_udeBtnToolArrowType,
        udeSizePolicyH:udeQtSizePolicy=c_udeBtnRadioSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBtnRadioSizePolicyV,
        strStyleSheet:str=c_strBtnToolStyleSheet,
        strMethClick:str=c_strBtnToolMethClick
    ):
        super().__init__()

        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strCaption=strCaption
        self.blnValue=bool(blnValue)
        self.blnValueOrig=bool(blnValue)
        self.strValue=str(blnValue)
        self.strValueOrig = str(strValueOrig)
        self.blnChg=False
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnChkable=blnChkable
        self.strToolTip=strToolTip
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udePopupMode=udePopupMode
        self.udeArrowType=udeArrowType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.strStyleSheet=strStyleSheet

        self.strMethClick=strMethClick

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnCaption(self.strCaption)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnChkable(self.blnChkable)
        self.fnToolTip(self.strToolTip)
        self.fnPopupMode(self.udePopupMode)
        self.fnArrowType(self.udeArrowType)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnStyleSheet(self.strStyleSheet)

        self.clicked.connect(self.evtClick)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnCaption(self, strCaption:str):
        self.strCaption=strCaption
        self.setText(strCaption)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnChkable(self, blnChkable:bool):
        self.blnChkable=blnChkable
        self.setCheckable(blnChkable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnPopupMode(self, udePopupMode:udeQtToolButtonPopupMode):
        self.udePopupMode=udePopupMode
        self.setPopupMode(udePopupMode.value)

    def fnArrowType(self, udeArrowType:udeQtToolButtonArrowType):
        self.udeArrowType=udeArrowType
        self.setArrowType(udeArrowType.value)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyH
        self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtClick(self):
        self.blnValue=self.isChecked()
        self.strValue=str(self.blnValue)
        self.blnChg=self.blnValue!=self.blnValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethClick)

    def fnValueChgDet(self):
        self.blnChg=self.blnValue!=self.blnValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.blnValue = bool(strValue)
            self.strValue = strValue
        self.blnValueOrig=self.blnValue
        self.strValueOrig=self.strValue
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setChecked(self.blnValueOrig)
        self.blnValue=self.blnValueOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QToolButton; QBtnTool>

# <PyCmt:QRadioButton; QBtnRadio>
class QBtnRadio(QtWidgets.QRadioButton):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBtnRadioObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBtnRadioLayoutInd,
        strCaption:str=c_strBtnRadioCaption,
        blnValue:bool=c_blnBtnRadioValue,
        strTag: str = c_strBoxRadioTag,
        blnVisible:bool=c_blnBtnRadioVisible,
        blnEnable:bool=c_blnBtnRadioEnable,
        blnChkable:bool=c_blnBtnRadioChkable,
        strToolTip:str=c_strBtnRadioToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBtnRadioLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeSizePolicyV,
        strStyleSheet:str=c_strBtnRadioStyleSheet,
        strMethClick:str=c_strBtnRadioMethClick
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strCaption=strCaption
        self.blnValue=bool(blnValue)
        self.blnValueOrig=bool(blnValue)
        self.strValue=str(blnValue)
        self.strValueOrig = str(blnValue)
        self.blnChg=False
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnChkable=blnChkable
        self.strToolTip=strToolTip
        self.udeLayoutRoleType=udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.strStyleSheet=strStyleSheet

        self.strMethClick=strMethClick

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnCaption(self.strCaption)
        self.fnValue(self.blnValue)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnChkable(self.blnChkable)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnStyleSheet(self.strStyleSheet)

        self.clicked.connect(self.evtClick)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnCaption(self, strCaption:str):
        self.strCaption=strCaption
        self.setText(strCaption)

    def fnValue(self, blnValue:bool):
        self.blnValue=blnValue
        self.setChecked(blnValue)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnChkable(self,blnChkable:bool):
        self.blnChkable=blnChkable
        self.setCheckable(blnChkable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udePolicyH.value, udePolicyV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtClick(self):
        self.blnValue=self.isChecked()
        self.strValue=str(self.blnValue)
        self.blnChg=self.blnValue!=self.blnValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethClick)

    def fnValueChgDet(self):
        self.blnChg=self.blnValue!=self.blnValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.blnValue = bool(strValue)
            self.strValue = strValue
        self.blnValueOrig=self.blnValue
        self.strValueOrig = self.strValue
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setChecked(self.blnValueOrig)
        self.blnValue=self.blnValueOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QRadioButton; QBtnRadio>

# <PyCmt:QCheckBox; QBtnChk>
class QBoxChk(QtWidgets.QCheckBox):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBoxChkObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBoxChkLayoutInd,
        strCaption:str=c_strBoxCkhCaption,
        blnValue:bool=c_blnBoxChkValue,
        strTag:str=c_strBoxChkTag,
        blnVisible:bool=c_blnBoxChkVisible,
        blnEnable:bool=c_blnBoxChkEnable,
        blnChkable:bool=c_blnBoxChkChkable,
        strToolTip:str=c_strBoxChkToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBoxChkLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeBoxChkSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBoxChkSizePolicyV,
        strStyleSheet:str=c_strBoxChkStyleSheet,
        strMethStateChg:str=c_strBoxChkMethStateChg
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.strCaption=strCaption
        self.blnValue=bool(blnValue)
        self.blnValueOrig=bool(blnValue)
        self.strValue=str(blnValue)
        self.strValueOrig= str(blnValue)
        self.blnChg=False
        self.strTag=strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnChkable=blnChkable
        self.strToolTip=strToolTip
        self.udeLayoutRoleType = udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.strStyleSheet=strStyleSheet
        self.strMethStateChg=strMethStateChg

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnCaption(self.strCaption)
        self.fnValue(self.blnValue)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnChkable(self.blnChkable)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnStyleSheet(self.strStyleSheet)

        self.stateChanged.connect(self.evtStateChg)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnCaption(self, strCaption:str):
        self.strCaption=strCaption
        self.setText(strCaption)

    def fnValue(self, blnValue:bool):
        self.blnValue=blnValue
        self.setChecked(blnValue)

    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnChkable(self,blnChkable:bool):
        self.blnChkable=blnChkable
        self.setCheckable(blnChkable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udePolicyH.value, udePolicyV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtStateChg(self):
        self.blnValue=self.isChecked()
        self.strValue=str(self.blnValue)
        self.blnChg=self.isChecked()!=self.blnValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethStateChg, self)

    def fnValueChgDet(self):
        self.blnChg=self.isChecked()!=self.blnValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.blnValue = bool(strValue)
            self.strValue = strValue
        self.blnValueOrig=self.blnValue
        self.strValueOrig=str(self.strValue)
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setChecked(self.blnValueOrig)
        self.blnValue=self.blnValueOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QtCheckBox; QBtnChk>

# <PyCmt:Qt\SpinBox; QBoxSpin>
class QBoxSpin(QtWidgets.QSpinBox):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBoxSpinObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBoxSpinLayoutInd,
        intValue:int=c_intBoxSpinValue,
        intValueMin:int=c_intBoxSpinValueMin,
        intValueMax:int=c_intBoxSpinValueMax,
        strTag: str = c_strBoxSpinTag,
        blnVisible:bool=c_blnBoxSpinVisible,
        blnEnable:bool=c_blnBoxSpinEnable,
        strToolTip:str=c_strBoxSpinToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBoxSpinLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeBoxSpinSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBoxSpinSizePolicyV,
        udeAlignmentH:udeQtAlignment=c_udeBoxSpinAlignmentH,
        udeAlignmentV:udeQtAlignment=c_udeBoxSpinAlignmentV,
        strStyleSheet: str = c_strBoxSpinStyleSheet,
        strMethValueChg:str=c_strBoxSpinMethValueChg
    ):
        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.intValue=int(intValue)
        self.intValueOrig=int(intValue)
        self.strValue=str(intValue)
        self.strValueOrig=str(intValue)
        self.blnChg=False
        self.strTag = strTag
        self.intValueMin=intValueMin
        self.intValueMax=intValueMax
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.strToolTip=strToolTip
        self.udeLayoutRoleType = udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV=udeAlignmentV
        self.strStyleSheet = strStyleSheet

        self.strMethValueChg=strMethValueChg

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnValue( self.intValue)
        self.fnValueMin(self.intValueMin)
        self.fnValueMax(self.intValueMax)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(
            self.udeSizePolicyH,
            self.udeSizePolicyV
        )
        self.fnAlignment(self.udeAlignmentH,self.udeAlignmentV)
        self.fnStyleSheet(self.strStyleSheet)
        
        self.valueChanged.connect(self.evtValueChg)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnValue(self, intValue:int):
        self.intValue=intValue
        self.setValue(intValue)

    def fnValueMin(self, intValueMin:int):
        self.intValueMin=intValueMin
        self.setMinimum(intValueMin)

    def fnValueMax(self, intValueMax:int):
        self.intValueMax=intValueMax
        self.setMaximum(intValueMax)
        
    def fnVisible(self, blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self, blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnToolTip(self, strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

    def fnAlignment(
        self,
        udeAlignmentH:udeQtAlignment,
        udeAlignmentV:udeQtAlignment
    ):
        self.udeAlignmentH=udeAlignmentH
        self.udeAlignmentV = udeAlignmentV
        self.setAlignment(udeAlignmentH.value)
        self.setAlignment(udeAlignmentV.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtValueChg(self):
        self.intValue=self.value()
        self.strValue=str(self.intValue)
        self.blnChg = self.value() != self.intValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethValueChg, self)

    def fnValueChgDet(self):
        self.blnChg=self.value()!=self.intValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.intValue = int(strValue)
            self.strValue = strValue
        self.intValueOrig = int(self.intValue)
        self.strValueOrig=str(self.strValue)
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setValue(self.intValueOrig)
        self.intValue=self.intValueOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QSpinBox; QBoxSpin>

# <PyCmt:QComboBox; QBoxCmb>
class QBoxCmb(QtWidgets.QComboBox):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBoxCmbObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBoxCmbLayoutInd,
        lstItem:list=None,
        strValue:str=c_strBoxCmbValue,
        strTag:str=c_strBoxCmbTag,
        blnVisible:bool=c_blnBoxCmbVisible,
        blnEnable:bool=c_blnBoxCmbEnable,
        blnEditable:bool=c_blnBoxCmbEditable,
        strToolTip:str=c_strBoxCmbToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBoxCmbLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeBoxCmbSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBoxCmbSizePolicyV,
        strStyleSheet:str=c_strBoxCmbStyleSheet,
        strMethIndexChg:str = c_strBoxCmbMethIndexChg,
        strMethTextChg:str=c_strBoxCmbMethTextChg
    ):
        if lstItem is None: lstItem=c_lstBoxCmbItem

        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.lstItem=lstItem
        self.strValue=str(strValue)
        self.strValueOrig=str(strValue)
        self.strText=strValue
        self.strTextOrig=self.strText
        self.blnChg=False
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnEditable=blnEditable
        self.strToolTip=strToolTip
        self.udeLayoutRoleType = udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.strStyleSheet=strStyleSheet
        self.strMethIndexChg=strMethIndexChg
        self.strMethTextChg = strMethTextChg

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnItem(self.lstItem)
        self.fnValue(self.strValue)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnEditable(self.blnEditable)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnBoxCmbMinHeight(26)
        self.fnSizeAdjustPolicy(
            adjustPolicy=QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents
        )
        self.fnStyleSheet(self.strStyleSheet)

        self.currentIndexChanged.connect(self.evtIndexChg)
        self.currentTextChanged.connect(self.evtTextChg)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnItem(self,lstItem:list):
        if not lstItem is None:
            for strItem in lstItem:
                self.addItem(str(strItem))

    def fnValue(self,strValue:str):
        self.strValue=strValue
        intIndex=self.findText(str(self.strValue))
        self.setCurrentIndex(intIndex)

    def fnVisible(self,blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable:bool):
        self.blnEnable=blnEnable
        if blnEnable:
            strStyleSheet = 'QComboBox{background-color:white;border:1px solid gray;}'
        else:
            strStyleSheet = ''
        self.fnStyleSheet(strStyleSheet)
        self.setEnabled(blnEnable)

    def fnEditable(self,blnEditable:bool):
        self.blnEditable=blnEditable
        self.setEditable(blnEditable)

    def fnToolTip(self,strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV

    def fnBoxCmbMinHeight(self, intMinHeight:int):
        self.setMinimumHeight(intMinHeight)

    def fnSizeAdjustPolicy(self, adjustPolicy):
        self.setSizeAdjustPolicy(adjustPolicy)
        # self.setMinimumWidth(self.width())

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def evtIndexChg(self):
        self.strValue=self.currentText()
        self.blnChg = self.currentText() != self.strValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethIndexChg, self)

    def evtTextChg(self):
        self.strText=self.currentText()
        self.strValue=self.strText
        self.blnChg = self.currentText() != self.strValueOrig
        EHPyMdl.fnMdlFuncCall(self.strMethTextChg, self)

    def fnValueChgDet(self):
        self.blnChg = self.currentText() != self.strValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue: self.strValue=strValue
        self.strValueOrig = str(self.strValue)
        self.blnChg = False

    def fnValueChgDiscard(self):
        self.setCurrentText(self.strTextOrig)
        self.strText=self.strTextOrig
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QComboBox; QBoxCmb>

# <PyCmt:QListWidget; QBoxLst>
class QBoxLst(QtWidgets.QListWidget):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBoxLstObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBoxLstLayoutInd,
        lstItem:list=None,
        strValue:str=c_strBoxLstValue,
        strTag: str = c_strBoxLstTag,
        blnVisible:bool=c_blnBoxLstVisible,
        blnEnable:bool=c_blnBoxLstEnable,
        blnSeltRect:bool=c_blnBoxLstSeltRect,
        strToolTip:str=c_strBoxLstToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBoxLstLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeBoxLstSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBoxLstSizePolicyV,
        udeFrmShp:udeQtFrmShp=c_udeBoxLstFrmShp,
        strStyleSheet:str=c_strBoxLstStyleSheet,
        strMethItmChg:str=c_strBoxLstMethItmChg
    ):
        if lstItem is None: lstItem = c_lstBoxLstItem

        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.lstItem=lstItem
        self.strValue=str(strValue)
        self.strValueOrig=str(strValue)
        self.blnChg=False
        self.strTag=strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.blnSeltRect=blnSeltRect
        self.strToolTip=strToolTip
        self.udeLayoutRoleType = udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeFrmShp=udeFrmShp
        self.strStyleSheet=strStyleSheet
        self.strMethItmChg=strMethItmChg

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnItem(self.lstItem)
        self.fnValue(self.strValue)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnSeltRect(self.blnSeltRect)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnFrmShp(self.udeFrmShp)
        self.fnStyleSheet(self.strStyleSheet)

        self.itemChanged.connect(self.evtItmChg)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnItem(self,lstItem:list):
        if not lstItem is None:
            for strItem in lstItem:
                self.addItem(str(strItem))

    def fnValue(self,strValue:str):
        self.strValue=strValue
        intIndex=self.findItems(self.strValue, Qt.MatchFlag.MatchExactly)
        self.setCurrentIndex(intIndex)

    def fnVisible(self,blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnSeltRect(self,blnSeltRect:bool):
        self.blnSeltRect=blnSeltRect
        self.setSelectionRectVisible(blnSeltRect)

    def fnToolTip(self,strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value,udeSizePolicyV.value)
        self.adjustSize()

    def fnFrmShp(self,udeFrmShp:udeQtFrmShp):
        self.udeFrmShp=udeFrmShp
        self.setFrameShape(udeFrmShp.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)
        
    def evtItmChg(self):
        self.strValue=self.currentItem()
        self.blnChg = self.currentItem() != self.strValueOrig
        EHPyMdl.fnMdlFuncCall(self.c_strBoxLstMethItmChg, self)

    def fnValueChgDet(self):
        self.blnChg=self.currentItem()!=self.strValueOrig
        return self.blnChg

    def fnValueSetDft(self, strValue:str=None):
        if strValue:
            self.strValue = strValue
        self.strValueOrig = str(self.strValue)
        self.blnChg = False

    def fnValueChgDiscard(self):
        intIndex=self.findItems(self.strValueOrig, Qt.MatchFlag.MatchExactly)
        self.setCurrentIndex(intIndex)
        self.strValue=self.strValueOrig
        self.blnChg = False
# </PyCmt:QListWidget; QBoxLst>

# <PyCmt:QTreeWidget; QBoxTree>
class QBoxTree(QtWidgets.QTreeWidget):
    def __init__(
            self,
            objParent:object,
            strName:str,
            strObjName:str=c_strBoxTreeObjName,
            objLayoutInd:QtWidgets.QLayout=c_objBoxTreeLayoutInd,
            lstTitleRow:list=None,
            intRowCount:int=c_intBoxTreeRowCount,
            intColCount:int=c_intBoxTreeColCount,
            intColKey:int=c_intBoxTreeColKey,
            lstItem:list=None,
            blnSortingEnabled:bool=c_blnBoxTreeSortingEnabled,
            blnEditDblClick:bool=c_blnBoxTreeDblClick,
            blnEditKeyPress:bool=c_blnBoxTreeKeyPress,
            blnDragEnable:bool=c_blnBoxTreeDragEnable,
            udeDragDropMode:udeQtBoxTreeDragDropMode=c_udeBoxTreeDragDropMode,
            blnRowColor:bool=c_blnBoxTreeRowColor,
            udeSeltMode:udeQtBoxTreeSeltMode=c_udeBoxTreeSeltMode,
            udeTextElideMode:udeQtTextElideMode=c_udeBoxTreeTextElideMode,
            intIndentation:int=c_intBoxTreeIndentation,
            blnHeaderVisible:bool=c_blnBoxTreeHeaderVisible,
            intRowSelt:int=c_intBoxTreeRowSelt,
            strTag: str = c_strBoxTreeTag,
            blnVisible:bool=c_blnBoxTreeVisible,
            blnEnable:bool=c_blnBoxTreeEnable,
            strToolTip:str=c_strBoxTreeToolTip,
            udeLayoutRoleType:udeQtLayoutRoleType=c_udeBoxTreeLayoutRoleType,
            udeSizePolicyH:udeQtSizePolicy=c_udeBoxTreeSizePolicyH,
            udeSizePolicyV:udeQtSizePolicy=c_udeBoxTreeSizePolicyV,
            blnMinSizeCol:bool=c_blnBoxTreeMinSizeCol,
            udeFrmShp:udeQtFrmShp=c_udeBoxTreeFrmShp,
            strStyleSheet: str = c_strBoxTreeStyleSheet,
            strMethItemSelt:str='',
            strMethItemClick:str=''
    ):
        if lstTitleRow is None: lstTitleRow = c_lstBoxTreeTitleRow
        if lstItem is None: lstItem = c_lstBoxTreeItem

        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.lstTitleRow=lstTitleRow
        self.lstItem=lstItem
        self.intItemCount=0
        self.intRowCount=intRowCount
        self.intColCount=intColCount
        self.intColKey=intColKey
        self.strValue =''
        self.strValueOrig =''
        self.blnSortingEnabled=blnSortingEnabled
        self.blnEditDblClick=blnEditDblClick
        self.blnEditKeyPress=blnEditKeyPress
        self.blnDragEnable=blnDragEnable
        self.udeDragDropMode=udeDragDropMode
        self.blnRowColor=blnRowColor
        self.udeSeltMode=udeSeltMode
        self.udeTextElideMode=udeTextElideMode
        self.intIndentation=intIndentation
        self.blnHeaderVisible=blnHeaderVisible
        self.intRowSelt=intRowSelt
        self.intRowOrig=intRowSelt
        self.strValue=''
        self.strValueOrig=''
        self.blnChg=False
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.strToolTip=strToolTip
        self.udeLayoutRoleType = udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.blnMinSizeCol=blnMinSizeCol
        self.udeFrmShp=udeFrmShp
        self.strStyleSheet=strStyleSheet
        self.strMethItemSelt=strMethItemSelt
        self.strMethItemClick=strMethItemClick

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        # <PyCmt:SetTreeCol to 0>
        self.fnColDefault()
        self.fnTitleRow(self.lstTitleRow)
        self.fnItem(
            self.lstItem,
            self.intRowCount,
            self.intColCount
        )
        self.fnSortingEnabled(self.blnSortingEnabled)
        self.fnEditDblClick(self.blnEditDblClick)
        self.fnEditKeyPress(self.blnEditKeyPress)
        self.fnDragEnable(self.blnDragEnable)
        self.fnDragDropMode(self.udeDragDropMode)
        self.fnRowColor(self.blnRowColor)
        self.fnSeltMode(self.udeSeltMode)
        self.fnTextElideMode(self.udeTextElideMode)
        self.fnIndentation(self.intIndentation)
        self.fnHeaderVisible(self.blnHeaderVisible)
        # <PyCmt: Setup strValue and strValueOrig >
        self.fnRowSelt(self.intRowSelt, self.intColKey, blnInit = True)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(
            self.udeSizePolicyH,
            self.udeSizePolicyV,
            self.blnMinSizeCol
        )
        self.fnScrollBarDft()
        self.fnFrmShp(self.udeFrmShp)
        self.fnStyleSheet(self.strStyleSheet)

        self.itemSelectionChanged.connect(self.evtItmSelt)
        self.itemClicked.connect(self.evtItmClick)

    @property
    def ItemCount(self):
        self.fnTreeItemIter(treeRun=self)
        return self.intItemCount

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self,strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnColDefault(self):
        self.setColumnCount(0)

    def fnTitleRow(self,lstTitleRow):
        self.lstTitleRow=lstTitleRow
        if lstTitleRow:
            self.setHeaderLabels(lstTitleRow)
        else:
            self.fnHeaderVisible(False)

    def fnItem(
            self,
            lstItem,
            intRowCount=c_intBoxTreeRowCount,
            intColCount=c_intBoxTreeColCount
    ):
        if EHArray.fnArrayDimGet(lstItem) != 2:
            import EHMsg
            EHMsg.fnDlgOpt('lstItem dimension error!')
            return

        self.lstItem=lstItem
        if intRowCount==-1 and not lstItem is None:
            intRowCount=len(lstItem)
        self.intRowCount=intRowCount

        if intColCount==-1 and not lstItem is None:
            intColCount=len(lstItem[0])
        self.intColCount=intColCount
        self.setColumnCount(intColCount)

        itmLast=None
        for intRow in range(intRowCount):
            if self.intItemCount==0:
                itemParent = self
            elif self.intItemCount==1:
                itemParent = itmLast
            else:
                strItmKey=self.lstItem[intRow][self.intColKey]
                strParentFind=c_strBoxTreeSplitor.join(strItmKey.split(c_strBoxTreeSplitor)[:-1])
                if len(strParentFind)>0 :
                    itemKey= \
                        self.fnTreeItemIter(
                            treeRun=self,
                            strMatch=strParentFind
                        )
                    if itemKey:
                        itemParent=itemKey[self.intColKey]
                    else:
                        itemParent=self
                else:
                    if itmLast:
                        itemParent=itmLast
                    else:
                        itemParent=self

            itmLast=QtWidgets.QTreeWidgetItem(itemParent, lstItem[intRow][:intColCount])
            self.setCurrentItem(itmLast)
            self.intItemCount+=1

        # for intLayer in range(self.topLevelItemCount()):
        #     self.topLevelItem(intLayer).setExpanded(True)

    def fnSortingEnabled(self,blnSortingEnabled):
        self.blnSortingEnabled=blnSortingEnabled
        self.setSortingEnabled(blnSortingEnabled)

    def fnEditDblClick(self,blnEditDblClick):
        self.blnEditDblClick=blnEditDblClick
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)

    def fnEditKeyPress(self,blnEditKeyPress):
        self.blnEditKeyPress=blnEditKeyPress
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)

    def fnDragEnable(self,blnDragEnable):
        self.blnDragEnable=blnDragEnable
        self.setDragEnabled(blnDragEnable)

    def fnDragDropMode(self,udeDragDropMode):
        self.udeDragDropMode=udeDragDropMode
        self.setDragDropMode(udeDragDropMode.value)

    def fnRowColor(self,blnRowColor):
        self.blnRowColor=blnRowColor
        self.setAlternatingRowColors(blnRowColor)

    def fnSeltMode(self,udeSeltMode):
        self.udeSeltMode=udeSeltMode
        self.setSelectionMode(udeSeltMode.value)

    def fnTextElideMode(self,udeTextElideMode):
        self.udeTextElideMode=udeTextElideMode
        self.setTextElideMode(udeTextElideMode.value)

    def fnIndentation(self,intIndentation):
        self.intIndentation=intIndentation
        self.setIndentation(intIndentation)

    def fnHeaderVisible(self,blnHeaderVisible):
        self.blnHeaderVisible=blnHeaderVisible
        self.setHeaderHidden(not blnHeaderVisible)

    def fnRowSelt(
        self,
        intRowSelt:int,
        intColKey:int=-1,
        blnInit:bool=False
    ):
        if intColKey==-1: intColKey=c_intBoxTreeColKey

        self.intRowSelt=intRowSelt
        self.fnTreeItemIter(treeRun=self, intRowSelt=intRowSelt)
        if len(self.selectedItems())>0:
            self.strValue=self.selectedItems()[0].text(intColKey)
        if blnInit:
            self.strValueOrig=self.strValue

    def fnVisible(self,blnVisible):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnToolTip(self,strToolTip):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy,
        blnMinSizeCol:bool
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.blnMinSizeCol=blnMinSizeCol
        if self.udeSizePolicyV==udeQtSizePolicy.udeQtSizePolicyMin or \
                self.udeSizePolicyV==udeQtSizePolicy.udeQtSizePolicyMinExp:
            self.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.resizeColumnToContents(0)
        else:
            self.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.setSizePolicy(self.udeSizePolicyH.value, self.udeSizePolicyV.value)
        if blnMinSizeCol :
            intColWidth:int=0
            for intCol in range(self.columnCount()):
                intColWidth+=self.sizeHintForColumn(intCol)
            intColWidth+=self.horizontalScrollBar().sizeHint().width()
            self.setMinimumWidth(intColWidth)

    def fnScrollBarDft(self):
        # <PyCmt:Scroll Bar Setup only on udeQtSizePolicyV=udeQtSizePolicyMin>
        if self.topLevelItemCount()>0 and \
            not self.blnMinSizeCol and \
            self.udeSizePolicyV==udeQtSizePolicy.udeQtSizePolicyMin:
            self.horizontalScrollBar().setFixedWidth(self.width())
            self.verticalScrollBar().setFixedHeight(self.height())
            
    def fnFrmShp(self,udeFrmShp):
        self.udeFrmShp=udeFrmShp
        self.setFrameShape(udeFrmShp.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)
        
    def evtItmSelt(self):
        self.intRowSelt= \
            self.fnTreeItemIter(
                treeRun=self,
                blnRtnRow=True
            )
        self.strValue=self.selectedItems()[0].text(self.intColKey)
        if not self.blnChg:
            self.blnChg= \
                self.selectedItems()[0].text(self.intColKey) != self.strValueOrig
        if len(self.strMethItemSelt)==0: return
        itemColl=self.selectedItems()
        EHPyMdl.fnMdlFuncCall(self.strMethItemSelt, itemColl)

    def evtItmClick(self):
        if len(self.strMethItemClick) == 0: return
        itemColl=self.selectedItems()
        EHPyMdl.fnMdlFuncCall(self.strMethItemClick, itemColl)

    @staticmethod      
    def fnTreeItemIter(
            treeRun:QtWidgets.QTreeWidget,
            intColMatch:int=-1,
            strMatch:str='',
            blnStartWith:bool=False,
            intRowSelt:int=-1,
            blnRtnRow:bool=False
    )->list:
        if len(strMatch)>0 and intColMatch<0: intColMatch=c_intBoxTreeColKey

        # <PyCmt: Loop TreeWidget Each Item, and Compare strMatch>
        iterRun =QtWidgets.QTreeWidgetItemIterator(treeRun)
        intRow:int=0
        lstItmMatch=[]
        while iterRun.value():
            itmRun:QtWidgets.QTreeWidgetItem = iterRun.value()
            if intColMatch>=0:
                for intCol in range(itmRun.columnCount()):
                    if intCol==intColMatch :
                        if blnStartWith:
                            if itmRun.text(intCol).startswith(strMatch):
                                lstItmMatch.append(itmRun)
                                if intRowSelt==-1: intRowSelt=intRow
                        elif itmRun.text(intCol)==strMatch:
                            lstItmMatch.append(itmRun)
                            if intRowSelt == -1: intRowSelt = intRow
            if 0 < intRowSelt == intRow:
                treeRun.setCurrentItem(itmRun)
            elif blnRtnRow and itmRun is treeRun.currentItem():
                return intRow
            itmRun.setExpanded(True)
            iterRun += 1
            intRow+=1
        return lstItmMatch

    def fnItemAdd(self, itmParent:QtWidgets.QTreeWidgetItem, lstItm:list):
        itmParent.addChild(QtWidgets.QTreeWidgetItem(itmParent, lstItm))
        self.lstItem.append(lstItm)
        itmParent.setExpanded(True)
        self.repaint()
        self.fnItmSelt(strItmKey=lstItm[c_intBoxTreeColKey], intColKey=c_intBoxTreeColKey)
        self.strValue = lstItm[c_intBoxTreeColKey]
        self.blnChg=True

    def fnItmSelt(
        self,
        strItmKey:str,
        intColKey:int=-1,
    )->QtWidgets.QTreeWidgetItem:
        if intColKey==-1: intColKey=c_intBoxTreeColKey
        itmFound= \
            self.findItems(
                strItmKey,
                Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive,
                intColKey
            )
        if itmFound: self.setCurrentItem(itmFound[0])

    def fnValueChgDet(self):
        return self.blnChg

    def fnValueSetDft(self):
        self.intRowOrig=self.intRowSelt
        self.strValueOrig=str(self.strValue)
        self.blnChg=False

    def fnValueChgDiscard(self):
        self.fnTreeItemIter(treeRun=self,intRowSelt = self.intRowOrig)
        self.intRowSelt=self.intRowOrig
        self.strValue=self.strValueOrig
        self.blnChg = False

    @staticmethod
    def fnTreeKeyMaxGet(itmParent:QtWidgets.QTreeWidgetItem)->str:
        treeRun=itmParent.treeWidget()
        strParentKey=itmParent.text(c_intBoxTreeColKey)
        lstKey= \
            treeRun.fnTreeItemIter(
                treeRun=treeRun,
                strMatch=strParentKey+c_strBoxTreeSplitor,
                blnStartWith=True
            )

        if len(lstKey)>0:
            lstKeyStr:list=[]
            for itmTree in lstKey:
                lstKeyStr.append(itmTree.text(c_intBoxTreeColKey))
            lstKeyStr=sorted(lstKeyStr, reverse=True)
            strItmKey=lstKeyStr[0]
            strKeyTail=int(strItmKey.split(c_strBoxTreeSplitor)[-1])+1
            strItmKey=c_strBoxTreeSplitor.join(strItmKey.split(c_strBoxTreeSplitor)[:-1])
            return strItmKey+c_strBoxTreeSplitor+str(strKeyTail)
        else:
            return strParentKey+c_strBoxTreeSplitor+str(1)
# </PyCmt:QTreeWidget; QBoxTree>

# <PyCmt:QTableWidget; QBoxTbl>
class QBoxTbl(QtWidgets.QTableWidget):
    def __init__(
        self,
        objParent:object,
        strName:str,
        strObjName:str=c_strBoxTblObjName,
        objLayoutInd:QtWidgets.QLayout=c_objBoxTblLayoutInd,
        lstTitleRow:list=None,
        lstTitleCol:list=None,
        intRowCount:int=c_intBoxTblRowCount,
        intColCount:int=c_intBoxTblColCount,
        lstItem:list=None,
        intSeltRow:int=c_intBoxTblSeltRow,
        strTag: str = c_strBoxTblTag,
        blnVisible:bool=c_blnBoxTblVisible,
        blnEnable:bool=c_blnBoxTblEnable,
        udeSeltMode:udeQtBoxTblSeltMode=c_udeBoxTblSeltMode,
        strToolTip:str=c_strBoxTblToolTip,
        udeLayoutRoleType:udeQtLayoutRoleType=c_udeBoxTblLayoutRoleType,
        udeSizePolicyH:udeQtSizePolicy=c_udeBoxTblSizePolicyH,
        udeSizePolicyV:udeQtSizePolicy=c_udeBoxTblSizePolicyV,
        udeFrmShp:udeQtFrmShp=c_udeBoxTblFrmShp,
        strStyleSheet:str=c_strBoxTblStyleSheet
    ):
        if lstTitleRow is None: lstTitleRow = c_lstBoxTblTitleRow
        if lstTitleCol is None: lstTitleCol = c_lstBoxTblTitleCol
        if lstItem is None: lstItem = c_lstBoxTblItem

        super().__init__()
        self.objParent=objParent
        self.strName=strName
        self.strObjName=strObjName
        self.objLayoutInd=objLayoutInd
        self.lstTitleRow=lstTitleRow
        self.lstTitleCol=lstTitleCol
        self.intRowCount=intRowCount
        self.intColCount=intColCount
        self.lstItem=lstItem
        self.intSeltRow=intSeltRow
        self.blnChg=False
        self.strTag = strTag
        self.blnVisible=blnVisible
        self.blnEnable=blnEnable
        self.udeSeltMode=udeSeltMode
        self.strToolTip=strToolTip
        self.udeLayoutRoleType = udeLayoutRoleType
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.udeFrmShp=udeFrmShp
        self.strStyleSheet = strStyleSheet

        self.fnParent(self.objParent, self.udeLayoutRoleType)
        self.fnName(self.strName)
        self.fnTitleRow(self.lstTitleRow)
        self.fnTitleCol(self.lstTitleCol)
        self.fnRowCount(self.intRowCount)
        self.fnColCount(self.intColCount)
        self.fnItem(self.lstItem)
        self.fnSeltRow(self.intSeltRow)
        self.fnVisible(self.blnVisible)
        self.fnEnable(self.blnEnable)
        self.fnSeltMode(self.udeSeltMode)
        self.fnToolTip(self.strToolTip)
        self.fnSizePolicy(self.udeSizePolicyH, self.udeSizePolicyV)
        self.fnFrmShp(self.udeFrmShp)
        self.fnStyleSheet(self.strStyleSheet)

    def fnParent(self, objParent, udeLayoutRoleType):
        fnParentSet(
            objRun = self,
            objParent=objParent,
            udeLayoutRoleType=udeLayoutRoleType
        )

    def fnName(self, strName):
        self.strName=strName
        self.setObjectName(strName)

    def fnTitleRow(self, lstTitleRow:list):
        self.lstTitleRow=lstTitleRow
        if not lstTitleRow is None:
            self.setHorizontalHeaderLabels(lstTitleRow)

    def fnTitleCol(self, lstTitleCol:list):
        self.lstTitleCol=lstTitleCol
        if not lstTitleCol is None:
            self.setVerticalHeaderLabels(lstTitleCol)

    def fnRowCount(self, intRowCount:int):
        if intRowCount==-1:intRowCount=len(self.lstItem)
        self.intRowCount=intRowCount
        self.setRowCount(intRowCount)

    def fnColCount(self, intColCount:int):
        if intColCount==-1:intColCount=len(self.lstItem[0])
        self.intColCount=intColCount
        self.setColumnCount(intColCount)

    def fnItem(self,lstItem:list):
        self.lstItem=lstItem
        for intRowRun in range(self.intRowCount):
            lstRowData=lstItem[intRowRun]
            for intColRun in range(self.intColCount):
                strCellData=lstRowData[intColRun]
                self.setItem(intRowRun, intColRun, QTableWidgetItem(strCellData))

    def fnSeltRow(self,intSeltRow:int):
        self.intSeltRow=intSeltRow
        self.selectRow(intSeltRow)

    def fnVisible(self,blnVisible:bool):
        self.blnVisible=blnVisible
        self.setVisible(blnVisible)

    def fnEnable(self,blnEnable:bool):
        self.blnEnable=blnEnable
        self.setEnabled(blnEnable)

    def fnSeltMode(self,udeSeltMode:udeQtBoxTblSeltMode):
        self.udeSeltMode=udeSeltMode
        self.setSelectionMode(self.udeSeltMode.value)

    def fnToolTip(self,strToolTip:str):
        self.strToolTip=strToolTip
        self.setToolTip(strToolTip)

    def fnSizePolicy(
        self,
        udeSizePolicyH:udeQtSizePolicy,
        udeSizePolicyV:udeQtSizePolicy
    ):
        self.udeSizePolicyH=udeSizePolicyH
        self.udeSizePolicyV=udeSizePolicyV
        self.setSizePolicy(udeSizePolicyH.value, udeSizePolicyV.value)

    def fnFrmShp(self,udeFrmShp:udeQtFrmShp):
        self.udeFrmShp=udeFrmShp
        self.setFrameShape(udeFrmShp.value)

    def fnStyleSheet(self, strStyleSheet):
        self.strStyleSheet=strStyleSheet
        if len(strStyleSheet)>0: self.setStyleSheet(strStyleSheet)

    def fnValueChgDet(self):
        return self.blnChg
# </PyCmt:QTableWidget; QBoxTbl>

# <PyCmt:QtWidget>
def fnParentSet(
    objRun:QtWidgets.QWidget,
    *args,
    **kwargs
)->bool:
    objLayout=None
    if not objRun.objParent is None:
        if isinstance(objRun.objParent, QWgetCentral):
            objParentRun = objRun.objParent
        elif hasattr(objRun.objParent,'QWgetCentral'):
            if not objRun.objParent.QWgetCentral is None :
                objParentRun = objRun.objParent.QWgetCentral
                objLayout = objRun.objParent.QWgetCentral.layout
            else:
                objParentRun = objRun.objParent
        else:
            objParentRun = objRun.objParent

        if not objRun.objLayoutInd is None:
            objLayout = objRun.objLayoutInd
        elif not objLayout:
            objLayout = objRun.objParent.layout

        objRun.setParent(objParentRun)

        # <PyCmt: Add Object with setup Changed Detect Function into lstChgDetSub>
        if hasattr(objParentRun,'lstChgDetSub') and \
            hasattr(objRun,'blnChg'):
            objParentRun.lstChgDetSub.append(objRun)
        elif c_strAttrSplitor + objRun.strObjName + c_strAttrSplitor in \
            c_strAttrSplitor + c_strContainerColl + c_strAttrSplitor and \
            hasattr(objParentRun, 'fnSubValueChgDet'):
            objParentRun.lstChgDetSub.append(objRun)

        if isinstance(objLayout, QtWidgets.QFormLayout):
            udeLayoutRoleType=kwargs.get('udeLayoutRoleType', udeQtLayoutRoleType.udeQtLayoutRoleTypeField)
            intRow=objLayout.rowCount()-1
            if hasattr(objParentRun, 'objLayout'):
                if objParentRun.objLayout.udeLayoutRoleTypeLast.value is None:
                    pass
                elif udeLayoutRoleType==udeQtLayoutRoleType.udeQtLayoutRoleTypeLabel:
                    intRow+=1
                if intRow<0: intRow=0
                objLayout.setWidget(intRow, udeLayoutRoleType.value, objRun)
                objParentRun.objLayout.udeLayoutRoleTypeLast=udeLayoutRoleType
        else:
            objLayout.addWidget(objRun)
        return True

def fnWgetValueChgDet(
    wgetRun:QtWidgets.QWidget,
    blnChg:bool=False,
    lstItmChgd:list=None
):
    if lstItmChgd is None: lstItmChgd = []
    for objRun in wgetRun.lstChgDetSub:
        if hasattr(objRun, 'fnSubValueChgDet'):
            blnChg, lstItmChgd=\
                objRun.fnSubValueChgDet(
                    blnChg=blnChg,
                    lstItmChgd=lstItmChgd
                )
        elif hasattr(objRun, 'fnValueChgDet'):
            if objRun.fnValueChgDet():
                blnChg=True
                lstItmChgd.append(objRun)
    return blnChg, lstItmChgd

def fnStyleSheetProcess(strRun, blnAdd:bool=True):
    pass

def fnChildWidgetDestroy(
    objRun: QtWidgets.QWidget
):
    if isinstance(
        objRun,
        QtWidgets.QGroupBox
        | QtWidgets.QFrame
        | QtWidgets.QScrollArea
        | QtWidgets.QDockWidget,
    ):
        while len(objRun.children()) - 1 > 0:
            if not objRun.findChild(QtWidgets.QWidget) is None:
                objRun.findChild(QtWidgets.QWidget).setParent(None)
        objRun.resize(0,0)
        objRun.fnSizePolicy(
            udeFrmSizePolicyH=objRun.udeFrmSizePolicyH,
            udeFrmSizePolicyV=objRun.udeFrmSizePolicyV,
            intWidth=0,
            intHeight=0,
        )

def fnWidgetDestroy(QtWidget:QtWidgets.QWidget):
    # QtWget.layout.removeWidget(QtWget)
    # QtWget.destroy()
    QtWidget.deleteLater()
# </PyCmt:QtWidget>

# <PyCmt:PyQt Class>
def fnPyQt6ClsGet(strClsName:str='')->list:
    import EHPyMdl
    mdlRun=EHPyMdl.fnMdlLoad(strMdlName = 'PyQt6.QtWidgets')
    lstClsType=EHPyMdl.fnMdlClsNameGet(mdlRun)
    if len(strClsName)==0:
        return lstClsType
    else:
        return [strCls for strCls in lstClsType if strClsName in strCls]
# </PyCmt:PyQt Class>

# <PyCmt:EHPyQt Class>
def fnEHPyQtClsGet(strClsName:str='')->list:
    lstClsName= EHPyMdl.fnMdlClsNameGet(mdlRun = sys.modules[__name__])
    return [strClsNameRun for strClsNameRun in lstClsName if strClsName in strClsNameRun]

# </PyCmt:EHPyQt Class>

# <PyCmt:EHPyQt General Func>
def fnStrValueCvrt(strValue:str):
    if not isinstance(strValue, str):
        if isinstance(strValue, udeQtLayoutType):
            return strValue.value()
        else:
            return strValue

    import inspect
    import EHPyFunc

    lstDataTypeStr, lstDataType = \
        EHPyFunc.fnPyDataType(strUserTypeName=strValue)
    if len(lstDataType)>0: return lstDataType[0]

    strArgName:str=''
    strArgValue:str=''
    dictArgNames = inspect.getargvalues(inspect.currentframe().f_back)
    for strArgName, strArgValue in dictArgNames.locals.items():
        if strArgName!='self': break

    # Get the local variables
    dictArgItems = inspect.getargvalues(inspect.currentframe().f_back)[3]
    for strArgNameRun, strArgValueRun in dictArgItems.items():
        if strArgName=='udeQtLayoutType':
            return strArgValueRun
        else:
            global s_lstEHPyQtUdeColl
            if len(s_lstEHPyQtUdeColl)==0:
                s_lstEHPyQtUdeColl = fnEHPyQtClsGet('ude')
            mdlRun = sys.modules[__name__]
            if strArgName in s_lstEHPyQtUdeColl:
                lstClsEnum= \
                    EHPyMdl.fnMdlEnumClsGet(
                        mdlRun=mdlRun,
                        strClsName=strArgName
                    )
                if strArgValue in lstClsEnum:
                    return getattr(mdlRun, strArgName)[strArgValue]
                else:
                    return None

# </PyCmt:EHPyQt General Func>