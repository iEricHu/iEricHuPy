# EHAttrMgt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import EHSysMgt
import EHDBApply

#<PyDecl: AttrMgt DBTable Func>
c_strDBTblNameAttr= EHSysMgt.c_strSysDBTblPrefix + 'AttrMgt'
c_strDBColNameAttrType='AttrType'
c_strDBColNameAttrTypeSub='AttrTypeSub'
c_strDBColNameAttrName='AttrName'
c_strDBColNameAttrNameSub='AttrNameSub'
c_strDBColValueAttrValue='AttrValue'
c_strDBColValueAttrValueSub='AttrValueSub'
c_strDBColValueRemark='Remark'

c_dictTblSchemaAttrMgt= \
    {
        EHDBApply.c_strDBTblColNameUqeNo: EHDBApply.c_strDataTypeInt,
        c_strDBColNameAttrType: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrTypeSub1: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrTypeSub2: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrTypeSub3: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrName: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrNameSub1: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrNameSub2: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColNameAttrNameSub3: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrValue: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrValueSub1: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrValueSub2: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrValueSub3: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrRemark: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrRemarkSub1: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrRemarkSub2: EHDBApply.c_strDataTypeVarChar + '(20)',
        c_strDBColValueAttrRemarkSub3: EHDBApply.c_strDataTypeVarChar + '(20)',
        EHDBApply.c_strDBTblColNameDeleted: EHDBApply.c_strDataTypeVarChar + '(1)',
        EHDBApply.c_strDBTblColNameLastVer: EHDBApply.c_strDataTypeVarChar + '(1)',
        EHDBApply.c_strDBTblColNameUploader: EHDBApply.c_strDataTypeVarChar + '(20)',
        EHDBApply.c_strDBTblColNameUpdateTime: EHDBApply.c_strDataTypeDateTime
    }
#<PyDecl: AttrMgt DBTable Func>
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHAttrMgt.py !')
# </PyDecl: RunTime>
def fnAttrTblChk(blnReBud=False)->bool:
    blnResult = \
        EHDBApply.fnDBTblChk(
            strTblName=c_strDBTblNameAttr,
            dictTblSchema=c_dictTblSchemaAttrMgt,
            blnReBud=blnReBud
        )
    return blnResult