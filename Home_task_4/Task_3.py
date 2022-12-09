import random


# def write_file(st):
#     with open('file1.txt', 'w') as data:
#         data.write(st)


def rnd():
    return random.randint(0,10)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

dic = {a: random.randrange(-10,10) for a in range(5) }
print(dic)
#ivd = {v: k for k, v in d.items()}
#dic1 = {a: k for k, a in dic.items()}
#print(dic1)
my_str = ''
i = len(dic)-1


while i != 0:
    if dic.get(i)>0:
        k = str('+')
        if dic.get(i) == 0:
            my_str += ''
        elif dic.get(i) == 1:
            my_str += f' {k} x^{i}'
        else:      
            my_str += f' {k} {abs(dic.get(i))}x^{i}'
    else:
        k = str('-')
        if dic.get(i) == 0:
            my_str += ''
        elif dic.get(i) == 1:
            my_str += f' {k} x^{i}'
        else:      
            my_str += f' {k} {abs(dic.get(i))}x^{i}'
    i-=1

my_str += f' {k} {abs(dic.get(i))} = 0'  
if my_str.startswith(' +'):    
    my_str = my_str.replace(' +','',1)
    
    
# lst = my_str.split(' ')[:-2]

# for x in range(len(lst)):
#     if lst[x] != '':
#         my_str = str(lst[x]).join(' + ')

     
print(my_str)
#print(lst)