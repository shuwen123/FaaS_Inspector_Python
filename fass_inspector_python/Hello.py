# TCSS 499
# Wen Shu
# Winter 2019

# This is just a Hello world python script for
# AWS Lambda function with JSON as input and 
# output

import json
import logging
import os
import subprocess
import re

# my_handler is the lambda function on aws that will be called
# event: is the JSON object or message that passed in
# context: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
# return JSON with customized fields.

def my_handler(event, context):
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

    # using try catch
    try:
        name = event['name']
        message = 'Hello {} from lambda!'.format(name)  
        return {
                'message' : message,
                'name' : name,
                'CPU' : cpuType,
                'vmUpTime' : vmbt 
                }
    except:
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        logger.error('THE INPUT JSON DOESN\'T HAVE SPECIFIED FIELD.')
        return {
                'error': 'please check log and input JSON'
                }