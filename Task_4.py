"""
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
"""
factorial = 1

for i in range(1, 11, 1):
    factorial = factorial * i
    print("Step {0} ___ {1}".format(i, factorial))

print("Произведение ряда чисел от 1 до 10 будет равно {0}".format(factorial))
