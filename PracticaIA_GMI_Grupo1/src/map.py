import geopy.distance
import networkx as nx
from map_constants import metro_times, lines, metro_coord_geodesic

def create_network():
    # Create an undirected graph
    G = nx.DiGraph()
    
    # Add nodes (stations) and edges (connections)
    for line_name, stations in lines.items():
        line_colors = {
            'A': 'light blue',
            'B': 'red',
            'C': 'blue',
            'D': 'green',
            'E': 'purple',
        }
        
        # Add nodes and edges for each line
        for i in range(len(stations)):
            # Add node with attributes
            G.add_node(stations[i], line=line_name)
            
            # Add edge to next station if it exists
            if i < len(stations) - 1:
                edge_name = f'{stations[i]} - {stations[i+1]}'
                weight = metro_times[line_name][edge_name]

                G.add_edge(stations[i], stations[i + 1], 
                        line=line_name, 
                        color=line_colors[line_name],
                        weight=weight)
                G.add_edge(stations[i+1], stations[i], 
                        line=line_name, 
                        color=line_colors[line_name],
                        weight=weight)

    for transfer, weight in metro_times['T'].items():
        station1, station2 = transfer.split(' - ')
        G.add_edge(station1, station2, line='T', color='orange', weight=weight)
        G.add_edge(station2, station1, line='T', color='orange', weight=weight)

    return G

# Geodesic distance is the chosen h(n) that Astar requires
def heuristic(node, target):
    coord_node = metro_coord_geodesic[node]
    coord_target = metro_coord_geodesic[target]
    return geopy.distance.geodesic(coord_node,coord_target).km


def astar(G, source, target):
    if source == 'Alberti':
        raise ValueError("El origen no pude ser Alberti")
    if target == 'Pasco':
        raise ValueError("El destino no puede ser Pasco")

    return nx.astar_path(G, source=source, heuristic=heuristic, target=target)
