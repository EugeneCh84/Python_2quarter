import itertools


with open('file1.txt', 'r') as data:
        file1 = data.read()   

with open('file2.txt', 'r') as data:
        file2 = data.read()   



#print(file1, '\n', file2)

lst1 = file1.replace('= 0','').strip().split(' ')
lst2 = file2.replace('= 0','').strip().split(' ')


#print(lst1, '\n', lst2)



k = list()
l = list()
for i in range(len(lst1)):
    if 'x' in lst1[i]:
        k.append(int(lst1[i][:lst1[i].index('x')]))
    else:
        k.append(int(lst1[i]))
    if '^' in lst1[i]:
        l.append(int(lst1[i][lst1[i].index('^')+1:]))
    else:
        l.append(0)
#print(k,l)

m = list()
n = list()
for i in range(len(lst2)):
    if 'x' in lst2[i]:
        m.append(int(lst2[i][:lst2[i].index('x')]))
    else:
        m.append(int(lst2[i]))
    if '^' in lst2[i]:
        n.append(int(lst2[i][lst2[i].index('^')+1:]))
    else:
        n.append(0)
#print(m,n)

dic1 = dict(zip(l,k))
dic1 = dict(sorted(dic1.items(), key=lambda x: x[0]))

dic2 = dict(zip(n,m))
dic2 = dict(sorted(dic2.items(), key=lambda x: x[0]))
#print(dic1)
#print(dic2)


#com_dic = dict(itertools.zip_longest(dic1, dic2, fillvalue=))

for i in dic2:
    if i in dic1:
        dic1[i] += dic2[i]
    else:
        dic1[i] = dic2[i]



com_dic = dict(sorted(dic1.items(), key=lambda x: -x[0]))
    

#print(dic1)
#print(com_dic)

my_str = ''
i = len(com_dic) -1
while i != 0:
    if com_dic[i]>0:
        k = '+'
        if com_dic[i] == 0:
            my_str += ''
            # elif dic.get(i) == 1:
            #     my_str += f' {k}x^{i}'
        else:      
            my_str += f' {k}{com_dic[i]}x^{i}' 
    else:
        if com_dic[i] == 0:
            my_str += ''
            # elif dic.get(i) == 1:
            #     my_str += f' {k}x^{i}'
        else:      
            my_str += f' {com_dic[i]}x^{i}'
    i-=1
    
my_str += f' {k}{com_dic[i]} = 0'  

print(my_str)

with open('result.txt', 'w') as data:
        data.write(my_str)   