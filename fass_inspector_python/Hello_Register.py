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

def getVmuptime():
    # https://www.quora.com/Whats-the-difference-between-os-system-and-subprocess-call-in-Python
    # using subprocess.check_output() for linux command
    cliInput = 'grep btime /proc/stat'
    args = shlex.split(cliInput)
    # this returns a bytes object, so I need to decode it into a string.
    f = subprocess.check_output(args).decode('utf-8')
    # temp = f.communicate()
    return f.strip().replace('btime ','')

def getCpuType():
    # using os.popen() for linux command
    p = os.popen('grep \'model name\' /proc/cpuinfo | head -1')
    result = p.read()
    temp = re.sub('[\n\t]','', result)
    return temp.replace('model name: ', '')

def stampVM():
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
def profileVM(event, vmbt = '', cpuType = '', myUuid = '', newContainer = ''):
    vmbt = getVmuptime()
    cpuType = getCpuType()
    myUuid, newContainer = stampVM()
        # print('im here! write uuid to the file!')
    # using try catch
    try:
        name = event['name']
        message = 'Hello {} from lambda!'.format(name)  
        return {
                'message' : message,
                'name' : name,
                'CPU' : cpuType,
                'vmuptime' : vmbt,
                'uuid' : myUuid,
                'newcontainer' : newContainer
                }
    except:
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        logger.error('THE INPUT JSON DOESN\'T HAVE SPECIFIED FIELD.')
        return {
                'error': 'please check log and input JSON'
                }