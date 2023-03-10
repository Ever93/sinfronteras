#Estes es un comentario y la siguiente es una condicion
#if 5 > 3:
    #print("Es mayor que tres")
    
#declaramos una variable
x = 5
y = 'chanchito feliz'

#print(x, y)

email = 'test@example.com'

#print(email)
#Para nombrar variables que no pueden cambiar su valor se nombra generalmente en mayuscula
#Tampoco se puede usar guiones para separar los nombres de la variable
#Los numeros se pueden utilizar pero despues de una letra
#Tampoco se puede usar espacio para separar nombres de la variable

#Python permite definir varias variables con diferentes datos en una sola linea
a, b, c = 1, 2, 3
#print(a, b, c)
#Se puede crear multiples variables en una sola linea

#Tambien puedo definir varias variables con el mismo dato en una sola linea
valor1 = valor2 =  valor3 = 'Prueba de variables'
#print(valor1, valor2, valor3)

#Puedo realizar concatenacion, es tomar una palabra y juntar con otra palabra
inicio = 'hogar '
final = 'feliz'
#print(inicio + final)
#Para la concatenacion se utliza el simbolo +, porque si se separa con coma python lo representa con espacio

#Tipos de datos en python
# 1. Tipos de datos string
#Un string es una palabra o una frase
#El string se puede escribir con comilla simple, tambien los string se pueden definir con comillas dobles
palabra = 'hola mundo comilla simple'
oracion = "hola mundo comilla doble"

#Tambien se puede utilizar numeros
#dentro de los numeros estan los enteros, los float y los complejos
entero = 20 #integer
conDecimales = 5.3 #float
complejo = 1j

#print(palabra, oracion, entero, complejo, conDecimales)

#listas son varios datos agrupados en una lista
lista = [1, 2, 3, 4, 5, 5]
#Manipulacion de listas
#print(lista)
#Agregar elemento a nuestra lista, utilizamos el metodo append
lista.append(5)
#print(lista)

#realizamos una copia de la lista
lista2 = lista.copy()
#print(lista2)

#Eliminar los elementos de una lista, utilizamos clear
#lista.clear()
#print(lista)
#Contar elementos dentro de una lista y ver cuantas veces se repite
#Utlizamos el metodo count
#print(lista.count(5))

#Podemos contar la cantidad de elementos que posee la lista
#print(len(lista))

#Tambien podemos acceder a los elementos de una lista
#En programacion el primer elemento de una lista se encuentra en el indice 0

#print(lista[0])
#print(lista[3])
lista3 = ['hola', 'adios', 'Buen dia', 'Buenas noches']

print(lista3[1])

#Para acceder a los elementos de una lista utilizamos el indice lo cual en programacion empieza en el indice 0

#Eliminamos elementos de una lista
#utilizamos el metodo pop, este metodo solo nos sirve para eliminar el ultimo elemento de la lista
#lista3.pop()
#print(lista3)

#Si queremos eliminar un elemento especifico de la lista usamos el metodo remove
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#lista4.remove(8)
#print(lista4)

#Ordenar la lista
lista4.reverse()
#print(lista4)

lista5 = ['hola', 'adios', 'Buen dia',]
#ordenar lista usando el metodo sort, para usar este metodo los datos deben ser del mismo tipo
lista5.sort()
#print(lista5)

#Tuplas
#print("Las tuplas utilizan parentesis() en vez de corchetes[] como el caso de las listas")
#print("las tuplas a diferencia de las listas tienen menos metodos")

tupla = ('hola', 'mundo', 'de', 'tuplas')
#print(tupla)
#print('metodo count para contar la cantida de veces que repite un dato')
#print(tupla.count('hola'))
#print('metodo index para devolver la posicion en la que encontro el dato')
#print(tupla.index('de'), 'corresponde a esta posicion contando de izquierda a derecha, desde el 0')
#print('Para acceder al primer elemento de mi tupla tengo que indicarle la posicion 0')
#print('Ejemplo')
#print(tupla[0])
#print('Las tuplas no son modificables')
#print('Para modificar los datos de una tupla debemos convertirlo a una lista')

listaDeTupla = list(tupla)
listaDeTupla.append('agregando lista')
#print(listaDeTupla)

#print('RANGOS')
rango = range(6)
#print(rango)

#print('Introduccion a Diccionarios')
#print('Los diccionarios se definen utilizando las llaves {')

diccionario = {
    "nombre": "Adalberto",
    "apellido": "Reyes Palacios",
    "usuario": "adalreyes"
}

#print(diccionario)
#print('Acceder a un valor del diccionario, usamos [] indicandole donde queremos acceder')
#print('Ejemplo')
#print(diccionario['apellido'])
#print('Tambien se puede utilizar metodos para acceder a los datos del diccionario')
#print(diccionario.get('usuario'))
#print('Tambien se puede cambiar los valores del diccionario')
diccionario['apellido'] = 'Rojas'
#print(diccionario)
#print('En los diccionarios tambien puedo utilizar la funcion de len')
#print(len(diccionario))
#print('Agregar Valores dentro del Diccionario')
diccionario["clave"] = '12345'
#print(diccionario)
#print('Eliminar datos del Diccionario')
diccionario.pop('apellido')
#print('Ejemplo de diccionario eliminando apellido')
#print(diccionario)
#print('Diccionario con contenido agregado')
diccionario["apellido"] = 'Reyes Palacios'
#print(diccionario)
#print('Tambien podemos eliminar el ultimo item agregado usando el metodo popitem')
diccionario.popitem()
#print(diccionario)
#print('Tambien podemos eliminar datos usando el metodo del')
del diccionario['nombre']
#print(diccionario)
copiadiccionario = diccionario.copy()
#print(diccionario, copiadiccionario)
#print('Podemos eliminar todo el contenido del diccionario usando el metodo clear')
diccionario.clear()
#print(diccionario)
#print('Creamos un diccionario que contenga otro diccionario, Diccionario Anidado')
personas = {
    "Perfil": {
        "nombre": "Hilario",
        "edad": "20"
    },
    "Referencia": {
        "nombre": "Aurelio",
        "edad": "32"
    }
}

#print(personas)
#print('Tipos de datos Boolean, estos pueden contener solo dos tipos de datos, verdadero o falso')
verdadero = True
falso = False


print('Control de Flujo utilizando la condional if')

