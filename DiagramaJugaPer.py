from datetime import date

class Persona:
    def __init__(self, nif: str, nombre: str, fechaNac: date):
        self.nif = nif
        self.nombre = nombre
        self.fechaNac = fechaNac

class Jugador(Persona):
    def __init__(self, nif: str, nombre: str, fechaNac: date, numFed: int):
        super().__init__(nif, nombre, fechaNac)
        self.numFed = numFed

if __name__ == "__main__":
    jugadores = [
        Jugador("1125118249", "Diego Armando Giraldo", date(1999, 8, 15), 201),
        Jugador("1053874214", "Yeison Acosta Lopez", date(2006, 9, 3), 202)
    ]

    print("Lista de jugadores registrados:")
    for j in jugadores:
        print(f"{j.nombre} (NIF: {j.nif}, Nº Federado: {j.numFed})")
