"""
Задача 5
Вывести цифры числа на каждой строчке.

Задача 6
Найти сумму цифр числа.

Задача 7
Найти произведение цифр числа.

Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?

Задача 9
Найти максимальную цифру в числе

Задача 10
Найти количество цифр 5 в числе
"""
num = 0
digits_sum = 0
digits_product = 1
digit_five_contains = False
digit_max = 0
digit_five_quantity = 0

while True:
    num = input("Введите любое не десятичное положительное число: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Вы ввели {0}".format(num))
        print("Bвод некорректен...")

num_len = 0
num_reverse = num

print('___________________________________________')
print('Вывести все цифры числа от младших разрядов')
while num != 0:
    numeral = num % 10
    print(numeral)
    num = num // 10
    # определить количество цифр в числе
    num_len += 1
    # получить сумму цифр числа
    digits_sum += numeral
    # получить произведение цифр числа (БЕЗ УЧЁТА НУЛЕЙ)
    if numeral != 0:
        digits_product = digits_product * numeral

    if numeral == 5:
        # определить содержится ли цифра 5 в числе
        digit_five_contains = True
        # определить количество цифр 5 в числе
        digit_five_quantity += 1

    # определить максимальную цифру в числе
    if numeral >= digit_max:
        digit_max = numeral

print('___________________________________________')
print('Вывести все цифры числа от старших разрядов')
for i in range(num_len, 0, -1):
    s = 10**(i-1)
    #print(s)
    print(num_reverse//s)
    num_reverse = num_reverse % s

print('___________________________')
print('Анализ состава цифр в числе')
print('___________________________')

print("Сумма всех цифр равна: {0}".format(digits_sum))
print("Произведение всех цифр, за исключением нулей: {0}".format(digits_product))
print("Самая большая цифра в составе числа: {0}".format(digit_max))
five_in_number = "да" if digit_five_contains else "нет"
print("Наличие в составе числа цифр \"5\": {0}".format(five_in_number))
if digit_five_contains:
    print("Количество цифр \"5\" в составе числа: {0}".format(digit_five_quantity))







