# -*- coding: utf-8 -*-
"""
Created on Sun March 01, 2020 12:31 Hrs
@author: Shrikant Velankar, VCS
"""
############ Imports - Dependencies ###########################################
from tkinter import *
from AspectFactors import *

############ Class Constructor ################################################
class MultiKbd(object):
    def __init__(self):
        self.Buttons=[]
        self.RetStrg=''
        self.CurrLang=''
        self.LangZero=''
        self.CurLangIdx=0
        self.indx=0
        self.Stln1=''
        self.NxLang=''
        self.sep2=3
        self.xDone=False 
        self.HeadLine=' Multi Language Input Virutal Keybord Ver 2.2'
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
              foreground=fg, command=lambda : self.DataUpdt('CHARS',str(vals)))
        self.b2.place(relwidth=wd, relheight=ht, relx=xpos,rely=ypos)
        return self.b2
############ End of Function ##################################################

############ Function : Label Maker ###########################################
    def MakeLbl(self,master,txt,font1,bg,fg,wd,ht,xpos,ypos):
        self.x1=Label(master,text=txt,font=font1,background=bg,foreground=fg)
        self.x1.place(relwidth=wd, relheight=ht, relx=xpos,rely=ypos)
        return self.x1
############ End of Function ##################################################

############ Function : Character Rendering ###################################
    def UpdTheChr(self,Xchar):
        if self.LangZero.upper()=='D':
            Conv1=self.ConvDvn
        elif self.LangZero.upper()=='G':
            Conv1=self.ConvGuj
        else:
            Conv1=self.ConvEcp
        i2=0
        for ele2 in Conv1:
            if Xchar==ele2:
                break
            else:
                i2=i2+1
        return self.ConvTab[i2]
                
############ Principle Data Updating Routine ##################################
    def DataUpdt(self,Opt,TheChr):
        self.lbData.focus()   
        if Opt=='CHARS':
            TheChr1=self.UpdTheChr(TheChr)
            CurPos=self.lbData.index('insert')
            self.lbData.insert(CurPos,TheChr1)      
        if Opt=='SPACE':
            CurPos=self.lbData.index('insert')
            self.lbData.insert(CurPos,' ')      
        if Opt=='BS':
            CurPos=self.lbData.index('insert')
            self.lbData.delete(CurPos+'- 1 chars')                 
        if Opt=='DEL':
            CurPos=self.lbData.index('insert')
            self.lbData.delete(CurPos)    
        if Opt=='RET':
            CurPos=self.lbData.index('insert')
            self.lbData.insert(CurPos,'\n')          
        if Opt=='UP':
            CurPos=self.lbData.index('insert')
            self.lbData.mark_set("insert", CurPos+"-1 lines")             
        if Opt=='DN':
            CurPos=self.lbData.index('insert')
            self.lbData.mark_set("insert", CurPos+"+1 lines")   
        if Opt=='FWD':
            CurPos=self.lbData.index('insert')
            self.lbData.mark_set("insert", CurPos+"+1 chars") 
        if Opt=='REV':
            CurPos=self.lbData.index('insert')
            self.lbData.mark_set("insert", CurPos+"-1 chars") 
        if Opt=='DONE':
#            self.RetStrg+='\n'
            self.xDone=True
            self.RetStrg=self.lbData.get('1.0','end')
            print(self.RetStrg)
            self.FrDevKbd.destroy()
            return
        CurPos=self.lbData.index('insert')
        self.lbData.see(CurPos)

