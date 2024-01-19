'''
    INVENTORY MANAGEMENT SYSTEM
    Developed By->PJ28105
    Started On ->08/11/18
'''
import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Addtional_features import mycombobox,myentry
import datetime
import os

# USER MENU
class User:
    def __init__(self,mainw):
         self.mainw=mainw

    def user_mainmenu(self,a,b):
        self.mainframe = LabelFrame(self.mainw, width=800, height=140, bg="#f7f7f7")
        self.mainframe.place(x=330, y=120)
        mi = PhotoImage(file="images/items.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="Items",bd=5,font="roboto 11 bold",bg="cyan", image=mi, compound=TOP,command=self.builditemtable)
        self.aitems.image = mi
        self.aitems.place(x=260, y=17)
        mi = PhotoImage(file="images/invoice2.png")
        mi = mi.subsample(a,b)
        self.aitems = Button(self.mainframe, text="Invoice",bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP,command=self.make_invoice)
        self.aitems.image = mi
        self.aitems.place(x=62, y=17)
        mi = PhotoImage(file="images/change1.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="Sign out",bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP)
        self.changeuser.image = mi
        self.changeuser.place(x=460, y=17)
        mi = PhotoImage(file="images/Door_Out-512.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="Quit",bd=5,bg="cyan",font="roboto 11 bold", image=mi, compound=TOP)
        self.logout.image = mi
        self.logout.place(x=670, y=17)
        self.tableframe1 =Frame(self.mainw, width=150, height=400,bg="#FFFFFF")
        self.tableframe1.place(x=1230, y=270, anchor=NE)
        self.tableframe1info=self.tableframe1.place_info()
        self.tableframe =Frame(self.mainw, width=350, height=700,bg="#FFFFFF")
        self.tableframe.place(x=1110, y=300, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.entryframe = Frame(self.mainw, width=800, height=350, bg="#FFFFFF")
        self.entryframe.place(x=810, y=460+20)
        self.entryframeinfo = self.entryframe.place_info()
        self.entryframe1 = Frame(self.mainw, width=500, height=350, bg="#FFFFFF")
        self.entryframe1.place(x=230, y=470+20)
        self.entryframe1info=self.entryframe1.place_info()

    def builditemtable(self):
         self.entryframe.place_forget()
         self.entryframe1.place_forget()
         self.tableframe.place(self.tableframeinfo)
         self.tableframe1.place_forget()
         scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",
                                                            'Price', 'Stocks'), selectmode="extended", height=18,
                                  yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=100)
         self.tree.column('#2', stretch=NO, minwidth=0, width=150)
         self.tree.column('#3', stretch=NO, minwidth=0, width=150)
         self.tree.column('#4', stretch=NO, minwidth=0, width=100)
         self.tree.column('#5', stretch=NO, minwidth=0, width=100)
         self.tree.column('#6', stretch=NO, minwidth=0, width=100)
         self.tree.heading('Product ID', text="Product ID", anchor=W)
         self.tree.heading('Product Name', text="Product Name", anchor=W)
         self.tree.heading('Description', text="Description", anchor=W)
         self.tree.heading('Category', text="Category", anchor=W)
         self.tree.heading('Price', text="Price", anchor=W)
         self.tree.heading('Stocks', text="Stocks", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getproducts()

    def getproducts(self):
         self.cur.execute("select * from products")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
    def make_invoice(self):
        def buildprodtable(self):
         self.searchframe.place_forget()
         self.tableframe.place(self.tableframeinfo)
         self.formframe.place(self.formframeinfo)
         self.tableframe1.place_forget()
         self.formframe1.place_forget()
         self.itemframe.place_forget()
         if(self.cond==1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
         scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",
         'Price', 'Stocks'), selectmode="browse", height=18,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=100)
         self.tree.column('#2', stretch=NO, minwidth=0, width=100)
         self.tree.column('#3', stretch=NO, minwidth=0, width=150)
         self.tree.column('#4', stretch=NO, minwidth=0, width=150)
         self.tree.column('#5', stretch=NO, minwidth=0, width=100)
         self.tree.column('#6', stretch=NO, minwidth=0, width=100)
         self.tree.heading('Product ID', text="Product ID", anchor=W)
         self.tree.heading('Product Name', text="Product Name", anchor=W)
         self.tree.heading('Description', text="Description", anchor=W)
         self.tree.heading('Category', text="Category", anchor=W)
         self.tree.heading('Price', text="Price", anchor=W)
         self.tree.heading('Stocks', text="Stocks", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getproducts()
         self.tree.bind("<<TreeviewSelect>>", self.clickprodtable)
         self.formframe.focus_set()
         self.itemeditv = StringVar()
         self.itemeditdescv = StringVar()
         self.itemeditcatv = StringVar()
         self.itemeditpricev = StringVar()
         self.itemeditstockv = StringVar()
         self.addstock = StringVar()
         va = 5
         l1 = ['Product Name', 'Description', 'Category', 'Price', 'Current Stock', 'Add Stock']
         for i in range(0,6):
             Label(self.formframe, text=l1[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
             va += 60
         Entry(self.formframe, textvariable=self.itemeditv, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=0, height=40)
         Entry(self.formframe, textvariable=self.itemeditdescv, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=60, height=40)
         x=myentry(self.formframe, textvariable=self.itemeditcatv, font="roboto 14",bg="#FFFFFF", width=20)
         x.place(x=142, y=120, height=40)
         self.cur.execute("select product_cat from products")
         li = self.cur.fetchall()
         a = []
         self.desc_name = []
         for i in range(0, len(li)):
             if (a.count(li[i][0]) == 0):
                 a.append(li[i][0])
         x.set_completion_list(a)
         Entry(self.formframe, textvariable=self.itemeditpricev, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=180, height=40)
         Entry(self.formframe, textvariable=self.itemeditstockv, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=240, height=40)
         Entry(self.formframe, textvariable=self.addstock, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=300, height=40)
         Button(self.formframe, text="Update", font="robot 11 bold",bg="#FFFFFF", bd=5, width=10, height=2,
         command=self.changeprodtable).place(x=105, y=361)
         Button(self.formframe, text="Remove", font="robot 11 bold",bg="#FFFFFF", bd=5, width=10, height=2,
         command=self.delproduct).place(x=305, y=361)
         self.cond=1
         self.mainsearch(1)

    #SEARCH FRAME FOR BOTH USER AND PRODUCT TABLE
    def mainsearch(self, f):
        self.searchvar.set('')
        if (f==1):
            self.searchframe.config(width=720)
            self.searchframe.place(x=575, y=245)
            self.searchbut.config(text="Search Description",command=self.searchprod)
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar,width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select product_desc from products")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
            self.resetbut.config(command=self.resetprodtabel)
            self.resetbut.place(x=460, y=22, height=37)
        elif(f==0):
            self.searchframe.place(x=661, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchuser)
            self.searchbut.config(text="Search Username")
            self.searchbut.place(x=0,y=23)
            self.searchentry.config(width=18,textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.resetusertable)
            self.resetbut.place(x=415,y=23)
            self.cur.execute("select username from users")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
        else:
            self.searchframe.place(x=138, y=245)
            self.searchframe.config(width=520)
            self.searchbut.config(command=self.searchinvoice)
            self.searchbut.config(text="Search Invoice No.")
            self.searchbut.place(x=0, y=23)
            self.searchentry.config(width=18, textvariable=self.searchvar)
            self.searchentry.place(x=195, y=25, height=35)
            self.resetbut.config(command=self.buildsalestable)
            self.resetbut.place(x=415, y=23)
            self.cur.execute("select invoice from sales")
            li = self.cur.fetchall()
            a = []
           # print(li)
            for i in range(0, len(li)):
                if(a.count(str(li[i][0]))==0):
                    a.append(str(li[i][0]))
            self.searchentry.set_completion_list(a)

    def user_input(self):
       self.cur.execute('select max(trans_id) from sales')
       li = self.cur.fetchall()
       if(li[0][0]!=None):
        self.transid = li[0][0] + 1
       else:
           self.transid = 100
       self.qty = StringVar(value=1)
       self.additem=StringVar()
       self.total=IntVar(value=0)
       Button(self.entryframe,text="Proceed",command=self.transtableadd,bd=10,width=8,height=7,bg="#FFFFFF",font="roboto 10").place(x=0,y=30)
       Button(self.entryframe, text="Add to cart", command=self.addtotrans, bd=10, width=10, height=3,bg="#FFFFFF",font="roboto 10").place(x=100,y=80)
       Button(self.entryframe, text="Remove", command=self.removecart, bd=10, width=10, height=3, bg="#FFFFFF",font="roboto 10").place(x=210, y=80)
       entercart=mycombobox(self.entryframe,width=20,textvariable=self.additem,font="roboto 12")
       entercart.place(x=100,y=30,height=30)
       cartqty = Entry(self.entryframe,textvariable=self.qty,width=9,bg="#ffffff",font="roboto 12")
       cartqty.place(x=320,y=30,height=30)
       carttotal = Entry(self.entryframe, textvariable=self.total, width=20, state='readonly', bg="#ffffff", font="roboto 12")
       carttotal.place(x=130, y=185, height=60)
       Label(self.entryframe, text="Quantity", font="roboto 12 bold", bg="#ffffff").place(x=318,y=0)
       Label(self.entryframe, text="Search", font="roboto 12 bold", bg="#ffffff").place(x=100, y=0)
       Label(self.entryframe, text="Amount Due", font="roboto 14 bold", bg="#ffffff").place(x=0, y=205)
       self.cur.execute("select max(invoice) from sales")
       self.invoice = self.cur.fetchall()
       self.invoice = self.invoice[0][0] + 1
       Label(self.tableframe1, text="Invoice No. "+str(self.invoice), font="roboto 14 bold", bg="#ffffff").grid(row=0, column=0)
       self.cur.execute("select product_desc,product_price from products")
       li=self.cur.fetchall()
       self.inventory = []
       self.desc_price=dict()
       for i in range(0, len(li)):
           if (self.inventory.count(li[i][0]) == 0):
               self.inventory.append(li[i][0])
           self.desc_price[li[i][0]]=li[i][1]
       entercart.set_completion_list(self.inventory)
       li=['Product Id','Product Name','Price','Left Stock']
       va=0
       for i in range(0,4):
           Label(self.entryframe1, text=li[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
           va += 65
       self.cartitemid = StringVar()
       self.cartitem = StringVar()
       self.cartitemprice = StringVar()
       self.cartitemstock = StringVar()
       Entry(self.entryframe1, textvariable=self.cartitemid, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=0,height = 40)
       Entry(self.entryframe1, textvariable=self.cartitem, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=65,height=40)
       Entry(self.entryframe1, textvariable=self.cartitemprice, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*2,height=40)
       Entry(self.entryframe1, textvariable=self.cartitemstock, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*3,height=40)
       self.id_qty=dict()
       self.cur.execute("select product_id from products")
       l=self.cur.fetchall()
       for i in range(0,len(l)):
           self.id_qty[l[i][0]]=0

    def addtotrans(self):
        if(len(self.additem.get()) == 0 or self.inventory.count(self.additem.get())==0):
            messagebox.showerror("Error", "Product Not Found!")
            return
        else:
            if(not self.qty.get().isdigit()):
                messagebox.showerror('Error','Invalid quantity!')
                return
            if(int(self.qty.get()) <= 0):
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            self.cur.execute("select product_id,product_desc from products where product_desc = ? ",(self.additem.get(),))
            row = self.cur.fetchall()
            row = [list(row[0])]
            row[0].insert(0,self.transid)
            self.transid+=1
            row[0].append(int(self.qty.get()))
            row[0].append((int(self.qty.get())*self.desc_price[self.additem.get()]))
            x=str(datetime.datetime.now().strftime("%d-%m-%y"))
            row[0].append(x)
            x=datetime.datetime.now()
            x=str(x.hour)+' : '+str(x.minute)+' : '+str(x.second)
            row[0].append(x)
            row = [tuple(row[0])]
            self.cartitemid.set(row[0][1])
            self.cartitemprice.set(self.desc_price[self.additem.get()])
            self.cartitem.set(row[0][2])
            self.cur.execute("select stocks from products where product_id=?", (row[0][1],))
            li = self.cur.fetchall()
            if((li[0][0]-self.id_qty[row[0][1]])-int(self.qty.get())<0):
                if(li[0][0]!=0):
                    messagebox.showerror('Error','Product with this quantity not available!')
                else:
                    messagebox.showerror('Error', 'Product out of stock!')
                return
            self.id_qty[row[0][1]] += int(self.qty.get())
            self.cartitemstock.set(li[0][0]-self.id_qty[row[0][1]])
            for data in row:
                self.tree.insert('', 'end', values=(data))
            self.total.set(self.total.get() + (int(self.qty.get()) * self.desc_price[self.additem.get()]))
            self.qty.set('1')
            self.additem.set('')

    def transtableadd(self):
        x=self.tree.get_children()
        if(len(x) == 0):
            messagebox.showerror('Error','Empty cart!')
            return
        if (messagebox.askyesno('Alert!','Do you want to proceed?') == False):
            return
        a=[]
        self.cur.execute("select max(invoice) from sales")
        self.invoice=self.cur.fetchall()
        self.invoice=self.invoice[0][0]+1
        for i in x:
            l=self.tree.item(i)
            a.append(l['values'])
        for i in a:
            s = (str(i[5])).split('-')
            i[5] = s[2] + "-" + s[1] + "-" + s[0]
            self.cur.execute("insert into sales values (?,?,?,?,?,?)",(int(i[0]),int(self.invoice),int(i[1]),int(i[3]),i[5],i[6]))
            self.cur.execute("select stocks from products where product_id=?",(int(i[1]),))
            l=self.cur.fetchall()
            self.cur.execute("update products set stocks=? where product_id=?",(l[0][0]-self.id_qty[str(i[1])],int(i[1])))
            self.base.commit()
        messagebox.showinfo('Success','Transaction Successful!')
        self.makeprint()
        self.tree.delete(*self.tree.get_children())
        self.cartitemstock.set('')
        self.cartitem.set('')
        self.cartitemid.set('')
        self.cartitemprice.set('')
        self.total.set(0)
        self.additem.set('')
        self.qty.set('1')
        self.cur.execute("select product_id from products")
        l = self.cur.fetchall()
        for i in range(0, len(l)):
            self.id_qty[l[i][0]] = 0
        self.make_invoice()

    def removecart(self):
        re = self.tree.selection()
        if(len(re)==0):
            messagebox.showerror('Error','No cart selected')
            return
        if (messagebox.askyesno('Alert!','Remove cart?') == True):
            x = self.tree.get_children()
            re=re[0]
            l=[]
            fi=[]
            for i in x:
                if(i!=re):
                    l.append(tuple((self.tree.item(i))['values']))
                else:
                    fi=((self.tree.item(i))['values'])
            self.tree.delete(*self.tree.get_children())
            for i in l:
                self.tree.insert('', 'end', values=(i))
            self.cartitemstock.set('')
            self.cartitem.set('')
            self.cartitemid.set('')
            self.cartitemprice.set('')
            self.additem.set('')
            self.qty.set('1')
            self.id_qty[str(fi[1])]-=fi[3]
            self.total.set(self.total.get()-fi[4])
            return

    def makeprint(self):
       if messagebox.askyesno("Alert!","Print this transaction?")== True:
          pass
       ''''
           x = datetime.datetime.now()
           x = str(x.hour) + ' - ' + str(x.minute) + ' - ' + str(x.second)
           dir="E:\GUI\docs\ "
           if not os.path.exists(dir):
               os.makedirs(dir)
           shop="\t\t\t\t\t  The Bake Shop\n"
           address="\t\t\t\t Dwarka Sec-12, New Delhi\n"
           phone="\t\t\t\t     Phone-:1122334455\n"
           sample="\t\t\t\t\t   Invoice No.-:"+str(self.invoice)+"\n"
           dt="\t\t\t\t      "+x
           head="\n\n\t\t------------------------------------------------------\n"
           row="\t     Sno.\t\tProduct Name\t\tQuantity\tTotal\n"
           final=shop+address+phone+sample+dt+head+row
           file_name=str(dir)+str(x)+".rtf"
           f=open(file_name,"x")
           f.write(final)
           x=self.tree.get_children()
           for i in range(0,len(x)):
               f.write("\t     "+str(i+1)+"\t\t")
               for j in range(2,len(self.tree.item(x[i])['values'])-2):
                   f.write(str(self.tree.item(x[i])['values'][j])+"\t\t")
               f.write("\n")
           f.close()
       '''
    def clicktranstable(self,event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 7):
            self.cartitemid.set((li[1]))
            self.cartitem.set((li[2]))
            self.cur.execute("select product_price,stocks from products where product_id=?",(li[1],))
            li = self.cur.fetchall()
            self.cartitemprice.set(li[0][0])
            self.cartitemstock.set(li[0][1]-self.id_qty[self.cartitemid.get()])
