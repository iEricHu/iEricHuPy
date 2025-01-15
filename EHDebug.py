#EHDebug
c_blnEHDebugMode = False

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHDebug.py !')
# </PyDecl: RunTime>

class EHDebugClass(object):
    _instance=None
    s_blnEHDebugMode=False
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)#, *args, **kw)
            cls.s_blnEHDebugMode = c_blnEHDebugMode
        return cls._instance

    def __init__(self, *args, **kw):
        pass

    @property
    def p_EHDebugMode(self):
        return self.s_blnEHDebugMode
def fnErrRtn(
    *args,
    **kwargs
)->tuple:
    #<PyCmt: fnErrRtn>
    #Return with fixed as below:
        # blnResult:bool=False
        # blnErrRtn:bool=False
        # strErrMsg:str=''
        # strFuncName:str=''
        # blnLog:bool=False
        # others: tupReturn=tuple([blnResult, strErrMsgRun] + lstKWArgRun)
    #</PyCmt: fnErrRtn>

    blnResult:bool=False
    blnErrRtn:bool=False
    strErrMsg:str=''
    strFuncName:str=''
    blnLog:bool=False

    lstKWArgRun=[]
    for strKey,varValue in kwargs.items():
        if strKey=='blnResult':
            blnResult=varValue
        elif strKey=='blnErrRtn':
            blnErrRtn=varValue
        elif strKey=='strErrMsg':
            strErrMsg=varValue
        elif strKey=='strFuncName':
            strFuncName=varValue
        elif strKey=='blnLog':
            blnLog=varValue
        else:
            lstKWArgRun.append(varValue)

    strErrMsgRun:str=''
    if blnResult:
        strErrMsgRun=''
    elif len(strFuncName) > 0:
        strErrMsgRun = ": ".join([strFuncName, strErrMsg])
    tupReturn=tuple([blnResult, strErrMsgRun] + lstKWArgRun)

    import EHMsg
    if blnErrRtn:
        if blnLog: EHMsg.fnLog(strMsg=strErrMsg, strFuncName=strFuncName)
        return tupReturn
    EHMsg.fnMsgPrt(strMsg=strErrMsgRun, strFuncName=strFuncName, blnLog=True)
    return tupReturn
