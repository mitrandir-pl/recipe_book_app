import tkinter as tk 
from tkinter import *
from tkinter import ttk 


root = Tk()
frame = tk.Frame(root)


data = [
        [1,"AAA","BBB","ab@mail.com",17],
        [3,"EEE","FFF","ef@mail.com",91],
        [4,"GGG","HHH","gh@mail.com",47],
        [7,"MMM","NNN","mn@mail.com",25],
        [8,"PPP","QQQ","pq@mail.com",43],
        [9,"RRR","SSS","rs@mail.com",94],
       ]


label_fname = tk.Label(frame, text='Название блюда:')
entry_fname = tk.Entry(frame)

label_lname = tk.Label(frame, text='Ингридиенты:')
entry_lname = tk.Entry(frame)

label_email = tk.Label(frame, text='Колличество каллорий:')
entry_email = tk.Entry(frame)

label_age = tk.Label(frame, text='Способ приготовления:')
entry_age = tk.Entry(frame)



trv = ttk.Treeview(frame, columns=(1,2,3,4,5), show='headings')
trv.column(1, anchor='center', width=100)
trv.column(2, anchor='center', width=100)
trv.column(3, anchor='center', width=100)
trv.column(4, anchor='center', width=100)
trv.column(5, anchor='center', width=100)

trv.heading(1, text='ID')
trv.heading(2, text='First Name')
trv.heading(3, text='Last Name')
trv.heading(4, text='Email')
trv.heading(5, text='Age')

# create a function to display data in treeview
def displayData():
    for row in data:
        trv.insert('',END, values=row)


displayData()


# create a function to display the selected row from treeview
def displaySelectedItem(a):

    # clear entries
    entry_fname.delete(0,END)
    entry_lname.delete(0,END)
    entry_email.delete(0,END)
    entry_age.delete(0,END)

    selectedItem = trv.selection()[0]
    # entry_id.insert(0, trv.item(selectedItem)['values'][0])
    entry_fname.insert(0, trv.item(selectedItem)['values'][1])
    entry_lname.insert(0, trv.item(selectedItem)['values'][2])
    entry_email.insert(0, trv.item(selectedItem)['values'][3])
    entry_age.insert(0, trv.item(selectedItem)['values'][4])


trv.bind("<<TreeviewSelect>>", displaySelectedItem)


frame.grid(row=0, column=0)



trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

label_fname.grid(row=0, column=0, sticky='e')
entry_fname.grid(row=0, column=1)

label_lname.grid(row=2, column=0, sticky='e')
entry_lname.grid(row=2, column=1)

label_email.grid(row=3, column=0, sticky='e')
entry_email.grid(row=3, column=1)

label_age.grid(row=4, column=0, sticky='e')
entry_age.grid(row=4, column=1)

tk.mainloop()
# from tkinter import *
# from tkinter import ttk
 
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("900x450") 
# root.rowconfigure(index=0, weight=1)
# root.columnconfigure(index=0, weight=1)
 
# # определяем данные для отображения
# # people = [
# #     ("1", "ывавыаыва", "tom@email.com", 42, 'Pass'), ("4", "ывавыаыва", "bob@email.com", 42, 'Pass'), ("7", "ывавыаыва", "sam@email.com", 42, 'Pass'),
# #     ("2", "ывавыаыва", "alice@email.com", 42, 'Pass'), ("5", "ывавыаыва", "kate@email.com", 42, 'Pass'), ("8", "ывавыаыва", "ann@email.com", 42, 'Pass'),
# #     ("3", "ывавыаыва", "mike@email.com", 42, 'Pass'), ("6", "ывавыаыва", "alex@email.com", 42, 'Pass'), ("9", "ывавыаыва", "jess@email.com", 42, 'Pass'),
# #     ]
 
# # определяем столбцы
# columns = ("id", "name", "ingridients", "kalCount", "metod")
 
# tree = ttk.Treeview(columns=columns, show="headings")
# tree.grid(row=0, column=0, sticky="nsew")
 
# # определяем заголовки
# tree.heading("id", text="ID", anchor=W)
# tree.heading("name", text="Название блюда", anchor=W)
# tree.heading("ingridients", text="Требуемые ингридиенты", anchor=W)
# tree.heading("kalCount", text="Каллорий", anchor=W)
# tree.heading("metod", text="Способ приготовления", anchor=W)

 
# tree.column("#1", stretch=NO, width=32)
# tree.column("#2", stretch=NO, width=150)
# tree.column("#3", stretch=NO, width=500)
# tree.column("#4", stretch=NO, width=100)
# tree.column("#5", stretch=NO, width=100)

# tree.bind('<<TreeviewSelect>>')
# # добавляем данные
# # for person in people:
# #     tree.insert("", END, values=person)
 
# # добавляем вертикальную прокрутку
# scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky="ns")

# def he():
#     print('hello')

# root.mainloop()

# # import tkinter as tk
# # from tkinter import *


# # def WindowsPattern():
# #     WindowName = tk.Tk()
# #     x, y = 900, 550
# #     xpad = 0
# #     ypad = 0
    
# #     WindowName.title('test')
# #     WindowName.geometry(f'{x}x{y}')
# #     btnname = []
# #     count = 0
# #     scroll = tk.Sc
# #     lblname = tk.Label(text= 'text', font= 25).grid(row = 0, column=1)
# #     for i in range(10):
# #         count += 1
# #         btnname.append(f'btn{count + 1}')
# #         lblname = tk.Label(text= 'text', font= 25).grid(pady=ypad,row = i+1, column=0)
# #         lblname = tk.Label(text= 'text', font= 25).grid(pady=ypad,row = i+1, column=1)
# #         btnname[i] = tk.Button(text= "способ приготовления",height=2, command= None).grid(pady=ypad,row = i+1, column=2)
# #         btn_back = tk.Button(text='Назад', width=50, height=2, command=None).grid(pady=ypad + 15, row = 11, column=2)

# #         btnname[i] = tk.Button(text= count + 10, width=50, height=2, command= None).grid(pady=ypad,row = i+1, column=3)
# #         btn_back = tk.Button(text='Главное меню', width=50, height=2, command=None).grid(pady=ypad + 15, row = 11, column=3)


# # if __name__ == '__main__':
# #     WindowsPattern()
# #     tk.mainloop()
