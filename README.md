# Routing Algorithms Laboratory 

This Laboratory  implements several routing algorithms in a network of nodes, including Flooding, Dijkstra, and Link State Routing. Each of these algorithms is designed to send messages across a simulated network of nodes, calculating the most efficient route between nodes according to the selected algorithm.

## Contents

- **Main.py**: The main file that starts the project and provides a menu to select which routing algorithm to execute.
- **Nodos.py**: Defines the `Node` class, which represents a node in the network and handles basic operations like sending and receiving messages.
- **flooding.py**: Implements the Flooding algorithm to send messages to all nodes in the network.
- **Dijkstra.py**: Implements the Dijkstra algorithm to find the shortest path between two nodes.
- **link_state_routing.py**: Implements the Link State Routing algorithm that uses network topology information to calculate the shortest paths and build routing tables.

## Installation

1. Clone the repository or download the files.
2. Make sure you have Python 3 installed on your system.
3. Install any necessary dependencies (if required).
4. Run the `Main.py` file to start the program.

## Usage

After running `Main.py`, a menu will appear with the following options:

1. **Execute Dijkstra Algorithm**: Calculates the shortest path between two nodes using the Dijkstra algorithm.
2. **Execute Flooding Algorithm**: Sends a message across the network using the Flooding algorithm.
3. **Execute Link State Routing Algorithm**: Calculates the shortest paths and builds the routing tables using the Link State Routing algorithm.
4. **Exit**: Closes the program.

### Execute Dijkstra Algorithm

To execute the Dijkstra algorithm:

1. Select option `1`.
2. Enter the start node's name.
3. Enter the destination node's name.
4. Enter the message to be sent.

The program will calculate the shortest path and send the message through the nodes along that path.

### Execute Flooding Algorithm

To execute the Flooding algorithm:

1. Select option `2`.
2. Enter the start node's name.
3. Enter the destination node's name.
4. Enter the message to be sent.

The program will send the message to all nodes until it reaches the destination node.

### Execute Link State Routing Algorithm

To execute the Link State Routing algorithm:

1. Select option `3`.
2. Enter the start node's name.
3. Enter the destination node's name.
4. Enter the message to be sent.

The program will calculate the shortest paths, display the routing table for each node, and send the message along the shortest path.

## Project Structure

- **Json/**: Directory containing configuration files like `names.txt` and `topo.txt`, which define the nodes and the network topology.
- **Main.py**: The main entry point of the project.
- **Nodos.py**: Defines the basic logic of the nodes in the network.
- **flooding.py**: Contains the implementation of the Flooding algorithm.
- **dijkstra_routing.py**: Contains the implementation of the Dijkstra algorithm.
- **link_state_routing.py**: Contains the implementation of the Link State Routing algorithm.

## Configuration Example

In the `Json/` folder, you will find the `names.txt` and `topo.txt` files, which define the network configuration.

### `names.txt` File

```json
{
  "type": "names",
  "config": {
    "A": "5001",
    "B": "5002",
    "C": "5003",
    "D": "5004",
    "E": "5005",
    "F": "5007",
    "G": "5008"
  }
}


```
### `topo.txt` File

```json
{
  "type": "topo",
  "config": {
    "A": ["D", "E"],
    "B": ["D", "F", "G"],
    "C": ["E", "G"],
    "D": ["A", "B", "G"],
    "E": ["A", "C", "F"],
    "F": ["B", "E"],
    "G": ["B", "D"]
  }
}
```

These files define the topology and ports used by each node in the network.

- **names.txt**: Assigns a specific port to each node.
- **topo.txt**: Defines the connections between nodes, i.e., who is a neighbor of whom.

## Contributions
- Manuel Rodas
- Diego Valdez






