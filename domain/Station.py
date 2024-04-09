class Station:
    def __init__(self, name):
        self.name = name
        self.neighbor = {}
    
    def add_neighbor(self, station, time):
        self.neighbor[station] = time