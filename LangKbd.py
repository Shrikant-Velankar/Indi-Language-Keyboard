# -*- coding: utf-8 -*-
"""
Created on Sun March 01, 2020 12:31 Hrs
@author: Shrikant Velankar, VCS
"""
############ Imports - Dependencies ###########################################
from tkinter import *

class MultiKbd(object):
    def __init__(self):
        self.Buttons=[]
        self.RetStrg=''
        self.xDone=False 
        self.HeadLine='Multi Language Input Virutal Keybord Ver 1.3'
        self.ConvDvn= ('\u0966','\u0967','\u0968','\u0969','\u096A',
              '\u096B','\u096C','\u096D','\u096E','\u096F',
              '\u093E','\u093F','\u0940','\u0941','\u0942',
              '\u0947','\u0948','\u094B','\u094C','\u094D',           
              '\u0901','\u0902','\u0903','\u0943','\u093C',
              '\u0964','\u0945','\u0949','\u0946','\u094A',           
              '\u0905','\u0906','\u0907','\u0908','\u0909',
              '\u090A','\u090F','\u0910','\u0913','\u0914',
              '\u0915','\u0916','\u0917','\u0918','\u0919',
              '\u091A','\u091B','\u091C','\u091D','\u091E',
              '\u091F','\u0920','\u0921','\u0922','\u0923',
              '\u0924','\u0925','\u0926','\u0927','\u0928',
              '\u092A','\u092B','\u092C','\u092D','\u092E',
              '\u092F','\u0930','\u0932','\u0933','\u0935',
              '\u0936','\u0937','\u0938','\u0939','\u090B',
              '*','#','@','%','&','.','$','_','+','-')

        self.ConvGuj= ('\u0AE6','\u0AE7','\u0AE8','\u0AE9','\u0AEA',
              '\u0AEB','\u0AEC','\u0AED','\u0AEE','\u0AEF',
              '\u0ABE','\u0ABF','\u0AC0','\u0AC1','\u0AC2',
              '\u0AC7','\u0AC8','\u0ACB','\u0ACC','\u0ACD',           
              '\u0A81','\u0A82','\u0A83','\u0AC3','\u0AC4',
              '\u0AD0','\u0AE0','\u0A8B','\u0A8C','\u0AE1',
              '\u0A85','\u0A86','\u0A87','\u0A88','\u0A89',
              '\u0A8A','\u0A8F','\u0A90','\u0A93','\u0A94',               
              '\u0A95','\u0A96','\u0A97','\u0A98','\u0A99',
              '\u0A9A','\u0A9B','\u0A9C','\u0A9D','\u0A9E',
              '\u0A9F','\u0AA0','\u0AA1','\u0AA2','\u0AA3',
              '\u0AA4','\u0AA5','\u0AA6','\u0AA7','\u0AA8',
              '\u0AAA','\u0AAB','\u0AAC','\u0AAD','\u0AAE',
              '\u0AAF','\u0AB0','\u0AB2','\u0AB3','\u0AB5',
              '\u0AB6','\u0AB7','\u0AB8','\u0AB9','\u0ABD',
              '*','#','@','%','&','.','$','_','+','-')
    
        self.ConvEcp= ('0','1','2','3','4','5','6','7','8','9',
              'Q','W','E','R','T','Y','U','I','O','P',           
              'A','S','D','F','G','H','J','K','L',':',           
              'Z','X','C','V','B','N','M','<','>','?',
              'q','w','e','r','t','y','u','i','o','p',           
              'a','s','d','f','g','h','j','k','l',';',           
              'z','x','c','v','b','n','m',',','.','=',            
              '[',']','{','}','^','*','#','@','%','&',
              '.','$','_','+','-')   

############ Function : Button Maker ##########################################
    def MakeBtn(self,master,txt,font1,bg,fg,wd,ht,xpos,ypos):
        self.b1=Button(master,text=txt,font=font1,background=bg,foreground=fg)
        self.b1.place(relwidth=wd, relheight=ht, relx=xpos,rely=ypos)
        return self.b1
############ End of Function ##################################################

############ Function : Button Maker 1 ########################################
    def MakeBtn1(self,master,txt,font1,bg,fg,wd,ht,xpos,ypos,vals):
        self.b2=Button(master,text=txt,font=font1,background=bg,
              foreground=fg, command=lambda : self.DataUpdt(0,str(vals)))
        self.b2.place(relwidth=wd, relheight=ht, relx=xpos,rely=ypos)
        return self.b2
############ End of Function ##################################################

############ Function : Label Maker ###########################################
    def MakeLbl(self,master,txt,font1,bg,fg,wd,ht,xpos,ypos):
        self.x1=Label(master,text=txt,font=font1,background=bg,foreground=fg)
        self.x1.place(relwidth=wd, relheight=ht, relx=xpos,rely=ypos)
        return self.x1
############ End of Function ##################################################

