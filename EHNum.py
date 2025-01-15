import decimal
import datetime
import time

import pandas as pd
import EHArray
import EHDBApply

def fnNumSchema(
    tupData:tuple,
    lstColName:list
)->list:
    strDataTypeInt = EHDBApply.c_strMySQLDataTypeInt
    strDataTypeFloat = EHDBApply.c_strMySQLDataTypeFloat
    strDataTypeDbl = EHDBApply.c_strMySQLDataTypeDbl
    strDataTypeDecimal = EHDBApply.c_strMySQLDataTypeDecimal
    strDataTypeBool = EHDBApply.c_strMySQLDataTypeBool
    strDataTypeVarChar = EHDBApply.c_strMySQLDataTypeVarChar
    strDataTypeDateTime = EHDBApply.c_strMySQLDataTypeDateTime
    strDataTypeDate = EHDBApply.c_strMySQLDataTypeDate
    strDataTypeTime = EHDBApply.c_strMySQLDataTypeTime
    strDataTypeBin = EHDBApply.c_strMySQLDataTypeBin
    strDataTypeBLOB = EHDBApply.c_strMySQLDataTypeBLOB

    # <PyCmt: Array Initialization>
    lstColDataType=EHArray.fnArrayInit(intLen=len(tupData[0]))
    lstColDataLen = EHArray.fnArrayInit(intLen=len(tupData[0]))

    dfRun=pd.DataFrame(tupData, columns=lstColName)
    intColRun=0
    while intColRun<len(dfRun.columns):
        strDataType=''
        dfColData=dfRun.iloc[:, intColRun]
        pdDataType=pd.api.types.infer_dtype(dfColData)
        if pdDataType == 'string':
            strDataType=strDataTypeVarChar
        elif pdDataType == 'bytes':
            strDataType = strDataTypeBLOB
        elif pdDataType == 'floating':
            strDataType = strDataTypeFloat
        elif pdDataType == 'integer':
            strDataType = strDataTypeInt
        elif pdDataType == 'mixed-integer':
            strDataType = strDataTypeVarChar
        elif pdDataType == 'mixed-integer-float':
            strDataType = strDataTypeFloat
        elif pdDataType == 'decimal':
            strDataType = strDataTypeDecimal
        elif pdDataType == 'complex':
            strDataType = strDataTypeVarChar
        elif pdDataType == 'categorical':
            strDataType = strDataTypeVarChar
        elif pdDataType == 'boolean':
            strDataType = strDataTypeBool
        elif pdDataType == 'datetime64':
            strDataType = strDataTypeDateTime
        elif pdDataType == 'datetime':
            strDataType = strDataTypeDateTime
        elif pdDataType == 'date':
            strDataType = strDataTypeDate
        elif pdDataType == 'timedelta64':
            strDataType = strDataTypeTime
        elif pdDataType == 'timedelta':
            strDataType = strDataTypeTime
        elif pdDataType == 'time':
            strDataType = strDataTypeTime
        elif pdDataType == 'period':
            strDataType = strDataTypeVarChar
        elif pdDataType == 'mixed':
            strDataType = strDataTypeVarChar
        elif pdDataType == 'unknown-array':
            strDataType = ''
        elif pdDataType == 'empty':
            strDataType = ''

        strDataLen=''
        if not strDataType in [strDataTypeInt, strDataTypeFloat, strDataTypeDbl, strDataTypeBool,
           strDataTypeDateTime,strDataTypeDate, strDataTypeTime, strDataTypeBin, strDataTypeBLOB]:
            strDataLen = max(dfColData.astype(str).apply(len))
            strDataLen=''.join(['(', str(strDataLen), ')'])

        if len(strDataType) == 0:
            strDataLen = 1
            strDataLen = ''.join(['(', str(strDataLen), ')'])
            strDataType = strDataTypeVarChar

        lstColDataType[intColRun]=strDataType
        lstColDataLen[intColRun]=strDataLen
        intColRun+=1
    return list(zip(lstColDataType, lstColDataLen))

def fnIsNum(var):
    try:
        return isinstance(float(var), (int, float))
    except ValueError:
        return False