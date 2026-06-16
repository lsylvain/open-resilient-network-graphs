import networkx as nx
import random
import csv
from pathlib import Path

def generate_quasi_random_topology(
    num_switches: int = 128,
    degree: int = 32,
    num_shuffle_layers: int = 2,
    seed: int = 42
) -> nx.Graph:
    """Generate a quasi-random regular graph suitable for RNG-style fabrics."""
    random.seed(seed)
    G = nx.random_regular_graph(degree, num_switches, seed=seed)
    
    # Tag edges with simulated ShuffleBox layer for cabling planning
    for u, v in G.edges():
        G[u][v]['shuffle_layer'] = random.randint(1, num_shuffle_layers)
        G[u][v]['cable_group'] = random.randint(1, 8)  # for quasi-random bundling
    
    return G

def export_cabling_matrix(G: nx.Graph, filename: str = "cabling_matrix.csv"):
    """Export edges for manufacturing ShuffleBox permutations."""
    Path(filename).parent.mkdir(exist_ok=True)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Switch_A', 'Port_A', 'Switch_B', 'Port_B', 'Shuffle_Layer'])
        for u, v, data in G.edges(data=True):
            writer.writerow([u, 0, v, 0, data.get('shuffle_layer', 1)])  # placeholder ports

# Example usage
if __name__ == "__main__":
    G = generate_quasi_random_topology(num_switches=64, degree=16)
    print(f"Generated {G.number_of_nodes()} switches, {G.number_of_edges()} links")
    print(f"Avg shortest path: {nx.average_shortest_path_length(G):.2f}")
    export_cabling_matrix(G)
    print("Cabling matrix exported.")
