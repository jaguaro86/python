# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# def my_func(x, y):
#     x = int(x)
#     y = abs(int(y))
#     z = 1 / (x ** y)
#     return z


def my_func(x, y):
    n = int(x)
    m = abs(int(y))
    m -= 1
    for i in range(m):
        x = int(x) * n
    x = 1 / x
    return x


a = input("Введите число: ")
b = input("Введите степень: ")

print(my_func(a, b))