# EHXW.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import xlwings as xw
import EHSymbolDef

# <PyDecl: Symbol Define & UDE import >
c_strNewLine = EHSymbolDef.c_strNewLine # '\n'
# </PyDecl: Symbol Define & UDE import >

# <PyDecl: RunTime>
p_blnXWMode:bool=False
objXWApp:xw.App=None
if c_blnEHDebugMode: print('DebugMode Entry: EHXW.py !')
# </PyDecl: RunTime>
class EHXWClass(object):
    _clsEHXW=None
    def __new__(cls, *args, **kwargs):
        if cls._clsEHXW is None:
            cls._clsEHXW = object.__new__(cls) #, *args, **kw)
            cls.s_objApp=None
            cls.s_winAct = None
            cls.s_wbXWWB = None
            cls.s_strXWWBFilePath:str = ''
            cls.s_shtAct=None
            cls.s_objSel=None
            cls.fnCallerAssign(cls)
        return cls._clsEHXW

    def __init__(self):
        global objXWApp
        if objXWApp is None:
            objXWApp=fnXWXLIso()
            if not objXWApp is None:
                self.s_objApp:xw.App=objXWApp
                self.s_wbXWWB:xw.Book = objXWApp.books.active
                self.s_shtAct:xw.Sheet=objXWApp.books.active.sheets.active
                self.s_strXWWBFilePath:str=''
        else:
            self.s_strXWWBFilePath:str=getattr(self.s_wbXWWB, 'fullname')
            self.s_winAct:xw.Window = self.s_objApp.api.ActiveWindow
            self.s_objSel:xw.Range = self.s_objApp.selection
        objXWApp.visible = True

    @property
    def p_objApp(self):
        return self.s_objApp

    @p_objApp.setter
    def p_objApp(self, objAppNew):
        self.s_objApp=objAppNew

    @property
    def p_winAct(self):
        return self.s_winAct

    @property
    def p_wbXWWB(self)->xw.main.Book:
        return self.s_wbXWWB
    @p_wbXWWB.setter
    def p_wbXWWB(self, wbXWWBNew)->xw.main.Book:
        self.s_wbXWWB=wbXWWBNew

    @property
    def p_strXWWBFilePath(self)->str:
        return self.s_strXWWBFilePath

    @property
    def p_shtAct(self)->xw.Sheet:
        return self.s_shtAct

    @property
    def p_objSel(self)->xw.Range:
        return self.s_objSel

    @staticmethod
    def p_blnXWMode()->bool:
        return p_blnXWMode

    def fnCallerAssign(self)->bool:
        if c_blnEHDebugMode: print('clsEHXW.fnCallerAssign')
        global p_blnXWMode
        global objXWApp
        try:
            self.s_wbXWWB = xw.Book.caller()
            self.s_strXWWBFilePath = getattr(self.s_wbXWWB, 'fullname')
            self.s_objApp = self.s_wbXWWB.app
            objXWApp=self.s_objApp
            self.s_winAct = self.s_objApp.api.ActiveWindow
            self.s_shtAct = self.s_wbXWWB.sheets.active
            self.s_objSel = self.s_objApp.selection
            p_blnXWMode=True
            return True
        except Exception as Err:
            strMsg = 'Main Call, p_blnXWMode: {}, '.format(p_blnXWMode) + \
                     c_strNewLine + 'Err: {}'.format(Err)
            print(strMsg)
            return False

def fnXWXLIso() -> xw.App :
    if c_blnEHDebugMode: print('fnXWXLIso!')
    return xw.App(visible=True, add_book = True)
def fnClsEHXWInit()->EHXWClass:
   return EHXWClass()