# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))


def result(a, b):
    if (b == 1):
        return (a)
    elif (b != 1):
        return (a * (result(a, b - 1)))


print(f'Число A в степени B равно - {result(a,b)}')
