# ЗАДАНИЕ 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где
# сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number_ticket = int(input("Введите номер билета: "))
if number_ticket >= 100000 and number_ticket <= 1000000:
    num1 = number_ticket % 10
    zero = number_ticket // 10
    num2 = zero % 10
    zero1 = zero // 10
    num3 = zero1 % 10
    zero2 = zero1 // 10
    num4 = zero2 % 10
    zero3 = zero2 // 10
    num5 = zero3 % 10
    zero4 = zero3 // 10
    num6 = zero4 % 10
    result1 = num1 + num2 + num3
    result2 = num4 + num5 + num6
    print(result1)
    print(result2)
    print(zero)
    if result1 == result2:
        print("yes")
    else:
        print("no")
else:
    print("Введите 6-ти значное число")