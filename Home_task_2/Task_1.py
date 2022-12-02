num = float(input('Enter number'))
while num != int(num):
    num = num*10
sum = 0
while (num > 0):
    sum += num % 10
    num = num // 10

print(f'Sum of numbers is  {int(sum)}')