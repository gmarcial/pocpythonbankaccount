class Amount(object):

    def __init__(self, value):
        
        if (value < 0):
            raise ValueError("The value is invalid to a bank operation")
        
        self.__value = value
    
    def __add__(self, other):
        newvalue = (self.__value + other.__value)
        return Amount(newvalue)
    
    def __sub__(self, other):
        newvalue = (self.__value - other.__value)
        return Amount(newvalue)

    def __lt__(self, other):
        return (self.__value < other.__value)

    def __gt__(self, other):
        return (self.__value > other.__value)
        
    def __eq__(self, other):
        return (self.__value == other.__value)
    
    def __int__(self):
        return self.__value
    
    def getvalue(self):
        return self.__value