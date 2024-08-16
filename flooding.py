import threading

class Flooding:
    def __init__(self, nodes):
        self.nodes = nodes
        self.running_event = threading.Event()

    def flood(self, start_node_name, message):
        self.running_event.clear()
        visited = set()
        self._flood_recursive(start_node_name, message, visited, [])
        self.running_event.wait()  # Esperar a que el algoritmo termine

    def _flood_recursive(self, node_name, message, visited, path):
        if node_name in visited:
            return

        visited.add(node_name)
        path.append(node_name)

        print(f"Node {node_name} received the message. Path: {' -> '.join(path)}")

        node = self.nodes[node_name]
        threads = []
        for neighbor_name in node.neighbors:
            thread = threading.Thread(target=self._flood_recursive, args=(neighbor_name, message, visited.copy(), path.copy()))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # If the node is the intended recipient or there are no neighbors to forward to
        if len(node.neighbors) == 0:
            print(f"Final path for message '{message}': {' -> '.join(path)}")

        # Si todos los hilos han terminado, establece el evento
        if all(not thread.is_alive() for thread in threads):
            self.running_event.set()

    def is_running(self):
        return not self.running_event.is_set()