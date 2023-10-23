def crear_laberinto(dimension, obstaculos):
    ''' Función que construye un laberinto cuadrado de una dimensión dada con obstáculos en posiciones especificadas.
    Parámetros requeridos:
        - dimension: la dimensión de la matriz cuadrada que representa el laberinto.
        - obstaculos: una lista de tuplas con posiciones donde hay obstáculos.
    Salida: 
        Una matriz que representa el laberinto. 
    '''
    laberinto = [['0' for _ in range(dimension)] for _ in range(dimension)]

    for obstaculo in obstaculos:
        x, y = obstaculo
        laberinto[x][y] = 'X'

    return laberinto

# Lista de posiciones de las celdas con obstáculos en el laberinto
obstaculos = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
# Tamaño de la matriz
dimension = 5
# Llamada a la función una vez establecidos los valores de obstáculos
laberinto = crear_laberinto(dimension, obstaculos)   

# Imprimir el laberinto
# SOLO COMO EJEMPLO
for fila in laberinto:
    print(''.join(fila))

def encontrar_camino(laberinto, inicio, objetivo):
    def es_valida(x, y):
        return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == '0'

    def encontrar_camino_recursivo(x, y):
        if (x, y) == objetivo:
            return True
        if es_valida(x, y):
            laberinto[x][y] = 'Visitado'
            if encontrar_camino_recursivo(x - 1, y):  # Arriba
                camino.append("arriba")
                return True
            if encontrar_camino_recursivo(x + 1, y):  # Abajo
                camino.append("abajo")
                return True
            if encontrar_camino_recursivo(x, y - 1):  # Izquierda
                camino.append("izquierda")
                return True
            if encontrar_camino_recursivo(x, y + 1):  # Derecha
                camino.append("derecha")
                return True
            laberinto[x][y] = '0'
            return False

    camino = []
    encontrar_camino_recursivo(inicio[0], inicio[1])
    camino.reverse()  # Revertir el camino para obtener la solución
    return camino

# Definir las coordenadas de inicio y objetivo
inicio = (0, 0)
objetivo = (4, 4)

# Encontrar el camino en el laberinto
solucion = encontrar_camino(laberinto, inicio, objetivo)

if solucion:
    print("El camino hacia el objetivo es:", " -> ".join(solucion))
else:
    print("No se encontró un camino hacia el objetivo.")

# Esperamos al usuario
input("Presione Enter para salir")
