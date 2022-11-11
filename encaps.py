class Protected:
    def __init__(self):
        self._protectedVar = 21

class Protected:
    def __init__(self):
        self.__privateVar = 21

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj._protectedVar = 0
print(obj._protectedVar)
obj.getPrivate()
obj.setPrivate(39)
obj.getPrivate
