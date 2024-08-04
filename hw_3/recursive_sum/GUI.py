import customtkinter as ctk
from tkinter.messagebox import showerror
from recursive_sum.main import *
from recursive_sum.config import *


class ErrorMessage:
    """
    Класс, содержащий в себе окна ошибок  с определенным текстом. соответствующим семантике той или иной ошибки
    """
    @staticmethod
    def err_type():
        showerror(title='Ошибка', message='Получен не верный тип данных, ожидались целые числа')

    @staticmethod
    def err_empty():
        showerror(title='Ошибка', message='Получена пустая строка, введите данные')

    @staticmethod
    def err_length():
        showerror(title='Ошибка', message='Для сортировки необходимо более 2 элементов')


class MainFrame(ctk.CTkFrame):
    """
    Класс- контейнер, формирует в себе поля ввода и вывода, а так же кнопку и ее обработчики
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__input_field = None
        self.__info_output_field = None
        self.__result_output_field = None

        self.__config_input_field()
        self.__config_output_fields()
        self.__config_result_button()

    def __config_input_field(self):
        """
        Формирует в себе поля ввода данных
        """
        self.__input_field = ctk.CTkEntry(self, width=400, height=50, placeholder_text=ph_ia, font=ft, border_color=brc)
        self.__input_field.place(relx=0.20, rely=0.3)

    def __config_output_fields(self):
        """
        Формирует в себе поля вывода обработанных данных или текстовых сообщений
        """
        self.__info_output_field = ctk.CTkLabel(self, width=500, height=70, text=tt_if, font=ft, fg_color=fgc)
        self.__info_output_field.place(relx=0.14, rely=0.1)

        self.__result_output_field = ctk.CTkLabel(self, width=500, height=70, text='', font=ft, fg_color=fgc, text_color=ftc)
        self.__result_output_field.place(relx=0.14, rely=0.5)

    def __config_result_button(self):
        """
        Создает кнопку и пренимает в ее параметры метод- обработчик клика по ней
        """
        self.__result_button = ctk.CTkButton(self, width=250, height=50, font=ft_res, text=tt_rb, fg_color=fgc_rb, hover_color=hc_rb)
        self.__result_button.configure(command=self.button_click)
        self.__result_button.place(relx=0.31, rely=0.75)

    def button_click(self):
        """
        Основной метод обработки клика по кнопке, формирует данные для вывода результата пользователю, а так же некоторые проверки данных
        :return: None
        """
        input_data = self.__input_field.get()

        assert input_data != '', ErrorMessage.err_empty()

        lst_nums = create_arr_numbers(input_data)

        assert lst_nums, ErrorMessage.err_type()

        assert len(lst_nums) > 1, ErrorMessage.err_length()

        sum_elems = recursive_sum(lst_nums)

        self.__result_output_field.configure(text=f'Сумма элементов массива: {sum_elems}')


class App(ctk.CTk):
    """
    Основной мейн класс, содержащий в себе остальные контейнеры виджетов
    """
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_frame()

    def __config_window(self):
        """
        Формирует параметры главного окна
        :return: None
        """
        self.title(app_t)
        self.geometry(app_g)

    def __config_frame(self):
        """
        Добавляет главный контейнер на основное окно
        :return: None
        """
        self.__main_frame = MainFrame(self, width=700, height=500, fg_color=fgc)
        self.__main_frame.place(relx=0, rely=0)

    def run(self):
        """
        Формирует метод, запускающий приложение
        :return: None
        """
        App.mainloop(self)


if __name__ == '__main__':
    app = App()
    app.run()