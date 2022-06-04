import numpy as np
import random as rd

print("Ejercicios con Arreglos")
'''print(np.arange(4))
#arreglo = np.arange(4)
#print(arreglo)
print(np.arange(2,7))
'''
arregloA = np.ones(100,dtype = int)  # inicializar el arreglo con ceros
print(arregloA)

for i in range(len(arregloA)):
    arregloA[i] = rd.randint(0,500)
print()
print(arregloA)

#Mostrar por pantalla sólo los valores que se encuentren en los índices pares del arreglo
for i in range(len(arregloA)):
    if i%2 == 0:
        print(arregloA[i])
print()
print(arregloA[::2]) # otra forma, by Jaziel, en una linea

#Mostrar el elemento mayor del arreglo
mayor = arregloA.max()
print("El elemento Mayor es: ",mayor)

print()
print("indice mayor")
#Mostrar el índice (posición) del elemento mayor.
mayor  =0
for i in range(len(arregloA)):
    if arregloA[i] > mayor:
        mayor = arregloA[i]
        posicion = i

print("El mayor esta en la posicion arregloA[",posicion,"] = ",mayor)    
print()
#Mostrar el índice (posición) del elemento mayor.
menor  = 501
for i in range(len(arregloA)):
    if arregloA[i] < menor:
        menor = arregloA[i]

print("El menor elemento es : ",menor)

print("copia arreglo")
arregloB = arregloA.copy()
print(arregloB)
print()
print(arregloB*3)
print()
print(arregloA)
print()

print("suma de elementos del arreglo B")
suma = arregloB.sum()
print("Suma: ",suma)
print()

print("Promedio de elementos del arreglo B")
suma = arregloB.mean()
print("Promedio: ",suma)



  
