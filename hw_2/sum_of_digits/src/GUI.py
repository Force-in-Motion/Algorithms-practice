import customtkinter as ctk
from main import *
from config import *
from tkinter.messagebox import showerror

class Error_message:
    """
    Класс, содержащий в себе окна ошибок  с определенным текстом. соответствующим семантике той или иной ошибки
    """

    @staticmethod
    def err_empty_data():
        showerror(title='Ошибка', message='Получена пустая строка, введите данные')

    @staticmethod
    def err_type():
        showerror(title='Ошибка', message='Получен не верный тип данных, ожидались целые числа')


class Main_frame(ctk.CTkFrame):
    """
    Класс- контейнер, формирует в себе поля ввода и вывода, а так же кнопку и ее обработчики
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__config_input_field()
        self.__config_output_fields()
        self.__config_result_button()

    def __config_input_field(self):
        """
        Формирует в себе поля ввода данных
        """
        self.__input_field = ctk.CTkEntry(self, width=500, height=70, placeholder_text=ph_ia, font=ft)
        self.__input_field.place(relx=0.15, rely=0.3)

    def __config_output_fields(self):
        """
        Формирует в себе поля вывода обработанных данных или текстовых сообщений
        """
        self.__info_output_field = ctk.CTkLabel(self, width=600, height=70, fg_color=fgc, text=tt_if, font=ft)
        self.__info_output_field.place(relx=0.07, rely=0.1)
        self.__result_output_field = ctk.CTkLabel(self, width=500, height=70, text='', font=ft_res, fg_color=fgc)
        self.__result_output_field.place(relx=0.15, rely=0.5)

    def __config_result_button(self):
        """
        Создает кнопку и пренимает в ее параметры метод- обработчик клика по ней
        """
        self.__result_button = ctk.CTkButton(self, width=300, height=50, fg_color=fgc_rb, hover_color=hc_rb, text=tt_rb, font=ft)
        self.__result_button.configure(command=self.button_click)
        self.__result_button.place(relx=0.28, rely=0.8)

    def button_click(self):
        """
        Основной метод обработки клика по кнопке, формирует данные для вывода результата пользователю, а так же некоторые проверки данных
        :return:
        """
        input_data = self.__input_field.get()

        assert len(input_data) > 0, Error_message.err_empty_data()

        number = create_number(input_data)

        if not number:
            Error_message.err_type()
            return

        lst_nums = create_arr_nums(number)

        result_lst = reversed_elems_arr(lst_nums)

        self.__result_output_field.configure(text=result_lst)


class App(ctk.CTk):
    """
    Основной мейн класс, содержащий в себе остальные контейнеры виджетов
    """
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_main_frame()

    def __config_window(self):
        """
        Формирует параметры главного окна
        :return: None
        """
        self.title(app_t)
        self.geometry(app_g)
        self.resizable(False, False)

    def __config_main_frame(self):
        """
        Добавляет главный контейнер на основное окно
        :return: None
        """
        self.__main_frame = Main_frame(self, width=700, height=500, fg_color=fgc)
        self.__main_frame.place(relx=0, rely=0)




class Program:
    @staticmethod
    def main():
        app = App()
        app.mainloop()

Program.main()

