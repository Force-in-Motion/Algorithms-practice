import customtkinter as ctk
from config import *
from main import *
from tkinter.messagebox import showerror

class Error_messeges:
    """
    Класс, содержащий в себе окна ошибок  с определенным текстом. соответствующим семантике той или иной ошибки
    """
    @staticmethod
    def err_length():
        showerror(title='Ошибка', message='Расчет невозможен если в списке меньше 2 элементов')

    @staticmethod
    def err_type_start_or_end():
        showerror(title='Ошибка', message='Получен не верный тип данных, ожидалось целое число')

    @staticmethod
    def err_value_for_start_zero():
        showerror(title='Ошибка', message='Начальное значение не может быть меньше нуля')

    @staticmethod
    def err_value_for_start_or_end_empty():
        showerror(title='Ошибка', message='Передана пустая строка, введите целое число')

    @staticmethod
    def err_value_start_more_end():
        showerror(title='Ошибка', message='Начальное значение не может быть больше конечного')

    @staticmethod
    def err_value_not_isdigit():
        showerror(title='Ошибка', message='Начальное и конечное значение должны быть целыми числами')

    @staticmethod
    def err_index_start_or_end():
        showerror(title='Ошибка', message='Начальное или конечное значение не может быть больше длинны списка')


class Check_data:
    """
    Класс- обработчик полученных данных, выполняет проверки и возвращает булевое значение
    """
    @staticmethod
    def check_input_data_from_lst_entry(data):
        assert len(data) > 2, Error_messeges.err_length()

        return True

    @staticmethod
    def check_input_start_and_end(lst, start, end):
        if start == '' or end == '':
            Error_messeges.err_value_for_start_or_end_empty()
            return False

        if start < 0:
            Error_messeges.err_value_for_start_zero()
            return False

        if end < start:
            Error_messeges.err_value_start_more_end()
            return False

        if start >= len(lst) or end >= len(lst):
            Error_messeges.err_index_start_or_end()
            return False

        return True


class Main_frame(ctk.CTkFrame):
    """
    Класс- контейнер, формирует в себе поля ввода и вывода, а так же кнопку и ее обработчики
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__create_output_fields()
        self.__create_input_fields()
        self.__create_result_button()

    def __create_output_fields(self):
        """
        Формирует в себе поля вывода обработанных данных или текстовых сообщений
        """
        self.output_info = ctk.CTkLabel(self, width=600, height=70, text=tt_loi, font=ft)
        self.output_info.place(relx=0.07, rely=0.05)

        self.output_data = ctk.CTkLabel(self, width=500, height=20, fg_color=fgc,
                                          text_color='#09BBC1', text='', font=ft_out_lbl)
        self.output_data.place(relx=0.13, rely=0.23)

    def __create_input_fields(self):
        """
        Формирует в себе поля ввода данных
        """
        self.input_data_lst = ctk.CTkEntry(self, width=400, height=40, font=ft, placeholder_text=ph_lst)
        self.input_data_lst.place(relx=0.2, rely=0.33)

        self.input_data_start = ctk.CTkEntry(self, width=250, height=40, font=ft, placeholder_text=ph_start)
        self.input_data_start.place(relx=0.2, rely=0.44)

        self.input_data_end = ctk.CTkEntry(self, width=250, height=40, font=ft, placeholder_text=ph_end)
        self.input_data_end.place(relx=0.2, rely=0.55)

    def __create_result_button(self):
        """
        Создает кнопку и пренимает в ее параметры метод- обработчик клика по ней
        """
        self.result_button = ctk.CTkButton(self, width=300, height=40, border_width=1,
                                           fg_color='#008080', text=tt_btn, font=ft, hover_color=hc_btn,
                                             command=self.button_click)
        self.result_button.place(relx=0.25, rely=0.7)

    def button_click(self):
        """
        Основной метод обработки клика по кнопке, формирует данные для вывода результата пользователю, а так же некоторые проверки данных
        :return:
        """
        data = self.input_data_lst.get()
        if not Check_data.check_input_data_from_lst_entry(data):
            return

        lst = create_lst_int_from_input_data(data)
        start = self.input_data_start.get()
        end = self.input_data_end.get()

        assert start.isdigit() and end.isdigit(), Error_messeges.err_value_not_isdigit()
        start, end = convert_data(start, end)

        if not Check_data.check_input_start_and_end(lst, start, end):
            return

        result = max_in_range(lst, start, end)

        self.output_data.configure(text=f'Max elem = {result[0]}, relative_index = {result[1]}, absolute_index = {result[2]} ')



class App(ctk.CTk):
    """
    Основной мейн класс, содержащий в себе остальные контейнеры виджетов
    """
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_wigets()

    def __config_window(self):
        """
        Формирует параметры главного окна
        :return: None
        """
        self.geometry('700x500+500+100')
        self.title('max_in_range')
        self.resizable(False, False)

    def __config_wigets(self):
        """
        Добавляет главный контейнер на основное окно
        :return: None
        """
        self.main_frame = Main_frame(self, width=700, height=500, fg_color=fgc)
        self.main_frame.place(relx=0, rely=0)


class Program:
    @staticmethod
    def main():
        app = App()
        app.mainloop()

Program.main()
