import json
from Nodos import Node

def load_config(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data['config']

def get_names():
    return load_config('names.txt')

def get_topology():
    return load_config('topo.txt')

def create_and_start_node(node_name, names, topology):
    port = int(names[node_name])
    neighbors = {neighbor: int(names[neighbor]) for neighbor in topology[node_name]}
    
    node = Node(node_name, port, neighbors)
    node.start()
    return node

def show_menu():
    print("\nMenu:")
    print("1. Ejecutar algoritmo Dijkstra")
    print("2. Ejecutar algoritmo Flooding")
    print("3. Salir")

def main():
    names = get_names()
    topology = get_topology()

    nodes = {}
    node_names = names.keys()

    for name in node_names:
        node = create_and_start_node(name, names, topology)
        nodes[name] = node

    while True:
        show_menu()
        choice = input("Selecciona una opción: ")

        if choice == '1':
            print("Algoritmo Dijkstra aún no implementado.")
            # Aquí puedes implementar la funcionalidad de Dijkstra
        elif choice == '2':
            print("Algoritmo Flooding aún no implementado.")
            # Aquí puedes implementar la funcionalidad de Flooding
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
