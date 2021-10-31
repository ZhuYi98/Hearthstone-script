# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

from tkinter import *
from tkinter import ttk,filedialog
import time

#时钟
class Watch(Frame):
    msec=1000
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self._running=False
        self.timeStr=StringVar()
        self._start=time.time()
        self.makeWidgets()
    def makeWidgets(self):
        l1=Label(self,textvariable=self.timeStr,font=("",12))
        l1.pack()
    def _update(self):
        self._settime()
        self.timer=self.after(self.msec,self._update)
    def _settime(self):
        hours='{:0>2d}'.format(int((time.time()-self._start)/3600))
        minutes='{:0>2d}'.format(int((time.time()-self._start)/60%60))
        today=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+\
            ' 已启动'+hours+':'+minutes+' 重启'+str(MyGui.gRebootCnt)+'次'
        self.timeStr.set(today)
    def start(self):
        self._update()
        self.place(x=85,y=280)

#状态
class Status(Frame):
    msec=1000
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self._running=False
        self.statusStr=StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        l1=Label(self,textvariable=self.statusStr,font=("",12))
        l1.pack()
    def _update(self):
        self._setStatus()
        self.timer=self.after(self.msec,self._update)
    def _setStatus(self):
        status='通关次数='+str(MyGui.gFinish)+'  关卡='+str(MyGui.gRound)+\
            '  战斗='+str(MyGui.gContinue)+'/'+str(MyGui.gInterval)+'秒'
        self.statusStr.set(status)
    def start(self):
        self._update()
        self.place(x=115,y=220)

#调试
class Debug(Frame):
    msec=100
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self._running=False
        self.logStr=StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        l1=Label(self,textvariable=self.logStr,foreground='red',font=("",11))
        l1.pack()
    def _update(self):
        self._setLog()
        self.timer=self.after(self.msec,self._update)
    def _setLog(self):
        log=str(MyGui.gLog)
        log=log.replace('resource/','')
        log=log.replace('.png','')
        self.logStr.set(log)
    def start(self):
        self._update()
        self.place(x=10,y=250)

#调试
class Wait(Frame):
    msec=100
    def __init__(self,parent=None,**kw):
        Frame.__init__(self,parent,kw)
        self._running=False
        self.waitStr=StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        l1=Label(self,textvariable=self.waitStr,foreground='red',font=("",11))
        l1.pack()
    def _update(self):
        self._setWait()
        self.timer=self.after(self.msec,self._update)
    def _setWait(self):
        if MyGui.gWait>=0.1:
            MyGui.gWait-=0.1
        wait=str(round(MyGui.gWait,1))
        self.waitStr.set(wait+'s RC')
    def start(self):
        self._update()
        self.place(x=10,y=280)

class MyGui(object):

    gRound=0
    gFinish=0

    gReboot=1
    gContinue=0
    gInterval=300
    gRebootCnt=0

    bRunning=False
    gRunTime=time.time()

    gLog=None
    gWait=0.0

    def __init__(self):
        self.win=Tk()
        self.win.title('炉石AI--By琴弦上的宇宙') #标题
        self.win.attributes('-alpha',1.0) #透明度
        self.win.attributes('-topmost',True) #置顶
        self.win.geometry("420x310+0+360") #大小和位置
        self.win.resizable(width=False,height=False)

        self.lb1=Label(self.win,text='战网启动器：',font=("",12))
        self.lb1.place(x=10,y=10)
        self.text1=Text(self.win,width=20,height=1,font=("",12))
        self.text1.place(x=120,y=10)
        self.btn1=Button(self.win,text='选择启动器',font=("",12),command=self.setBattle)
        self.btn1.place(x=315,y=10)

        self.lb2=Label(self.win,text='游戏模式：',font=("",12))
        self.lb2.place(x=10,y=40)
        self.cmb1=ttk.Combobox(self.win)
        self.cmb1.place(x=120,y=40)

        self.lb3=Label(self.win,text='战斗模式：',font=("",12))
        self.lb3.place(x=10,y=70)
        self.cmb2=ttk.Combobox(self.win)
        self.cmb2.place(x=120,y=70)

        self.lb4=Label(self.win,text='游戏关卡：',font=("",12))
        self.lb4.place(x=10,y=100)
        self.cmb3=ttk.Combobox(self.win)
        self.cmb3.place(x=120,y=100)

        self.lb5=Label(self.win,text='卡组选择：',font=("",12))
        self.lb5.place(x=10,y=130)
        self.cmb4=ttk.Combobox(self.win)
        self.cmb4.place(x=120,y=130)

        self.lb6=Label(self.win,text='防掉线检测：',font=("",12))
        self.lb6.place(x=10,y=160)
        self.cmb5=ttk.Combobox(self.win)
        self.cmb5.place(x=120,y=160)

        self.lb7=Label(self.win,text='监控时间：',font=("",12))
        self.lb7.place(x=10,y=190)
        self.text2=Text(self.win,width=8,height=1,font=("",12))
        self.text2.place(x=120,y=190)
        self.lb8=Label(self.win,text='-',font=("",12))
        self.lb8.place(x=190,y=190)
        self.text3=Text(self.win,width=8,height=1,font=("",12))
        self.text3.place(x=210,y=190)

        self.lb9=Label(self.win,text='运行状态：',font=("",12))
        self.lb9.place(x=10,y=220)

        self.btn2=Button(self.win,text='运行',width=10,height=8,\
            foreground='blue',font=("",12),command=self.startAi)
        self.btn2.place(x=315,y=60)

        self.status=Status(self.win)
        self.status.start()
        self.debug=Debug(self.win)
        self.debug.start()
        self.wait=Wait(self.win)
        self.wait.start()
        self.watch=Watch(self.win)
        self.watch.start()

    def startAi(self):
        if self.btn2['text']=='运行':
            MyGui.bRunning=True
            MyGui.gRunTime=time.time()
            self.btn2['foreground']='green'
            self.btn2['text']='运行中...'
            
        else:
            MyGui.bRunning=False
            self.btn2['foreground']='blue'
            self.btn2['text']='运行'

    def setBattle(self):
        file=filedialog.askopenfilename()
        self.text1.delete(0.0,END)
        self.text1.insert(INSERT,file)

    def setInterval(self):
        self.gInterval=180
