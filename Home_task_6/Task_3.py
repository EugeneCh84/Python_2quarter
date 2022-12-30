# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.


num = int(input('Enter number :   '))

lst = [round((1+1/i)**i, 3) for i in range(1, num+1)]
print(f'Последовательность: {lst}\n Сумма: {round(sum(lst), 3)}')
