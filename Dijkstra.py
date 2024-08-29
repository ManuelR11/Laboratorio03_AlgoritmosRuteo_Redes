# dijkstra_routing.py

import heapq
from Nodos import Node

class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes

    def run_dijkstra(self, start_node_name, destination_node_name, message):
        if start_node_name not in self.nodes or destination_node_name not in self.nodes:
            print("Nodo de inicio o destino no válido.")
            return

        routing_table, path = self._dijkstra_algorithm(start_node_name, destination_node_name)

        if destination_node_name in routing_table:
            self._send_message_along_path(path, message)
            print(f"La ruta más corta de {start_node_name} a {destination_node_name} es: {' -> '.join(path)}")
        else:
            print(f"No se pudo encontrar una ruta desde {start_node_name} hasta {destination_node_name}.")

    def _dijkstra_algorithm(self, start_node_name, destination_node_name):
        distancias = {nodo: float('inf') for nodo in self.nodes}
        distancias[start_node_name] = 0
        pq = [(0, start_node_name)]
        heapq.heapify(pq)
        predecesores = {nodo: None for nodo in self.nodes}
        predecesores[start_node_name] = start_node_name
        
        while pq:
            distancia_actual, nodo_actual = heapq.heappop(pq)
            
            if distancia_actual > distancias[nodo_actual]:
                continue
            
            for vecino in self.nodes[nodo_actual].neighbors:
                distancia = distancia_actual + 1  
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(pq, (distancia, vecino))
                    
            if nodo_actual == destination_node_name:
                break
        
        # Reconstruir el camino desde el nodo destino hasta el nodo de inicio
        path = []
        step = destination_node_name
        while step is not None:
            path.insert(0, step)
            if step == start_node_name:
                break
            step = predecesores[step]
        
        routing_table = {nodo: (distancias[nodo], predecesores[nodo]) for nodo in self.nodes}
        return routing_table, path

    def _send_message_along_path(self, path, message):
        if len(path) < 2:
            print("No hay suficiente información para enviar el mensaje.")
            return

        for i in range(len(path) - 1):
            current_node = self.nodes[path[i]]
            next_node_name = path[i + 1]
            current_node.send_message(message, next_node_name)
