from tkinter import *
import os
import shutil
import subprocess

window =Tk()
window.title('TERMINAL')
window.configure(background='black')
window.geometry('1000x600')

defaultlabel=Label(window,text='WELCOME TO COMMAND LINE INTERFACE\n',bg='black',fg='lightgray').grid(row=0,column=0,sticky=W)

i=0
def set_y():
    global i
    i=i+1
    print(i)

def display_to_user():
    set_y()
    text_out=os.getcwd()
    label=Label(window,text=text_out+' > ',font=('Myanmar Text',10),bg='black',fg='gray').grid(row=i,column=0,sticky=W)
display_to_user()

def user_input():
    text_in=StringVar()
    t1=Entry(window,textvariable=text_in,font=('Myanmar Text',10),width=20,bg='black',fg='lightgray',bd=0)
    t1.config(insertwidth=10)
    t1.grid(row=i,column=1,sticky=W)
    t1.focus()
user_input()

def choice():
    global var1,var2,var3
    l=ch.split(' ')
    var1=l[0]
    if len(l)>1:
        var2=l[1]
        if len(l)>2:
            var3=l[2]

def interpret(event):
    global ch
    set_y()
    ch=event.widget.get()
    choice()
    if ch=='cd..':
        os.chdir('..')
    elif ch=='pwd':
        text_out=os.getcwd()
        label=Label(window,text=text_out,font=('Myanmar Text',10),bg='black',fg='lightgray',bd=0).grid(row=i,column=0,sticky=W)
    elif var1=='cd':
        os.chdir(var2)
    elif var1=='touch':
        f=open(var2,'w+')
    elif var1=='cpf':
        src=os.path.join(os.getcwd(),var2)
        dst=os.path.join(os.getcwd(),var3)
        shutil.copy(src,dst)
    elif var1=='cpd':
        src=os.path.join(os.getcwd(),var2)
        dst=os.path.join(os.getcwd(),var3)
        shutil.copytree(src,dst)
    elif var1=='rn':
        os.rename(var2,var3)
    elif var1=='mkdir':
        os.mkdir(var2)
    elif var1=='rmdir':
        os.rmdir(var2)
    elif var1=='rm':
        files=os.listdir(os.getcwd())
        if var2 in files:
            os.unlink(var2)
    elif var1=='ls':
        n=os.listdir(os.getcwd())
        for j in range (len(n)):
            set_y()
            if os.path.isfile(n[j])==True:
                label=Label(window,text=n[j],font=('Myanmar Text',10),bg='black',fg='lightgreen',bd=0).grid(row=i,column=0,sticky=W)
            else:
                label=Label(window,text=n[j],font=('Myanmar Text',10),bg='black',fg='orange',bd=0).grid(row=i,column=0,sticky=W)
    elif var1=='cat':
        cat=open(var2,'r')
        put=cat.read().split('\n')
        for j in range (len(put)):
            set_y()
            label=Label(window,text=put[j],font=('Myanmar Text',10),bg='black',fg='gray',bd=0).grid(row=i,column=0,sticky=W)
    elif var1=='head':
        cat=open(var2,'r')
        put=cat.read().split('\n')
        for j in range (10):
            set_y()
            label=Label(window,text=put[j],font=('Myanmar Text',10),bg='black',fg='gray',bd=0).grid(row=i,column=0,sticky=W)
    elif var1=='tail':
        cat=open(var2,'r')
        put=cat.read().split('\n')
        put.reverse()
        rev=[]
        for j in range (10):
            rev=rev+[put[j]]
        for j in range (1,11):
            set_y()
            label=Label(window,text=rev[-j],font=('Myanmar Text',10),bg='black',fg='gray',bd=0).grid(row=i,column=0,sticky=W)
    elif var1=='gedit':
        #os.startfile(var2)
        proc = subprocess.Popen(['gedit' , var2])
    elif var1=='grep':
        cat=open(var3,'r')
        put=cat.read().split('\n')
        for j in range (len(put)):
            set_y()
            if var2 in put[j] :
                label=Label(window,text=put[j],font=('Myanmar Text',10),bg='black',fg='gray',bd=0).grid(row=i,column=0,sticky=W)
    else :
        label=Label(window,text="ERROR\n",font=('Myanmar Text',10),bg='black',fg='lightgray',bd=0).grid(row=i,column=0,sticky=W)
    display_to_user()
    user_input()

window.bind('<Return>',interpret)

window.mainloop()
