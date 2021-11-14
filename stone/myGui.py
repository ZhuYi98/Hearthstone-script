# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

from tkinter import *
from tkinter import ttk,filedialog
import time
import datetime
import configparser

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
        self.place(x=85,y=310)

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
        abandon='通关'
        if MyGui.gAbandon==88:
            abandon='神秘人'
        elif MyGui.gAbandon<=6 and MyGui.gAbandon>=1:
            abandon=str(MyGui.gAbandon)
        status=\
            '通关='+str(MyGui.gFinish)+'次'+\
            ' 小关='+str(MyGui.gRound)+'/'+abandon+\
            ' 战斗='+str(MyGui.gContinue)+'/'+str(MyGui.gInterval)+'秒'
        self.statusStr.set(status)
    def start(self):
        self._update()
        self.place(x=115,y=250)

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
        self.place(x=10,y=280)

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
        self.place(x=10,y=310)

class MyGui(object):

    bSavePng=False
    gLog=None

    gRound=0
    gFinish=0

    bResetScene=False
    gContinue=0
    
    gRebootCnt=0
    gWait=0.0

    bAutoAi=False
    bRunning=False
    gRunTime=time.time()

    #界面配置
    gBattlePath=None
    gGameMode='1'
    gDifficulty='1'
    gLevel='2-5'
    gAbandon=99
    gViewTask=0
    gSkill='1'
    gCard='1-1'
    gInterval=600
    gStartTime=None
    gEndTime=None

    def __init__(self):

        #读取配置文件
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        MyGui.gBattlePath=config.get('config','battlepath').replace('\n','')
        MyGui.gGameMode=config.get('config','gamemode').replace('\n','')
        MyGui.gDifficulty=config.get('config','difficulty').replace('\n','')
        MyGui.gLevel=config.get('config','level').replace('\n','')
        MyGui.gAbandon=int(config.get('config','abandon').replace('\n',''))
        MyGui.gViewTask=int(config.get('config','task').replace('\n',''))
        MyGui.gSkill=config.get('config','skill').replace('\n','')
        MyGui.gCard=config.get('config','card').replace('\n','')
        MyGui.gInterval=int(config.get('config','interval').replace('\n',''))
        MyGui.gStartTime=config.get('config','starttime').replace('\n','')
        MyGui.gEndTime=config.get('config','endtime').replace('\n','')

        self.win=Tk()
        self.win.title('炉石AI--By琴弦上的宇宙--2021-11-14') #标题
        self.win.attributes('-alpha',1.0) #透明度
        self.win.attributes('-topmost',True) #置顶
        self.win.geometry("420x340+0+345") #大小和位置
        self.win.resizable(width=False,height=False)

        self.lb1=Label(self.win,text='战网启动器：',font=("",12))
        self.lb1.place(x=10,y=10)
        self.text1=Text(self.win,width=22,height=1,font=("",12))
        self.text1.place(x=120,y=10)
        self.text1.delete(0.0,END)
        self.text1.insert(INSERT,MyGui.gBattlePath)
        self.text1.config(state=DISABLED)
        self.btn1=Button(self.win,text='选择启动器',font=("",12),command=self.setBattle)
        self.btn1.place(x=315,y=10)

        self.lb2=Label(self.win,text='游戏模式：',font=("",12))
        self.lb2.place(x=10,y=40)
        self.cmb1=ttk.Combobox(self.win,width=13,font=("",12))
        self.cmb1['values']=['PVE副本坐牢','PVP正常对战','PVP友好互投']
        self.cmb1['state']='readonly'
        game=MyGui.gGameMode.replace('\n','')
        self.cmb1.current(int(game)-1)
        self.cmb1.place(x=120,y=40)
        self.btn555=Button(self.win,text='确定',width=5,height=1,\
            font=("",12),command=self.setGameMode)
        self.btn555.place(x=250,y=37)

        self.lb3=Label(self.win,text='副本选择：',font=("",12))
        self.lb3.place(x=10,y=70)
        self.cmb21=ttk.Combobox(self.win,width=6,font=("",12))
        self.cmb21['values']=['普通','英雄']
        self.cmb21['state']='readonly'
        diffcult=MyGui.gDifficulty.replace('\n','')
        self.cmb21.current(int(diffcult)-1)
        self.cmb21.place(x=120,y=70)
        self.text22=Text(self.win,width=5,height=1,font=("",12))
        self.text22.place(x=195,y=70)
        self.text22.delete(0.0,END)
        self.text22.insert(INSERT,MyGui.gLevel)
        self.cmb23=ttk.Combobox(self.win,width=12,font=("",12))
        self.cmb23['values']=['全力通关','神秘人后放弃',\
            '1小关后放弃','2小关后放弃','3小关后放弃',
            '4小关后放弃','5小关后放弃','6小关后放弃']
        self.cmb23['state']='readonly'
        if MyGui.gAbandon==99:
            self.cmb23.current(0)
        elif MyGui.gAbandon==88:
            self.cmb23.current(1)
        elif MyGui.gAbandon<=6 and MyGui.gAbandon>=1:
            self.cmb23.current(MyGui.gAbandon+1)
        self.cmb23.place(x=120,y=100)
        self.checkVar=StringVar(value='0')
        self.check=Checkbutton(self.win,text="自动点击任务",\
            variable=self.checkVar,width=12,font=("",10))
        if MyGui.gViewTask==1:
            self.check.select()
        self.check.place(x=5,y=100)
        self.btn666=Button(self.win,text='确定',width=5,height=2,\
            font=("",12),command=self.setZone)
        self.btn666.place(x=250,y=73)

        self.lb4=Label(self.win,text='技能选择：',font=("",12))
        self.lb4.place(x=10,y=130)
        self.cmb3=ttk.Combobox(self.win,width=13,font=("",12))
        self.cmb3['values']=\
            ['AOE后优先1','AOE后优先2','AOE后优先3','AOE后优先4','AOE后优先5','AOE后随机',\
             '必优先1技能','必优先2技能','必优先3技能','必优先4技能','必优先5技能','全技能随机']
        self.cmb3['state']='readonly'
        skill=MyGui.gSkill.replace('\n','')
        self.cmb3.current(int(skill)-1)
        self.cmb3.place(x=120,y=130)
        self.btn55=Button(self.win,text='确定',width=5,height=1,\
            font=("",12),command=self.setSkill)
        self.btn55.place(x=250,y=127)

        self.lb5=Label(self.win,text='卡组选择：',font=("",12))
        self.lb5.place(x=10,y=160)
        self.cmb4=ttk.Combobox(self.win,width=13,font=("",12))
        self.cmb4['values']=\
            ['第1行第1个','第1行第2个','第1行第3个',\
             '第2行第1个','第2行第2个','第2行第3个',\
             '第3行第1个','第3行第2个','第3行第3个']
        self.cmb4['state']='readonly'
        card1=MyGui.gCard.replace('\n','').split('-')
        self.cmb4.current(3*(int(card1[0])-1)+(int(card1[1])-1))
        self.cmb4.place(x=120,y=160)
        self.btn44=Button(self.win,text='确定',width=5,height=1,\
            font=("",12),command=self.setCard)
        self.btn44.place(x=250,y=157)

        self.lb6=Label(self.win,text='防掉线检测：',font=("",12))
        self.lb6.place(x=10,y=190)
        self.lb60=Label(self.win,text='秒',font=("",12))
        self.lb60.place(x=200,y=190)
        self.text2=Text(self.win,width=8,height=1,font=("",12))
        self.text2.place(x=120,y=190)
        self.text2.delete(0.0,END)
        self.text2.insert(INSERT,MyGui.gInterval)
        self.btn22=Button(self.win,text='确定',width=5,height=1,\
            font=("",12),command=self.setInterval)
        self.btn22.place(x=250,y=187)

        self.lb7=Label(self.win,text='监控时间：',font=("",12))
        self.lb7.place(x=10,y=220)
        self.text3=Text(self.win,width=6,height=1,font=("",12))
        self.text3.place(x=120,y=220)
        self.text3.delete(0.0,END)
        self.text3.insert(INSERT,MyGui.gStartTime)
        self.lb8=Label(self.win,text='-',font=("",12))
        self.lb8.place(x=173,y=220)
        self.text4=Text(self.win,width=6,height=1,font=("",12))
        self.text4.place(x=190,y=220)
        self.text4.delete(0.0,END)
        self.text4.insert(INSERT,MyGui.gEndTime)
        self.btn33=Button(self.win,text='确定',width=5,height=1,\
            font=("",12),command=self.setRunTime)
        self.btn33.place(x=250,y=217)

        self.lb9=Label(self.win,text='运行状态：',font=("",12))
        self.lb9.place(x=10,y=250)

        self.btn2=Button(self.win,text='运行',width=10,height=8,\
            foreground='blue',font=("",12),command=self.startAi)
        self.btn2.place(x=315,y=75)

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
            MyGui.bResetScene=True
            MyGui.bRunning=True
            MyGui.gRunTime=time.time()
            self.btn2['foreground']='green'
            self.btn2['text']='运行中...'
            self.cmb1.config(state=DISABLED)
            self.cmb21.config(state=DISABLED)
            self.text22.config(state=DISABLED)
            self.cmb23.config(state=DISABLED)
            self.cmb3.config(state=DISABLED)
            self.cmb4.config(state=DISABLED)
            self.check.config(state=DISABLED)
            self.text2.config(state=DISABLED)
            self.text3.config(state=DISABLED)
            self.text4.config(state=DISABLED)
        else:
            MyGui.bRunning=False
            MyGui.bAutoAi=False
            self.btn2['foreground']='blue'
            self.btn2['text']='运行'
            self.cmb1.config(state=NORMAL)
            self.cmb21.config(state=NORMAL)
            self.text22.config(state=NORMAL)
            self.cmb23.config(state=NORMAL)
            self.cmb3.config(state=NORMAL)
            self.cmb4.config(state=NORMAL)
            self.check.config(state=NORMAL)
            self.text2.config(state=NORMAL)
            self.text3.config(state=NORMAL)
            self.text4.config(state=NORMAL)

    def setBattle(self):
        file=filedialog.askopenfilename().replace('\n','')
        MyGui.gBattlePath=file
        self.text1.delete(0.0,END)
        self.text1.insert(INSERT,file)
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        config.set("config","battlepath",file)
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()

    def setGameMode(self):
        i=0
        all=['PVE副本坐牢','PVP正常对战','PVP友好互投']
        name1=self.cmb1.get().replace('\n','')
        for name in all:
            if name1!=name:i+=1
            else:
                if i==0:MyGui.gGameMode='1'
                elif i==1:MyGui.gGameMode='2'
                elif i==2:MyGui.gGameMode='3'
                break
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        config.set("config","gamemode",MyGui.gGameMode.replace('\n',''))
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()

    def setZone(self):
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")

        #副本难度
        i=0
        all=['普通','英雄']
        name1=self.cmb21.get().replace('\n','')
        for name in all:
            if name1!=name:i+=1
            else:
                if i==0:MyGui.gDifficulty='1'
                elif i==1:MyGui.gDifficulty='2'
                break
        config.set("config","difficulty",MyGui.gDifficulty.replace('\n',''))

        #副本地图
        MyGui.gLevel=self.text22.get(0.0,END).replace('\n','')
        config.set("config","level",self.text22.get(0.0,END).replace('\n',''))

        #小关卡次数
        i=0
        all=['全力通关','神秘人后放弃',\
            '1小关后放弃','2小关后放弃','3小关后放弃',
            '4小关后放弃','5小关后放弃','6小关后放弃']
        name1=self.cmb23.get().replace('\n','')
        for name in all:
            if name1!=name:i+=1
            else:
                if i==0:MyGui.gAbandon=99
                elif i==1:MyGui.gAbandon=88
                else:MyGui.gAbandon=i-1
                break
        config.set("config","abandon",str(MyGui.gAbandon).replace('\n',''))

        #点击任务
        MyGui.gViewTask=int(self.checkVar.get().replace('\n',''))
        config.set("config","task",self.checkVar.get().replace('\n',''))

        #保存
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()

    def setSkill(self):
        i=0
        all=['AOE后优先1','AOE后优先2','AOE后优先3','AOE后优先4','AOE后优先5','AOE后随机',\
             '必优先1技能','必优先2技能','必优先3技能','必优先4技能','必优先5技能','全技能随机']
        name1=self.cmb3.get().replace('\n','')
        for name in all:
            if name1!=name:i+=1
            else:
                if i==0:MyGui.gSkill='1'
                elif i==1:MyGui.gSkill='2'
                elif i==2:MyGui.gSkill='3'
                elif i==3:MyGui.gSkill='4'
                elif i==4:MyGui.gSkill='5'
                elif i==5:MyGui.gSkill='6'
                elif i==6:MyGui.gSkill='7'
                elif i==7:MyGui.gSkill='8'
                elif i==8:MyGui.gSkill='9'
                elif i==9:MyGui.gSkill='10'
                elif i==10:MyGui.gSkill='11'
                elif i==11:MyGui.gSkill='12'
                break
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        config.set("config","skill",MyGui.gSkill.replace('\n',''))
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()

    def setCard(self):
        i=0
        all=['第1行第1个','第1行第2个','第1行第3个',\
             '第2行第1个','第2行第2个','第2行第3个',\
             '第3行第1个','第3行第2个','第3行第3个']
        name1=self.cmb4.get().replace('\n','')
        for name in all:
            if name1!=name:i+=1
            else:
                if i==0:MyGui.gCard='1-1'
                elif i==1:MyGui.gCard='1-2'
                elif i==2:MyGui.gCard='1-3'
                elif i==3:MyGui.gCard='2-1'
                elif i==4:MyGui.gCard='2-2'
                elif i==5:MyGui.gCard='2-3'
                elif i==6:MyGui.gCard='3-1'
                elif i==7:MyGui.gCard='3-2'
                elif i==8:MyGui.gCard='3-3'
                break
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        config.set("config","card",MyGui.gCard.replace('\n',''))
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()

    def setInterval(self):
        MyGui.gInterval=int(self.text2.get(0.0,END).replace('\n',''))
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        config.set("config","interval",self.text2.get(0.0,END).replace('\n',''))
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()

    def setRunTime(self):
        MyGui.gStartTime=self.text3.get(0.0,END).replace('\n','')
        MyGui.gEndTime=self.text4.get(0.0,END).replace('\n','')
        config=configparser.ConfigParser()
        config.read("config/config.ini",encoding="utf8")
        config.set("config","starttime",MyGui.gStartTime.replace('\n',''))
        config.set("config","endtime",MyGui.gEndTime.replace('\n',''))
        o=open("config/config.ini","w",encoding="utf8")
        config.write(o)
        o.close()
