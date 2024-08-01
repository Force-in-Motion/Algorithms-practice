import customtkinter as ctk
from tkinter.messagebox import showerror
from main import *
from config import *


class Error_message:
    """
    Класс, содержащий в себе окна ошибок  с определенным текстом. соответствующим семантике той или иной ошибки
    """
    @staticmethod
    def err_length_arr():
        showerror(title='Ошибка', message='Расчет невозможен если передано меньше 2 элементов списка')
        return False

    @staticmethod
    def err_type():
        showerror(title='Ошибка', message='Получен не верный тип данных, ожидались целые числа')

    @staticmethod
    def err_value():
        showerror(title='Ошибка', message='В поле k передана пустая строка, или не целое число')
        return False

    @staticmethod
    def err_index():
        showerror(title='Ошибка', message='Число k не может иметь индекс меньше 1 и больше количества элементов переданной строки чисел')
        return False


class Check_data:
    """
    Класс- обработчик полученных данных, выполняет проверки и возвращает булевое значение
    """
    @staticmethod
    def check_input_data_entry_from_lst(lst):
        if len(lst) < 2: Error_message.err_length_arr()

        return True

    @staticmethod
    def check_input_data_entry_from_k_elem(lst, k):
        if k == '':
            Error_message.err_value()
            return False

        if k <= 0 or k > len(lst):
            Error_message.err_index()
            return False

        return True


class Main_frame(ctk.CTkFrame):
    """
    Класс- контейнер, формирует в себе поля ввода и вывода, а так же кнопку и ее обработчики
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__config_result_button()
        self.__config_input_fields()
        self.__config_output_fields()

    def __config_output_fields(self):
        """
        Формирует в себе поля вывода обработанных данных или текстовых сообщений
        """
        self.__info_field = ctk.CTkLabel(self, width=600, height=80, fg_color=fgc, font=ft, text=tt_if)
        self.__info_field.place(relx=0.07, rely=0.05)
        self.__result_label = ctk.CTkLabel(self, width=500, height=50, fg_color=fgc, text='', font=ft_res)
        self.__result_label.place(relx=0.14, rely=0.6)

    def __config_input_fields(self):
        """
        Формирует в себе поля ввода данных
        """
        self.__input_arr = ctk.CTkEntry(self, width=500, height=50, placeholder_text=ph_ia, font=ft, )
        self.__input_arr.place(relx=0.14, rely=0.25)

        self.__input_k = ctk.CTkEntry(self, width=500, height=50, placeholder_text=ph_ik, font=ft)
        self.__input_k.place(relx=0.14, rely=0.4)

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
        entered_arr = self.__input_arr.get()
        entered_k = self.__input_k.get()

        if not Check_data.check_input_data_entry_from_lst(entered_arr):
            return

        arr_numbers = create_lst_int_from_input_data(entered_arr)

        if not arr_numbers:
            Error_message.err_type()
            return

        assert entered_k.isdigit(), Error_message.err_value()

        int_k = convert_data(entered_k)

        if not Check_data.check_input_data_entry_from_k_elem(arr_numbers, int_k):
            return

        int_k = convert_data(entered_k)

        arr_numbers = create_lst_int_from_input_data(entered_arr)

        result_arr = revert_array(arr_numbers, int_k)

        self.__result_label.configure(text=result_arr)


class App(ctk.CTk):
    """
    Основной мейн класс, содержащий в себе остальные контейнеры виджетов
    """
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__create_main_frame()

    def __config_window(self):
        """
        Формирует параметры главного окна
        :return: None
        """
        self.title(app_t)
        self.geometry(app_g)
        self.resizable(False, False)

    def __create_main_frame(self):
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