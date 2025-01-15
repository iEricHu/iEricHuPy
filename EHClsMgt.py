# EHClsMgt.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import EHMsg

# <PyDecl: RunTime>
dictCls={}
if c_blnEHDebugMode: print('DebugMode Entry: EHClsMgt.py !')
# </PyDecl: RunTime>

class EHClsMgtClass(object):
    # <PyCmt: Get instanced Class from project>
    _instance = None
    _clsRun = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)#, *args, **kw)
            cls.fnClsGet(self=cls, strMdlName='EHXW', strClsFuncName='EHXWClass')

            # <PyCmt: get variable 'strMdlName'>
            strMdlName=kwargs.get('strMdlName')
            if strMdlName is None: strMdlName = args[0] if len(args)>0 else ''

            # </PyCmt: get variable 'strClsFuncName'>
            strClsFuncName=kwargs.get('strClsFuncName')
            if strClsFuncName is None: strClsFuncName = args[1] if len(args) > 1 else ''

            cls._clsRun = cls.fnClsGet(self=cls, strMdlName=strMdlName, strClsFuncName=strClsFuncName)
        return cls._clsRun

    def __init__(self, strMdlName, strClsFuncName, *args):
        pass

    @staticmethod
    def fnClsGet(self, strMdlName, strClsFuncName, blnCreateNew=True):
        if c_blnEHDebugMode:
            print('fnClsGet(strMdlName: {}, strClsFuncName: {}, blnCreateNew: {})'.\
                  format(strMdlName, strClsFuncName, blnCreateNew))
        strMdlClsName = strMdlName + '.' + strClsFuncName
        if strMdlClsName in dictCls:
            clsRun=dictCls[strMdlClsName]
        elif blnCreateNew:
            mdlRun = __import__(strMdlName)
            clsRun = getattr(mdlRun, strClsFuncName)
            clsRun=clsRun()
            dictCls[strMdlClsName]=clsRun
        else:
            clsRun=None
        return clsRun

def fnClsInfoGet(clsRun)->dict:
    # <PyFunc: Get ClassName and parent, Module Name>
    dictClsInfo={}
    if type(clsRun).__name__=='type':
        #<PyCmt: type, not class>
        dictClsInfo['ModuleName'] = vars(clsRun)['__module__'] #refer to vars
        dictClsInfo['ClassName'] = clsRun.__name__
        strMsg = 'Class not Init, pls check bracket!'
        strFuncName = 'EHClsMgt.fnClsMgtClsInfoGet'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
    else:
        dictClsInfo['ModuleName']=clsRun.__module__ #type(clsRun).__module__
        dictClsInfo['ClassName'] = clsRun.__class__.__name__ #type(clsRun).__name__
    return dictClsInfo

def fnClsInheritedParentName(clsRun)->str:
    # <PyFunc: Get ClassName and parent, Module Name>
    strParentName = clsRun.__bases__[0].__name__
    return strParentName

def EHClsMgtInit(*args):
    # <PyFunc: Init Class via ClassName>
    clsEHClsMgt=EHClsMgtClass(*args)
    return clsEHClsMgt

