from fiResponse import fiResponse

class Response(fiResponse):
    __value = ""
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value
    
    def __str__(self):
        return "value=" + self.getValue() + super().__str__()
