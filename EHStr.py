# EHStr.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import re

import EHSymbolDef
import EHMsg

import EHRegExp

# <PyDecl: Symbol Define & UDE import >
c_strNewLine = EHSymbolDef.c_strNewLine #'\n'
c_strAttrSplitor=EHSymbolDef.c_strAttrSplitor # ';'
c_strSQLBracketLeft=EHSymbolDef.c_strSQLBracketLeft # '('
c_strSQLBracketRight=EHSymbolDef.c_strSQLBracketRight # ')'
c_strSQLSpecialCharEscape=EHSymbolDef.c_strSQLSpecialCharEscape # r'\\'
# </PyDecl: Symbol Define & UDE import >
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHStr.py !')
# </PyDecl: RunTime>
def fnChrOrdCvrt(strRun)->str:
    strResult=''
    for chrRun in strRun:
        strResult=strResult+str(ord(chrRun))
    return int(strResult)
def fnStrRegExpKeywordSplit(
        strRun,
        strKeywordColl,
        blnDropSplitor=False,
        strSplitor=c_strAttrSplitor
)->list:
    #<PyFunc>
    #Desc: Split strRun by indicated strKeywordColl,
    #   strKeywordColl could be Multiple Indicated with strSplitor
    #Use By:
    #Noticed:
    #Parameter:
    #Option:
    #Optional Return:
    #Return:
    #</PyFunc>

    if strSplitor==strKeywordColl: strSplitor=c_strAttrSplitor
    if strKeywordColl in EHSymbolDef.c_strSpecialSymbolColl:
        strKeywordColl = c_strSQLSpecialCharEscape & strKeywordColl
    strPattern=strKeywordColl
    strPattern = r'.*?\(' + strPattern + r'\)'

    strPatternSub = strKeywordColl
    strPatternSub = strPatternSub.replace(strSplitor, '|')
    strPatternSub = r'\(' + strPatternSub + r'\)'

    lstRegExpMatch, lstRegExpSpan= \
        EHRegExp.fnRegExp(
            strRun=strRun,
            strPattern=strPattern,
            blnMulti=True
        )
    if blnDropSplitor:
        intRun=0
        for strResult in lstRegExpMatch:
            objMatch=re.search(strPatternSub,strResult,re.IGNORECASE)
            if objMatch:
                lstRegExpMatch[intRun]= lstRegExpMatch[intRun].Replace(objMatch.group(), "").strip()
            intRun=+1
    return lstRegExpMatch

def fnStrBracketBalJudge(
        strRun:str,
        strBracketLeft:str = c_strSQLBracketLeft,
        strBracketRight:str = c_strSQLBracketRight
)->(bool, str):
    # <PyFunc: fnStrBracketBalJudge>
    #    Desc: Judge strRun is balanced by strBracketLeft and strBracketRight
    #    Use By:
    #    Noticed:
    #    Parameter:
    #    Option:
    #    Return:
    # </PyFunc: fnStrBracketBalJudge>
    if strBracketLeft in EHSymbolDef.c_strBracketSingleColl:
        if strBracketRight!=strBracketLeft: strBracketRight=strBracketLeft

    blnSymbSng = False
    if len(strBracketRight)==0 or strBracketRight==strBracketLeft:
        strBracketRight=strBracketLeft
        blnSymbSng=True

    if not strBracketLeft in strRun:
        strFuncName = 'EHStr.fnStrBracketBalJudge'
        strMsg = 'Bracket Symbol Error!'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return False, blnSymbSng
    elif len(strRun.split(strBracketLeft))==len(strRun.split(strBracketRight)):
        return True, blnSymbSng
    elif blnSymbSng and len(strRun.split(strBracketLeft))%2==0:
        return True, blnSymbSng
    else:
        return False, blnSymbSng

def fnStrBracketBalFind(
        strRun:str,
        strBracketLeft:str = c_strSQLBracketLeft,
        strBracketRight:str = c_strSQLBracketRight
)->str:
    # <PyFunc: fnStrBracketBalFind>
    #    Desc: Find strRun's balanced bracket strBracketLeft and strBracketRight
    #    Use By:
    #    Noticed:
    #    Parameter:
    #        strRun: the string need to find bracket
    #    Option:
    #        strBracketLeft: Bracket Left Symbol
    #        strBracketRight: Bracket Right Symbol
    #    Return: Bracket Symbol Balanced String
    # </PyFunc: fnStrBracketBalFind>
    blnResult, blnSymbSng = \
        fnStrBracketBalJudge(
            strRun=strRun,
            strBracketLeft=strBracketLeft,
            strBracketRight=strBracketRight
        )
    if not blnResult: return False, ''

    lngPosLast=-1
    strRunNew=''
    while \
        len(strRunNew.split(strBracketLeft))!=len(strRunNew.split(strBracketRight)) or \
        (blnSymbSng and len(strRunNew.split(strBracketLeft))%2==1) or \
        len(strRunNew)==0:

        if blnSymbSng and lngPosLast==-1: lngPosLast=strRunNew.find(strBracketLeft)
        lngSplitorRightPos=strRun.find(strBracketRight, lngPosLast+1)
        if lngSplitorRightPos==-1:
            strMsg = 'Splitor LEFT/RIGHT not balance!' \
                + c_strNewLine + 'strRun: {}'.format(strRun)
            strFuncName = 'EHStr.fnStrBracketBalFind'
            EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
            return False, ''
        strRunNew=strRunNew+strRun[lngPosLast+1:lngSplitorRightPos+1]
        lngPosLast=lngSplitorRightPos
    return True, strRunNew

