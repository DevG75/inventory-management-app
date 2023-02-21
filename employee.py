from tkinter import*
from PIL import Image,ImageTk

class employeeClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("Inventory Management System | by Debabrata Ghosh")
        self.root.config(bg="white")


if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()
