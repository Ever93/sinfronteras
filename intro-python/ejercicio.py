#Realizar un arreglo que tenga una lista que contenera multiples opciones
print('Adivine la palabra correcta')
dato = input('Ingrese un dato: ')

lista = ['hola', 'mundo', 'perrito', 'gatito', 'feliz']
#Revisamos si la lista contiene los datos que ingresamos
if lista.count(dato) > 0:
    print('El dato existe ', dato)
    
else:
    print('El dato no existe ', dato)

