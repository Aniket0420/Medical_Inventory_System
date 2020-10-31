from tkinter import *
import sys
from tkinter import messagebox    
    
#Show Menu
def clickedbtn1():    
    show_menu_window = Tk()
    frame = Frame(show_menu_window)
    frame.pack()
    show_menu_window.title("Medical Inventory System")
    
    lbl = Label(frame, text="Items Menu!", font='Helvetica 14 bold', fg="green").pack(side = TOP)
    lb2 = Label(frame, text="PPE Kits - ₹300.00", font='Helvetica 12', fg="black").pack(side = TOP)
    lb3 = Label(frame, text="N95 Masks - ₹120.00", font='Helvetica 12', fg="black").pack(side = TOP)
    lb4 = Label(frame, text="Hand Sanitizers - ₹80.00", font='Helvetica 12', fg="black").pack(side = TOP)
    lb5 = Label(frame, text="Rambiflan - ₹60.00", font='Helvetica 12', fg="black").pack(side = TOP)
    lb6 = Label(frame, text="Injection - ₹30.00", font='Helvetica 12', fg="black").pack(side = TOP)
    button = Button(show_menu_window, text="Quit", command=show_menu_window.destroy).pack(side = TOP)
    
    show_menu_window.mainloop()
       
    
#Customer Menu
def clickedbtn2():   
    
    def hello():
        messagebox.showinfo("Medical Inventory System", "Item Added to cart Succesfully !")
        print(var.get())

    customer_menu = Tk()
    var = IntVar()
    frame = Frame(customer_menu)
    frame.pack()
    customer_menu.title("Medical Inventory System")

    R1 = Radiobutton(frame, text="PPE Kits", variable=var, value=1, command=hello).pack(anchor = W)
    R2 = Radiobutton(frame, text="N95 Masks", variable=var, value=2,command=hello).pack(anchor = W)
    R3 = Radiobutton(frame, text="Hand Sanitizers", variable=var, value=3,command=hello).pack(anchor = W)  
    R4 = Radiobutton(frame, text="Rambiflan", variable=var, value=4,command=hello).pack(anchor = W)   
    R5 = Radiobutton(frame, text="Injection", variable=var, value=5,command=hello).pack(anchor = W)
    button = Button(customer_menu, text="Quit", command=customer_menu.destroy).pack(anchor = S)
    
    customer_menu.mainloop()

    
#Order Supply
def clickedbtn3():

    def ord():
        messagebox.showinfo("Medical Inventory System", "Order Placed Succesfully !")
        print(var.get())
        
    orderSupply = Tk()
    var = IntVar()
    orderSupply.geometry('350x200')
    orderSupply.title("Medical Inventory System")
    
    lbl = Label(orderSupply, text="Order Supply", font='Helvetica 16 bold', fg="green").grid(column=1, row=0)
    lb2 = Label(orderSupply, text="Select an item:", font='Helvetica 12 bold', fg="black").grid(column=0, row=1)
    R1 = Radiobutton(orderSupply, text="PPE Kits", variable=var, value=1).grid(column=0,row=2,sticky=W)
    R2 = Radiobutton(orderSupply, text="N95 Masks", variable=var, value=2).grid(column=0,row=3,sticky=W)
    R3 = Radiobutton(orderSupply, text="Hand Sanitizers", variable=var, value=3).grid(column=0,row=4,sticky=W)
    R4 = Radiobutton(orderSupply, text="Rambiflan", variable=var, value=4).grid(column=0,row=5,sticky=W)
    R5 = Radiobutton(orderSupply, text="Injection", variable=var, value=5).grid(column=0,row=6,sticky=W)
    L1 = Label(orderSupply, text="Select Quantity:", font='Helvetica 12 bold', fg="black").grid(column=0, row=8)
    E1 = Entry(orderSupply, bd =5).grid(column=1, row=8)
    btn1 = Button(orderSupply, text="Place Order",fg="red", command=ord).grid(column=1, row=10)
    button = Button(orderSupply, text="Quit", command=orderSupply.destroy).grid(column=1, row=11)
    
    orderSupply.mainloop()



#Stocks Remaining
def clickedbtn4():
    top = Tk() 
    listbox = Listbox(top, height = 10, width = 20, bg = "grey", activestyle = 'dotbox', font = "Helvetica", fg = "yellow") 
    top.geometry("300x250")  
    top.title("Medical Inventory System")
    label = Label(top, text = "Stocks Remaining", font='Helvetica 16 bold', fg="green")  

    listbox.insert(1, "PPE Kits - 104") 
    listbox.insert(2, "N95 Masks - 54") 
    listbox.insert(3, "Hand Sanitizers - 213") 
    listbox.insert(4, "Rambiflan - 63") 
    listbox.insert(5, "Injection - 225")
    button = Button(top, text="Quit", command=top.destroy)
    label.pack() 
    listbox.pack() 
    button.pack()
    
    top.mainloop()



#MAIN MENU
window = Tk()
frame = Frame(window)
frame.pack()

bottomframe = Frame(window)
bottomframe.pack( side = BOTTOM )

window.title("Medical Inventory System")

lbl = Label(frame, text="WELCOME TO EMERGENCY COVID CLINIC", font='Helvetica 18 bold', fg="green").pack(side = TOP)
lb2 = Label(frame, text="SELECT AN OPTION", font='Helvetica 16', fg="red").pack(side = TOP)
btn1 = Button(frame, text="Show Menu", fg="black", command=clickedbtn1).pack(side = TOP)
btn2 = Button(frame, text="Customer Menu", fg="black", command=clickedbtn2).pack(side = TOP)
btn3 = Button(frame, text="Supplier Menu", fg="black", command=clickedbtn3).pack(side = TOP)
btn4 = Button(frame, text="Stocks Remaining", fg="black", command=clickedbtn4).pack(side = TOP)

window.mainloop()

