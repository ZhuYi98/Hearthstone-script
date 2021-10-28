# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
import time
#import win32com.client
from common import *
from myGui import *

class Monitor():

    processBattleExe='Battle.net.exe'
    processStoneExe='Hearthstone.exe'
    interval=180
    bRunning=True
    runTime=int(time.time())

    def __init__(self):
        pass

    def bRunning(self):
        return self.bRunning

    def setRunning(self,result):
        self.bRunning=result

    def getRunTime(self):
        return self.runTime

    def setRunTime(self):
        self.runTime=int(time.time())

    def bProcessExist(self,processName):
        if 0:
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
                    self.setRunning(True)
                    self.setRunTime()
            if self.bRunning:
                cnt=int(time.time())-self.getRunTime()
                if cnt>=self.interval:
                    self.setRunning(False)
                    self.killProcess(self.processStoneExe)
                    time.sleep(2)
                    self.startProcess(self.processBattleExe)

def threadMonitor():
    monitor=Monitor()
    monitor.run()
