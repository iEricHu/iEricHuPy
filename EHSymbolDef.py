# EHSymbolDef.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

# <PyCmt: Python>
c_strNewLine:str = '\n'
c_strTab:str = '\t'

# <PyCmt: SQL>
c_strCNNSplitor:str = ';'
c_strCNNDBNameSymbol:str = '\''
c_strSQLSplitor:str = ', '
c_strSQLValueSplitor:str = '='
c_strSQLCommaSplitor:str = ','
c_strSQLSelectColFuncSplitor:str = ','
c_strSQLFromTableNameSplitor:str = ','
c_strSQLDBNameSymbol:str = '`'
c_strSQLValueBracketSymbol:str = '\''
c_strDBNameAppendSymbol:str = '.'
c_strTableNameAppendSymbol:str = '.'
c_strNumericAppendSymbol:str = '.'
c_strSQLSpecialCharEscape:str = r'\\'
c_strSQLBracketLeft:str = '('
c_strSQLBracketRight:str = ')'

# <PyCmt: Attr>
c_strAttrSubNameSplitor:str = '_'
c_strAttrSplitor:str = ';'
c_strAttrSplitorSub1:str = ',,'
c_strAttrSplitorSub2:str = ','
c_strAttrSplitorGeneral:str = ', '
c_strAttrSpecialSplitor:str = '|'
c_strAttrSpecialSplitor2:str = '||'
c_strAttrSplitorSpecial1:str = '<;>'
c_strAttrSplitorSpecial2:str = '<&>'
c_strAttrValueSplitor:str = '::'
c_strValueAppendSymbol:str = '#'
c_strAttrSubValueSplitor:str = '-'
c_strAttrSubValueSplitor2:str = '=>'
c_strVarbBracketLeft:str = '<'
c_strVarbBracketRight:str = '>'
c_strLineSplitor:str = '&;'
c_strLineSubSplitor:str = '^;'

# <PyCmt: ColName>
c_strColNameSplitor:str = ';'
c_strWithSeqColPosSplitor:str = '-'
c_strExcelValueAppend:str = '\''

# <PyCmt: Excel Range>
c_strRangeAddressSplitor:str = ','
c_strRangeAddressSymbol:str = ':'
c_strPropertyValueSplitor:str = '='

# <PyCmt: Forms>
c_strFormLabelValueSymbol:str = ': '

# <PyCmt: DLL>
c_strDLLVerSplitor:str = '-'
c_strDLLVerSubSplitor:str = '.'
c_strGUIDInfoSplitor:str = '.'
c_strVBEDeclarationSplitor:str = ', '
c_strIPAddressSplitor:str = '.'

# <PyCmt: General>
c_strDecimalPoint:str = '.'
c_strFileExtSymbol:str = '.'
c_strFileNewSymbol:str = '_'
c_strFileDateSplitor:str = '-'
c_strPathSymbolLeft:str = '\\'
c_strPathSymbolRight:str = '/'
c_strPathVarSymbol:str = '%'
c_strBracketLeft:str = '('
c_strBracketRight:str = ')'
c_strBracketQuota:str  = '\''
c_strBracketQuotaSng:str = '\''
c_strBracketSingleColl:str = \
    c_strDecimalPoint + \
    c_strFileExtSymbol + \
    c_strBracketQuota + \
    c_strBracketQuotaSng

c_strSpecialSymbolColl:str = "\\!""#$%&'()*+,-./:;<=>?@[]^_`{|}~"

# <PyCmt: Py TxtImp>
c_strTxtImpHeaderSymbPrefix:str = '#'
c_strTxtImpHeaderSplitor:str = ','
c_strTxtImpHeaderSymbValSplitor:str = ':'
c_strTxtImpSymbFilePath:str = '\\'

c_strTxtImpDataSplitor:str = '<;>'
