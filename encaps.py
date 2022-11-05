class Protected:
    def __init__(self):
        self._protectedVar = 21

class Protected:
    def __init__(self):
        self.__privateVar = 9

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

thing = Protected()
thing._protectedVar = 57
print(thing._protectedVar)

obj = Protected()
obj.getPrivate()
obj.setPrivate(39)
obj.getPrivate
