# ЗАДАЧА 4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на
# два прямоугольника).

size_g = int(input("Введите размер шоколадки по горизонтали: "))
size_v = int(input("Введите размер шоколадки по вертикали: "))
number = int(input("Введите кол-во долек: "))
size_g_v = size_g * size_v
result = size_g
while result < size_g_v:
    if number == result:
        print("yes")
        break
    print(result)
    result += size_g
else:
    print("no")