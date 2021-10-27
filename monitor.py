# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import sys
import os
import time
import win32com.client
import win32api
from common import *

process_battle_exe='Battle.net.exe'
process_stone_exe='Hearthstone.exe'

#检测进程
def check_process(process_name):
    WMI=win32com.client.GetObject('winmgmts:')
    processCodeCov=WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov)>0:
        print(True)
        return True
    else:
        print(False)
        return False

#启动进程
def start_process():
    os.system('"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe"')

#结束进程
def end_process(process_name):
    os.system('%s%s' % ("C:\windows\system32\\taskkill /F /IM ",process_name))

def _monitor():
    myRunStatus=runStatus()
    while True:
        time.sleep(1)
        if check_process(process_stone_exe):
            if check_process(process_battle_exe):
                end_process(process_battle_exe)
                myRunStatus.setRunning(True)
                myRunStatus.setRunTime()
        if myRunStatus._bRunning:
            cnt=int(time.time())-myRunStatus.getRunTime()
            if cnt>=180:
                myRunStatus.setRunning(False)
                end_process(process_stone_exe)
                time.sleep(2)
                start_process()
