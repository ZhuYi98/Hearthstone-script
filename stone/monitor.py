# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
import time
import win32com.client
from common import *
from myGui import *

class Monitor(object):

    processBattleExe='Battle.net.exe'
    processStoneExe='Hearthstone.exe'

    def __init__(self):
        pass

    def bProcessExist(self,processName):
        WMI=win32com.client.GetObject('winmgmts:')
        processCodeCov=WMI.ExecQuery('select * from Win32_Process where Name="%s"' % processName)
        if len(processCodeCov)>0:return True
        else:return False
    
    def startProcess(self,processName):
        os.system('"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe"')

    def killProcess(self,processName):
        os.system('%s%s' % ("C:\windows\system32\\taskkill /F /IM ",processName))

    def run(self):
        while True:
            time.sleep(1)
            if self.bProcessExist(self.processStoneExe):
                if self.bProcessExist(self.processBattleExe):
                    self.killProcess(self.processBattleExe)
            if MyGui.bRunning:
                MyGui.gContinue=int(time.time()-MyGui.gRunTime)
                if MyGui.gContinue>=MyGui.gInterval:
                    self.killProcess(self.processStoneExe)
                    time.sleep(2)
                    self.startProcess(self.processBattleExe)
                    MyGui.gReboot=1
                    MyGui.gRunTime=time.time()

def threadMonitor():
    monitor=Monitor()
    monitor.run()