############ Function : Language Definition, Selection & Switching ############
    def LangSelect(self,LangDesc):
        if LangDesc.upper()=='E':
            self.ConvTab=self.ConvEcp
            self.sep2=4
            self.Stln1=" Current Language: ENGLISH ... Encoding UNICODE-8"
            self.lbHeader.configure(text=self.HeadLine+" ( ENGLISH )")             
        elif LangDesc.upper()=='D':
            self.ConvTab=self.ConvDvn
            self.sep2=3
            self.Stln1=" Current Language: DEVANAGARI ( हिंदी / मराठी ) ... Encoding UNICODE-16"
            self.lbHeader.configure(text=self.HeadLine+"  ( हिंदी / मराठी )")
        elif LangDesc.upper()=='G':
            self.ConvTab=self.ConvGuj
            self.sep2=3
            self.Stln1=" Current Language: GUJRATI (ગુજરાથી ) ... Encoding UNICODE-16 "
            self.lbHeader.configure(text=self.HeadLine+"  ( ગુજરાથી )")
        else:
            self.ConvTab=self.ConvEcp
            self.sep2=4
            self.Stln1=" Current Language: ENGLISH ... Encoding UNICODE-8"
            self.lbHeader.configure(text=self.HeadLine+"  ENGLISH")   
        self.lbStat.configure(text=self.Stln1)
            
    def NextLang(self,LangArr,csel):
        if LangArr[csel]=='D':
            self.CurrLang='DEVNAGARI'
        if LangArr[csel]=='E':
            self.CurrLang='ENGLISH'
        if LangArr[csel]=='G':
            self.CurrLang='GUJRATI'
        if (len(LangArr)-1)==csel:
            csel=-1
        if LangArr[csel+1]=='D':
            self.NxLang='DEVENAGARI'
        if LangArr[csel+1]=='E':
            self.NxLang='ENGLISH'
        if LangArr[csel+1]=='G':
            self.NxLang='GUJRATI'
        self.btLang.configure(text='CHANGE TO : '+self.NxLang)
        
    def SwitchLang(self,LangArr):
        if len(LangArr) ==1:
            return
        if self.CurLangIdx == (len(LangArr)-1):
            self.CurLangIdx=0
        else:
            self.CurLangIdx+=1
        self.LangSelect(LangArr[self.CurLangIdx])
        self.indx=0
        for ele1 in self.ConvTab:
            self.Buttons[self.indx].configure(text=ele1)
            self.indx+=1
        self.NextLang(LangArr,self.CurLangIdx)
        
