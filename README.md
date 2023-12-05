# Práctica 1
## Algoritmos de búsqueda.

### El siguiente mapa, representa las ciudades con las que vamos a trabajar y el nodo al que pertenece.

![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/1615b694-2a51-4e61-9303-3f017ca32ffe)

## Metodología : 

### ***DFS*** (Depth First Search) Este método añade los diferentes nodos a una pila y
### comprueba que el nodo seleccionado sea el destino
### indicado, si no lo es, añadimos los nuevos nodos al principio de la pila.

### ***BFS*** (Breath First Graph Search) Este método añade los diferentes nodos a una cola haciendo uso de la clase ### FIFOQueue y comprobando si  este es el destino, si no lo es, seguimos añadiendo al final de la cola.

### ***BB*** (Branch & Bound) Esta clase implementa una cola con funcionalidades específicas de ordenamiento y 
### gestión de tamaño.

### ***BBS*** (Branch and Bound subestimated) Esta clase se utiliza para gestionar una cola de prioridad donde los ### elementos se ordenan según una combinación de un costo de camino y una heurística asociada. 
