# EHArray.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>
# <PyCmt: List >
# <PyCmt: Dict Func>
# dictTmp={} #dict init
# dict['strKey']=intValue #Add or Assign Value
# 'strKey' in dictTmp # Check if strKey in dictTmp
# 1. Dict Get: dictTmp.items() # item sorted show
# 2. Dict GetValue:
#   dictTmp['strKey'] #Get strKey in dictTmp, if strKey Not Exist, It will cause Error
# 3. Dict GteValue:
#   dictTmp.get(strKey[, strValueDft])
#   #Get strKey in dictTmp, if strKey Not Exist, return strValueDft or None
# 4. dictTmp.pop['strKey'] #delete dictTmp element
# 5. len(dictTmp) #dict length
# </PyCmt: Dict Func>

import numpy as np
import EHMsg
import EHStr
import EHSymbolDef
import EHPyFunc

# <PyDecl: Symbol Define & UDE import >
c_strAttrSplitor = EHSymbolDef.c_strAttrSplitor
c_strAttrValueSplitor = EHSymbolDef.c_strAttrValueSplitor
# </PyDecl: Symbol Define & UDE import >

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHArray.py !')
# </PyDecl: RunTime>
class EHFixElmDict(dict):
    def __init__(self, lstElmKey:list, blnErrShow:bool=True):
        dictRun={}
        lstElmKeyNew=[]
        for strKey in lstElmKey:
            strDataType=''
            if '|' in strKey:
                strDataType=strKey.split('|')[1]
                strKey=strKey.split('|')[0]
            lstElmKeyNew.append(strKey)
            dictRun[strKey]=''
            if len(strDataType)>0:
                if strDataType[0]!='[' and strDataType[-1]!=']':
                    dictRun[strKey+'DataType']=strDataType
                else:
                    if strDataType=='[MySQLColSchema]':
                        import EHDBApply
                        dictRun[strKey+'DataType']=EHDBApply.c_lstMySQLDataType

        super().__init__(dictRun)
        self.__dict__ = dictRun
        self.lstElmKey=lstElmKeyNew
        self.blnErrShow=blnErrShow

    def __setitem__(self, key, value):
        if key in  self.lstElmKey:
            super().__setitem__(key, value)
        elif self.blnErrShow:
            raise ValueError('Key: \'{}\' Not in dict: {}'.format(key, self.__class__.__name__))

# <PyRegion: Array Func>
def fnArrayInit(intLen:int=1)->list:
    if not isinstance(intLen, int): return None
    return [0] * intLen

def fnArryInitSeq(intLen:int=1)->list:
    if not isinstance(intLen, int): return None
    return list(range(intLen))

def fnArrayDimGet(
    lstRun:list,
    intLayer:int=0
)->int:
    if not isinstance(lstRun, (list, tuple)):
        return 0
    else:
        intLayer = intLayer + 1

    if isinstance(lstRun[0], (list, tuple)):
        intLayer = fnArrayDimGet(lstRun=lstRun[0], intLayer=intLayer)

    return intLayer
    # try:
    #     nlstRun=np.array(lstRun)
    #     intListDim = nlstRun.ndim
    # except Exception as Err:
    #     strFuncName='EHArray.fnArrayDimGet'
    #     EHMsg.fnMsgPrt(strMsg=Err, strFuncName=strFuncName)
    #     intListDim=0
    # return intListDim

def fnArrayTranspose(lstRun:list) -> list:
    try:
        nlstRun = np.array(lstRun)
        nlstRun = np.transpose(nlstRun, None)
        lstRun = nlstRun.tolist()
    except Exception as Err:
        lstRun = None
        strErrMsg = 'Error in fnArrayTranspose: {}'.format(Err)
        strFuncName = 'EHArray.fnArrayTranspose'
        EHMsg.fnMsgPrt(strMsg=strErrMsg, strFuncName=strFuncName, blnLog=True)
    return lstRun


