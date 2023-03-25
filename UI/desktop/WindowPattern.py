import tkinter as tk
from tkinter import *
from tkinter import ttk


class Pattern:
    def __init__(self):
        self.UpperButton = ''

    def WindowsPattern(self, backButton=True, Standart=True, geometry='900x500+200+100'):
        self.x, self.y = 900, 500
        self.lpad = self.x / 50  # Отступы для кнопок и лейблов
        self.mpad = self.y / 50
        self.xpad = self.x / 3.5
        self.ypad = self.y / 30
        self.WindowName.title(self.title)
        self.WindowName.geometry(geometry)
        if Standart == True:  # Если окно является стандартным, то кнопки и лейблы создаются автоматически
            self.LabelsPattern()  # создание labels
            self.ButtonsPattern(backButton)  # создание buttons

    # Создаем кнопки для стандартных окон
    def ButtonsPattern(self, backButton):
        btnname = []
        count = 1
        for i in range(len(self.buttons)):
            count += 1
            btnname.append(f'btn{count + 1}')
            btnname[i] = tk.Button(text=self.buttons[i], width=50, height=2, command=self.commands[i]).grid(
                padx=self.xpad, pady=self.ypad)
        if backButton == True:
            btn_back = tk.Button(text='Назад', width=50, height=2, command=self.BackCommand).grid(padx=self.xpad,
                                                                                                  pady=self.ypad)
            btn_back = tk.Button(text='Выйти', width=50, height=2, command=quit).grid(padx=self.xpad, pady=self.ypad)

    # Создаем лейблы для стандартных окон
    def LabelsPattern(self):
        count = 0
        lblname = []
        for j in range(len(self.labels)):
            count += 1
            lblname.append(f'lbl{count + 1}')
            lblname[j] = tk.Label(text=self.labels[j], font=25).grid(padx=self.lpad, pady=self.mpad)

    # Создаем таблицу для выбранных меню готовых блюд
    def CreateTree(self):
        self.CreateTreeWindow()
        self.people = [
            ("1", "Примерное название блюда", "ну там картошка, морковь, лук, мясо, масло", 25, 'Жарить'),
            ("4", "ывавыаыва", "Для дальнейшей работы необходимо добавить Базу Знаний.com", 42, 'Варить'),
            ("7", "ывавыаыва", "sam@email.com", 37, 'Pass'),
            ("2", "ывавыаыва", "alice@email.com", 123, 'Pass'),
            ("5", "ывавыаыва", "kate@email.com", 420, 'Pass'),
            ("8", "ывавыаыва", "ann@email.com", 840, 'Pass'),
            ("3", "ывавыаыва", "mike@email.com", 54, 'Pass'),
            ("6", "ывавыаыва", "alex@email.com", 953, 'Pass'),
            ("9", "ывавыаыва", "jess@email.com", 321, 'Pass'),
            ("10", "ывавыаыва", "tom@email.com", 42, 'Pass'),
            ("13", "ывавыаыва", "bob@email.com", 42, 'Pass'),
            ("16", "ывавыаыва", "sam@email.com", 42, 'Pass'),
            ("11", "ывавыаыва", "alice@email.com", 42, 'Pass'),
            ("14", "ывавыаыва", "kate@email.com", 42, 'Pass'),
            ("17", "ывавыаыва", "ann@email.com", 42, 'Pass'),
            ("12", "ывавыаыва", "mike@email.com", 42, 'Pass'),
            ("15", "ывавыаыва", "alex@email.com", 42, 'Pass'),
            ("18", "ывавыаыва", "jess@email.com", 42, 'Pass'),
        ]

        for j in range(len(self.labels)):
            lblname = tk.Label(text=self.labels[j], font=25).grid(row=0, column=0, padx=self.lpad, pady=self.mpad)
            lblTitle = tk.Label(text="Для выбора блюда, щелкните 2 раза по названию", font=25).grid(row=1, column=0,
                                                                                                    padx=self.lpad,
                                                                                                    pady=self.mpad)

        # определяем столбцы
        columns = ("id", "name", "ingridients", "kalCount", "metod")

        self.tree = ttk.Treeview(height=13, columns=columns, show="headings")
        self.tree.grid(row=2, column=0, sticky="nsew")

        # определяем заголовки
        self.tree.heading("id", text="ID", anchor=W)
        self.tree.heading("name", text="Название блюда", anchor=W)
        self.tree.heading("ingridients", text="Требуемые ингридиенты", anchor=W)
        self.tree.heading("kalCount", text="Каллорий", anchor=W)
        self.tree.heading("metod", text="Способ приготовления", anchor=W)

        self.tree.column("#1", stretch=NO, width=32)
        self.tree.column("#2", stretch=NO, width=150)
        self.tree.column("#3", stretch=NO, width=500)
        self.tree.column("#4", stretch=NO, width=60)
        self.tree.column("#5", stretch=NO, width=140)

        btn_back = tk.Button(text='Назад', width=50, height=2, command=self.BackCommand).grid(row=3, column=0,
                                                                                              padx=self.xpad, pady=10)
        btn_back = tk.Button(text='Выйти', width=50, height=2, command=quit).grid(padx=self.xpad, pady=10)
        self.tree.bind('<<TreeviewSelect>>', self.displaySelectedItem)
        # добавляем данные
        for person in self.people:
            self.tree.insert("", END, values=person)

        # добавляем вертикальную прокрутку
        scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=2, rowspan=5, sticky="ns")

    # Создаем вспомогательного окна для описания способа готовки, а так же списка всех необходимых ингридиентов
    def CreateTreeWindow(self):
        self.second_window.title = 'Hello'
        self.second_window.geometry('400x500+1100+100')

        self.label_name = tk.Label(self.second_window, text='Название блюда:').grid(row=0, column=0, sticky='e', padx=0,
                                                                                    pady=0)
        self.label_kalCount = tk.Label(self.second_window, text='Колличество каллорий:').grid(row=1, column=0,
                                                                                              sticky='e', padx=0,
                                                                                              pady=0)
        self.label_ingridients = tk.Label(self.second_window, text='Ингридиенты:').grid(row=2, column=0, sticky='e',
                                                                                        padx=0, pady=0)
        self.label_name = tk.Label(self.second_window, text='Способ приготовления:').grid(row=3, column=0, sticky='e',
                                                                                          padx=0, pady=0)
        self.inst_name = tk.Label(self.second_window, text='Видео обзор:').grid(row=4, column=0, sticky='e', padx=0,
                                                                                pady=0)

        self.name_input = tk.Text(self.second_window, height=1, width=30)
        self.name_input.grid(row=0, column=1, padx=0, pady=0)

        self.KalCount_input = tk.Text(self.second_window, height=1, width=30)
        self.KalCount_input.grid(row=1, column=1, padx=0, pady=0)

        self.ingridients_input = tk.Text(self.second_window, height=10, width=30)
        self.ingridients_input.grid(row=2, column=1, padx=0, pady=0)

        self.cook_input = tk.Text(self.second_window, height=10, width=30)
        self.cook_input.grid(row=3, column=1, padx=0, pady=0)

        self.textMetod = tk.Button(self.second_window, text='Посмотреть:', command=None).grid(row=4, column=1, padx=0,
                                                                                              pady=0)

    # Функция для очистки
    def displaySelectedItem(self, event):
        self.name_input.delete(0.0, END)
        self.KalCount_input.delete(0.0, END)
        self.ingridients_input.delete(0.0, END)
        self.cook_input.delete(0.0, END)

        selectedItem = self.tree.selection()[0]

        self.name_input.insert(0.0, self.tree.item(selectedItem)['values'][1])
        self.KalCount_input.insert(0.0, self.tree.item(selectedItem)['values'][3])
        self.ingridients_input.insert(0.0, self.tree.item(selectedItem)['values'][2])
        self.cook_input.insert(0.0, self.tree.item(selectedItem)['values'][4])

    # def item_selected(self, event):

    #         # вывод текстовых id всех выбранных строк
    #         # (их может быть несколько, если при создании дерева не было указано selectmode='browse')
    #         print(self.tree.selection())

    #         # Если привязывались не к событию <<TreeviewSelect>>,
    #         # то тут нужно проверить, что вообще что-то выбрано:
    #         if not self.tree.selection():
    #             return

    #         # Получаем id первого выделенного элемента
    #         selected_item = self.tree.selection()[0]

    #         # Получаем значения в выделенной строке
    #         values = self.tree.item(selected_item, option="values")
    #         print(values)

