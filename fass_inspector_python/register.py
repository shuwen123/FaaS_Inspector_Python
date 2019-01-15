import Request
import os
import pathlib
import uuid

class register:
    STAMP_SUCCESS = 0
    STAMP_ERROR_READING_EXISTING_UUID = 1
    STAMP_ERROR_WRITING_NEW_UUID = 2
    
    __STAMP_ERR_READING_EXISTING_UUID = "Error reading existing UUID"
    __STAMP_ERR_WRITING_NEW_UUID = "Error writing new UUID"
    __STAMP_ERR_UNKNOWN = "Unknown error obtaining UUID"
    __STAMP_ERR_NONE = ""
    
    __uuid = "unset"     # universal unique identifier for container - uniquely identifies runtime container on Lambda
    __newcontainer = 0       # integer that tracks if this lambda invocation created a new container (0=no, 1=yes)
    __vuptime = 0
    __sError = __STAMP_ERR_NONE
    
    __logger = None
    
    def __init__(self, l):
        self.__logger = l
    
    # Stamps container with UUID - returns false on error
    def StampContainer(self):
        # Stamp container with a UUID
        # https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
        f = pathlib.Path("/tmp/container-id")
        if f.is_file():
            self.__newcontainer = 0
            f1 = open("/tmp/container-id", "r")
            self.__uuid = f1.readline()
            f1.close()
        else:
            self.__newcontainer = 1
            f1 = open("/tmp/container-id", "w")
            self.__uuid = str(uuid.uuid4())
            try:
                f1.write(self.__uuid)
                f1.close()
            except:
                self.__sError = self.STAMP_ERROR_WRITING_NEW_UUID
        
        v2 = self.getVmCpuStat()
        vmuptime = self.getUptime(v2)
        
        if self.__sError:
            pass
            

    class VmCpuStat:
        cpuusr = 0
        cpunice = 0
        cpukrn = 0
        cpuidle = 0
        cpuiowait = 0
        cpuirq = 0
        cpusirq = 0
        cpusteal = 0
        def __init__(self, cpuusr = 0, cpunice = 0, cpukrn = 0, cpuidle = 0, cpuiowait = 0, cpuirq = 0, cpusirq = 0, cpusteal = 0):
            self.cpuusr = cpuusr
            self.cpunice = cpunice
            self.cpukrn = cpukrn
            self.cpuidle = cpuidle
            self.cpuiowait = cpuiowait
            self.cpuirq = cpuirq
            self.cpusirq = cpusirq
            self.cpusteal = cpusteal
    
    def getVmCpuStat(self):
        filename = "/proc/stat"
        f = pathlib.Path(filename)
        if f.is_file():
            fr = open(filename, "r")
            text = fr.readline()
            params = text.split()
            vcs = self.VmCpuStat()
            vcs.cpuusr = int(params[2])
            vcs.cpunice = int(params[3])
            vcs.cpukrn = int(params[4])
            vcs.cpuidle = int(params[5])
            vcs.cpuiowait = int(params[6])
            vcs.cpuirq = int(params[7])
            vcs.cpusirq = int(params[8])
            vcs.cpusteal = int(params[9])
            
            for line in fr:
                if "btime" in line:
                    prms = line.split()
                    vcs.btime = int(prms[1])
            fr.close()
            return vcs
        else:
            return self.VmCpuStat()

    def getUptime(self, vmcpustat):
        return vmcpustat.btime

    def getUuid(self):
        return self.__uuid
    
    def getNewContainer(self):
        return self.__newcontainer

    def getVmUpTime(self):
        return self.__vuptime