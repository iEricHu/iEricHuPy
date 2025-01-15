# EHUDE.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHUDE.py !')
# </PyDecl: RunTime>

from enum import Enum
class udeINIOperType(Enum):
    udeINIOperTypeRead = 'INIRead'
    udeINIOperTypeWrite = 'INIWrite'


class udeDBType(Enum):
    udeDBTypeNA = 'NA'
    udeDBTypeMySQL = 'MySQL'
    udeDBTypeMSSQL = 'MSSQL'
    udeDBTypeAccess = 'Access'
    udeDBTypeOracle = 'Oracle'

class udtCNN:
    strSectName=''
    dictCNN={}
    udeDBType=None
    strDBName=''
    DBNameSection=''
    strServerAddr=''
    strDBFilePath=''
    strCNN=''
    strCNNRun = ''
    lstCNNSecurity=None
    objCNN=None
    objCursor=None

    def __repr__(self):
        return 'strSectName: {}, udeDBType: {}, strCNN: {}, dictCNN: {}, objCNN: {}, objCursor: {}'.format(
            self.strSectName, self.udeDBType, self.strCNN, self.dictCNN, self.objCNN, self.objCursor)