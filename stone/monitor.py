# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import os
import time
import datetime
import win32com.client
from common import *
from myGui import *

class Monitor(object):

    processBattleExe='Battle.net.exe'
    processStoneExe='Hearthstone.exe'

    def __init__(self):
        pass

    def bProcessExist(self,processName):
        return False
        WMI=win32com.client.GetObject('winmgmts:')
        processCodeCov=WMI.ExecQuery('select * from Win32_Process where Name="%s"' % processName)
        if len(processCodeCov)>0:return True
        else:return False

    def startProcess(self,processName):
        os.system('"{}"'.format(processName))

    def killProcess(self,processName):
        os.system('%s%s' % ("C:\windows\system32\\taskkill /F /IM ",processName))

    def run(self):
        while True:
            time.sleep(1)
            if MyGui.bRunning:
                tStart=MyGui.gStartTime.replace('\n','').split(':')
                tEnd=MyGui.gEndTime.replace('\n','').split(':')
                sHour=int(tStart[0])
                sMin=int(tStart[1])
                eHour=int(tEnd[0])
                eMin=int(tEnd[1])
                bSwap=False
                if sHour>eHour:
                    bSwap=True
                    tmp=sHour
                    sHour=eHour
                    eHour=tmp
                    tmp=sMin
                    sMin=eMin
                    eMin=tmp
                elif sHour==eHour and sMin>eMin:
                    bSwap=True
                    tmp=sMin
                    sMin=eMin
                    eMin=tmp
                cHour=datetime.datetime.now().hour
                cMin=datetime.datetime.now().minute
                bIn=((cHour>sHour or (cHour==sHour and cMin>=sMin)) and \
                    (cHour<eHour or (cHour==eHour and cMin<=eMin)))
                bValid=False
                if bSwap:
                    bValid=(not bIn)
                else:
                    bValid=(bIn)
                if bValid:
                    MyGui.bAutoAi=True
                    if self.bProcessExist(self.processStoneExe):
                        if self.bProcessExist(self.processBattleExe):
                            self.killProcess(self.processBattleExe)
                    else:
                        self.startProcess(MyGui.gBattlePath)
                        MyGui.gReboot=1
                        MyGui.gRunTime=time.time()
                    MyGui.gContinue=int(time.time()-MyGui.gRunTime)
                    if MyGui.gContinue>MyGui.gInterval:
                        if self.bProcessExist(self.processBattleExe):
                            self.killProcess(self.processBattleExe)
                        if self.bProcessExist(self.processStoneExe):
                            self.killProcess(self.processStoneExe)
                        time.sleep(2)
                        self.startProcess(MyGui.gBattlePath)
                        MyGui.gReboot=1
                        MyGui.gRebootCnt+=1
                        MyGui.gRunTime=time.time()
                else:
                    if self.bProcessExist(self.processBattleExe):
                        self.killProcess(self.processBattleExe)
                    if self.bProcessExist(self.processStoneExe):
                        self.killProcess(self.processStoneExe)
                    MyGui.bAutoAi=False
                    MyGui.gLog='AI未到运行时间('+MyGui.gStartTime.replace('\n','')+\
                        '-'+MyGui.gEndTime.replace('\n','')+')'
            else:
                MyGui.bAutoAi=False
                MyGui.gLog='软件暂未运行'

def threadMonitor():
    monitor=Monitor()
    monitor.run()
