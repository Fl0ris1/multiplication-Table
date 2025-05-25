import tkinter as tk
from tkinter.ttk import *

def multtable():
    tables=""
    for i in range(1,radioVal.get()+1):
        mul=num.get()*i
        tables+=str(num.get())+" X "+str(i)+" = "+str(mul)+"\n"
        table_lbl.config(text=tables,font=("consolas",12,"bold"))
        



root=tk.Tk()
root.title("Multiplication")
root.config(background="#75F4F4")

titleLbl=tk.Label(root,text="Multiplication Table",font=("consolas",16,"bold"),background="#75F4F4",foreground="#003459")
titleLbl.grid(row=0,column=0,columnspan=3,pady=25)

rangeLbl=tk.Label(root,text="Number and Range: ",font=("consolas",12,"bold"),background="#75F4F4",foreground="#003459")
rangeLbl.grid(row=1,column=0,padx=10)

#creating comboBox
num=tk.IntVar()
numbers=Combobox(root,textvariable=num,width=5,state="readonly")
numbers["values"]=tuple(range(101))
numbers.grid(row=1,column=1)

#creating radio buttons
radioVal=tk.IntVar()
r10=tk.Radiobutton(root,text="10",variable=radioVal,value=10)
r20=tk.Radiobutton(root,text="20",variable=radioVal,value=20)
r30=tk.Radiobutton(root,text="30",variable=radioVal,value=30)

radioVal.set(10)
r10.grid(row=1,column=2,pady=3,padx=30)
r20.grid(row=2,column=2,pady=3,padx=30)
r30.grid(row=3,column=2,pady=3,padx=30)

generateBut=tk.Button(root,text="Generate",font=("consolas",12,"bold"),background="#BDBBB6",command=multtable)
generateBut.grid(row=4,column=1)

table_lbl=tk.Label(root,anchor="center",background="#75F4F4")
table_lbl.grid(row=5,column=1,pady=25)
root.mainloop()

