x = [int(input('Enter coordinates x ')) for i in range(2) ]
y = [int(input('Enter coordinates y ')) for i in range(2) ]
print(round(float((((x[0]+y[0])**2 + (x[1]+y[1])**2)**0.5)),2))