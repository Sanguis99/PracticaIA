import networkx as nx
from matplotlib import pyplot as plt

from map import create_network, astar

if __name__ == '__main__':
    G = create_network()
    print(f"Number of stations: {len(G.nodes())}")
    print(f"Number of connections: {len(G.edges())}")

    shortest_path = astar(G, 'Retiro', 'Facultad de Medicina')
    print(f"Shortest path from Retiro to Facultad de Medicina: {shortest_path}")

    # Set up the plot
    plt.figure(figsize=(15, 10))
    ax = plt.gca()

    # Draw the graph
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=300, font_size=6, font_weight='bold')

    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, 'line')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    # Set title and remove axis
    plt.title("Buenos Aires Metro Map Graph", fontsize=16)
    plt.axis('off')

    # Adjust layout and display
    plt.tight_layout()
    plt.show()