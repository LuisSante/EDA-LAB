from mtree_ import MTree
import pandas as pd
import math

def d_int(x,y):
    return abs(x-y)

'''2. Inserta conjunto de puntos proporcionado en la tabla 1 en el M-Tree y mostrar gráficamente el estado del árbol después de
insertar:
a) El quinto elemento de la tabla(North Macedonia)
b) El décimo elemento de la tabla(Gibraltar)
c) El último elemento de la tabla(USA)

North Macedonia 103485 3639
Gibraltar 215221 2910
USA 148104 2406

>>> como ya sabemos los valores de cada lugar 
    procedemos a insertarlo
'''
def three_pair():
    tree = MTree(d_int, max_node_size=3)
    tree.add_all([103485,3639])
    tree.add_all([215221,2910])
    tree.add_all([148104,2406])
    print(list(tree.search(103485)))
    print(list(tree.search(2910,2)))
    print(list(tree.search(3639,3)))
    print(list(tree.search(103485,4)))
print(" ##################### Ejercicio 2 #####################")
three_pair()

'''3. Dada una distancia de 37000, cuantos y cuales son los países más próximos a Perú (mostrar la búsqueda ejecutada y el
resultado en el lenguaje de programación escogido)'''

A = []
dataset = pd.read_csv('tabla1.csv')
nombres = dataset.iloc[:, [1]].values
x = dataset.iloc[:, [2]].values
y = dataset.iloc[:, [3]].values
print("\n")
print(" ##################### Ejercicio 3 #####################")
print(" Lenguaje de Programacion Python")
euclid = []
for i in range(1,20,1):
    distance = math.sqrt((x[0] - x[i]) ** 2 + (y[0] - y[i]) ** 2)
    euclid.append(distance)

cont = 0
for i in range(len(euclid)):
    if(euclid[i] <= 37000):
        cont+=1
        print(euclid[i],nombres[i+1])
print("Paises mas cercanos a Peru: ",cont)
    

'''4. Cual es el país más próximo de Hungary. (mostrar la búsqueda ejecutada y el resultado en el lenguaje de programación
escogido)'''

A = []
dataset = pd.read_csv('tabla1.csv')
nombres = dataset.iloc[:, [1]].values
x = dataset.iloc[:, [2]].values
y = dataset.iloc[:, [3]].values
print("\n")
print(" ##################### Ejercicio 4 #####################")
print(" Lenguaje de Programacion Python")
euclid = []
menor = 1000000000000000
j = 0
for i in range(20):
    distance = math.sqrt((x[5] - x[i]) ** 2 + (y[5] - y[i]) ** 2)
    if(distance < menor and distance != 0):
        menor = distance
        j=i
print(menor,nombres[j])
    
'''6. Utilice el conjunto de datos proporcionado en la tabla 2 para determinar si existe influencia del orden de inserción de los
datos en el resultado de la búsquedas en términos de los nodos recorridos para generar la respuesta.'''

'''def main():
    tree = MTree(d_int, max_node_size=4)
    tree.add(1)
    tree.add_all([5, 9])
    print(list(tree.search(10)))
    print(list(tree.search(9,2)))
print("Ejerccio")
main()'''
