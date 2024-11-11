import networkx as nx
from matplotlib import pyplot as plt

def create_subte_network():
    # Create an undirected graph
    G = nx.Graph()
    
    # Define lines with their stations in order
    lines = {
        'A': ['Plaza de Mayo', 'Peru', 'Piedras', 'Lima', 'Saenz Pena', 'Congreso', 'Pasco', 
              'Alberti', 'Plaza Miserere', 'Loria', 'Castro Barros', 'Rio de Janeiro',
              'Acoyte', 'Primera Junta', 'Puan', 'Carabobo'],
        
        'B': ['Leandro N. Alem', 'Florida', 'C. Pellegrini', 'Uruguay', 'Callao', 'Pasteur', 
              'Pueyrredon', 'Carlos Gardel', 'Medrano', 'Angel Gallardo', 'Malabia',
              'Dorrego', 'Federico Lacroze', 'Tronador - Villa Ortuzar', 'De Los Incas Parque Chas'],
        
        'C': ['Retiro', 'General San Martin', 'Lavalle', 'Diagonal Norte', 'Av. de Mayo', 
              'Moreno', 'Independencia', 'San Juan', 'Constitucion'],
        
        'D': ['Catedral', '9 de Julio', 'Tribunales', 'Callao', 
              'Facultad de Medicina', 'Pueyrredon', 'Agüero', 'Bulnes', 'Scalabrini Ortiz',
              'Plaza Italia', 'Palermo', 'Ministro Carranza', 'Olleros', 'Jose Hernandez', 
              'Juramento', 'Congreso de Tucuman'],
              
        'E': ['Bolivar', 'Belgrano', 'Independencia', 'San Jose', 'Entre Rios', 
		 		  'Pichincha', 'Jujuy', 'General Urquiza', 
              'Boedo', 'Av. La Plata', 'Jose M. Moreno', 'Emilio Mitre', 'Medalla Milagrosa',
              'Varela', 'Plaza de los Virreyes'],
              
        'H': ['Once', 'Alberti', 'Venezuela', 'Humberto I', 'Inclan', 'Caseros']
    }
    
    # Add nodes (stations) and edges (connections)
    for line_name, stations in lines.items():
        # Add line color attribute to edges
        line_colors = {
            'A': 'light blue',
            'B': 'red',
            'C': 'blue',
            'D': 'green',
            'E': 'purple',
            'H': 'yellow'
        }
        
        # Add nodes and edges for each line
        for i in range(len(stations)):
            # Add node with attributes
            G.add_node(stations[i], line=line_name)
            
            # Add edge to next station if it exists
            if i < len(stations) - 1:
                G.add_edge(stations[i], stations[i + 1], 
                          line=line_name, 
                          color=line_colors[line_name])
    
    # Add transfer stations (connections between different lines)
    transfers = [
        ('Plaza de Mayo', 'A', 'D'),
        ('Lima', 'A', 'C'),
        ('Plaza Miserere', 'A', 'H'),
        ('Pueyrredon', 'B', 'D'),
        ('Carlos Pellegrini', 'B', 'C'),
        ('Diagonal Norte', 'C', 'D'),
        ('Independencia', 'C', 'E'),
        ('Jujuy', 'E', 'H'),
        ('Venezuela', 'B', 'H')
    ]
    
    # Add transfer edges
    for station, line1, line2 in transfers:
        # Find connecting station names
        stations1 = [s for s in G.nodes() if G.nodes[s].get('line') == line1]
        stations2 = [s for s in G.nodes() if G.nodes[s].get('line') == line2]
        
        # Add transfer edges
        for s1 in stations1:
            for s2 in stations2:
                if s1.lower() == s2.lower() or s1.lower() in s2.lower() or s2.lower() in s1.lower():
                    G.add_edge(s1, s2, transfer=True, color='gray')
    
    return G

# Create the network
G = create_subte_network()

# Example usage:
"""
# Print basic information about the network
print(f"Number of stations: {len(subte_network.nodes())}")
print(f"Number of connections: {len(subte_network.edges())}")

# Find shortest path between two stations
shortest_path = nx.shortest_path(subte_network, 
                               source='Retiro',
                               target='Congreso de Tucuman')
print(f"Shortest path from Retiro to Congreso de Tucuman: {shortest_path}")
"""


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
