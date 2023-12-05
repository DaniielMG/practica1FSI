# Práctica 1
## Algoritmos de búsqueda.

### El siguiente mapa, representa las ciudades con las que vamos a trabajar y el nodo al que pertenece.

![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/1615b694-2a51-4e61-9303-3f017ca32ffe)

## ***Metodología***

#### ***DFS*** (Depth First Search) Este método añade los diferentes nodos a una pila y comprueba que el nodo seleccionado sea el destino indicado, si no lo es, añadimos los nuevos nodos al principio de la pila.

#### ***BFS*** (Breath First Graph Search) Este método añade los diferentes nodos a una cola haciendo uso de la clase  FIFOQueue y comprobando si  este es el destino, si no lo es, seguimos añadiendo al final de la cola.

#### ***BB*** (Branch & Bound) Esta clase implementa una cola con funcionalidades específicas de ordenamiento y 
gestión de tamaño.

#### ***BBS*** (Branch and Bound subestimated) Esta clase se utiliza para gestionar una cola de prioridad donde los elementos se ordenan según una combinación de un costo de camino y una heurística asociada. 

## ***Contenido***
### Dentro de este proyecto, podemos encontrar 7 archivos diferentes. 
#### De esos 7 archivos, 5 pertenecen a los test, llamados "runs.py", cada ejemplo que pide la práctica posee un test diferente para indicar la cantidad de nodos genrados, expandidos y el costo que tendría dependiendo del diferente algoritmo de búsqueda empleado.
#### Otro archivo es el "search.py", el cual contiene  el programa principal y donde se realizaran los diferentes métodos. En este archivo, tambien se encuentran las diferentes ciudades de rumaia a visitar, con el nodo al que pertenece.
#### El ultimo archivo, es el "utils.py" en este archivo se encuentran los métodos que crean la pilas, la colas etc. Estaos métodos serán usados con posterioridad para elaborar el DFS y el BFS. 

## ***Comparación de estrategias***

### Ahora, veremos las diferentes estrategias enn las 5 direcciones propuestas.
![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/ca7823bb-60ac-4b6e-a71c-14261fff6de2)
![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/dbd853fa-5baa-4bb6-985b-f2fbb01ae411)
![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/8260439e-327d-4d84-88dc-27cfa342f37d)
![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/251a6782-b54c-4b72-986e-ef90c6dced8f)
![image](https://github.com/DaniielMG/practica1FSI/assets/95304769/260bd8a2-4e8d-4328-9d2c-f523a08f8fc0)

## ***Recursos empleados***
### Para realizar dicha práctica, hemos hecho uso de diferentes páginas y herramientas, aparte del material proporcionado por la asignatura.

#### http://jc-info.blogspot.com/2012/04/star-algorithm-prolog-code.html
#### https://www.youtube.com/watch?v=qeXbUzNQUlw
#### https://www.youtube.com/watch?v=OffCfUstOXQ
#### https://chat.openai.com
#### Material de la asignatura




