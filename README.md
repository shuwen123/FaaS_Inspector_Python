﻿# Faas Inspector Python VersionThis is a python version of the Faas Inspector framework to profile the cloud infrastructure which your code is running on, the example here will target AWS Lambda.### Getting StartedFirst of all, download the project as zip file or clone it from Git. Then put the Register.py file into the same folder of your other python script for AWS Lambda.### Import the Module```import Register```### AWS IO Example#### Input JSON```{	"Name": "Fred Smith"}```#### Getting the JSON```vmSpec = Register.profileVM()```#### Output JSON```{  "cpuType": "Intel(R) Xeon(R) Processor @ 2.50GHz",  "vmuptime": 1551727835,  "uuid": "d241c618-78d8-48e2-9736-997dc1a931d4",  "newcontainer": 1,  "frameworkRuntime": 38.942128,  "name": "Fred Smith",  "message": "Hello Fred Smith from Node JS Lambda!",  "lambdaRuntime": 39.340805}```| **Field** | **Description** || --------- | --------------- || cpuType | The CPU of the machine which your code is running on|| vmuptime | This is the time at which the system booted, in seconds since the Unix epoch (January 1, 1970)|| uuid | The unique ID we gave to the container/firecracker|| newcontainer | 1 for new container/firecracker; otherwise, 0|| frameworkRuntime | The runtime/overhead of the framework|Other Version* [Java](https://github.com/wlloyduw/faas_inspector) - The Java version of Faas Inspector* [Node JS](https://github.com/shuwen123/Faas_Inspector_NodeJS) - The Node JS version of Faas Inspector