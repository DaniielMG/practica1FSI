# Search methods
import search
import time

oe = search.GPSProblem('O', 'E', search.romania)

print("\n\t\t ~~~~ [Desde O -> Hasta E] ~~~~")
print("\n\t\t-Amplitud-")
print("Ruta: " + str(search.breadth_first_graph_search(oe).path()))
print("OPCIONAL :Tiempo de ejecución Amplitud: " + str(time.time() - inicio))

print("\n\t\t-Profundidad-")
inicio = time.time()
print("Ruta: " + str(search.depth_first_graph_search(oe).path()))
print("OPCIONAL :Tiempo de ejecución en profundidad: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y acotación-")
inicio = time.time()
print("Ruta: " + str(search.bab(oe).path()))
print("OPCIONAL :Tiempo de ejecución BB: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y acotación con subestimación-")
inicio = time.time()
print("Ruta: " + str(search.babsub(oe).path()))
print("OPCIONAL : Tiempo de ejecución BBS: " + str(time.time() - inicio))
