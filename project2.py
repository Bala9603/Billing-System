from tkinter import *
import time
import datetime
import random
import sqlite3
from tkinter import messagebox
import csv
from tkinter import filedialog

window = Tk()
window.title("Hello")
window.geometry("1350x750+0+0")
window.configure(background='black')

Tops = Frame(window,bg='white',bd=20,relief=RIDGE)
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=('arial',60,'bold'),text='SHOP BUDDY',bd=21,bg='blue',fg='cornsilk',justify=CENTER)
lblTitle.grid(row=1)
ReceiptCal_F = Frame(window,bg='white')
ReceiptCal_F.pack(side=LEFT)


lbl = Label(ReceiptCal_F,text="Hey Please Login.....",font=('arial',20,'bold'))
lbl.grid(column=0,row=0)
lbl1 = Label(ReceiptCal_F,text='USERNAME',font=('arial',20,'bold'))
lbl1.grid(column =0,row=1)
txt = Entry(ReceiptCal_F,width =20)
txt.grid(column =1,row=1)
lbl2 = Label(ReceiptCal_F,text='PASSWORD',font=('arial',20,'bold'))
lbl2.grid(column =0,row=2)
txt1 = Entry(ReceiptCal_F,width =20,show="*")
txt1.grid(column =1,row=2)

