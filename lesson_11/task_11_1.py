# Реализовать класс «Дата».
#
# Техническое задание:
#     1. Конструктор принимает дату (параметр) в виде строки формата «день-месяц-год».
#     2. Методы:
#         1. Первый с декоратором @classmethod.
#         Извлекает число, месяц, год из строки «день-месяц-год»,
#         преобразовывает их тип к типу «Число».
#         Возвращает три числа.
#         2. Второй с декоратором @staticmethod.
#         Проводит валидацию даты (три числа)
#         (например, месяц — от 1 до 12, дней в месяце не более 31 - далее на ваш выбор).
#         Подумайте что логично возвращать валидатору?
#     3. Конструктор создает объект только если он прошел валидацию вторым методом.
#     Объект хранится в виде трех чисел отдельно или в контейнере.
#     В случае неудачи контруктор выкидывает исключение DateInitError c внятным диагностическим сообщением.
#     4. Переопределить метод __str__ для печати числа в виде 2021.12.31
#     5. Создать несколько экземпляров и распечатать их.
#     Проверить работу на не валидных данных.
#     6. Исключение от конструктора ловить в основном коде программы
#     и подменять выводом диагностического сообщения (любого).

class Date:
    def __init__(self, date: str):
        self.nums = self.extract(date)
        self.validate(self.nums, date)

    def __str__(self):
        day, month, year = self.nums
        return f'{str(year)}.{str(month).zfill(2)}.{str(day).zfill(2)}'

    @classmethod
    def extract(cls, date):
        return [int(n) for n in date.split('-')]

    @staticmethod
    def validate(nums, date):
        day, month, year = nums
        try:
            if 31 < day <= 0 or day > 31:
                raise DateInitError(f'Дата: {date}, результат: день введен некорректно')
            elif month <= 0 or month > 12:
                raise DateInitError(f'Дата: {date}, результат: месяц введен некорректно')
            elif year <= 1800 or year > 2999:
                raise DateInitError(f'Дата: {date}, результат: год введен некорректно')
            return day, month, year
        except ValueError:
            return "Ошибка: некорректная дата"

class DateInitError(Exception):

    def __init__(self, error_message):
        self._error_message = error_message

    def __str__(self):
        return self._error_message

if __name__ == "__main__":
    # Корректные даты:
    # date1 = Date("22-02-1990")
    # print(date1)
    # print(date1.extract("32-02-1990"))
    # date2 = Date("07-10-1986")
    # print(date2)
    # print(date2.extract("32-02-1990"))

    # Неправильные даты:
    date3 = Date("44-03-2021")
    # date4 = Date("05-14-1967")
    # date5 = Date("18-09-2054")
