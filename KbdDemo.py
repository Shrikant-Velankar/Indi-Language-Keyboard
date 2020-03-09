# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 04:45:15 2020
@author: Shrikant
"""
from tkinter import *
import LangKbd

class KeyboardDemo(object):
    def __init__(self):
        self.xfont=('Ariel',20)
        self.btBgColor='light grey'
        self.lbBgColor='white'
        self.txColor='black'        
        self.CreateDemoFrame()
            
############ Shows Data Returned by Multi Language Keyboard ###################
    def ShowData(self,TheDStr):
        self.lbDat.configure(text=TheDStr[:-1])

############ Shows Data Returned by Multi Language Keyboard ###################
    def CreateDemoFrame(self):
        self.root=Tk()
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.root.overrideredirect(1)
        self.root.configure(background=self.lbBgColor)
        self.priscrwd=self.root.winfo_width()
        self.priscrht=self.root.winfo_height()
        self.root.geometry('%dx%d+%d+%d'%(self.priscrwd,self.priscrht,0,0))
        
        self.btExit=Button(self.root,text='Quit',font=self.xfont,background=self.btBgColor,foreground=self.txColor)
        self.btExit.place(relwidth=1,relheight=0.04,relx=0.0*self.root.winfo_width(),
                   rely=0.01*self.root.winfo_height())
        self.btExit.configure(command=lambda :self.root.destroy())
        self.btShow=Button(self.root,text='Show',font=self.xfont,background=self.btBgColor,foreground=self.txColor)
        self.btShow.place(relwidth=1,relheight=0.04,relx=0.0*self.root.winfo_width(),
                   rely=0.1*self.root.winfo_height())
        self.lbDat=Label(self.root,text="",font=self.xfont,background=self.lbBgColor,foreground=self.txColor)
        self.lbDat.place(relwidth=1,relheight=0.04,relx=0.0*self.root.winfo_width(),
                   rely=0.055*self.root.winfo_height())
        self.root.lift()
        
############ Main UI Program Loop #############################################  
def DispMain():
    Demo = KeyboardDemo()
    MulKbd = LangKbd.MultiKbd()
    
    pEnt="Enter Train Name :"
    MulKbd.MulKeyboard('D',Demo.root,50,pEnt,0.17,0.17,0.66,0.66,
                'dark blue','white','light cyan','black')
    
    Demo.btShow.configure(command=lambda :Demo.ShowData(MulKbd.RetStrg))
    Demo.root.mainloop()
    
"""
Multi Language Virtual Keyboard: Usage Note:
    Instatiate object of class MultiKbd from module LangKbd
    Execute method 'MultiKeyboard()' of this Instance 
    Specified Language UTF string is returned to Instance variable 'RetStrg'
    
    1st Arg: Language Specifier - 
    'D' for Devanagari, 'E' for English, 'G' for Gujrati - Mandatory Arg
    2nd Arg: UI Container - Window or Frame, Mandatory Arg
  [ 3rd Arg: Max. length of String acceptable by the Keyboard, Default=30 Characters
    4th Arg: Prompting String. Default='Enter:'
    5th Arg: Relative X Position, Default=0.2
    6th Arg: Relative Y Position, Default=0.2
    7th Arg: Width, Default=0.6
    8th Arg: Height, Default=0.6
    9th Arg: Frame Background Color, Default='white'
   10th Arg: Frame Border Color, Default='blue'
   11th Arg: Buttons Background Color, Default='light grey'
   12th Arg: Buttons Text Color, Default='black' ]
"""
############ MAIN PROGRAM Starts here #########################################
DispMain()    
############ END of the Code ##################################################
