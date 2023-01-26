#Para comentar varias lineas en vscode presiona ctrl + k + C
#Realizar un arreglo que tenga una lista que contenera multiples opciones
# print('Adivine la palabra correcta')
# dato = input('Ingrese un dato: ')

# lista = ['hola', 'mundo', 'perrito', 'gatito', 'feliz']
# #Revisamos si la lista contiene los datos que ingresamos
# if lista.count(dato) > 0:
#     print('El dato existe ', dato)
    
# else:
#     print('El dato no existe ', dato)

#2. Realizar una calculadora que solamente sume
primero = input('Ingrese primer numero: ')
#Usamos una nueva instruccion que se llama try, esta intentara ejecutar la logica que tenemos
try:
    primero = int(primero)
except: #Esta instruccion captura el error para que nos permita ejecutar la logica dentro del except
    primero = 'chanchito feliz'
segundo = input('Ingrese segundo numero: ')
try:
    segundo = int(segundo)
except: #Esta instruccion captura el error para que nos permita ejecutar la logica dentro del except
    segundo = 'chanchito feliz'

if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste mal un dato, intente nuevamente')
else:
    print(primero + segundo)
    