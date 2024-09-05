class NegativeNumberError(Exception):
    def __init__(self, num, message="Число должно быть положительным"):
        self.num = num
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.num}"

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    return

try:
    check_positive_number(-1)
    print("тест 1 пройден")
except NegativeNumberError as nne:
    print(f'тест 1 не пройден {nne}')    
    
try:
    check_positive_number(1)
    print("тест 2 пройден")
except NegativeNumberError as nne:
    print(f'тест 2 не пройден {nne}')     


# Упражнение 3: Написать класс собственного исключения и использовать его в примере кода:

# Задание: Создать класс NegativeNumberError, который будет генерироваться, если переданное число отрицательное. Использовать это исключение в функции check_positive_number.

# Пошаговая инструкция:
# •	Создайте класс NegativeNumberError, наследующий от Exception.
# •	Переопределите конструктор, чтобы принимать значение числа и сообщение об ошибке.
# •	Переопределите метод __str__, чтобы возвращать информативное сообщение.
# •	Создайте функцию check_positive_number, которая проверяет, является ли число положительным. Если число отрицательное, функция должна вызывать исключение NegativeNumberError.

# Проверка:
# •	Протестируйте функцию с отрицательным числом.
# •	Протестируйте функцию с положительным числом.
# •	Убедитесь, что исключение NegativeNumberError правильно обрабатывается и выводит информативное сообщение.    