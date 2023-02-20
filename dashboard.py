from tkinter import*
# from PIL import Image,ImageTK

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | by Debabrata Ghosh")

        ##---Title---##
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        #--button--#
        btn_logout=Button(self.root,text="Logout", font=("times new roman",15,"bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)

root=Tk()
obj=IMS(root)
root.mainloop()