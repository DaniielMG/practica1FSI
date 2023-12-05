# Search methods
import search
import time

# A -> B
ab = search.GPSProblem('A', 'B', search.romania)
print("\n\t\t ~~~~ [Desde A -> Hasta B] ~~~~")

print("\n\t\t-Amplitud-")
inicio = time.time()
print("Ruta: " + str(search.breadth_first_graph_search(ab).path()))
print("OPCIONAL :Tiempo de ejecución Amplitud: " + str(time.time() - inicio))


print("\n\t\t-Profundidad-")
inicio = time.time()
print("Ruta: " + str(search.depth_first_graph_search(ab).path()))
print("OPCIONAL :Tiempo de ejecución en profundidad: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y acotación-")
inicio = time.time()
print("Ruta: " + str(search.bab(ab).path()))
print("OPCIONAL :Tiempo de ejecución BB: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y acotación con subestimación-")
inicio = time.time()
print("Ruta: " + str(search.babsub(ab).path()))
print("OPCIONAL : Tiempo de ejecución BBS: " + str(time.time() - inicio))