def fnArrayZIPTranspose(lstRun:list) -> list:
    return list(zip(*lstRun)) if lstRun else None

def fnArrayCmp(
    lstRun1:list,
    lstRun2:list
) -> list:
    # return list(set(lstRun1) - set(lstRun2))
    return list(set(lstRun1).difference(lstRun2))

def fnArrayNumChk(lstRun:list) -> bool:
    blnResult:bool = False
    for objRun in lstRun:
        if isinstance(objRun, (list, tuple)):
            blnResult = fnArrayNumChk(objRun)
            return blnResult
        else:
            try:
                blnResult=isinstance( int(objRun), int)
            except Exception :
                return False
    return blnResult

def fnArrayLenChk(
    lstRun:list,
    intLenReq:int=0
) -> int:
    if fnArrayDimGet(lstRun) == 1: return len(lstRun)
    intArrayLenMax = 0
    for lstRow in lstRun:
        if intLenReq > 0 and intLenReq > len(lstRow):
            return len(lstRow)
        elif len(lstRow) > intArrayLenMax:
            intArrayLenMax = len(lstRow)
    return intArrayLenMax


def fnArraySort(
    lstRun:list,
    intElmPos:int=0
) -> list:
    if not isinstance(lstRun, list): return lstRun
    # <PyCmt: SortKey could be : (SortKey[intElmPos1], SortKey[intElmPos2]) >
    return sorted(lstRun, key=lambda SortKey: SortKey[intElmPos])

def fnArraySlice(
    lstRun:list,
    intPos:int=0,
    blnTranspose:bool=False
) -> list:
    if lstRun is None: return None

    if isinstance(lstRun, tuple): lstRun = lstRun[0]
    if lstRun is None: return None

    if blnTranspose:
        if len(lstRun) == 1:
            lstRun = lstRun[0]
            lstRun = fnArrayTranspose(lstRun=lstRun)
        else:
            lstRun = fnArrayZIPTranspose(lstRun)
    lstRun = lstRun[intPos:intPos + 1]
    if len(lstRun) >= 1: lstRun = lstRun[0]
    return lstRun

def fnArrayColPosGet(
    lstRun:list,
    strColName:str
) -> int:
    intArrayDim = fnArrayDimGet(lstRun=lstRun)
    if intArrayDim == 1:
        lstRunSub = lstRun
    elif intArrayDim == 2:
        lstRunSub = lstRun[0]
    else:
        return None
    return lstRunSub.index(strColName)

def fnArrayStrColPosGet(
    strRun:str,
    strTarget:str,
    strSplitor:str=EHSymbolDef.c_strAttrSplitor
) -> int:
    strCompare = strSplitor + strRun + strSplitor
    strTarget = strSplitor + strTarget + strSplitor
    if not strTarget in strCompare: return None
    return strRun.split(strSplitor).index(strTarget)

def fnArrayColStrLenMaxGet(
    lstRun:list,
    lstColValueMaxLen:list=None
):
    # <PyFunc: fnArrayColStrLenMaxGet>
        #    Desc: get List Each Row Max Length String
        #    Use By:
        #    Noticed:
        #    Parameter:
        #        lstRun: List to get max length string
        #        lstColValueMaxLen: List to store max length string
        #    Option:
        #        OptPara1:
        #        OptPara2:
        #        OptPara3:
        #    Return:
        #        lstColValueMaxLen:List of max length string for each row in lstRun
        # </PyFunc: fnDBRSTInsert>
    if fnArrayDimGet(lstRun) == 1:
        intListLen = 1
    else:
        intListLen = len(lstRun)
    if lstColValueMaxLen is None:
        lstColValueMaxLen = [0] * intListLen
    elif intListLen>len(lstColValueMaxLen):
        lstColValueMaxLen=lstColValueMaxLen+['']*(len(lstRun)-len(lstColValueMaxLen))
    for intRowRun in range(0, len(lstRun)):
        strMaxLen = max(lstRun[intRowRun], key=len)
        if len(strMaxLen)> lstColValueMaxLen[intRowRun]:
            lstColValueMaxLen[intRowRun] = strMaxLen
    return lstColValueMaxLen

