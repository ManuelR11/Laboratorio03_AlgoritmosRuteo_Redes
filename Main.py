import json
from Nodos import Node
from flooding import Flooding

def load_config(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data['config']

def get_names():
    return load_config('Json/names.txt')

def get_topology():
    return load_config('Json/topo.txt')

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

    flooding = Flooding(nodes)  # Crear la instancia de Flooding con los nodos

    while True:
        show_menu()
        choice = input("Selecciona una opción: ")

        if choice == '1':
            print("Algoritmo Dijkstra aún no implementado.")
            # Aquí puedes implementar la funcionalidad de Dijkstra
        elif choice == '2':
            start_node = input("Ingresa el nodo de inicio para Flooding: ")
            destination_node = input("Ingresa el nodo de destino para Flooding: ")
            message = input("Ingresa el mensaje para Flooding: ")
            
            destination_reached = flooding.flood(start_node, destination_node, message)

            while flooding.is_running():
                pass
            
            if destination_reached:
                print(f"El mensaje llegó exitosamente al nodo destino: {destination_node}")
            else:
                print(f"El mensaje no pudo llegar al nodo destino: {destination_node}")
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

    for node in nodes.values():
        node.close()

if __name__ == "__main__":
    main()