#!/usr/bin/env python3
#coding:utf-8
import os
import time
from subprocess import check_output

workpath=(os.getcwd() +'/.acestream/start-engine --client-console') 

def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def get_pid(name):
    return int(check_output(["pidof","-s",name]))

try:
    get_pid('acestreamengine')
except BaseException:
    pass
else:
    a = get_pid('acestreamengine')
try:
    check_pid(a)
except BaseException:
    b = False
else:
    b = check_pid(a)
while 0 < 5:        
    if b == False:
        os.system(workpath)    
    else:
        time.sleep (1)      
        
