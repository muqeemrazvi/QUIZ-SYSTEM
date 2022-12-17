from tkinter import *

import time


root=Tk()


corrAns=0
wrongAns=0

root.geometry("1500x1500")

f2=Frame(root,bg="gray",borderwidth=6)
f2.pack(fill=BOTH)
labelQ1=Label(f2,text="QUIZ SYSTEM",font="bold").pack()

fFram=Frame(root)
fFram.pack()
fFram.pack_propagate(False)
fFram.configure(bg="#9898F5",width=500,height=500)

def backup():
    global corrAns,wrongAns
    f=open("FormBackUp.txt","a")
    f.write(f" NAME     :    {nameValue.get()}")
    f.write(f"\nROLL NO   :   {rNoValue.get()}")
    f.write(f"\n AGE      :   {ageValue.get()}")
    f.write(f"\n PHONE NO :   {phNoValue.get()}")
    f.write(f"\nGot CORRECT ANSWERS : {corrAns}")
    f.write(f"\nGot CORRECT ANSWERS : {wrongAns}\n\n\n")



    f.close()
    f=open("RegistrationFormBackUP.txt","r")
    formback=f.read()

def getVal():
    f=open("RegistrationForm.txt","w")
    f.write(f"  NAME \t    :    {nameValue.get()}")
    f.write(f"\nROLL NO   :   {rNoValue.get()}")
    f.write(f"\n AGE\t    :   {ageValue.get()}")
    f.write(f"\n PHONE NO :   {phNoValue.get()}")
    

    f.close()
    f=open("RegistrationForm.txt","r")
    formContent=f.read()
    print(formContent)
    f.close() 
    startQuiz()
    fFram.destroy()

def getvalue1():
   global corrAns,wrongAns
   fb1.destroy()
   
   if var1.get()==1:
      ans1=Label(f1a,text="CORRECT ANSWER",bg="green")
      ans1.pack(pady=20)
      corrAns+=1
      Button(f1a,text="NEXT",command=Q2,font="bold").pack(padx=100)      
   else:
      ans1=Label(f1a,text="WRONG ANSWER",bg="red")
      ans1.pack(pady=20)
      wrongAns+=1
      # time.sleep(2.4)
      Button(f1a,text="NEXT",command=Q2,font="bold").pack(padx=100)      
      

def getvalue2():
    global corrAns,wrongAns
    fb2.destroy()
    if var2.get()==1:
      ans2=Label(f2a,text="CORRECT ANSWER",bg="green")
      ans2.pack()
      corrAns+=1
      Button(f2a,text="NEXT",command=Q3,font="bold").pack()
    else:
      ans2=Label(f2a,text="WRONG ANSWER",bg="red")
      ans2.pack()
      wrongAns+=1
      Button(f2a,text="NEXT",command=Q3,font="bold").pack()

def getvalue3():
    global corrAns,wrongAns
    fb3.destroy()
    if var3.get()==9:
      ans2=Label(f3a,text="CORRECT ANSWER",bg="green")
      ans2.pack()
      corrAns+=1
      Button(f3a,text="NEXT",command=Q4,font="bold").pack(padx=100)
    else:
      ans2=Label(f3a,text="WRONG ANSWER",bg="red")
      ans2.pack()
      wrongAns+=1
      Button(f3a,text="NEXT",command=Q4,font="bold").pack(padx=100)  

def getvalue4():
    global corrAns,wrongAns
    fb4.destroy()
    if var4.get()==1:
      ans2=Label(f4a,text="CORRECT ANSWER",bg="green")
      ans2.pack()
      corrAns+=1
      Button(f4a,text="NEXT",command=Q5,font="bold").pack(padx=100)
    else:
      ans2=Label(f4a,text="WRONG ANSWER",bg="red")
      ans2.pack()
      wrongAns+=1
      Button(f4a,text="NEXT",command=Q5,font="bold").pack(padx=100) 

