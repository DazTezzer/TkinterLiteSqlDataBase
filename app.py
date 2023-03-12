from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import SqlList

class main_form():
    def __init__(self):
        form = Tk()
        form.geometry('1080x400')
        form.title("База данных магазина")
        tabControl = ttk.Notebook(form)
        self.tab1 = ttk.Frame(tabControl)
        self.tab2 = ttk.Frame(tabControl)
        self.tab2 = ttk.Frame(tabControl)
        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Товары')
        self.Products()
        tabControl.add(self.tab2, text='Клиенты')
        self.Clients()
        tabControl.add(self.tab3, text='Продажи')
        tabControl.pack(expand=1, fill="both")

        form.mainloop()


    def Products(self):
        img = Image.open('dog.png')
        img = img.resize((250, 250))
        tkimage = ImageTk.PhotoImage(img)
        self.PPhoto = ttk.Label(self.tab1, image=tkimage).grid(column = 0, row = 0,padx = 30,pady = 30)
        self.PName = ttk.Label(self.tab1,text = "Название товара").grid(column = 0, row = 1,padx = 30,pady = 30)
        self.PNum = ttk.Label(self.tab1, text="Количество").grid(column=0, row=2, padx=30, pady=30)
        self.PPrice = ttk.Label(self.tab1, text="Цена").grid(column=0, row=3, padx=30, pady=30)

        self.PName_entry = ttk.Entry(self.tab1)
        self.PName_entry.insert(0, "Введите название товара")
        self.PName_entry.grid(column=1, row=1, padx=30, pady=30, ipadx= 30)


        self.PNum_entry = ttk.Entry(self.tab1)
        self.PNum_entry.insert(0, "Введите количество")
        self.PNum_entry.grid(column=1, row=2, padx=30, pady=30, ipadx= 30)

        self.PPrice_entry = ttk.Entry(self.tab1)
        self.PPrice_entry.insert(0, "Введите цену")
        self.PPrice_entry.grid(column=1, row=3, padx=30, pady=30, ipadx=30)


        self.PNew_but = ttk.Button(self.tab1,text="Добавить", command=lambda: self.Add_Click(SqlList.P_In_sql,self.PData())).grid(column=0, row=4, padx=30, pady=30)
        self.PChange_but = ttk.Button(self.tab1, text="Изменить", command=lambda: self.Change_Click(SqlList.P_Ch_sql, self.PData())).grid(column=1, row=4, padx=30, pady=30)
        self.PDel_but = ttk.Button(self.tab1, text="Удалить", command=lambda: self.Del_Click(SqlList.P_Del_sql)).grid(column=2, row=4, padx=30, pady=30)
        columns = ("Id","PName", "PNum", "PPrice")
        self.tree = ttk.Treeview(self.tab1,columns=columns, show="headings")
        self.tree.place(x = 400, y = 30)
        self.tree.heading("Id", text="Id")
        self.tree.heading("PName", text="Название")
        self.tree.heading("PNum", text="Количество")
        self.tree.heading("PPrice", text="Цена")
        self.tree["displaycolumns"] = ("1","2","3")
        self.tree.bind("<ButtonRelease-1>", self.TextIn)
        self.Tableload(SqlList.PTableGet())

    def Clients(self):
        self.CName = ttk.Label(self.tab2,text = "ФИО").grid(column = 0, row = 0,padx = 30,pady = 30)
        self.CTel = ttk.Label(self.tab2, text="Телефон").grid(column=0, row=1, padx=30, pady=30)
        self.CCode= ttk.Label(self.tab2, text="Код").grid(column=0, row=2, padx=30, pady=30)

        self.CName_entry = ttk.Entry(self.tab2)
        self.CName_entry.insert(0, "Введите ФИО")
        self.CName_entry.grid(column=1, row=0, padx=30, pady=30, ipadx= 30)


        self.CTel_entry = ttk.Entry(self.tab2)
        self.CTel_entry.insert(0, "Введите телефон")
        self.CTel_entry.grid(column=1, row=1, padx=30, pady=30, ipadx= 30)

        self.CCode_entry = ttk.Entry(self.tab2)
        self.CCode_entry.insert(0, "Введите код")
        self.CCode_entry.grid(column=1, row=2, padx=30, pady=30, ipadx=30)

        self.CNew_but = ttk.Button(self.tab2,text="Добавить", command=self).grid(column=0, row=3, padx=30, pady=30)
        self.CChange_but = ttk.Button(self.tab2, text="Изменить", command=self).grid(column=1, row=3, padx=30, pady=30)
        self.CDel_but = ttk.Button(self.tab2, text="Удалить", command=self).grid(column=2, row=3, padx=30, pady=30)


    def TextIn(self, id):
        selected = self.tree.selection()[0]
        values = self.tree.item(selected, option="values")
        self.PName_entry.delete(0, 'end')
        self.PName_entry.insert(0, str(values[1]))
        self.PNum_entry.delete(0, 'end')
        self.PNum_entry.insert(0, str(values[2]))
        self.PPrice_entry.delete(0, 'end')
        self.PPrice_entry.insert(0, str(values[3]))


    def PData(self):
        data = [(self.PName_entry.get(), self.PNum_entry.get(), self.PPrice_entry.get())]
        return data


    def Tableload(self,table):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in table:
            self.tree.insert("",END ,values=row)

    def Add_Click(self,sql,Data):
        SqlList.Add(sql,Data)
        self.Tableload(SqlList.PTableGet())

    def Del_Click(self,sql):
        selected = self.tree.selection()[0]
        values = self.tree.item(selected, option="values")
        SqlList.Del(sql + str(values[0]))
        self.Tableload(SqlList.PTableGet())

    def Change_Click(self,sql,Data):
        selected = self.tree.selection()[0]
        values = self.tree.item(selected, option="values")
        SqlList.Change(sql,(Data[0] + tuple(values[0])))
        self.Tableload(SqlList.PTableGet())

