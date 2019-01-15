class fiResponse:
    __uuid = ""
    __error = ""
    vmuptime = 0
    newcontiner = 0

    def getUuid(self):
        return self.__uuid
    
    def setUuid(self, uuid):
        self.__uuid = uuid

    def getError(self):
        return self.__error
    
    def setError(self, err):
        self.__error = err

    def getVmuptime(self):
        return self.vmuptime

    def setVmuptime(self, vmuptime):
        self.vmuptime = vmuptime
    
    def getNewcontainer(self):
        return self.newcontiner

    def setNewcontainer(self, newcontiner):
        self.newcontiner = newcontiner
    
    def __str__(self):
        return "\nuuid=" + self.getUuid() + "\nvmuptime=" + self.getVmuptime()


    
    