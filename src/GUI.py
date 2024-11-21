import tkinter as tk
from tkinter import messagebox

import networkx as nx

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

from map_constants import metro_times
from map import astar


def Window(G):
    # Definicion de la ventana para la GUI
    window = tk.Tk()
    window.rowconfigure([0, 2], minsize=100)
    window.columnconfigure([0, 2], minsize=623)
    window.state('zoomed')

    frameOrigen = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
    labelOrigen = tk.Label(text="Introduce la parada origen", font=("Arial", 20), master=frameOrigen)
    labelOrigen.pack(expand=True)
    # Definimos el espacio para introducir la estacion origen
    entryOrigen = tk.Entry(master=frameOrigen, font='Arial 12')
    entryOrigen.pack(fill=tk.BOTH, expand=True)

    frameDestino = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
    labelDestino = tk.Label(text="Introduce la parada destino", font=("Arial", 20), master=frameDestino)
    labelDestino.pack(expand=True)
    # Definimos el espacio para introducir la estacion destino
    entryDestino = tk.Entry(master=frameDestino, font='Arial 12')
    entryDestino.pack(fill=tk.BOTH, expand=True)

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
            origen = entryOrigen.get()
            destino = entryDestino.get()
            shortest_path = astar(G, source=origen, target=destino)
            graph = nx.DiGraph()
            time = 0
            for i in range(len(shortest_path)):
                graph.add_node(shortest_path[i])
                if i < len(shortest_path) - 1:
                    edge = f'{shortest_path[i]} - {shortest_path[i+1]}'
                    edgeInv = f'{shortest_path[i+1]} - {shortest_path[i]}'
                    line = ""
                    weight = ""
                    for linea in metro_times:
                        if edge in metro_times[linea]:
                            line = linea
                            weight = metro_times[linea][edge]
                            time = time + int(weight)
                            break
                        elif edgeInv in metro_times[linea]:
                            line = linea
                            weight = metro_times[linea][edgeInv]
                            time = time + int(weight)
                            break

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
            plt.title(f'Grafo del recorrido\nTiempoTotal: {time} minutos', fontsize=16)
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