def fnArraySplitorGuess(strRun:str)->str:
    # <PyFunc: fnArraySplitorGuess>
    #    Desc: Guess Splitor in strRun
    #    Use By:
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
    # </PyFunc: fnArraySplitorGuess>
    strChrMax=''
    intChrMax=0
    for strChr in EHSymbolDef.c_strSpecialSymbolColl:
        if strChr in strRun:
            intChrCount = strRun.count(strChr)
            if intChrCount > intChrMax:
                intChrMax = intChrCount
                strChrMax = strChr
    if len(strChrMax) == 0: return None
    return strRun.split(strChrMax)


def fnArrayFilter(
    lstSource:str | list,
    lstFilter:str | list,
    blnInclude=True,
    strSplitor=c_strAttrSplitor
) -> list:
    # <PyFunc: fnArrayFilter>
    #    Desc:
    #    Use By:
    #       lstSource=['AAA', 'BBB', 'CCC', 'FFF']
    #       lstFilter=['AAA','BBB','CCC','DDD','EEE']
    #           lstResult=['AAA', 'BBB', 'CCC'] # blnInclude=True
    #           lstResult=['DDD', 'EEE'] # blnInclude=False
    #    Noticed:
    #    Parameter:
    #        lstSource: List or String to filter
    #        lstFilter: List or String Filter
    #    Option:
    #        blnInclude: True to include, False to exclude
    #        strSplitor: if lstSource or lstFilter is string, use strSplitor to split
    #    Return: lstResult: Filtered List or String
    # </PyFunc: fnArrayFilter>
    if isinstance(lstSource, str): lstSource = lstSource.split(strSplitor)
    if isinstance(lstFilter, str): lstFilter = lstFilter.split(strSplitor)

    lstResult = \
        list(filter(lambda strItem: (strItemstrItem in lstSource) if blnInclude
            else (strItem not in lstSource), lstFilter))
    return lstResult

def fnArrayRand(
        intArrayDim:int = 1,
        intArraySize:int = 0,
        intArrayRowSize:int = 0,
        strCharFix:str = '',
        intCharLen:int = 0,
        blnCharLenFix:bool = True,
        blnWithNumber:bool = True,
        blnWithAlphabetU:bool = False,
        blnWithAlphabetL:bool = False,
        blnWithSymbol = False
) -> list:
    # <PyFunc: fnArrayRand>
    #    Desc: Generate Random List
    #    Use By:
    #    Noticed:
    #    Parameter:
    #    Option:
    #        intArrayDim: Dimension of List, 1 for 1D List, 2 for 2D List
    #        intArraySize: Column Size of List
    #        intArrayRowSize: Row Size of List
    #        strCharFix: Fixed Character in List
    #        intCharLen: Length of Character in List
    #        blnCharLenFix: True to fix length of Character in List, False to random length
    #        blnWithNumber: True to include Number in Character in List
    #        blnWithAlphabetU: True to include Uppercase Alphabet in Character in List
    #        blnWithAlphabetL: True to include Lowercase Alphabet in Character in List
    #        blnWithSymbol: True to include Symbol in Character in List
    #    Return:
    # </PyFunc: fnArrayRand>
    import random
    import EHStr

    #        OptPara2:
    #        OptPara3:
    #    Return:
    # </PyFunc: fnArrayRand>
    import random
    import EHStr

    if intArraySize == 0: intArraySize = random.randint(1, 100)
    if intArrayDim > 1 and intArrayRowSize == 0:
        intArrayRowSize = random.randint(1, 100)
    elif intArrayDim == 1 and intArrayRowSize == 0:
        intArrayRowSize = 1

    lstColl = []
    intArrayRow = 0
    while intArrayRow < intArrayRowSize:
        strChrRun=''
        lstRun = []
        intArrayCol = 0
        while intArrayCol < intArraySize:
            if intCharLen > len(strCharFix):
                if not blnCharLenFix: intCharLen = random.randint(1, 30)
                strChrRun = \
                    EHStr.fnChrRnd(
                        intDigi=intCharLen - len(strCharFix),
                        blnWithNumber=blnWithNumber,
                        blnWithAlphabetU=blnWithAlphabetU,
                        blnWithAlphabetL=blnWithAlphabetL,
                        blnWithSymbol=blnWithSymbol
                    )
            strChr = strCharFix + strChrRun
            lstRun.append(strChr)
            intArrayCol += 1
        if intArrayDim == 1:
            return lstRun
        else:
            lstColl.append(lstRun)
            intArrayRow += 1
    return lstColl

