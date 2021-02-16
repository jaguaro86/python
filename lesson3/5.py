# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def int_func(s, n=0):
    arr = s.split(" ")
    summa = n
    end = False
    for i in range(len(arr)):
        if arr[i].isdigit():
            summa += int(arr[i])
        else:
            end = True
            return summa, end
    return summa, end


total = 0
stop = False
while stop is False:
    user_input = input("Введите числа через пробел: ")
    total, stop = int_func(user_input, total)
    print(total)