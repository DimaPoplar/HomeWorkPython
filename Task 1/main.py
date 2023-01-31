# ЗАДАЧА 1. Найдите сумму цифр трехзначного числа.
number = int(input("Введите 3х значное число: "))
result = number % 10 + (number//10) % 10 + number//100
print(result)
