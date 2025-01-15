# EHDate.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import datetime
import EHMsg

c_strDateTimeSecFormat='%Y-%m-%d %H:%M:%S.%f'
c_strDateTimeFormat='%Y-%m-%d %H:%M:%S'
c_strDateTimeFormat2='%m-%d-%Y %H:%M:%S'
c_strDateFormat='%Y-%m-%d'
c_strDateFormat2='%Y%m%d'
c_strTimeSecFormat='%H:%M:%S.%f'
c_strTimeFormat='%H:%M:%S'
c_strTimeFormat2='%H%M%S'

c_dateDateTimeZero='1899-12-30 00:00:00'
c_dateDateZero='1899-12-30'
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHDate.py !')
# </PyDecl: RunTime>
def fnNow(
        blnStr=False,
        strDateFmt=c_strDateTimeFormat
)->datetime :
    dateRun=datetime.datetime.now()
    if blnStr:
        return dateRun.strftime(strDateFmt)
    else:
        return dateRun

def fnDateChk(
    dateRun:str | None=None,
    blnErrRtn:bool = False
)->(bool, str):
    if dateRun is None: dateRun=fnNow()
    blnResult, dateRun= \
        fnStrDateCvt(
            strRun = dateRun,
            blnErrRtn = blnErrRtn
        )
    return blnResult, dateRun

def fnWKNo(varDate):
    print('fnWKNo!')
    dateRun=fnDateChk(varDate)
    return dateRun.strftime('%V')

def fnDateToStr(
        dateRun,
        strDateFmt=c_strDateTimeFormat,
        blnDBDate=False
):
    if dateRun is None:
        dateRun=fnNow()
        strDateFmt = c_strDateTimeSecFormat
    elif not isinstance(dateRun, (datetime.datetime, datetime.date, datetime.time)):
        return None
    elif blnDBDate:
        strDateFmt=c_strDateTimeSecFormat
    return dateRun.strftime(strDateFmt)

def fnStrDateCvt(
        strRun:str,
        blnErrRtn:bool = False
)->(bool, str, str | datetime.datetime ):
    # <PyCmt: strptime: parse time string>
    # <PyCmt: strftime: format time string>
    strErrMsg=''
    if isinstance(strRun, (datetime.datetime, datetime.date, datetime.time)):
        return True, strErrMsg, strRun

    if strRun is None or len(strRun)==0:
        strFuncName = "EHDate.fnStrDateCvt"
        strErrMsg = "Str(\'{0}\') Convert to Date Error!".format(strRun)
        if not blnErrRtn:
            EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
        return False, strErrMsg, None

    strFmt=''
    if '.' in strRun:
        if '-' in strRun or '/' in strRun:
            strFmt = c_strDateTimeSecFormat
        else:
            strFmt = c_strTimeSecFormat
    elif ':' in strRun:
        if '-' in strRun or '/' in strRun:
            strFmt = c_strDateTimeFormat
        else:
            strFmt = c_strDateTimeSecFormat
    elif '-' in strRun or '/' in strRun:
        strFmt = c_strDateFormat
    elif len(strRun)==8 and strRun.isnumeric():
        strFmt = c_strDateFormat2
    elif len(strRun) == 6 and strRun.isnumeric():
        strFmt = c_strTimeFormat2

    try:
        dateRun=datetime.datetime.strptime(strRun, strFmt)
        return True, strErrMsg, dateRun
    except ValueError:
        strFmt = c_strDateFormat2
        try:
            dateRun = datetime.datetime.strptime(strRun, strFmt)
            return True, strErrMsg, dateRun
        except ValueError:
            strFuncName='EHDate.fnStrDateCvt'
            strErrMsg='Str(\'{0}\') Convert to Date Error!'.format(strRun)
            if not blnErrRtn:
                EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
            return False, strErrMsg, None

def fnDayWKNoGet(
        strDate:str='',
        blnWK=False,
        intChrLen=0
)->str:
    print('fnDayWKNoGet!')
    if len(strDate)==0 : strDate=EHDate.fnNow(blnStr=True)
    dateRun:datetime = EHDate.fnDateChk(dateRun=strDate)
    if not blnWK:
        strDay:str=str(dateRun.day)
        # strDay=str(0*(intChrLen
        strDay='0'*(intChrLen-len(strDay))+strDay
        return strDay
    else:
        strWK=dateRun.isocalendar()[1]
        return strWK
