from domain.Station import Station
import matplotlib.pyplot as plt
import networkx as nx
import heapq

class Graph:
    def __init__(self):
        self.stations = {}

    def add_station(self, name):
        if name not in self.stations:
            new_station = Station(name)
            self.stations[name] = new_station

    def add_connection(self, station1, station2, time):
        if station1 in self.stations and station2 in self.stations:
            self.stations[station1].add_neighbor(station2, time)
            self.stations[station2].add_neighbor(station1, time)
        else:
            print("Estação não encontrada.")

    def dijkstra(self, start, end):
        min_times = { station: float('inf') for station in self.stations }
        min_times[start] = 0

        priority_queue = [(0, start)]

        path = {}

        while priority_queue:
            current_time, current_station = heapq.heappop(priority_queue)

            if (current_station == end):
                end_path = []
                while current_station:
                    end_path.append(current_station)
                    current_station = path.get(current_station)

                return list(reversed(end_path)), current_time
            
            try:
                for neighbor, time in self.stations[current_station].neighbor.items():
                    new_time = current_time + time
                    if new_time < min_times[neighbor]:
                        min_times[neighbor] = new_time
                        path[neighbor] = current_station
                        heapq.heappush(priority_queue, (new_time, neighbor))
            except:
                print("Não foi possível encontrar essas estações.")

        return None, None

    def get_graph_for_show(self):
        G = nx.Graph()
        for station_name, station in self.stations.items():
            for neighbor, time in station.neighbor.items():
                G.add_edge(station_name, neighbor, weight=time)

        return G

    def show(self):
        G = self.get_graph_for_show()
        pos = nx.spring_layout(G, k=0.5, iterations=100)  # Ajuste os parâmetros k e iterations conforme necessário
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show() 
