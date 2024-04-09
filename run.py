from domain.Graph import Graph
from utils.utils import add_stations, print_shortest_path, clean_terminal
import time

def main():
    graph = Graph()
    add_stations(graph)

    while True:
        clean_terminal()
        print("\nMenu:")
        print("1. Encontrar caminho mais curto")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            clean_terminal()

            start_station = input("Digite a estação de partida: ")
            end_station = input("Digite a estação de destino: ")

            path, duration = graph.dijkstra(start_station, end_station)

            if path:
                print("Caminho mais curto de", start_station, "para", end_station, ":")
                print_shortest_path(path)
                print("Tempo total:", duration, "minutos")
                input()
            else:
                print("Não há caminho entre", start_station, "e", end_station)
                time.sleep(3)

        elif opcao == "2":
            clean_terminal()
            print("Saindo do programa...")
            break

        else:
            clean_terminal()
            print("Opção inválida. Por favor, escolha uma opção válida.")
            time.sleep(3)

if __name__ == "__main__":
    main()