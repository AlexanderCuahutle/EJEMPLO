#Serie A B A B A B A B A B

#w = interruptor
n = int(input('ingrese un numero: '))
w = 0

for i in range (1,n+1):
    if w == 0:
        print('A', end = ', ')
        w = 1
    else:
        print('B', end = ', ')
        w = 0