def getvalue5():
    global corrAns,wrongAns
    fb5.destroy()
    if var5.get()==4:
      ans2=Label(f5a,text="CORRECT ANSWER",bg="green")
      ans2.pack()
      corrAns+=1
      Button(f5a,text="RESULT",command=result,background="#A9A9A9",font="bold").pack(pady=20)    
    else:
      ans2=Label(f5a,text="WRONG ANSWER",bg="red")
      ans2.pack() 
      wrongAns+=1
      Button(f6a,text=" RESULT",command=result,background="#A9A9A9",font="bold").pack()



  

def startQuiz():
  Q1()

var1=IntVar()
def Q1():
  labelQ1=Label(f1a,text="Q1 what is the value of pi",font="18",bg="#7F7FFF").pack(pady=20)
  radio1=Radiobutton(f1a,text="A)     3.123",variable=var1,value="4",font="18",bg="#7F7FFF").pack()
  radio1=Radiobutton(f1a,text="B)     3.143",variable=var1,value="1",font="18",bg="#7F7FFF").pack()
  radio1=Radiobutton(f1a,text="C)     3.153",variable=var1,value="2",font="18",bg="#7F7FFF").pack()
  rradio1=Radiobutton(f1a,text="D)     2.143",variable=var1,value="3",font="18",bg="#7F7FFF").pack()
  q1Sb1=Button(fb1,text="SUBMIT",command=getvalue1,font="bold").pack() 
     

var2=IntVar()
def Q2():
   f1a.destroy()
   labelQ2=Label(f2a,text="Q2what is the answer of 2+4/2",font="18",bg="#7F7FFF").pack(pady=20)
   radio2=Radiobutton(f2a,text="A)     3",variable=var2,value="2",font="18",bg="#7F7FFF").pack()
   radio2=Radiobutton(f2a,text="B)     2",variable=var2,value="3",font="18",bg="#7F7FFF").pack()
   radio2=Radiobutton(f2a,text="C)     4",variable=var2,value="1",font="18",bg="#7F7FFF").pack()
   radio2=Radiobutton(f2a,text="D)     6",variable=var2,value="4",font="18",bg="#7F7FFF").pack()
   Button(fb2,text="SUBMIT",command=getvalue2,font="bold").pack()


var3=IntVar()
def Q3():
   f2a.destroy()  
   labelQ3=Label(f3a,text="Q3) what is the answer of 25 X 25",font="18",bg="#7F7FFF").pack(pady=20)
   radio3=Radiobutton(f3a,text="A)     625",variable=var3,value="9",font="18",bg="#7F7FFF").pack()
   radio3=Radiobutton(f3a,text="B)     325",variable=var3,value="10",font="18",bg="#7F7FFF").pack()
   radio3=Radiobutton(f3a,text="C)     725",variable=var3,value="11",font="18",bg="#7F7FFF").pack()
   radio3=Radiobutton(f3a,text="D)     125",variable=var3,value="12",font="18",bg="#7F7FFF").pack()
   Button(fb3,text="SUBMIT",command=getvalue3,font="bold").pack()

var4=IntVar()
def Q4():
   f3a.destroy()
   labelQ4=Label(f4a,text="Q4)  HCF of 8, 9, 25 is",font="18",bg="#7F7FFF").pack(pady=20)
   radio4=Radiobutton(f4a,text="A)     1",variable=var4,value="1",font="18",bg="#7F7FFF").pack()
   radio4=Radiobutton(f4a,text="B)     3",variable=var4,value="10",font="18",bg="#7F7FFF").pack()
   radio4=Radiobutton(f4a,text="C)     5",variable=var4,value="11",font="18",bg="#7F7FFF").pack()
   radio4=Radiobutton(f4a,text="D)     2",variable=var4,value="12",font="18",bg="#7F7FFF").pack()
   Button(fb4,text="SUBMIT",command=getvalue4,font="bold").pack() 

