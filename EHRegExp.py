# EHRegExp.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import re

import EHStr
import EHSymbolDef
# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHRegExp.py !')
# </PyDecl: RunTime>
def fnRegExp(
        strRun:str,
        strPattern:str,
        blnCaseSensitive:bool = False,
        blnTestOnly:bool = False,
        blnSplit:bool = False,
        blnMulti:bool = False,
        blnFromStart:bool = False,
        blnReturnList:bool = True,
        blnBracketBalance:bool = False
)->(bool | list | str | None, list | str| None):
    intFlag=0
    #<PyCmt: re.MULTILINE>
    intFlag=intFlag+int(re.MULTILINE) if blnMulti else 0
    # <PyCmt: re.IGNORECASE>
    intFlag = intFlag + int(re.IGNORECASE) if not blnCaseSensitive else 0
    # <PyCmt: re.LOCALE>
    #intFlag = intFlag + int(re.LOCALE) if blnLocaleAware else 0

    if blnTestOnly:
        blnResult= \
            re.search(
                pattern=strPattern,
                string=strRun,
                flags=intFlag
            )
        blnResult=not blnResult is None
        return blnResult, None
    elif blnSplit:
        blnResult= \
            re.split(
                pattern=strPattern, 
                string=strRun 
            )
        blnResult = not blnResult is None
        return blnResult, None
    elif blnMulti:
        lstMatch = []
        lstSpan = []
        if blnBracketBalance:
            strRunNew=strRun
            intPosLast=0
            while len(strRunNew)>0:
                objMatch = re.search(strPattern, strRunNew, intFlag)
                if not objMatch: break
                intPosStart=objMatch.span()[0]
                strResult=EHStr.fnStrBracketBalFind(strRun=strRunNew[intPosStart:])
                lstMatch.append(strResult)
                tupSpan=(intPosLast+intPosStart, intPosLast+intPosStart+len(strResult) )
                lstSpan.append(tupSpan)
                intPosLast=intPosLast+intPosStart+len(strResult)
                strRunNew=strRunNew[intPosStart+len(strResult):]
            if len(lstMatch)>0:
                return lstMatch, lstSpan
            else:
                return None, None
        else:
            objMatch=re.finditer(strPattern, strRun, intFlag)
            for objMatchItem in objMatch:
                lstMatch.append(objMatchItem.group())
                lstSpan.append(objMatchItem.span())
            if len(list(objMatch))>0:
                if blnReturnList:
                    return lstMatch, lstSpan
                else:
                    strMatch=EHSymbolDef.c_strAttrSplitor.join(lstMatch)
                    strSpan = EHSymbolDef.c_strAttrSplitor.join(lstSpan)
                    return strMatch, strSpan
            else:
                return None, None
    else:
        if blnFromStart:
            objMatch=re.match(strPattern, strRun, intFlag)
            if objMatch:
                return objMatch.group(), objMatch.span()
            else:
                return None, None
        else:
            objMatch = re.findall(strPattern,strRun, intFlag)
            if blnReturnList:
                return objMatch, None
            else:
                strMatch=';'.join(objMatch)
                return strMatch, None

def fnREMatch(
        strRun:str,
        strPattern:str
)->bool:
    strPatternRun=strPattern.replace('*','.*?')
    objMatch=re.findall(pattern=strPatternRun, string=strRun )
    return len(objMatch)>0

def fnREReplace(
        strRun:str,
        strPattern:str,
        strNew:str
)->str:
    strPatternRun = strPattern.replace('*', r'.*?')
    strPatternRun = strPatternRun.replace('(', r'\(')
    strPatternRun = strPatternRun.replace(')', r'\)')
    strResult=re.sub(pattern=strPatternRun, repl=strNew, string=strRun)
    return strResult