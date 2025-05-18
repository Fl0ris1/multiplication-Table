from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Multiplication")
root.config(background="#75F4F4")

titleLbl=Label(root,text="Multiplication Table",font=("consolas",16,"bold"),background="#75F4F4",foreground="#003459")
titleLbl.grid(row=0,column=0,columnspan=3,pady=25)

rangeLbl=Label(root,text="Number and Range: ",font=("consolas",12,"bold"),background="#75F4F4",foreground="#003459")
rangeLbl.grid(row=1,column=0,padx=10)

#creating comboBox
num=IntVar()
numbers=Combobox(root,textvariable=num,width=5,state="readonly")
numbers["values"]=tuple(range(101))
numbers.grid(row=1,column=1)

#creating radio buttons
radioVal=IntVar()
r10=Radiobutton(root,text="10",variable=radioVal,value=10)
r20=Radiobutton(root,text="20",variable=radioVal,value=20)
r30=Radiobutton(root,text="30",variable=radioVal,value=30)

radioVal.set(10)
r10.grid(row=1,column=2,pady=3,padx=30)
r20.grid(row=2,column=2,pady=3,padx=30)
r30.grid(row=3,column=2,pady=3,padx=30)

generateBut=Button(root,text="Generate",bg)
root.mainloop()

