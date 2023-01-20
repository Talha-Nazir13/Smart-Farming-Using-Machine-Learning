#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import Tk
class MyWindow:
    def __init__(self, win):
              
        self.backGroundImage = PhotoImage(file="tal.png")
        self.backGroundImageLabel = Label(win,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0,width=800,height=600)
        
        
        self.lbl1=Label( text='Nitrogen')
        self.lbl2=Label( text='Phosphorus')
        self.lbl4=Label( text='Potassium')
        self.lbl5=Label( text='Temperature')
        self.lbl6=Label( text='Humidity')
        self.lbl7=Label( text='Ph')
        self.lbl8=Label( text='Rainfall')
        self.lbl9=Label( text='District')
        
        self.lbl3=Label(win, text='CROP PREDICTION')
        
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t4=Entry()
        self.t5=Entry()        
        self.t6=Entry()
        self.t7=Entry()
        self.t8=Entry()
        self.t9=Entry()
        
        self.t3=Entry()
        
#         self.btn1 = Button(win, text='Add')
#         self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=70, y=50)
        self.t1.place(x=150, y=50)
        self.lbl2.place(x=330, y=50)
        self.t2.place(x=430, y=50)
        
#         lbl3 and t3 is reserved for results
        
        self.lbl4.place(x=70, y=85)
        self.t4.place(x=150, y=85)
        self.lbl5.place(x=330, y=85)
        self.t5.place(x=430, y=85)
        
        self.lbl6.place(x=70, y=120)
        self.t6.place(x=150, y=120)
        self.lbl7.place(x=330, y=120)
        self.t7.place(x=430, y=120)
        
        self.lbl8.place(x=70, y=155)
        self.t8.place(x=150, y=155)
        self.lbl9.place(x=330, y=155)
        self.t9.place(x=430, y=155)
        
        
        
        

        def OnPressed(event):
            self.add()
        def OnHover(event):
            self.b1.config(bg='red', fg='blue')
        def OnLeave(event):
            self.b1.config(bg='blue', fg='black')

        self.b1 = Button(win, text='SUBMIT', bg='blue', relief='groove')
#         self.b1=Button(win, text='SUBMIT', command=self.add)
#         self.b1.place(x=280, y=200)
        self.b1.place(x=290, y=210)
        self.b1.bind('<Button>', OnPressed)
        self.b1.bind('<Enter>', OnHover)
        self.b1.bind('<Leave>', OnLeave)

#         root.mainloop()
        
        
        
        
        
#         self.b2=Button(win, text='Subtract')
#         self.b2.bind('<Button-1>', self.sub)


#         self.b1=Button(win, text='SUBMIT', command=self.add)
#         self.b1.place(x=280, y=200)
#         self.b2.place(x=200, y=150)

        self.lbl3.place(x=230, y=310)
        self.t3.place(x=380, y=310)
        
        
        

    def add(self):
        self.t3.delete(0, 'end')
#         get value from gui and pass value to database for processing
        nitrogen=float(self.t1.get())
        phosphorus=float(self.t2.get())
        potassium=float(self.t4.get())
        temperature=float(self.t5.get())
        humidity=float(self.t6.get())
        ph=float(self.t7.get()) 
        rainfall=float(self.t8.get())
#         getting result of prediction from database 
        data = np.array([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
        prediction = LogReg.predict(data)
        result=prediction
        self.t3.insert(END, str(result))
        

window=Tk()
mywin=MyWindow(window)
window.title('SMART FARMING USING ML')
window.geometry("700x500+10+10")
window.mainloop()

