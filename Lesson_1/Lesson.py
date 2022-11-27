# 1 task   

# a = int(input('Enter number 1     '))
# b = int(input('Enter number 2      '))
# if a**2 == b:
#     print('a is a square of b')
# elif b**2 == a:
#     print('b is square of a')
# else:
#     print('no squares')


# 2 task   Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# nums = [int(i) for i in input().split()]
# max = nums[0]
# for i in range(1,len(nums)):
#     if nums[i] > max:
#         max = nums[i]
# print(max)



# 3 task     Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# print('Enter n')
# n = int(input())
# for i in range(-n,n+1):
#     print(i,end= ' ') 

#     another variant

# n = int(input())
# nums = [int(i) for i in range(-n, n+1)]
# print(*nums, sep = ', ')


# 4 task        Напишите программу, которая будет принимать на вход дробь и 
#               показывать первую цифру дробной части числа.

# num = float(input())
# print(int(num * 10 %10)) 

#    another variant   string metod
# num = input()
# for i in range(0,len(num)):
#     if num[i] == ".":
#         print(num[i+1])
#         break




#  5 task        Напишите программу, которая принимает на вход число и проверяет, 
#                 кратно ли оно 5 и 10 или 15, но не 30.


num = int(input())
print((num%5 == 0 and num%10 or num%15 ==0) and not num%30 ==0)



