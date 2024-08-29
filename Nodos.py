import socket
import threading
import heapq

class Node:
    def __init__(self, name, port, neighbors=None):
        self.name = name
        self.port = port
        self.neighbors = neighbors if neighbors is not None else {}
        self.routing_table = {name: (0, name)}  # Distancia a sí mismo es 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', port))
        self.running = True  # Para controlar el estado de ejecución del nodo
        print(f"Node {self.name} running on port {self.port}. Neighbors: {self.neighbors}")

    def start(self):
        self.listener_thread = threading.Thread(target=self.listen)
        self.listener_thread.start()

    def listen(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = data.decode()
                self.message_received(message, addr)
            except socket.error as e:
                print(f"Socket error: {e}")
                break

    def message_received(self, message, addr):
        print(f"Node {self.name} received message from {addr}: {message}")
        # Aquí se puede añadir lógica adicional, como actualizar la tabla de enrutamiento, etc.

    def send_message(self, message, neighbor_name):
        if neighbor_name in self.neighbors:
            neighbor_port = self.neighbors[neighbor_name]
            self.sock.sendto(message.encode(), ('localhost', neighbor_port))
            print(f"Node {self.name} sent message to {neighbor_name} on port {neighbor_port}: {message}")
        else:
            print(f"Neighbor {neighbor_name} not found for Node {self.name}")

    def broadcast(self, message):
        for neighbor in self.neighbors:
            self.send_message(message, neighbor)

    def add_neighbor(self, neighbor_name, neighbor_port):
        if neighbor_name not in self.neighbors:
            self.neighbors[neighbor_name] = neighbor_port
            print(f"Node {self.name} added neighbor {neighbor_name} on port {neighbor_port}")
        else:
            print(f"Neighbor {neighbor_name} already exists for Node {self.name}")

    def close(self):
        self.running = False
        self.sock.close()
        self.listener_thread.join()
        print(f"Node {self.name} has closed its socket and stopped listening.")


'''
    def dijkstra(self):
        distancias = {nodo: float('inf') for nodo in self.neighbors}
        distancias[self.name] = 0
        pq = [(0, self.name)]
        heapq.heapify(pq)
        predecesores = {nodo: None for nodo in self.neighbors}
        predecesores[self.name] = self.name
        
        while pq:
            distancia_actual, nodo_actual = heapq.heappop(pq)
            
            if distancia_actual > distancias[nodo_actual]:
                continue
            
            for vecino, port in self.neighbors.items():
                distancia = distancia_actual + 1  
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(pq, (distancia, vecino))
        
        self.routing_table = {nodo: (distancia, predecesores[nodo]) for nodo, distancia in distancias.items()}
        print(f"Tabla de ruteo para node {self.name}: {self.routing_table}")
'''