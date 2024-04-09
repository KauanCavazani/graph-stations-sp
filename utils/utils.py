import random
import os
import json

def add_stations(graph):

    with open('data/data.json', 'r', encoding='utf-8') as file:
        stations_lines = json.load(file)

    for line, stations in stations_lines.items():
        add_line(graph, stations)

def add_line(graph, stations):
    for station in stations:
        graph.add_station(station)

    for i in range(len(stations) - 1):
        current_station = stations[i]
        next_station = stations[i + 1]
        time = random.randint(2, 3)
        graph.add_connection(current_station, next_station, time)

def print_shortest_path(path):
    if path:
        for station in path:
            print(" ->", station)
    else:
        print("Não há caminho entre as estações fornecidas.")

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')