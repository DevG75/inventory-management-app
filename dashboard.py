from tkinter import*
from PIL import Image,ImageTk

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | by Debabrata Ghosh")
        self.root.config(bg="white")
        ##---Title---##
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        #--button--#
        btn_logout=Button(self.root,text="Logout", font=("times new roman",15,"bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
        #--clock--#
        self.lbl_clock=Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white", anchor="w").place(x=0, y=70, relwidth=1, height=30)

        #---Left Menu ---#
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102, width=200, height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")

        lbl_menu=Label(LeftMenu,text="Menu", font=("times new roman",20),bg="#009688").pack(side=TOP, fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_product=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20, "bold"),bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
root=Tk()
obj=IMS(root)
root.mainloop()
