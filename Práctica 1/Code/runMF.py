# Search methods
import search
import time

mf = search.GPSProblem('M', 'F', search.romania)
print("\n\t\t ~~~~ [Desde M -> Hasta F] ~~~~")

print("\n\t\t-Amplitud-")
inicio = time.time()
print("Ruta: " + str(search.breadth_first_graph_search(mf).path()))
print("OPCIONAL :Tiempo de ejecución Amplitud: " + str(time.time() - inicio))

print("\n\t\t-Profundidad-")
inicio = time.time()
print("Ruta: " + str(search.depth_first_graph_search(mf).path()))
print("OPCIONAL :Tiempo de ejecución en profundidad: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y acotación-")
inicio = time.time()
print("Ruta: " + str(search.bab(mf).path()))
print("OPCIONAL :Tiempo de ejecución BB: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y acotación con subestimación-")
inicio = time.time()
print("Ruta: " + str(search.babsub(mf).path()))
print("OPCIONAL : Tiempo de ejecución BBS: " + str(time.time() - inicio))
