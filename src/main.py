from map import create_network
from GUI import Window

if __name__ == '__main__':
    G = create_network()
    Window(G)