############ Principle Data Updating Routine ##################################
    def DataUpdt(self,Opt,TheChr):
        global RetData
        if Opt==0:
            self.RetStrg+=TheChr
        elif Opt==1:
            self.RetStrg+=' '
        elif Opt==2:
            self.RetStrg=self.RetStrg[:-1]
        else:
            self.RetStrg+='\n'
            self.xDone=True
            self.FrDevKbd.destroy()
            print(self.RetStrg)
            return
        if len(self.RetStrg) > self.DataLen:
            self.RetStrg=self.RetStrg[:self.DataLen]
            self.StatLine="Status: Maximum Character Length Exceeded"
            self.lbStat.configure(text=self.StatLine,fg='red')
        else:
            self.StatLine=self.Stln1
            self.StatLine+='(Characters Remaining :'+str(self.DataLen-len(self.RetStrg))+')'
            self.lbStat.configure(text=self.StatLine,fg='black')
        if Opt < 3:
            self.lbData.configure(text=self.RetStrg)  
 
############ Main Devanagari Keyboard Input Function ##########################
    def MulKeyboard(self,Lang,ScrRoot,InLen=30,Prompt="Enter:",xPos=0.2,yPos=0.2,
                xWd=0.6,yHt=0.6,FrBg='white',FrBd='blue',ObjBg='light grey',
                ObjFg='black'):
        self.DataLen=InLen
        self.lbFont=('Ariel',int(ScrRoot.winfo_screenmmwidth()*xWd/17))
        self.btFont=('Ariel',int(ScrRoot.winfo_screenmmwidth()*xWd/16))
        self.stFont=('Ariel',int(ScrRoot.winfo_screenmmwidth()*xWd/20),'italic')
   
        self.FrDevKbd=Frame(ScrRoot,background=FrBg)
        self.FrDevKbd.place(relheight=yHt,relwidth=xWd, relx=xPos, rely=yPos)
        self.csco,self.cfrwd,self.cfrht=self.FrDevKbd,self.FrDevKbd.winfo_width(),self.FrDevKbd.winfo_height()
        self.FrDevKbd.configure(highlightbackground=FrBd,highlightcolor=FrBg, 
                       highlightthickness=2)
        self.lbHeader=self.MakeLbl(self.csco,self.HeadLine,self.lbFont,
                    ObjBg,ObjFg,0.994,0.06,0.003*self.cfrwd,0.01*self.cfrht) 
        self.lbInput=self.MakeLbl(self.csco,Prompt,self.lbFont,
                    ObjBg,ObjFg,0.31,0.06,0.003*self.cfrwd,0.09*self.cfrht) 
        self.lbData=self.MakeLbl(self.csco,self.RetStrg,self.lbFont,
                    'white','black',0.68,0.06,0.317*self.cfrwd,0.09*self.cfrht) 
        self.lbData.configure(anchor='w',justify=LEFT)
        self.lbData.configure(relief=RIDGE)
        if Lang.upper()=='E':
            self.ConvTab=self.ConvEcp
            Sep2=4
            self.Stln1="Encoding UNICODE-8 ENGLISH ...."
            self.lbHeader.configure(text=self.HeadLine+" ( ENGLISH )")             
        elif Lang.upper()=='D':
            self.ConvTab=self.ConvDvn
            Sep2=3
            self.Stln1="Encoding UNICODE-16 DEVANAGARI ( हिंदी / मराठी ) ...."
            self.lbHeader.configure(text=self.HeadLine+"  ( हिंदी / मराठी )")
        elif Lang.upper()=='G':
            self.ConvTab=self.ConvGuj
            Sep2=3
            self.Stln1="Encoding UNICODE-16 GUJRATI (ગુજરાથી ) ... "
            self.lbHeader.configure(text=self.HeadLine+"  ( ગુજરાથી )")
        else:
            self.ConvTab=self.ConvEcp
            Sep2=4
            self.Stln1="Encoding UNICODE-8 ENGLISH ... "
            self.lbHeader.configure(text=self.HeadLine+"  ENGLISH")              
        self.lbStat=self.MakeLbl(self.csco,self.Stln1,self.stFont,
                    'white','black',0.994,0.06,0.003*self.cfrwd,0.935*self.cfrht) 
        self.lbStat.configure(anchor='w',justify=LEFT)
        xBut,yBut,iBut=0,0,0.0
        for ele in self.ConvTab:
            self.Buttons.append(self.MakeBtn1(self.csco,ele,self.btFont,ObjBg,ObjFg,
                0.095,0.063,(xBut+0.03)*self.cfrwd/10,
                (((iBut+yBut)*0.07)+0.2)*self.cfrht,ele))
            xBut=xBut+1
            if xBut==10:
                xBut=0
                yBut=yBut+1
            if ((xBut==0) and ((yBut == 1) or (yBut==Sep2))):
                iBut=iBut+0.2
        self.Buttons.append(self.MakeBtn(self.csco,'Space',self.btFont,ObjBg,ObjFg,
                0.495,0.063,0.503*self.cfrwd,0.788*self.cfrht))  
        self.Buttons[-1].configure(command=lambda : self.DataUpdt(1,' '))
        self.Buttons.append(self.MakeBtn(self.csco,'Back Space',self.btFont,ObjBg,ObjFg,
                0.495,0.063,0.003*self.cfrwd,0.86*self.cfrht))   
        self.Buttons[-1].configure(command=lambda : self.DataUpdt(2,' '))
        self.Buttons.append(self.MakeBtn(self.csco,'Enter (Confirm)',self.btFont,ObjBg,ObjFg,
                0.495,0.063,0.503*self.cfrwd,0.86*self.cfrht))  
        self.Buttons[-1].configure(command=lambda : self.DataUpdt(3,'\n'))
        
########### End of Object Module ##############################################
