#Дано целое число, больше 999.
#Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру,
#соответствующую разряду сотен в записи этого числа.
a = int(input("Введите целое число больше 999:"))
if a > 999:
  b = a // 100
  c = b % 10
  print("Цифра соответствующая разряду сотен:",c)
else:
  print("Число должно быть больше 999!")
