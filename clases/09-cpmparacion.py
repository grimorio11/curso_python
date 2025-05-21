class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.__coordenadas = (lat, lon)

    def __eq__(self, value):
        return self.lat == value.lat and self.lon == value.lon
    def __ne__(self, value):
        return self.lat != value.lat or self.lon != value.lon
    
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords != coords2)  # False