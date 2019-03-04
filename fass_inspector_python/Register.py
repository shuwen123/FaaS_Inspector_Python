# TCSS 499
# Wen Shu
# Winter 2019

# This is just library for profiling the VM's
# spec which your program is running on. It
# targets AWS Lambda for now.

import json
import logging
import os
import subprocess
import re
import uuid
import shlex
import time


def __getUpTime():
    # https://www.quora.com/Whats-the-difference-between-os-system-and-subprocess-call-in-Python
    # using subprocess.check_output() for linux command
    cliInput = 'grep btime /proc/stat'
    args = shlex.split(cliInput)
    # this returns a bytes object, so I need to decode it into a string.
    f = subprocess.check_output(args).decode('utf-8')
    # temp = f.communicate()
    return int(f.strip().replace('btime ',''))

def __getVmCpuStat():
    # using os.popen() for linux command
    p = os.popen('grep \'model name\' /proc/cpuinfo | head -1')
    result = p.read()
    temp = re.sub('[\n\t]','', result)
    return temp.replace('model name: ', '')

def __stampContainer():
    myUuid = ''
    newContainer = 1
    if os.path.isfile('/tmp/container-id'):
        stampFile = open('/tmp/container-id', 'r')
        stampID = stampFile.readline()
        myUuid = stampID
        stampFile.close()
        # print('im here! read uuid from file!')
        newContainer = 0
    else:
        stampFile = open('/tmp/container-id', 'w')
        myUuid = str(uuid.uuid4()) # uuid4() generates a random uuid, uuid is not str
        stampFile.write(myUuid)
        stampFile.close()
        # print('im here! write uuid to the file!')
    return myUuid, newContainer

# event: is the JSON object or message that passed in.
# return JSON/Dictionary with customized fields.
def profileVM():
    fwst = time.time()
    vmbt = __getUpTime()
    cpuType = __getVmCpuStat()
    myUuid, newContainer = __stampContainer()
    fwft = time.time()
    return {
                'cpuType' : cpuType,
                'vmuptime' : vmbt,
                'uuid' : myUuid,
                'newcontainer' : newContainer,
                'frameworkRuntime' : (fwft - fwst) * 1000
                }