  

rng = int(input('Enter range of list :  \n'))
my_list = []
for i in range(-rng, rng+1):
    my_list.append(i)   
print(my_list)


m = input('Enter 1 position :  \n')
n = input('Enter 2 position :  \n')
file_pos = open('file.txt', 'w')
file_pos.write(m + '\n')
file_pos.write(n)
file_pos.close
if (int(m) or int(n)) in range(len(my_list)):
        
    file_pos = open('file.txt', 'r')
    pos1 = int((file_pos.readline()))
    pos2 = int((file_pos.readline()))
    file_pos.close
    print(f'pos1 =  {pos1}    pos2 =  {pos2}'+ '\n')
    result = my_list[pos1] * my_list[pos2]
    print(f'Result :    {result}')
else:    
    print('Positions not in range')