def fnArrayTypeDistinct(
    lstRun:list,
    strSplitor:str = c_strAttrSplitor, 
    strSplitorPos:str = c_strAttrValueSplitor
) -> list:
    # <PyFunc: fnArrayTypeDistinct>
    #    Desc: Split List Element with Digit and Non-Digit, and return distinct Type List
    #    Use By:
    #    Noticed:
    #       digit: digit present[1~n]
    #       non-digit: minus digit present[-1~-n]
    #       Split by Splitor
    #    Parameter:
    #        lstRun: List to get distinct Type List
    #    Option:
    #        strSplitor: Splitor to split List Element
    #    Return: Distinct Type List
    # </PyFunc: fnArrayTypeDistinct>
    if lstRun is None: return None
    if fnArrayDimGet(lstRun=lstRun) == 1: return None

    lstChrLen = []
    lstColType = []
    intCount = 0
    for lstSub in lstRun:
        lstChrFmt = lstSub[0]
        intColPosNumLast = lstSub[1]

        intArrayLen = len(lstChrFmt)
        strElm = ''
        for strRun in lstChrFmt:
            # <PyCmt: Convert All Col Format(Num/Non-Num) to strElm>
            strElm = \
                strElm + (strSplitor if len(strElm) > 0 else '') + \
                ('-' if not strRun.isdigit() else '') + str(len(strRun))
        strElm = strElm + strSplitorPos + str(intColPosNumLast)
        # <PyCmt: Chk if Col Format(Num/Non-Num) Exist in lstChrLen, lstColType>
        if not intArrayLen in lstChrLen:
            lstChrLen.append(intArrayLen)
            lstColType.append(strElm)
        elif not strElm in lstColType:
            lstChrLen.append(intArrayLen)
            lstColType.append(strElm)
        intCount += 1
    return lstColType
# </PyRegion: Array Func>

# <PyRegion: Dict Func>
def fnDictCntntClean(dictRun):
    for strItem in dictRun:
        dictRun[strItem] = ''


def fnDictNoneRpl(dictRun):
    if not isinstance(dictRun, dict): return None
    for strItem in dictRun:
        if dictRun[strItem] is None: dictRun[strItem] = ''


def fnDictNewKeyGet(dictRun, strKey) -> str:
    # <PyCmt: Check if strKey Exist in dictRun, if yes, add a number after strKey>
    strKeyNew = ''
    for strKeyRun in dictRun.keys():
        if strKeyRun == strKey:
            if strKey[-1].isdigit():
                lstNum = EHStr.fnStrNumGet(lstRun=strKey)
                intNum = lstNum[-1]
                strKeyNew = strKey[:len(str(intNum))] + intNum + 1
            else:
                strKeyNew = strKey + '1'
            strKeyNew = \
                fnDictNewKeyGet(dictRun=dictRun, strKey=strKeyNew)
            break
    if len(strKeyNew) == 0: strKeyNew = strKey
    return strKeyNew
