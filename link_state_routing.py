# link_state_routing.py

import heapq
from Nodos import Node

class LinkStateRouting:
    def __init__(self, nodes):
        self.nodes = nodes

    def run_link_state_routing(self, start_node_name, destination_node_name, message):
        if start_node_name not in self.nodes or destination_node_name not in self.nodes:
            print("Nodo de inicio o destino no válido.")
            return

        topology = self._gather_topology()
        routing_table, path = self._dijkstra_algorithm(start_node_name, destination_node_name, topology)

        if destination_node_name in routing_table:
            self._send_message_along_path(path, message)
            print(f"La ruta más corta de {start_node_name} a {destination_node_name} es: {' -> '.join(path)}")
            self._print_routing_table(routing_table)
        else:
            print(f"No se pudo encontrar una ruta desde {start_node_name} hasta {destination_node_name}.")

    def _gather_topology(self):
        # Recolecta la información de la topología de la red a partir de las tablas de ruteo de los nodos
        topology = {}
        for node_name, node in self.nodes.items():
            for neighbor in node.neighbors:
                if node_name not in topology:
                    topology[node_name] = {}
                topology[node_name][neighbor] = 1  # Asumimos un costo de 1 por cada enlace
        return topology

    def _dijkstra_algorithm(self, start_node_name, destination_node_name, topology):
        distancias = {nodo: float('inf') for nodo in topology}
        distancias[start_node_name] = 0
        pq = [(0, start_node_name)]
        heapq.heapify(pq)
        predecesores = {nodo: None for nodo in topology}
        predecesores[start_node_name] = start_node_name
        
        while pq:
            distancia_actual, nodo_actual = heapq.heappop(pq)
            
            if distancia_actual > distancias[nodo_actual]:
                continue
            
            for vecino in topology[nodo_actual]:
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
        
        # Construir la tabla de ruteo que muestra el siguiente salto (next hop) para cada destino
        routing_table = {}
        for nodo, predecesor in predecesores.items():
            if nodo != start_node_name and predecesor is not None:
                # Determinar el siguiente salto (next hop)
                next_hop = nodo
                while predecesores[next_hop] != start_node_name:
                    next_hop = predecesores[next_hop]
                routing_table[nodo] = (distancias[nodo], next_hop)
            elif nodo == start_node_name:
                routing_table[nodo] = (0, start_node_name)

        return routing_table, path

    def _send_message_along_path(self, path, message):
        if len(path) < 2:
            print("No hay suficiente información para enviar el mensaje.")
            return

        for i in range(len(path) - 1):
            current_node = self.nodes[path[i]]
            next_node_name = path[i + 1]
            current_node.send_message(message, next_node_name)

    def _print_routing_table(self, routing_table):
        print("\nTabla de Ruteo:")
        print(f"{'Destino':<10}{'Costo':<10}{'Siguiente Salto':<15}")
        print("-" * 35)
        for destino, (costo, next_hop) in routing_table.items():
            print(f"{destino:<10}{costo:<10}{next_hop:<15}")
