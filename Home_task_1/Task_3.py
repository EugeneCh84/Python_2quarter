print('Enter 2 numbers in range 1 - 100')
x = int(input('x=  '))
y = int(input('y=  '))
if x == 0 and y == 0:
    print('Numbers not in range(Zero point)')
elif x > 0 and y > 0:
    print('1 quarter')
elif x >0 and y < 0:
    print('4 quarter')
elif x < 0 and y <0:
    print('3 quarter')
else:
    print('2 quarter')
