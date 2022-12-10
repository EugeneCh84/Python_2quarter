import random


m = int(input('Enter number of degree :  \n'))
n = int(input('Enter number of degree :  \n'))

def write_f(str2,str3):
    with open('file1.txt', 'w') as data:
        data.write(str2)   
    with open('file2.txt', 'w') as data:
        data.write(str3)   

def create_dic(m):
    dic1 = {a: random.randrange(-10,10) for a in range(m) }
    return dic1



def create_str(dic):
    i = len(dic)-1
    my_str = ''
    while i != 0:
        if dic.get(i)>0:
            k = '+'
            if dic.get(i) == 0:
                my_str += ''
            # elif dic.get(i) == 1:
            #     my_str += f' {k}x^{i}'
            else:      
                my_str += f' {k}{abs(dic.get(i))}x^{i}' 
        else:
            k = '-'
            if dic.get(i) == 0:
                my_str += ''
            # elif dic.get(i) == 1:
            #     my_str += f' {k}x^{i}'
            else:      
                my_str += f' {k}{abs(dic.get(i))}x^{i}'
        i-=1
    
    my_str += f' {k}{abs(dic.get(i))} = 0'  
    # if my_str.startswith(' +'):    
    #     my_str = my_str.replace(' +','',1)
    print(dic)
    print(my_str)
    return my_str

dic2 = create_dic(m)
dic3 = create_dic(n)
write_f(create_str(dic2),create_str(dic3))
#with open('file1.txt', 'w') as data:
#    data.write(create_str(my_str))    
     
#print(my_str)

