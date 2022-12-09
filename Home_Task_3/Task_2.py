import random


def User_input_rnd(k):
    lst=[]
    for i in range(k):
        lst.append(random.uniform(0, 10))  
    return lst


b = int(input('Enter length of list =   '))
lst1 = User_input_rnd(b)
lst2 = [i%1 for i in lst1]
print(lst1)
print(round((max(lst2) - min(lst2)),2))