class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def MyLocation (self):
        print("Hola, Mi nombre es " + self.name + " y yo vivo en " + self.country + ".")

# Primera instancia de la ubicación de la clase 
loc1 = Location("Tomas", "Portugal")
# Llamar a un método de la clase instanciada
loc1.MyLocation()

loc2 = Location("Ying", "China")
loc2.MyLocation()

loc3 = Location("Amare", "Kenya")
loc3.MyLocation()

your_loc = Location("Carlos Oré", "Perú")
your_loc.MyLocation()




