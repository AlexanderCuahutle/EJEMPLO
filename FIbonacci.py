#Realizar la serie Fibonacci

n = int (input('Ingrese un numero: '))
w1 = 1
w2 = 1
s = 0
c = 0
if n <= 0:
    print('ingrese otro numero error')
elif n == 1:
    print(w1)
else:
    while c < n:
        print(w1)
        s = w1 + w2
        #actualizar los datos
        w1 = w2
        w2 = s
        c += 1