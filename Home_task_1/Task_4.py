m = int(input('Enter number of quarter  m=   '))
if m not in range(1,5):
    print('Wrong number')
elif m == 1:
    print('x>0 and y>0')
elif m == 2:
    print('x<0 and y>0')
elif m == 3:
    print('x<0 and y<0')
else:
    print('x>0 and y<0')