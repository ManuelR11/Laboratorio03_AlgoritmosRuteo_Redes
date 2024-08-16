import socket
import threading

class Node:
    def __init__(self, name, port, neighbors):
        self.name = name
        self.port = port
        self.neighbors = neighbors
        self.routing_table = {name: (0, name)}  # Distancia a sí mismo es 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', port))
        print(f"Node {self.name} running on port {self.port}. Neighbors: {self.neighbors}")

    def start(self):
        thread = threading.Thread(target=self.listen)
        thread.start()

    def listen(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            message = data.decode()
            print(f"Node {self.name} received message: {message}")

    def send_message(self, message, neighbor_name):
        neighbor_port = self.neighbors[neighbor_name]
        self.sock.sendto(message.encode(), ('localhost', neighbor_port))

    def broadcast(self, message):
        for neighbor in self.neighbors:
            self.send_message(message, neighbor)

    # Métodos para agregar Dijkstra y Flooding aquí en el futuro
