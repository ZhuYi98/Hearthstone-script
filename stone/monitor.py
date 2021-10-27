# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
import time
import win32com.client
from common import *

processBattleExe='Battle.net.exe'
processStoneExe='Hearthstone.exe'

#检测进程
def bProcessExist(processName):
    WMI=win32com.client.GetObject('winmgmts:')
    processCodeCov=WMI.ExecQuery('select * from Win32_Process where Name="%s"' % processName)
    if len(processCodeCov)>0:return True
    else:return False

#启动进程
def StartProcess(processName):
    os.system('"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe"')

#结束进程
def KillProcess(processName):
    os.system('%s%s' % ("C:\windows\system32\\taskkill /F /IM ",processName))

def threadMonitor():
    myRunStatus=runStatus()
    while True:
        time.sleep(1)
        if bProcessExist(processStoneExe):
            if bProcessExist(processBattleExe):
                KillProcess(processBattleExe)
                myRunStatus.setRunning(True)
                myRunStatus.setRunTime()
        if myRunStatus._bRunning:
            cnt=int(time.time())-myRunStatus.getRunTime()
            if cnt>=180:
                myRunStatus.setRunning(False)
                KillProcess(processStoneExe)
                time.sleep(2)
                StartProcess(processBattleExe)
