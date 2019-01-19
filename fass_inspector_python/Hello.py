# TCSS 499
# Wen Shu
# Winter 2019

# This is just a Hello world python script for
# AWS Lambda function with JSON as input and 
# output

import logging
<<<<<<< HEAD
import Hello_Register
=======
import os
import subprocess
import re
import uuid
>>>>>>> e36c2fbd140b1511e4a1a106fe713517ee1a5065

# my_handler is the lambda function on aws that will be called
# event: is the JSON object or message that passed in
# context: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
# return JSON with customized fields.

def my_handler(event, context):
<<<<<<< HEAD
    vmbt = Hello_Register.getVmuptime()
    cpuType = Hello_Register.getCpuType()
    myUuid, newContainer = Hello_Register.stampVM()
    vmSpec = Hello_Register.profileVM(event, vmbt, cpuType, myUuid, newContainer)
    return vmSpec
=======
#     # using if else
#     inputKeyset = list(event.keys())
#     if 'name' in inputKeyset:
        # name = event['name']
        # message = 'Hello {} from lambda!'.format(name)  
        # return {
        #         'message' : message,
        #         'name' : name
        #         }
#     else:
        # logger = logging.getLogger()
        # logger.setLevel(logging.ERROR)
        # logger.error('THE INPUT JSON DOESN\'T HAVE SPECIFIED FIELD.')
        # return {
        #         'error': 'please check log'
        #         }
    # using os.popen() for linux command
    f = os.popen('grep \'btime\' /proc/stat')
    temp = f.read().strip()
    vmbt = temp.replace('btime ', '')
    p = os.popen('grep \'model name\' /proc/cpuinfo | head -1')
    result = p.read()
    temp = re.sub('[\n\t]','', result)
    cpuType = temp.replace('model name: ', '')
    myUuid = ''
    newContainer = 0
    if os.path.isfile('/tmp/container-id'):
        stampFile = open('/tmp/container-id', 'r')
        stampID = stampFile.readline()
        myUuid = stampID
        stampFile.close()
        print('im here! read uuid from file!')
        newContainer = 1
    else:
        stampFile = open('/tmp/container-id', 'w')
        myUuid = str(uuid.uuid4()) # uuid4() generates a random uuid
        stampFile.write(myUuid)
        stampFile.close()
        print('im here! write uuid to the file!')
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
>>>>>>> e36c2fbd140b1511e4a1a106fe713517ee1a5065