def fnStrBracketSplit(
    strRun:str,
    strBracketLeft:str = c_strSQLBracketLeft,
    strBracketRight:str = c_strSQLBracketRight,
    strSplitor:str = c_strAttrSplitor
)->list:
    # <PyFunc: fnStrBracketSplit>
    #    Desc: Find SubString in balanced bracket, and split by strSplitor into List
    #    Use By:
    #    Noticed:
    #    Parameter:
    #        strRun: Processing String
    #        Para2:
    #        Para3:
    #    Option:
    #        strBracketLeft: Bracket Left Symbol
    #        strBracketRight: Bracket Right Symbol
    #        strSplitor: Split Symbol
    #    Return: Including in Bracket SubString List
    # </PyFunc: fnStrBracketSplit>
    if strBracketLeft in EHSymbolDef.c_strBracketSingleColl:
        if strBracketRight!=strBracketLeft: strBracketRight=strBracketLeft

    blnSymbSng = False
    if len(strBracketRight)==0 or strBracketRight==strBracketLeft:
        strBracketRight=strBracketLeft
        blnSymbSng=True

    if not strBracketLeft in strRun:
        strMsg = 'Bracket Symbol Error!' \
            + c_strNewLine + 'strRun: {}'.format(strRun)
        strFuncName = 'EHStr.fnStrBracketSplit'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return None, blnSymbSng

    strSplitor=strSplitor.strip()
    if not strSplitor in strRun:
        strMsg = 'Splitor Symbol Error!' \
            + c_strNewLine + 'strRun: {}'.format(strRun)
        strFuncName = 'EHStr.fnStrBracketSplit'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return None, blnSymbSng

    if len(strRun.split(strBracketLeft))!=len(strRun.split(strBracketLeft)) or \
        (blnSymbSng and len(strRun.split(strBracketLeft))%2==1):
        strMsg = 'strRun Bracket LEFT/RIGHT not balance!' \
            + c_strNewLine + 'strRun: {}'.format(strRun) \
            + c_strNewLine + objErr
        strFuncName = 'EHStr.fnStrBracketSplit'
        EHMsg.fnMsgPrt(strMsg=strMsg, strFuncName=strFuncName, blnLog=True)
        return None, blnSymbSng

    strRunSub = \
        fnStrBracketBalFind(
            strRun=strRun,
            strBracketLeft=strBracketLeft,
            strBracketRight=strBracketRight
        )
    intBracketPosLeft=strRunSub.index(strBracketLeft)
    strRunSub=strRunSub[intBracketPosLeft+1:intBrackPosRight]

    intPosSplitor=-1
    intPosSplitorLast=0
    lstBracketSplit=[]
    while intPosSplitor < len(strRunSub):
        intPosSplitor = strRunSub[intPosSplitorLast:].find(strSplitor)
        if intPosSplitor==-1: intPosSplitor=len(strRunSub)
        strRunSubNew=strRunSub[intPosSplitorLast:][:intPosSplitor]
        if len(strRunSubNew.split(strBracketLeft))!=len(strRunSubNew.split(strBracketRight)):
            strRunSubNew=\
                fnStrBracketBalFind(
                    strRun=strRunSubNew,
                    strBracketLeft=strBracketLeft,
                    strBracketRight=strBracketRight,
                )
            intPosSplitor=len(strRunSubNew)+1
        lstBracketSplit.append(strRunSubNew)
        intPosSplitorLast = intPosSplitorLast+intPosSplitor+1
    return lstBracketSplit

