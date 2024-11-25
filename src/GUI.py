import tkinter as tk
from tkinter import messagebox, ttk

import networkx as nx

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import time as t
import sys

from map_constants import metro_times, lines, metro_node_coord
from map import astar


def Window(G):

    # Funciones para cuando cambie el elemento de un desplegable
    def origen_changed(event):
        comboOrigen["values"] = lines[comboLineaOrigen.get()]
        comboOrigen['state'] = 'normal'

    def destino_changed(event):
        comboDestino["values"] = lines[comboLineaDestino.get()]
        comboDestino['state'] = 'normal'

    # Definicion de la ventana para la GUI
    window = tk.Tk()
    window.rowconfigure([0, 2], minsize=100)
    window.columnconfigure([0, 2], minsize=623)
    window.state('zoomed')
    window.configure(bg='lightblue')

    # Definimos el espacio para introducir la estacion origen
    frameOrigen = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
    labelOrigen = tk.Label(text="Introduce la parada origen", font=("Arial", 20), master=frameOrigen)
    labelOrigen.pack(expand=True, side=tk.TOP)
    # Definimos el espacio para introducir la estacion origen
    # Labels para linea y parada
    lblLineaOrigen = tk.Label(master=frameOrigen, text="linea", font=("Arial", 10))
    lblParadaOrigen = tk.Label(master=frameOrigen, text="parada", font=("Arial", 10))
    lblLineaOrigen.pack(expand=True, side=tk.LEFT)
    lblParadaOrigen.pack(expand=True, side=tk.RIGHT)

    # Dropdowns para elegir la linea y parada origen
    comboOrigen = ttk.Combobox(master=frameOrigen, state="readonly", font='Arial 12', values=["Escoja primero la linea"])
    comboLineaOrigen = ttk.Combobox(master=frameOrigen, width=2, state="readonly", font='Arial 12', values=["A", "B", "C", "D", "E"])
    comboLineaOrigen.bind("<<ComboboxSelected>>", origen_changed)
    comboLineaOrigen.pack(fill=tk.BOTH, side=tk.LEFT)
    comboOrigen.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

    # Creamos el Frame contenedor de los elementos del destino
    frameDestino = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
    labelDestino = tk.Label(text="Introduce la parada destino", font=("Arial", 20), master=frameDestino)
    labelDestino.pack(expand=True)

    # Definimos el espacio para introducir la estacion destino
    # Labels para linea y parada
    lblLineaDestino = tk.Label(master=frameDestino, text="linea", font=("Arial", 10, ))
    lblParadaDestino = tk.Label(master=frameDestino, text="parada", font=("Arial", 10))
    lblLineaDestino.pack(expand=True, side=tk.LEFT)
    lblParadaDestino.pack(expand=True, side=tk.RIGHT)

    # Dropdowns para elegir la linea y parada destino
    comboDestino = ttk.Combobox(master=frameDestino, state="readonly", font='Arial 12', values=["Escoja primero la linea"])
    comboLineaDestino = ttk.Combobox(master=frameDestino, width=2, state="readonly", font='Arial 12', values=["A", "B", "C", "D", "E"])
    comboLineaDestino.bind("<<ComboboxSelected>>", destino_changed)
    comboLineaDestino.pack(fill=tk.BOTH, side=tk.LEFT)
    comboDestino.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

    # Definimos el espacio para contener la flecha de relacion origen-destino
    frameFlecha = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5, background='lightblue')
    labelFlecha = tk.Label(master=frameFlecha, font=("Arial", 40), text="\u2B95", background='lightblue')
    labelFlecha.pack(expand=True)

    # Posicionamiento de los frames
    frameOrigen.grid(row=0, column=0, sticky="W")
    frameDestino.grid(row=0, column=2, sticky="E")
    frameFlecha.grid(row=0, column=1)

    def comprobarLineasElegidas():
        if comboLineaOrigen.current() == -1:
            raise ValueError("No se ha seleccionado la linea origen")
        elif comboLineaDestino.current() == -1:
            raise ValueError("No se ha seleccionado la linea destino")
        elif comboOrigen.current() == -1:
            raise ValueError("No se ha elegido la estacion de origen")
        elif comboDestino.current() == -1:
            raise ValueError("No se ha elegido la estacion de destino")

    # pathImage se ejecuta cuando se pulsa el boton de confirmar paradas
    # Comprueba que efectivamente se han escogido las lineas y paradas
    # Crea el canvas que será el encargado de guardar el grafo de las estaciones que hay que pasar
    # Crea también el grafo y realiza con una llamada a la funcion map.astar() el camino minimo
    # Se determina como tiempo minimo del tren en una parada 1 minuto
    def pathImage(event):
        try:
            confirmBtn["relief"] = tk.SUNKEN
            comprobarLineasElegidas()
            canvas = FigureCanvasTkAgg(figure=plt.figure(figsize=(6,5)), master = window)  
            canvas.get_tk_widget().destroy()
            origen = comboOrigen.get()
            destino = comboDestino.get()
            shortest_path = astar(G, source=origen, target=destino)
            graph = nx.DiGraph()
            time = 0
            for i in range(len(shortest_path)):
                graph.add_node(shortest_path[i], pos=metro_node_coord[shortest_path[i]])
                if i < len(shortest_path) - 1:
                    edge = f'{shortest_path[i]} - {shortest_path[i+1]}'
                    edgeInv = f'{shortest_path[i+1]} - {shortest_path[i]}'
                    line = ""
                    weight = ""
                    for linea in metro_times:
                        if edge in metro_times[linea]:
                            line = linea
                            weight = metro_times[linea][edge]
                            time += int(weight) + 1
                            break
                        elif edgeInv in metro_times[linea]:
                            line = linea
                            weight = metro_times[linea][edgeInv]
                            time += int(weight) + 1
                            break

                    graph.add_edge(shortest_path[i], shortest_path[i+1], line=f'Linea:{line}\nTiempo:{int(weight)+1}')

            # Set up the plot
            Figure = plt.figure(figsize=(6, 5))
            ax = plt.gca()

            # Draw the graph
            pos = nx.get_node_attributes(graph,'pos')
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

            # Eliminamos la figura para liberar espacio en memoria
            # Se pasa el argumento all por si había quedado alguna figura abierta, aunque no debería pasar
            plt.close('all')

            t.sleep(0.1)
            confirmBtn["relief"] = tk.RAISED
        # Tratamiento de los errores que pueda generar la funcion
        # ValueError será normalmente un error que hayamos subido nosotros
        # Exception es un valor generico para todas las demas excepciones
        except ValueError as err:
            confirmBtn["relief"] = tk.RAISED
            messagebox.showerror(title="ERROR", message=err)
        except Exception as err:
            confirmBtn["relief"] = tk.RAISED
            messagebox.showerror(title="ERROR", message=f'Error del tipo: {type(err)}\nTraza del error: {err}')

    # Definimos el boton y su Frame contenedor
    frameBtn = tk.Frame(master=window, width=50)
    confirmBtn = tk.Button(master=frameBtn, text="Confirmar paradas", font="Arial 20", relief=tk.RAISED)
    confirmBtn.bind("<Button-1>", pathImage)
    confirmBtn.pack(side=tk.BOTTOM)
    frameBtn.grid(row=1, column=1)

    # Funcion para regular como se comporta la aplicacion al cerrar la ventana
    def windowClosed():
        # Eliminamos la figura para liberar espacio en memoria
        # Se pasa el argumento all por si había quedado alguna figura abierta, aunque no debería pasar
        plt.close('all')
        window.destroy()
        sys.exit()

    # Asociamos la accion de cerrar la ventana
    window.protocol("WM_DELETE_WINDOW", windowClosed)
    
    # Main loop de la ventana (Hecho por defecto)
    window.mainloop()
