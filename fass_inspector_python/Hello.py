# TCSS 499
# Wen Shu
# Winter 2019

# This is just a Hello world python script for
# AWS Lambda function with JSON as input and 
# output

import logging
import Hello_Register

# my_handler is the lambda function on aws that will be called
# event: is the JSON object or message that passed in
# context: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
# return JSON with customized fields.

def my_handler(event, context):
    vmbt = Hello_Register.getVmuptime()
    cpuType = Hello_Register.getCpuType()
    myUuid, newContainer = Hello_Register.stampVM()
    vmSpec = Hello_Register.profileVM(event, vmbt, cpuType, myUuid, newContainer)
    return vmSpec