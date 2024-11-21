import tkinter as tk
from tkinter import messagebox

import networkx as nx

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

from map_constants import metro_times, stations
from map import astar


def Window(G):
    # Definicion de la ventana para la GUI
    window = tk.Tk()
    window.rowconfigure([0, 2], minsize=100)
    window.columnconfigure([0, 2], minsize=623)
    window.state('zoomed')
    window.configure(bg='lightblue')

    # Example list of stations

    frameOrigen = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
    labelOrigen = tk.Label(text="Introduce la parada origen", font=("Arial", 20), master=frameOrigen)
    labelOrigen.pack(expand=True)
    # Dropdown menu for selecting the origin station
    origin_var = tk.StringVar(window)
    origin_var.set(stations[0])  # default value
    dropdownOrigen = tk.OptionMenu(frameOrigen, origin_var, *stations)
    dropdownOrigen.pack(fill=tk.BOTH, expand=True)

    frameDestino = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
    labelDestino = tk.Label(text="Introduce la parada destino", font=("Arial", 20), master=frameDestino)
    labelDestino.pack(expand=True)
    # Dropdown menu for selecting the destination station
    destino_var = tk.StringVar(window)
    destino_var.set(stations[0])  # default value
    dropdownDestino = tk.OptionMenu(frameDestino, destino_var, *stations)
    dropdownDestino.pack(fill=tk.BOTH, expand=True)

    frameFlecha = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)
    labelFlecha = tk.Label(master=frameFlecha, font=("Arial", 40), text="\u2B95")
    labelFlecha.pack(expand=True)

    # Posicionamiento de los frames
    frameOrigen.grid(row=0, column=0, sticky="W")
    frameDestino.grid(row=0, column=2, sticky="E")
    frameFlecha.grid(row=0, column=1)

    

    def pathImage(event):
        try:
            canvas = FigureCanvasTkAgg(figure=plt.figure(figsize=(6,7)), master = window)  
            canvas.get_tk_widget().destroy()
            origen = origin_var.get()
            destino = destino_var.get()
            shortest_path = astar(G, source=origen, target=destino)
            graph = nx.DiGraph()
            for i in range(len(shortest_path)):
                graph.add_node(shortest_path[i])
                if i < len(shortest_path) - 1:
                    edge = f'{shortest_path[i]} - {shortest_path[i+1]}'
                    line = ""
                    weight = ""
                    for linea in metro_times:
                        if edge in metro_times[linea]:
                            line = linea
                            weight = metro_times[linea][edge]

                    graph.add_edge(shortest_path[i], shortest_path[i+1], line=f'linea:{line}\ntiempo:{weight}')
                    graph.add_edge(shortest_path[i+1], shortest_path[i])

            # Set up the plot
            Figure = plt.figure(figsize=(6, 7))
            ax = plt.gca()

            # Draw the graph
            pos = nx.spring_layout(graph, k=0.5, iterations=50, seed=1)
            nx.draw(graph, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=300, font_size=6, font_weight='bold')

            # Add edge labels
            edge_labels = nx.get_edge_attributes(graph, 'line')
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

            # Set title and remove axis
            plt.title("Grafo del recorrido", fontsize=16)
            plt.axis('off')

            # Adjust layout and display
            plt.tight_layout()
            # creating the Tkinter canvas 
            # containing the Matplotlib figure 
            canvas = FigureCanvasTkAgg(Figure, master = window)   
            canvas.draw() 

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().grid(row=2, column=0, columnspan=3) 
        except ValueError as err:
            messagebox.showerror(title="ERROR", message=err)
        except Exception as err:
            messagebox.showerror(title="ERROR", message=f'Error del tipo: {type(err)}\nTraza del error: {err}')


    frameBtn = tk.Frame(master=window, width=50)
    confirmBtn = tk.Button(master=frameBtn, text="Confirmar paradas", font="Arial 20")
    confirmBtn.bind("<Button-1>", pathImage)
    confirmBtn.pack(side=tk.BOTTOM)
    frameBtn.grid(row=1, column=1)

    def windowClosed():
        if messagebox.askyesno("Exit", "¿Está seguro de que quiere cerrar la ventana?"):
            plt.close()
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", windowClosed)
    
    window.mainloop()