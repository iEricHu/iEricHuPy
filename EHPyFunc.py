# EHPyFunc.py
# <PyDecl: Module Init, Setup DebugMode>
from enum import Enum
import datetime
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

class udePyDataType(Enum):
    udeDataTypeInt:str=['int', int]
    udeDataTypeFloat:str=['float',float]
    udeDataTypeStr:str=['str', str]
    udeDataTypeBytes:str=['bytes', bytes]
    udeDataTypeByteArray:str=['bytearray', bytearray]
    udeDataTypeList:str=['list',list]
    udeDataTypeTuple:str=['tuple', tuple]
    udeDataTypeSet:str=['set', set]
    udeDataTypeBool:str=['bool', bool]
    udeDataTypeNoneType:str=['none', None]
    udeDataTypeNoneTypeA: str = ['NoneType', None]
    udeDataTypeRange:str=['range', range]
    udeDataTypeSlice:str=['slice', slice]

    udeDataTypeDate: str = ['date', datetime.date]
    udeDataTypeDateTime: str = ['datetime', datetime]
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHPyFunc.py !')
# </PyDecl: RunTime>
def fnBinToDec(intRun):
    return int(intRun, 2)

def fnTypeName(objRun)->str:
    # print('type(objRun).__name__: {}'.format(type(objRun).__name__))
    # print('vars(objRun): {}'.format(vars(objRun)))
    # print('dir(objRun): {}'.format(dir(objRun)))
    # print('getattr(objRun, _inner, )',getattr(objRun, '_inner', 'None'))
    if getattr(objRun, '_inner', None) is not None:
        return type(getattr(objRun, '_inner', None)).__name__
    return type(objRun).__name__

def fnPyDataType(strUserTypeName:str=''):
    # <PyFunc: fnPyDataType>
    #    Desc: Get Python Data, [int;float;str;bytes;bytearray;list;tuple;set;bool;'none';'NoneType';range;slice]
    #    Use By:
            # return lstDataTypeStr, lstDataType
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
    # </PyFunc: fnPyDataType>
    lstDataTypeStr:list=[]
    lstDataType:list=[]
    for udeRun in udePyDataType:
        if len(strUserTypeName)>0 and udeRun.value[0]==strUserTypeName.lower():
            lstDataTypeStr.append(udeRun.value[0])
            lstDataType.append(udeRun.value[1])
        elif len(strUserTypeName)==0:
            lstDataTypeStr.append(udeRun.value[0])
            lstDataType.append(udeRun.value[1])
    return lstDataTypeStr, lstDataType

def fnPyDataTypeSum()->list:
    # <PyCmt: Abandon>

    # </PyCmt: Abandon>
    import builtins
    import types

    # Get all attributes from the builtins module
    all_builtins = dir(builtins)
    print('all_builtins: {}'.format(all_builtins))
    
    # Filter out the ones that are types (by checking if they are instances of type)
    builtin_types = [
        getattr(builtins, name)
        for name in all_builtins
        if isinstance(getattr(builtins, name), type)
    ]
    print('builtin_types: {}'.format(builtin_types))

    basic_data_types = [
        'int', 'float', 'complex', 'str', 'bytes', 'bytearray', 'list', 'tuple', 'set', 'frozenset', 'dict',
        'bool', 'NoneType', 'range', 'slice', 'memoryview', 'types.FunctionType', 'types.BuiltinFunctionType',
        # Note: 'NoneType' is a bit special since it's not directly accessible as a type in code (you use None)
        # and 'types.FunctionType' and 'types.BuiltinFunctionType' are more specific than just 'function'
    ]

    basic_type_objects = []
    for name in basic_data_types:
        if name == "NoneType":
            basic_type_objects.append(type(None))
        elif name.startswith("types."):
            # Strip the 'types.' prefix and get the attribute from the types module
            attr_name = name[len("types.") :]
            basic_type_objects.append(getattr(types, attr_name))
        else:
            basic_type_objects.append(getattr(builtins, name))
    print('basic_type_objects: {}'.format(basic_type_objects))