def fnChrASCLstGet(
        blnWithNumber=True,
        blnWithAlphabetU=True,
        blnWithAlphabetL=True,
        blnWithSymbol=True
):
    # <PyFunc: fnChrASCLstGet>
    #    Desc: Get ASC Char List by Section['S':Symbol; 'N':Number; 'U':Uppercase; 'L': Lowercase]
    #    Use By:
    #    Noticed:
    #    Parameter:
    #    Option:
    #        blnWithNumber: Include Number Section
    #        blnWithAlphabetU: Include Uppercase Section
    #        blnWithAlphabetL: Include Lowercase Section
    #        blnWithSymbol: Include Symbol Section
    #    Return: List of ASC Char
    # </PyFunc: fnChrASCLstGet>
    c_lstASCSectSymb1 = ['S',32,47]
    c_lstASCSectNum = ['N',48,57]
    c_lstASCSectSymb2 = ['S',58, 64]
    c_lstASCSectAphbU = ['U',65, 90]
    c_lstASCSectSymb3 = ['S',91, 96]
    c_lstASCSectAphbL = ['L',97, 122]
    c_lstASCSectSymb4 = ['S',123, 126]
    c_lstASCRngColl= [
        c_lstASCSectSymb1,
        c_lstASCSectNum,
        c_lstASCSectSymb2,
        c_lstASCSectAphbU,
        c_lstASCSectSymb3,
        c_lstASCSectAphbL,
        c_lstASCSectSymb4
    ]
    lstASCScp=[]
    for lstRng in c_lstASCRngColl:
        lstChrScp=[]
        if blnWithNumber and lstRng[0]=='N' :
            lstChrScp = [chr(intChr) for intChr in range(lstRng[1], lstRng[-1])]
        elif blnWithAlphabetU and lstRng[0]=='U' :
            lstChrScp = [chr(intChr) for intChr in range(lstRng[1], lstRng[-1])]
        elif blnWithAlphabetL and lstRng[0]=='L' :
            lstChrScp = [chr(intChr) for intChr in range(lstRng[1], lstRng[-1])]
        elif blnWithSymbol and lstRng[0]=='S' :
            lstChrScp = [chr(intChr) for intChr in range(lstRng[1], lstRng[-1])]
        lstASCScp = lstASCScp + lstChrScp
    return lstASCScp

def fnChrRnd(
        intDigi=1,
        blnWithNumber=True,
        blnWithAlphabetU=True,
        blnWithAlphabetL=True,
        blnWithSymbol=True
)->str:
    # <PyFunc: fnChrRnd>
    #    Desc: Get Random Char by Section['S':Symbol; 'N':Number; 'U':Uppercase; 'L': Lowercase]
    #    Use By:
    #    Noticed:
    #    Parameter:
    #    Option:
    #        intDigi: Random Char Count
    #        blnWithNumber: Include Number Section
    #        blnWithAlphabetU: Include Uppercase Section
    #        blnWithAlphabetL: Include Lowercase Section
    #        blnWithSymbol: Include Symbol Section
    #    Return: str of Random Char
    # </PyFunc: fnChrRnd>
    import random

    lstASCChr = \
        fnChrASCLstGet(
            blnWithNumber=blnWithNumber,
            blnWithAlphabetU=blnWithAlphabetU,
            blnWithAlphabetL=blnWithAlphabetL,
            blnWithSymbol=blnWithSymbol
        )
    intChrDigiRun=0
    strChrColl=''
    while intChrDigiRun<intDigi:
        chrRun = lstASCChr[int(random.random() * len(lstASCChr))-1]
        strChrColl = strChrColl + chrRun
        intChrDigiRun+=1
    return strChrColl

def fnStrNumGet(
    lstRun:list | str,
    strNotSplit:str = ''
)->list:
    # <PyFunc: fnStrNumGet>
    #    Desc: Split List Value to Digit and Non-Digit by List Column
    #       Digit Char key in one Column, Non-Digit Char key in another Column
    #       Non-Digit Char will be converted to 'X'
    #    Use By:
    #    Noticed:
    #    Parameter:
    #        lstRun: List or String to be split
    #    Option:
    #        strNotSplit: Char to be keep in Digit Column, Like '.'
    #    Return:
    # </PyFunc: fnStrNumGet>
    if lstRun is None: return None
    if isinstance(lstRun, str): lstRun=[lstRun]

    lstRtn=[]
    for strRun in  lstRun:
        strSect = ''
        strNonNum=''
        lstNum = []
        intColCount=0
        intColPosNumLast=0
        for chrRun in strRun:
            if chrRun.isdigit():
                strSect = strSect + chrRun
                if len(strNonNum)>0:
                    lstNum.append(strNonNum)
                    intColCount=intColCount+1
                    strNonNum=''
            elif chrRun in strNotSplit :
                strSect = strSect + chrRun
                if len(strNonNum)>0:
                    lstNum.append(strNonNum)
                    intColCount=intColCount+1
                    strNonNum=''
            else:
                # <PyCmt: Convert Non-Numeric Char into 'X'>
                strNonNum=strNonNum+'X'
                if len(strSect)>0:
                    lstNum.append(strSect)
                    intColPosNumLast=intColCount
                    intColCount=intColCount+1
                strSect=''
        if len(strSect)>0:
            lstNum.append(strSect)
            strSect=''
            if strSect.isdigit(): intColPosNumLast=intColCount
        if len(strNonNum)>0: lstNum.append(strNonNum)
        lstRtn.append([lstNum, intColPosNumLast])
    return lstRtn
