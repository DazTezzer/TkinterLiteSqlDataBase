from tkinter import *
import os
import ctypes
import pathlib




ctypes.windll.shcore.SetProcessDpiAwareness(True)

class ExApp():
    def __init__(self):
        self.path = ""
        self.root = Tk()
        self.root.title('Simple Explorer')
        self.root.geometry('400x400')

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.newFileName = StringVar(self.root, "File.dot", 'new_name')
        self.currentPath = StringVar(
            self.root,
            name='currentPath',
            value=pathlib.Path.cwd()
        )

        self.currentPath.trace('w', self.pathChange)

        Button(self.root, text='Folder Up', command=self.goBack).grid(
            sticky='NSEW', column=0, row=0
        )

        self.root.bind("<Alt-Up>", self.goBack)
        Entry(self.root, textvariable=self.currentPath).grid(
            sticky='NSEW', column=1, row=0, ipady=10, ipadx=10
        )

        self.list = Listbox(self.root)
        self.list.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)

        self.list.bind('<Double-1>', self.changePathByClick)
        self.list.bind('<Return>', self.changePathByClick)

        self.menubar = Menu(self.root)

        self.root.config(menu=self.menubar)

        self.pathChange('')

        self.root.mainloop()

    def pathget(self):
        return(self.path)

    def pathChange(self,*event):
        directory = os.listdir(self.currentPath.get())
        self.list.delete(0, END)
        for file in directory:
            self.list.insert(0, file)

    def changePathByClick(self,event=None):
        picked = self.list.get(self.list.curselection()[0])
        self.path = os.path.join(self.currentPath.get(), picked)
        if os.path.isfile(self.path):
            print('Opening: ' + self.path)
            self.root.quit()
            self.root.destroy()
        else:
            self.currentPath.set(self.path)

    def goBack(self,event=None):
        newPath = pathlib.Path(self.currentPath.get()).parent
        self.currentPath.set(newPath)
        print('Going Back')








