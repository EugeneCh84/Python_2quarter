num = int(input('Enter number :   '))
my_list = []
for i in range(1, num+1):
    my_list.append(((1+(1/i))**i))
    
print(my_list,  end= '\n\n' )
print(f'Summ of numbers {round(sum(my_list), 3)}')