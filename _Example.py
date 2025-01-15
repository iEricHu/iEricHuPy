def fnTxtDBImpExecTest()->bool:
    import EHXW
    if not EHXW.p_blnXWMode:
        import EHTxt
        blnResult: bool = EHTxt.fnTxtDBImpPreProc(
            strFilePath=r"D:\\!!Python\\!xlwings\\!DHxlwings XLSM\\wxPython SysAttr.txt"
        )
        print('blnResult: {}'.format(blnResult))
        import EHSysMgt
        EHSysMgt.fnSysExit()

# def fnUIFormCreateShow():
#     import EHUI
#     EHUI.fnUIFormCreateShow()

def SQLToRpt():
    import EHXLRpt
    import EHSysMgt
    # strSQLRun='SELECT UpdateTime FROM dhsysattr'#' LIMIT 1'
    strSQLRun = "SELECT * FROM dhsysattr"
    EHXLRpt.fnRptSQLTbl(
        strShtName = 'test',
        intTitleRow=3,
        strTblName=EHSysMgt.c_strTblNameSysAttr,
        strDBName=EHSysMgt.c_strDBName,
        strSQL =strSQLRun
    )