def clicked():
        flag=0
        with open("login.csv",'r')as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0]==txt.get() and row[1]==txt1.get():
                    flag=1  

        if txt.get() =='' or txt1.get() =='':
            messagebox.askretrycancel('Invalid Syntax','Enter Valid content')
        elif flag==1:
            window.destroy()
            root =Tk()
            root.geometry("1350x750+0+0")
            root.title("Food Billing System")
            root.configure(background='black')
            con = sqlite3.connect('Quantity.db')
            cursorObj = con.cursor()
            list1 = []
            Tops = Frame(root,bg='white',bd=20,relief=RIDGE)
            Tops.pack(side=TOP)
            DateofOrder = StringVar()


            lblTitle=Label(Tops,font=('arial',60,'bold'),text='SHOP BUDDY',bd=21,bg='blue',fg='cornsilk',justify=CENTER)
            lblTitle.grid(row=1)

            ReceiptCal_F = Frame(root,bg='white')
            ReceiptCal_F.pack(side=LEFT)

            Buttons_F=Frame(ReceiptCal_F,bg='white',bd=3,relief=RIDGE)
            Buttons_F.pack(side=RIGHT)

            text_Input = StringVar()
            operator = ""
            def Stock():
                Stock = Tk()
                Stock.geometry("1350x750+0+0")
                Stock.title("Food Billing System")
                Stock.configure(background='black')
                Search_F=Frame(Stock,bg='white',bd=4,relief=RIDGE)
                Search_F.pack(side=TOP)
                Stock_F=Frame(Stock,bg='white',bd=4,relief=RIDGE)
                Stock_F.pack(side=LEFT)  
                cursorObj.execute('SELECT * FROM Stock')
                rows = cursorObj.fetchall()

                def Search():
                    txtStock.delete('1.0',END)
                    product=txtDisplay.get()
                    product = str(product)
                    txtStock.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Stock"+"\t"+"\n")
                    cursorObj.execute('SELECT * FROM Stock where Product =?;',(product,))
                    rows2 = cursorObj.fetchall()
                    for row in rows2:
                        for c in row:
                            txtStock.insert(END,str(c)+"\t")
                        txtStock.insert(END,"\n")
                
                def Add_Stock():
                    Add_s = Tk()
                    Add_s.geometry("1350x750+0+0")          
                    Add_s.title("Stock Add")
                    Add_s.configure(background='black')
                    Add_F=Frame(Add_s,bg='white',bd=4,relief=RIDGE) 
                    Add_F.pack(side=LEFT)
                    Stock_Fr=Frame(Add_s,bg='white',bd=4,relief=RIDGE)
                    Stock_Fr.pack(side=TOP)
                    New_Fr=Frame(Add_s,bg='white',bd=4,relief=RIDGE)
                    New_Fr.pack(side=RIGHT)
                    cursorObj.execute('SELECT * FROM Stock')
                    row2 = cursorObj.fetchall()
                    def Stock_add():
                        txtAdd2.delete('1.0',END)
                        prod=txtProduct.get()
                        quant=txtQuantity.get()
                        quant=int(quant)
                        txtAdd2.insert(END,"Before Updation"+"\n")
                        cursorObj.execute("SELECT * FROM Stock where Product = ? ;",(prod,))
                        row7 = cursorObj.fetchall()
                        txtAdd2.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Quantity"+"\t"+"\n")
                        for row in row7:
                            for c in row:
                                txtAdd2.insert(END,str(c)+"\t")
                            txtAdd2.insert(END,"\n")
                        cursorObj.execute('SELECT Quantity FROM Stock where Product =?;',(prod,))
                        row9 = cursorObj.fetchall()
                        for s in row9:
                            for i in s:
                                s_quant=int(i)
                                new_quant=s_quant+quant
                                cursorObj.execute('UPDATE Stock SET Quantity=? where Product =?;',(new_quant,prod))
                                con.commit()
                        txtAdd2.insert(END,"After Updation"+"\n")
                        cursorObj.execute("SELECT * FROM Stock where Product = ? ;",(prod,))
                        row8 = cursorObj.fetchall()
                        txtAdd2.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Quantity"+"\t"+"\n")
                        for row in row8:
                            for c in row:
                                txtAdd2.insert(END,str(c)+"\t")
                            txtAdd2.insert(END,"\n")

                    
                    def Refresh():
                        txtAdd.delete('1.0',END)
                        cursorObj.execute('SELECT * FROM Stock')
                        row2 = cursorObj.fetchall()
                        txtAdd.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Quantity"+"\t"+"\n")
                        for row in row2:
                            for c in row:
                                txtAdd.insert(END,str(c)+"\t")
                            txtAdd.insert(END,"\n")

            
                    txtAdd=Text(Add_F,width=40,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                    txtAdd.grid(row=1,column=0)
                    txtAdd2=Text(New_Fr,width=40,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                    txtAdd2.grid(row=1,column=0)
                    txtAdd.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Quantity"+"\t"+"\n")
                    for row in row2:
                        for c in row:
                            txtAdd.insert(END,str(c)+"\t")
                        txtAdd.insert(END,"\n")
                    btnAdd_s=Button(Stock_Fr,padx=25,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Add Stock',
                                bg='white',command=Stock_add).grid(row=0,column=2)
                    btnRefresh=Button(Stock_Fr,padx=25,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Refresh',
                                bg='white',command=Refresh).grid(row=1,column=2)
                    product_l=Label(Stock_Fr,text="Product",font=('arial',12,'bold'))
                    product_l.grid(row=0,column=0)
                    txtProduct=Entry(Stock_Fr,width=30,bg='white',bd=4,font=('arial',12,'bold'),textvariable=text_Input)
                    txtProduct.grid(row=0,column=1,pady=1)
                    quantity_l=Label(Stock_Fr,text="Quantity",font=('arial',12,'bold'))
                    quantity_l.grid(row=1,column=0)
                    txtQuantity=Entry(Stock_Fr,width=30,bg='white',bd=4,font=('arial',12,'bold'))
                    txtQuantity.grid(row=1,column=1,pady=1)


                btnSearch=Button(Search_F,padx=16,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Search',
                                    bg='white',command=Search).grid(row=0,column=2)
                btnAdd_s=Button(Search_F,padx=25,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Add Stock',
                                    bg='white',command=Add_Stock).grid(row=1,column=2)
                txtDisplay=Entry(Search_F,width=30,bg='white',bd=4,font=('arial',12,'bold'),textvariable=text_Input)
                txtDisplay.grid(row=0,column=0,pady=1)
                
                txtStock=Text(Stock_F,width=50,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                txtStock.grid(row=1,column=0)

                txtStock.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Quantity"+"\t"+"\n")
                for row in rows:
                    for c in row:
                        txtStock.insert(END,str(c)+"\t")
                    txtStock.insert(END,"\n")

            def Receipt():
                Receipt = Tk()
                Receipt.geometry("1350x750+0+0")
                Receipt.title("Receipt")
                Receipt.configure(background='black')
                Add_F=Frame(Receipt,bg='white',bd=4,relief=RIDGE)
                Add_F.pack(side=TOP)
                Receipt_F=Frame(Receipt,bg='white',bd=4,relief=RIDGE)
                Receipt_F.pack(side=LEFT)
                Print_F=Frame(Receipt,bg='white',bd=4,relief=RIDGE)
                Print_F.pack(side=RIGHT)
                
                def add():
                    list1=[]
                    product=txtProduct.get()
                    quantity = txtQuantity.get()
                    quantity=int(quantity)
                    product = str(product)
                    cursorObj.execute('SELECT * FROM Stock where Product =?;',(product,))
                    rows3 = cursorObj.fetchall()
                    for row in rows3:
                        for c in row:
                            list1.append(c)
                    id =int(list1[0])
                    productname=str(list1[1])
                    price=int(list1[2])
                    sum=price*quantity
                    cursorObj.execute("INSERT INTO Receipt(Id,Product,Price,Quantity,Sum) VALUES(?,?,?,?,?);",(id,productname,price,quantity,sum))
                    con.commit()
                    cursorObj.execute('SELECT * FROM Receipt where Product = ?;',(productname,)) 
                    rows2 = cursorObj.fetchall()
                    for row in rows2:
                        for c in row:
                            txtStock.insert(END,str(c)+"\t")
                        txtStock.insert(END,"\n")
                    cursorObj.execute('SELECT Quantity FROM Stock where Product =?;',(productname,))
                    row4 = cursorObj.fetchall()
                    for s in row4:
                        for i in s:
                            s_quantity=int(i)
                            new_quantity=s_quantity-quantity
                            cursorObj.execute('UPDATE Stock SET Quantity=? where Product =?;',(new_quantity,productname))
                            con.commit()
                def Print():  
                    txtPrint=Text(Print_F,width=50,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                    txtPrint.grid(row=0,column=5)       
                    DateofOrder.set(time.strftime("%d%m%Y"+"-"+"%H"+"%M"+"%S"))
                    date=DateofOrder.get()
                    txtPrint.insert(END, "Bill no. "+"= "+date+"\n" )
                    txtPrint.insert(END,"S.no"+"\t"+"Product"+"\t"+"Price"+"\t"+"Quantity "+"\t"+" Sum"+"\t"+"\n")
                    cursorObj.execute('SELECT * FROM Receipt ') 
                    rows2 = cursorObj.fetchall()
                    for row in rows2:
                        for c in row:
                            txtPrint.insert(END,str(c)+"\t")
                        txtPrint.insert(END,"\n")
                    cursorObj.execute('SELECT Id,Product,Price,Quantity FROM Receipt')
                    rows3 = cursorObj.fetchall()
                    print(rows3)
                    for row in rows3:
                        print(row)
                        cursorObj.execute("INSERT INTO Sales(Id,Bill_no,Product,Price,Quantity) VALUES(?,?,?,?,?);",(row[0],date,row[1],row[2],row[3]))
                        con.commit()
                        cursorObj.execute('DELETE FROM Receipt WHERE Id > 0;')
                        con.commit()
                txtStock=Text(Receipt_F,width=50,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                txtStock.grid(row=1,column=0)
                txtStock.insert(END,"S.no"+"\t"+"Product"+"\t"+"Price"+"\t"+"Quantity "+"\t"+" Sum"+"\t"+"\n")
                product_l=Label(Add_F,text="Product",font=('arial',12,'bold'))
                product_l.grid(row=0,column=0)
                txtProduct=Entry(Add_F,width=30,bg='white',bd=4,font=('arial',12,'bold'),textvariable=text_Input)
                txtProduct.grid(row=0,column=1,pady=1)
                quantity_l=Label(Add_F,text="Quantity",font=('arial',12,'bold'))
                quantity_l.grid(row=1,column=0)
                txtQuantity=Entry(Add_F,width=30,bg='white',bd=4,font=('arial',12,'bold'))
                txtQuantity.grid(row=1,column=1,pady=1)
                btnProduct=Button(Add_F,padx=16,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Add item',
                                    bg='white',command=add).grid(row=0,column=2)
                btnPrint=Button(Add_F,padx=30,pady=1,bd=7,fg='blue',font=('arial',10,'bold'),width=4,text='Print Receipt',
                                    bg='white',command=Print).grid(row=1,column=2)

            def Sales():
                Sales = Tk()
                Sales.geometry("1350x750+0+0")
                Sales.title("Food Billing System")
                Sales.configure(background='black')
                Search_F=Frame(Sales,bg='white',bd=4,relief=RIDGE)
                Search_F.pack(side=TOP)
                Sales_F=Frame(Sales,bg='white',bd=4,relief=RIDGE)
                Sales_F.pack(side=LEFT)
                New2_F=Frame(Sales,bg='white',bd=4,relief=RIDGE)
                New2_F.pack(side=RIGHT)
                
                def Bill():
                    txtBill.delete('1.0',END)
                    Bill_no=txtDisplay.get()
                    txtBill.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Stock"+"\t"+"Bill No."+"\t"+"\n")
                    cursorObj.execute('SELECT * FROM Sales where Bill_no =?;',(Bill_no,))
                    rows2 = cursorObj.fetchall()
                    for row in rows2:
                        for c in row:
                            txtBill.insert(END,str(c)+"\t")
                        txtBill.insert(END,"\n")

                btnSearch=Button(Search_F,padx=16,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Bill No.',
                                    bg='white',command=Bill).grid(row=0,column=2)  
                txtDisplay=Entry(Search_F,width=30,bg='white',bd=4,font=('arial',12,'bold'),textvariable=text_Input)
                txtDisplay.grid(row=0,column=0,pady=1)
                txtStock=Text(Sales_F,width=50,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                txtStock.grid(row=1,column=0)
                txtBill=Text(New2_F,width=50,height=20,bg='white',bd=4,font=('arial',12,'bold'))
                txtBill.grid(row=1,column=0)
                txtStock.insert(END,"S.no"+"\t"+"Product "+"\t"+"Price"+"\t"+"Stock"+"\t"+"Bill No."+"\t"+"\n")
                cursorObj.execute('SELECT * FROM Sales')
                rows = cursorObj.fetchall()
                for row in rows:    
                    for c in row:
                        txtStock.insert(END,str(c)+"\t")
                    txtStock.insert(END,"\n")

            ###########################################BUTTONS################################################################################
            btnStock=Button(Buttons_F,padx=16,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Stock',
                                    bg='white',command=Stock).grid(row=0,column=1)

            btnSales=Button(Buttons_F,padx=20,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Sales',
                                    bg='white',command=Sales).grid(row=0,column=3)

            btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Receipt',
                                    bg='white',command=Receipt).grid(row=0,column=4)

            btnAccount=Button(Buttons_F,padx=16,pady=1,bd=7,fg='blue',font=('arial',16,'bold'),width=4,text='Camera',
                                    bg='white').grid(row=0,column=5)


        
        elif flag==0:
            messagebox.showinfo("Acsess Denied", "Wrond Credentials")

btn1 = Button(ReceiptCal_F,fg='blue',font=('arial',20,'bold'),width=20,text="submit",command=clicked)
btn1.grid(column=1,row=4)


window.mainloop()