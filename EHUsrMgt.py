# EHUsrMgt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>
import os

# import EHDBApply
c_blnSysUserMgtAvail=False
c_blnSysRootMgtFuncAvail=False
c_strRootMgtKey='z'
c_strRootMgtOnKeyFuncName='fnRootMgtChk'

c_strDBColNameUserID='UserID'
c_strDBColNameUserDept='UserDept'
c_strDBColNameUserGrade='UserGrade'
c_strDBColNameUserTitle='UserTitle'
c_strDBColNameUserName='UserName'
c_strDBColNameUserNameLocal='UserNameLocal'
c_strDBColNameUserPCName='UserPCName'
c_strDBColNameUserCUPID='UserCUPID'
c_strDBColNameUserIPAddr='UserIPAddr'
c_strDBColNameUserPwd='UserPwd'
c_strDBColNameUserPWDReqUpd='UserPwdReqUpd'
c_strDBColNameUserAuthExpd='UserAuthExpd'
c_strDBColNameUserPWDUpdTime='UserPwdUpdTime'
c_strDBColNameUserAuthInitTime='UserAuthInitTime'
c_strDBColNameUserAuthExpdTime='UserAuthExpdTime'

# c_dictTblSchemaUserMgt= \
#     {
#         EHDBApply.c_strDBTblColNameUqeNo: EHDBApply.c_strMySQLDataTypeInt,
#         c_strDBColNameUserID: EHDBApply.c_strMySQLDataTypeVarChar + '(10)',
#         c_strDBColNameUserDept: EHDBApply.c_strMySQLDataTypeVarChar + '(10)',
#         c_strDBColNameUserGrade: EHDBApply.c_strMySQLDataTypeInt,
#         c_strDBColNameUserTitle: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
#         c_strDBColNameUserName: EHDBApply.c_strMySQLDataTypeVarChar + '(50)',
#         c_strDBColNameUserNameLocal: EHDBApply.c_strMySQLDataTypeVarChar + '(50)',
#         c_strDBColNameUserPCName: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
#         c_strDBColNameUserCUPID: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
#         c_strDBColNameUserIPAddr: EHDBApply.c_strMySQLDataTypeVarChar + '(256)',
#         c_strDBColNameUserPwd: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
#         c_strDBColNameUserPWDReqUpd: EHDBApply.c_strMySQLDataTypeVarChar + '(1)',
#         c_strDBColNameUserAuthExpd: EHDBApply.c_strMySQLDataTypeVarChar + '(1)',
#         c_strDBColNameUserPWDUpdTime: EHDBApply.c_strMySQLDataTypeDateTime,
#         c_strDBColNameUserAuthInitTime: EHDBApply.c_strMySQLDataTypeDateTime,
#         c_strDBColNameUserAuthExpdTime: EHDBApply.c_strMySQLDataTypeDateTime,
#         EHDBApply.c_strDBTblColNameDeleted: EHDBApply.c_strMySQLDataTypeVarChar + '(1)',
#         EHDBApply.c_strDBTblColNameLastVer: EHDBApply.c_strMySQLDataTypeVarChar + '(1)',
#         EHDBApply.c_strDBTblColNameUploader: EHDBApply.c_strMySQLDataTypeVarChar + '(20)',
#         EHDBApply.c_strDBTblColNameUpdateTime: EHDBApply.c_strMySQLDataTypeDateTime
#     }

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHUsrMgt.py !')
# </PyDecl: RunTime>
class EHUsrMgtClass:
    s_strUSRID: str
    _instance=None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls) #, *args, **kw)
            cls.s_strUSRID=''
            cls.s_blnUserAuth:bool = False
            cls.fnUSRMInit(cls)

        return cls._instance

    def __init__(self):
        self.s_blnUserAuth = False
        self.s_strUSRID = ''
    @property
    def p_blnUserAuth(self)->bool:
        return self.s_blnUserAuth
    @p_blnUserAuth.setter
    def p_blnUserAuth(self, blnAuthNew:bool):
        self.s_blnUserAuth = blnAuthNew

    @property
    def p_strUSRID(self)->str:
        return self.s_strUSRID

    @p_strUSRID.setter
    def p_strUSRID(self, strUSRIDNew:str):
        self.s_strUSRID=strUSRIDNew
    def fnUSRMInit(self):
        self.p_strUSRID=os.environ.get('USERNAME','')
        self.p_blnUserAuth=True