############ Main Devanagari Keyboard Input Function ##########################
    def MulKeyboard(self,Lang,ScrRoot,InLen=30,Prompt="Enter:",xPos=0.2,yPos=0.2,
                xWd=0.6,yHt=0.6,FrBg='white',FrBd='blue',ObjBg='light grey',
                ObjFg='black',ObjSp='red',LayOut=9):
        if xWd/yHt > 2:
            LayOut1=0
        elif 2 >= xWd/yHt > 0.5:
            LayOut1=1
        else:
            LayOut1=2
        if 0 >= LayOut >= 2:
            pass
        else:
            LayOut=LayOut1
        self.DataLen=InLen
        self.lbFont=('Ariel',int((yHt+2*xWd)*facto[LayOut]/fnt1[LayOut]))
        self.btFont=('Ariel',int((yHt+2*xWd)*facto[LayOut]/fnt2[LayOut]))
        self.btFont1=('Ariel',int((yHt+2*xWd)*facto[LayOut]/fnt3[LayOut]),'bold')
        self.stFont=('Ariel',int((yHt+2*xWd)*facto[LayOut]/fnt4[LayOut]),'italic')
        self.btFont2=('Ariel',int((yHt+2*xWd)*facto[LayOut]/fnt5[LayOut]),'bold')    
        if LayOut==2:
            LayOut=1
        self.FrDevKbd=Frame(ScrRoot,background=FrBg)
        self.FrDevKbd.place(relheight=yHt,relwidth=xWd, relx=xPos, rely=yPos)
        self.csco,self.cfrwd,self.cfrht=self.FrDevKbd,self.FrDevKbd.winfo_width(), \
                self.FrDevKbd.winfo_height()
        self.FrDevKbd.configure(highlightbackground=FrBd,highlightcolor=FrBg, 
                highlightthickness=2)
        self.lbHeader=self.MakeLbl(self.csco,self.HeadLine,self.lbFont,
                ObjBg,ObjFg,lbHeaderW[LayOut],lbHeaderH[LayOut],
                lbHeaderX[LayOut]*self.cfrwd,lbHeaderY[LayOut]*self.cfrht) 
        self.lbHeader.configure(anchor='w',justify=LEFT)
        self.btLang=self.MakeBtn(self.csco,'CHANGE TO:',self.btFont2,'light yellow','dark blue',
                btLangW[LayOut],btLangH[LayOut],
                btLangX[LayOut]*self.cfrwd,btLangY[LayOut]*self.cfrht)
        self.btLang.configure(command=lambda : self.SwitchLang(Lang))
        self.lbInput=self.MakeLbl(self.csco,Prompt,self.lbFont,
                ObjBg,ObjFg,lbInputW[LayOut],lbInputH[LayOut],
                lbInputX[LayOut]*self.cfrwd,lbInputY[LayOut]*self.cfrht) 
        self.scrollvData = Scrollbar(self.csco)
        self.scrollvData.place(relwidth=scrollW[LayOut],relheight=lbDataH[LayOut],
                relx=scrollX[LayOut]*self.cfrwd,rely=lbDataY[LayOut]*self.cfrht)
        self.lbData=Text(self.csco,font=self.lbFont,background='white',foreground='black')
        self.lbData.place(relwidth=lbDataW[LayOut],relheight=lbDataH[LayOut],
                relx=lbDataX[LayOut]*self.cfrwd,rely=lbDataY[LayOut]*self.cfrht)
        self.lbData.configure(pady=1, yscrollcommand = self.scrollvData.set)
        self.lbData.configure(relief=RIDGE,wrap=WORD)
        self.lbData.configure(spacing1=3,spacing2=3,spacing3=2)
        self.scrollvData.configure(command=self.lbData.yview)      
        self.lbStat=self.MakeLbl(self.csco,self.Stln1,self.stFont,
                'white','black',lbStatW[LayOut],lbStatH[LayOut],
                lbStatX[LayOut]*self.cfrwd,lbStatY[LayOut]*self.cfrht) 
        self.lbStat.configure(anchor='w',justify=LEFT)
        self.LangZero=Lang[0]
        if len(Lang) > 1:
            self.NextLang(Lang,self.CurLangIdx)
        else:
            self.btLang.configure(text='')
        self.LangSelect(Lang[self.CurLangIdx])            
        xBut,yBut,iBut=0,0,0.0
        for ele in self.ConvTab:
            self.Buttons.append(self.MakeBtn1(self.csco,ele,self.btFont,ObjBg,ObjFg,
                btnsW[LayOut],btnsH[LayOut],(xBut+btnsX[LayOut])*self.cfrwd/btnsNo[LayOut],
                (((iBut+yBut)*btnsY[LayOut])+btnsSh[LayOut])*self.cfrht,ele))
            xBut=xBut+1
            if xBut==btnsNo[LayOut]:
                xBut=0
                yBut=yBut+1
            if ((xBut==0) and ((yBut == 1) or (yBut==self.sep2))):
                iBut=iBut+btnsIbSh[LayOut]
        self.Buttons.append(self.MakeBtn(self.csco,'↑',self.btFont1,ObjBg,ObjSp,
                upW[LayOut],upH[LayOut],upX[LayOut]*self.cfrwd,upY[LayOut]*self.cfrht)) 
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('UP',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'↓',self.btFont1,ObjBg,ObjSp,
                dnW[LayOut],dnH[LayOut],dnX[LayOut]*self.cfrwd,dnY[LayOut]*self.cfrht)) 
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('DN',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'→',self.btFont1,ObjBg,ObjSp,
                fwdW[LayOut],fwdH[LayOut],fwdX[LayOut]*self.cfrwd,fwdY[LayOut]*self.cfrht)) 
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('FWD',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'←',self.btFont1,ObjBg,ObjSp,
                revW[LayOut],revH[LayOut],revX[LayOut]*self.cfrwd,revY[LayOut]*self.cfrht)) 
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('REV',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'Del',self.btFont,ObjBg,ObjSp,
                delW[LayOut],delH[LayOut],delX[LayOut]*self.cfrwd,delY[LayOut]*self.cfrht))   
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('DEL',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'Space',self.btFont,ObjBg,ObjFg,
                spW[LayOut],spH[LayOut],spX[LayOut]*self.cfrwd,spY[LayOut]*self.cfrht))  
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('SPACE',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'Back-Space',self.btFont,ObjBg,ObjFg,
                bsW[LayOut],bsH[LayOut],bsX[LayOut]*self.cfrwd,bsY[LayOut]*self.cfrht))   
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('BS',' '))
        self.Buttons.append(self.MakeBtn(self.csco,'Enter',self.btFont,ObjBg,ObjSp,
                entW[LayOut],entH[LayOut],entX[LayOut]*self.cfrwd,entY[LayOut]*self.cfrht))  
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('RET','\n'))
        self.Buttons.append(self.MakeBtn(self.csco,'Done (Confirm)',self.btFont,ObjBg,ObjSp,
                doneW[LayOut],doneH[LayOut],doneX[LayOut]*self.cfrwd,doneY[LayOut]*self.cfrht))  
        self.Buttons[-1].configure(command=lambda : self.DataUpdt('DONE','\n'))
        
########### End of Object Module ##############################################
