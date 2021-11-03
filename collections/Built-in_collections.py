# Colecciones incorporadas
import math

# Listas
list1 = list()
list2 = ['t', 25, 'cat', math.pi]
list3 = [number*2 for number in range(1, 100, 3)]

print(list1)
print(list2)
print(list3)

# Tuplas
# Las tuplas son inmutables, no se pueden modificar que nos ayudan a almacenar datos constantes y ahorrar memoria.

tuple1 = tuple()
tuple2 = (1274, 25, 'cat', math.pi)
tuple3 = 'mulan', 'pucca', 'percy'

print(tuple1)
print(tuple2)
print(tuple3)

# sets

set1 = set()
set2 = { 3, 5, 9, 3, 9 }
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
set3 = set(numbers)

print(set1)
print(set2)
print(set3)

# Diccionarios

cats1 = {
    "mula": 2,
    "pucca": 1,
    "percy": 3
}

cats2 = dict(cats1)

cats3 = dict(mula=2, pucca=1, percy=3)

print(cats1)
print(cats2)
print(cats3)

# Reto de casos de uso

mimetype = ('text/html', 'application/json', 'image/png')

# Ejemplo con sets

oracion1 = set('Hola, soy una oración'.split(' '))
oracion2 = set('Esta es otra oración'.split(' '))

intersections = oracion1.intersection(oracion2) # Coincide en ambos
differences = oracion1.difference(oracion2) # Tiene A pero no B
simetric_difference = oracion1.symmetric_difference(oracion2) # Tiene A pero no B o B pero no A
union = oracion1.union(oracion2) # Une ambos

print(intersections)
print(differences)
print(simetric_difference)
print(union)

# Dicccionarios y arreglos

users = [
    {
        'username': 'jose',
        'first': 'jose',
        'last': 'jimenez',
    },
    {
        'username': 'juan',
        'first': 'juan',
        'last': 'perez',
    },
    {
        'username': 'pedro',
        'first': 'pedro',
        'last': 'lopez',
    }
]

