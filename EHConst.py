class _const:
    class ConstError(TypeError) : pass

    def __setattr__(self, key, value):
       # self.__dict__
        if key in self.__dict__:
            data="Can't rebind const (%s)" % key
            raise self.ConstError(data)
        self.__dict__[key] = value

import sys
sys.modules[__name__] = _const()

#<PyEx>
# import const
# const.c=1
# print(const.c)  # 1
# const.c=2   #const.ConstError: Can't rebind const (c)
#<PyEx>