from random import randint


user_input = int(input('Введите размер списка '))
lst1 = []
lst2 = []

for i in range(user_input):
    lst1.append(randint(0, 9))

for i in range(len(lst1)):
    while i < len(lst1)/2 and user_input > len(lst1)/2:
        user_input = user_input - 1
        a = lst1[i] * lst1[user_input]
        lst2.append(a)
        i += 1

print(lst1)
print(lst2)