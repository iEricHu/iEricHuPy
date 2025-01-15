import sys
import EHMsg

dictMdlLoaded:dict={}

def fnMdlFuncCall(strMdlFuncName:str, *args):
    # <PyCmt: Call Module Function>
    if len(strMdlFuncName) == 0:
        return
    elif '.' in strMdlFuncName:
        import importlib
        strMdlName, strFuncName = strMdlFuncName.split('.')

        objMdl = dictMdlLoaded.get(strMdlName)
        if objMdl is None:
            objMdl = importlib.import_module(strMdlName)
            dictMdlLoaded[strMdlName] = objMdl
        if objMdl is None:
            EHMsg.fnDlgOpt(f'Module {strMdlName} not found.')
        else:
            objFunc = getattr(objMdl, strFuncName)
            objFunc(*args)
    else:
        EHMsg.fnDlgOpt(f"Invalid function name: {strMdlFuncName}")

def fnFuncInfo()->dict:
    # <PyCmt: Get Running Func Info>
    import inspect
    objCallerFrame:object=inspect.currentframe().f_back
    if objCallerFrame is None: return None

    dictFuncInf = {
        "Function Name": objCallerFrame.f_code.co_name,
        "File Name": objCallerFrame.f_code.co_filename,
        "Line Number": objCallerFrame.f_lineno,
        "Local Variables": objCallerFrame.f_locals,
        "Global Variables": objCallerFrame.f_globals,
        "Arguments Count": objCallerFrame.f_code.co_argcount,
        "Variable Names": objCallerFrame.f_code.co_varnames
    }
    return dictFuncInf

def fnMdlCallByPath(strPath:str)->object:
    # <PyCmt: Load Module by Module File Path>

    # <PyCmt: strPath Example>
    # strPath10311="D:\\!!Python\\!xlwings\\!DHxlwings XLSM\\Tmp\\test10311.py"
    if len(strPath)==0: return None

    import EHFile
    strPath=EHFile.fnFileExist(strFileName=strPath)
    if len(strPath)==0: return None

    strMdlName=EHFile.fnFileNameOnly(strFilePath = strPath)

    import importlib.util
    specMdlLoad= importlib.util.spec_from_file_location(strMdlName, strPath)

    mdlLoad = importlib.util.module_from_spec(specMdlLoad)
    specMdlLoad.loader.exec_module(mdlLoad)
    return mdlLoad

def fnMdlLoad(strMdlName:str)->object:
    # from PyQt6 import QtWidgets
    # import EHPyMdl
    # mdlRun = EHPyMdl.fnMdlLoad(strMdlName="PyQt6.QtWidgets")
    # print(EHPyMdl.fnMdlClsNameGet(mdlRun))

    import importlib
    return importlib.import_module(strMdlName)

def fnObjInfoGet(objRun:object):
    if hasattr(objRun, "__module__"):
        print("objRun.__module__: {}".format(objRun.__module__))

    if hasattr(objRun, "__class__"):
        print("objRun.__class__.__name__: {}".format(objRun.__class__.__name__))

    print("type(objRun): {}".format(list(type(objRun))))

def fnMdlClsNameGet(mdlRun:object)->list:
    # <PyCmt: Get All Class Name of Module>
    import inspect
    lstMembers = inspect.getmembers(mdlRun, inspect.isclass)
    lstClassName = [Member[0] for Member in lstMembers]
    return lstClassName

def fnMdlEnumClsGet(mdlRun:object, strClsName:str)->list:
    clsRun = getattr(mdlRun, strClsName)
    lstResult=[member.name for member in clsRun]
    return lstResult

def fnMdlEnumClsValueGet(mdlRun:object, strClsName:str)->list:
    clsRun = getattr(mdlRun, strClsName)
    lstResult=[member.value for member in clsRun]
    return lstResult

def fnFilePathMEReturn()->str:
    # <PyCmt: return __file__, regular file path,
    #   ex: D:\!!Python\!xlwings\!DHxlwings XLSM\TmpTest.py>
    return __file__
def fnMdlMEReturn()->object:
    # <PyCmt: Return Current Module Object>
    import sys
    return sys.modules[__name__]

def fnCallerInfo()->dict:
    # <PyCmt: Show out Called Function>
    # inspect.stack()[0]: inspect.stack()
    # inspect.stack()[1]: Last Called Function
    # inspect.stack()[2]: Last 2 Called Function
    # ......
    import inspect
    frmCurr= inspect.stack()[4]
    dictCallInfo= {
        "Function Name": frmCurr.function,
        "File Name": frmCurr.filename,
        "Line Number": frmCurr.lineno
    }
    return dictCallInfo