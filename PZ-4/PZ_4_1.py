#Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
#X - X3/3 + X5/5 - ... + (-1)NX2N +1/(2N +1). Полученное число является приближенным
#значением функции arctg в точке X.

try:
    X = float(input("Введите вещественное число X (где |X| < 1): "))
    #Ввод числа X
    if X >= 1 or X <= -1:
    #Проверка условия
       raise ValueError("Число X должно быть в пределах (-1, 1)")
    #Ошибка если число не соответсвует условию
    N = int(input("Введите целое число N (> 0): "))
    #Ввод числа N
    if N <= 0:
        #Проверка условия
        raise ValueError("Число N должно быть больше 0")
    #Ошибка если число не соответвует условию

    a = 0
    #Присваевываем переменной a значение 0 для начала вычислений
    for n in range(N):
        b = ((-1) ** n) * (X ** (2 * n + 1)) / (2 * n + 1)
        a += b

    print(f"Приближенное значение arctg({X}) = {a}")
    #Вывод приближенного значения arctg
except ValueError as c:
    print(f"Ошибка ввода:{c}")
    #Ошибка ввода
