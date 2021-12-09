from mtree_ import MTree
import pandas as pd

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

# Importar el dataset
A = []
dataset = pd.read_csv('tabla1.csv')
punto = dataset.iloc[:, [2,3]].values
print(" ##################### Ejercicio 3 #####################")
print(" Lenguaje de Programacion Python")
for x in punto:
    tree = MTree(d_int, max_node_size=20)
    tree.add_all(x)
    print(list(tree.search(103485)))

'''4. Cual es el país más próximo de Hungary. (mostrar la búsqueda ejecutada y el resultado en el lenguaje de programación
escogido)'''

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
