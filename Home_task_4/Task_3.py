import random

k = int(input('Enter number of degree :  \n'))
dic = {a: random.randrange(-10,10) for a in range(k) }
print(dic)

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
    
with open('file1.txt', 'w') as data:
         data.write(my_str)    
     
print(my_str)