var5=IntVar()
def Q5():
   f4a.destroy() 
   labelQ4=Label(f5a,text="Q5. What is the average of first 150 natural numbers ?",font="18",bg="#7F7FFF").pack(pady=20)
   radio4=Radiobutton(f5a,text="A)     7",variable=var5,value="1",font="18",bg="#7F7FFF").pack()
   radio4=Radiobutton(f5a,text="B)     75.5",variable=var5,value="4",font="18",bg="#7F7FFF").pack()
   radio4=Radiobutton(f5a,text="C)     70",variable=var5,value="11",font="18",bg="#7F7FFF").pack()
   radio4=Radiobutton(f5a,text="D)     70.5",variable=var5,value="12",font="18",bg="#7F7FFF").pack()
   Button(fb5,text="SUBMIT",command=getvalue5,font="bold").pack()    




def result():
   f5a.destroy()
   f6a.destroy()   
   global corrAns,wrongAns
   f=open("RegistrationForm.txt","r")
   cont=f.read()
   res=Label(root,text=cont,font="bold",bg="#C1C1CD")
   res.place(x=30,y=100)
   f.close()
   marks=Label(root,text=f"Total correct answers = {corrAns}"+f"\nTotal wrong answers = {wrongAns}",font="bold",bg="#FFFFE4")
   marks.place(x=400,y=200)
   backup()



heading1=Label(fFram,text="Registration Form\n",bg="#646495",fg="white",font="bold")
heading1.pack()




def aboutus():
    global l31,btnsu
    l31=Label(root,text="\nMOHD ABDUL MUQEEM\n",font=10,fg="red",bg="yellow")
    l31.place(relx=0.10,rely=0.41)
    btnsu=Button(text="X",bg="red",font="bold 15",command=Up1)     
    btnsu.place(relx=0.255,rely=0.41,width=30,height=30)  
def Up1():
    l31.destroy()
    btnsu.destroy()
   
b1=Button(root,fg="black",text="CREATORS",height=1,width=10,font="bold 13",bg="grey",command=aboutus)
b1.place(x=40,y=350)   
   




nameValue=StringVar()
rNoValue=StringVar()
ageValue=IntVar()
phNoValue=IntVar()

name=Label(fFram,text="Enter Name                  :")
nameentry=Entry(fFram,textvariable=nameValue)

rNo=Label(fFram,text="Enter roll Number :")
rNoentry=Entry(fFram,text="enter",textvariable=rNoValue)

age=Label(fFram,text="Enter Age                  :")
ageentry=Entry(fFram,textvariable=ageValue)

phNo=Label(fFram,text="Enter  phone number :")
phNoentry=Entry(fFram,textvariable=phNoValue)
breakline=Label(fFram,bg="#9898F5",text="\n").pack()
name.pack()
nameentry.pack()
breakline=Label(fFram,bg="#9898F5",text="\n\n").pack()

rNo.pack()
rNoentry.pack()
breakline=Label(fFram,bg="#9898F5",text="\n\n").pack()
age.pack()
ageentry.pack()
breakline=Label(fFram,bg="#9898F5",text="\n\n").pack()
phNo.pack()
phNoentry.pack()




Button(fFram,text="submit",command=getVal,font="bold").pack(pady=10)
f1a=Frame(root,bg="#7F7FFF")
f1a.pack()
  
f2a=Frame(root,bg="#7F7FFF")
f2a.pack()
f3a=Frame(root,bg="#7F7FFF")
f3a.pack()
f4a=Frame(root,bg="#7F7FFF")
f4a.pack()
f5a=Frame(root,bg="#7F7FFF")
f5a.pack()
f6a=Frame(root,bg="#7F7FFF")
f6a.pack()


fb1=Frame(root)
fb1.pack()
fb2=Frame(root)
fb2.pack()
fb3=Frame(root)
fb3.pack()
fb4=Frame(root)
fb4.pack()
fb5=Frame(root)
fb5.pack()
Button(root,text="X",command=root.destroy,font="bold",bg="red").place(x=1470,y=0.7)
root.mainloop()