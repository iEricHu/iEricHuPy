# EHSysMgt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

# <PyDev: SysMgt>
#  1. UserMgt /LogRecMgt
#  2. DocMgt
#  3. FormMgt(EHUI)
#  4. SQLMgt / DBTableMgt
#  5. ReportMgt
#  6. AutoMgt(Func, Rec)
#  7. LogMgt(Integrate User Log, SQL Log, Debug Log, Error Log?)
#  8. FuncMgt
#  9. SysAttr
# 10. RemarkMgt:
#     All Table may with User Remark request,
#     Remark Mgt should depend on user input to Auto Create Remark ID; Counter Report Name, Remark Name and value.
# 11. RemarkAnalysis
#     Periodically analysis all remarks and generate report for remarks analysis.
# 12. WPS Integrate?
# 13. xlwings.xlam re-study!

# 11. SysMgt:
#     SysMgt should be a module to manage all system related functions, including:
#     - SysInit: Create all system tables and views, create all system functions, procedures, triggers, etc.
#     - SysAttr: Manage system attributes, including:
#         - SysAttrTbl: System Attributes Table
#         - SysAttrMgt: System Attributes Management Function
#     - SysLog: Manage system logs, including:
#         - SysLogTbl: System Logs Table
#         - SysLogMgt: System Logs Management Function
#     - SysUser: Manage system users, including:
#         - SysUserTbl: System Users Table
#         - SysUserMgt: System Users Management Function
#     - SysMenu: Manage system menus, including:
#         - SysMenuTbl: System Menus Table
#         - SysMenuMgt: System Menus Management Function
#     - SysForm: Manage system forms, including:
#         - SysFormTbl: System Forms Table
#         - SysFormMgt: System Forms Management Function
#     - SysReport: Manage system reports, including:
#         - SysReportTbl: System Reports Table
#         - SysReportMgt: System Reports Management Function
#     - SysFunc: Manage system functions, including:
#         - SysFuncTbl: System Functions Table
#         - SysFuncMgt: System Functions Management Function
#     - SysRemark: Manage system remarks, including:
#         - SysRemarkTbl: System Remarks Table
#         - SysRemarkMgt: System Remarks Management Function
#     - SysDoc: Manage system documents, including:
#         - SysDocTbl: System Documents Table
#         - SysDocMgt: System Documents Management Function
#     - SysSQL: Manage system SQL scripts, including:
#         - SysSQLTbl: System SQL Scripts Table
#         - SysSQLMgt: System SQL Scripts Management Function
#     - SysReport: Manage system reports, including:
#         - SysReportTbl: System Reports Table
#         - SysReportMgt: System Reports Management Function
#     - SysAuto: Manage system automatic tasks, including:
#         - SysAutoTbl: System Automatic Tasks Table
#         - SysAutoMgt: System Automatic Tasks Management Function
#     - SysIntegrate: Manage system internal functions, including:
#         - SysIntegrateTbl: System Internal Functions Table
#         - SysIntegrateMgt: System Internal Functions Management Function

# </PyDev: SysMgt>
import sys

c_strTxtImpPrefix='DH'
c_strSysDBTblPrefix='DH'
c_strTblNameSysTbl = c_strSysDBTblPrefix+'SysTbl'
c_strTblNameSysAttr = c_strSysDBTblPrefix+'SysAttr'

c_strDBName = c_strSysDBTblPrefix+'Py'
c_strCharSetDft='utf8mb4'
c_strCollateDft='utf8mb4_unicode_520_ci'

c_lstSysInitFuncChk=\
    [
        'EHSNMgt.fnSNTblChk'
        , 'EHAttrMgt.fnAttrTblChk'
    ]
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHSysMgt.py !')
# </PyDecl: RunTime>
def fnSysInit()->bool:
    returnEHSysMgt.fnSchemaCreate()

def fnSchemaCreate(
    strSchemaName:str = ''
)->bool:
    if len(strSchemaName)==0:
        import EHDB
        clsEHDB=EHDB.EHDBClass()
        strSchemaName = clsEHDB.p_strDBNameDft
    strSQL='CREATE SCHEMA `<SchemaName>`' +\
        ' DEFAULT CHARACTER SET <CharSet>' + \
        ' COLLATE <Collate>'
    strSQLRun=strSQL
    strSQLRun=strSQLRun.replace('<SchemaName>',strSchemaName)
    strSQLRun=strSQLRun.replace('<CharSet>',c_strCharSetDft)
    strSQLRun=strSQLRun.replace('<Collate>',c_strCollateDft)
    import EHDB
    blnResult=EHDB.fnExecSQL(strSQLRun)
    return False if blnResult is None else True

def fnSysExit():
    sys.exit(0)