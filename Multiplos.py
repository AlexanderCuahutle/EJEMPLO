'''#Generar los miltiplos de 3
#m = interrumtor multiplo
n = int(input('Ingrese un numero: '))
m = 3
for i in range (1,n+1):
    print(m,end = ', ')
    m = m + 3
'''
#Serie 4,3,2,1,4,3,2....
#c = controlador
#w = interruptor
n = int(input('ingrese un numero: '))
c = 0
w = 4
while c < n:
    print(w, end = ', ')
    if w > 1:
        w = w - 1
    else:
        w = 4
    c = c + 1