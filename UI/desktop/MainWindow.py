import tkinter as tk
from UI.desktop.WindowPattern import Pattern


class Windows:
    def __init__(self):
        Pattern.BackCommand = self.ButtonBack

        self.MainPage = Pattern()
        self.ReadyMeals = Pattern()
        self.SearchWindow = Pattern()
        self.HoldFoods = Pattern()
        self.FirstFoods = Pattern()
        self.SecondFoods = Pattern()
        self.DoughFoods = Pattern()

    ############################################################################## Основое или же Главное меню
    def MainWindows(self):
        # Вызываем шаблон
        self.MainPage.WindowName = tk.Tk()
        Pattern.UpperButton = "MainPage"
        # Навзание окни и его строки
        self.MainPage.title = 'Главное меню'
        self.MainPage.labels = ['Выберите раздел']
        # Название кнопок "buttons" и их выполняемые команды "commands"
        self.MainPage.buttons = ["Готовые рецепты", "Поиск рецептов по продуктам", "Выход"]
        self.MainPage.commands = [self.Recipies, self.Search, quit]
        # Вызов настроенных строк и кнопок, а так же изменяем название кнопки "назад" на "выход"
        self.MainPage.WindowsPattern(backButton=False)

    ############################################################################## Меню готовых блюд и его Подменю
    def Recipies(self):
        if Pattern.UpperButton == 'MainPage':
            self.MainPage.WindowName.destroy()
        self.ReadyMeals.WindowName = tk.Tk()
        Pattern.UpperButton = "ReadyMeals"

        self.ReadyMeals.title = 'Меню готовых блюд'
        self.ReadyMeals.labels = ['Выберите раздел']
        self.ReadyMeals.buttons = ["Холодные закуски", "Первые блюда", "Вторые блюда", "Изделия из теста"]
        self.ReadyMeals.commands = [self.FirstPage, self.SecondPage, self.ThirdPage, self.FourthPage]
        self.ReadyMeals.WindowsPattern()

    def FirstPage(self):
        if Pattern.UpperButton == 'ReadyMeals':
            self.ReadyMeals.WindowName.destroy()
        self.HoldFoods.WindowName = tk.Tk()
        self.HoldFoods.second_window = tk.Tk()  # Вспомогательное меню, для готовых блюд
        Pattern.UpperButton = "HoldFoods"

        self.HoldFoods.title = 'Холодные закуски'
        self.HoldFoods.labels = ['Меню холодных закусок']
        self.HoldFoods.WindowsPattern(Standart=False)  # Установка не стандартных окон
        self.HoldFoods.CreateTree()

    def SecondPage(self):
        if Pattern.UpperButton == 'ReadyMeals':
            self.ReadyMeals.WindowName.destroy()
        self.FirstFoods.WindowName = tk.Tk()
        self.FirstFoods.second_window = tk.Tk()
        Pattern.UpperButton = "FirstFoods"

        self.FirstFoods.title = 'Первые блюда'
        self.FirstFoods.labels = ['Меню первых блюд']
        self.FirstFoods.buttons = []
        self.FirstFoods.commands = []
        self.FirstFoods.WindowsPattern(Standart=False)
        self.FirstFoods.CreateTree()

    def ThirdPage(self):
        if Pattern.UpperButton == 'ReadyMeals':
            self.ReadyMeals.WindowName.destroy()
        self.SecondFoods.WindowName = tk.Tk()
        self.SecondFoods.second_window = tk.Tk()
        Pattern.UpperButton = "SecondFoods"

        self.SecondFoods.title = 'Вторые блюда'
        self.SecondFoods.labels = ['Меню вторых блюд']
        self.SecondFoods.buttons = []
        self.SecondFoods.commands = []
        self.SecondFoods.WindowsPattern(Standart=False)
        self.SecondFoods.CreateTree()

    def FourthPage(self):
        if Pattern.UpperButton == 'ReadyMeals':
            self.ReadyMeals.WindowName.destroy()
        self.DoughFoods.WindowName = tk.Tk()
        self.DoughFoods.second_window = tk.Tk()
        Pattern.UpperButton = "DoughFoods"

        self.DoughFoods.title = 'Изделия из теста'
        self.DoughFoods.labels = ['Меню изделий из теста']
        self.DoughFoods.buttons = []
        self.DoughFoods.commands = []
        self.DoughFoods.WindowsPattern(Standart=False)
        self.DoughFoods.CreateTree()

    ############################################################################## Поисковик
    def Search(self):
        if Pattern.UpperButton == 'MainPage':
            self.MainPage.WindowName.destroy()
        self.SearchWindow.WindowName = tk.Tk()
        Pattern.UpperButton = "SearchWindow"

        self.SearchWindow.title = 'Поиское Окно'
        self.SearchWindow.labels = ['Поисковое меню', 'Введите название блюда или', ' доступные вам ингридиенты:']
        self.SearchWindow.buttons = []
        self.SearchWindow.commands = []
        self.SearchWindow.WindowsPattern()

    ############################################################################## Кнопка назад
    def ButtonBack(self):
        if Pattern.UpperButton == 'ReadyMeals':
            self.ReadyMeals.WindowName.destroy()
            return self.MainWindows()
        elif Pattern.UpperButton == 'SearchWindow':
            self.SearchWindow.WindowName.destroy()
            return self.MainWindows()

        elif Pattern.UpperButton == 'HoldFoods':
            self.HoldFoods.WindowName.destroy()
            self.HoldFoods.second_window.destroy()
            return self.Recipies()
        elif Pattern.UpperButton == 'FirstFoods':
            self.FirstFoods.WindowName.destroy()
            self.FirstFoods.second_window.destroy()
            return self.Recipies()
        elif Pattern.UpperButton == 'SecondFoods':
            self.SecondFoods.WindowName.destroy()
            self.SecondFoods.second_window.destroy()
            return self.Recipies()
        elif Pattern.UpperButton == 'DoughFoods':
            self.DoughFoods.WindowName.destroy()
            self.DoughFoods.second_window.destroy()
            return self.Recipies()


if __name__ == "__main__":
    start = Windows()
    start.MainWindows()
    tk.mainloop()
