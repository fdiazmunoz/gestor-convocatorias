from jugadores import crear_jugador

equipo = [
    {"nombre": "Facundo Campazzo",        "dorsal": 7,  "posicion": "base",      "fecha_nacimiento": "1991-03-23"},
    {"nombre": "Théo Maledon",            "dorsal": 12, "posicion": "base",      "fecha_nacimiento": "2001-06-12"},
    {"nombre": "Andrés Feliz",            "dorsal": 24, "posicion": "base",      "fecha_nacimiento": "1997-07-15"},
    {"nombre": "Sergio Llull",            "dorsal": 23, "posicion": "escolta",   "fecha_nacimiento": "1987-11-15"},
    {"nombre": "Max Shulga",              "dorsal": 2,  "posicion": "escolta",   "fecha_nacimiento": "2002-06-25"},
    {"nombre": "Timothé Luwawu-Cabarrot", "dorsal": 3,  "posicion": "alero",     "fecha_nacimiento": "1995-05-09"},
    {"nombre": "Alberto Abalde",          "dorsal": 6,  "posicion": "alero",     "fecha_nacimiento": "1995-12-15"},
    {"nombre": "Gabriele Procida",        "dorsal": 9,  "posicion": "alero",     "fecha_nacimiento": "2002-06-01"},
    {"nombre": "Gabriel Deck",            "dorsal": 14, "posicion": "alero",     "fecha_nacimiento": "1995-02-08"},
    {"nombre": "Jaime Pradilla",          "dorsal": 4,  "posicion": "ala-pivot", "fecha_nacimiento": "2001-01-03"},
    {"nombre": "Chuma Okeke",             "dorsal": 8,  "posicion": "ala-pivot", "fecha_nacimiento": "1998-08-18"},
    {"nombre": "Usman Garuba",            "dorsal": 16, "posicion": "ala-pivot", "fecha_nacimiento": "2002-03-09"},
    {"nombre": "Mikael Jantunen",         "dorsal": 20, "posicion": "ala-pivot", "fecha_nacimiento": "2000-04-20"},
    {"nombre": "Edy Tavares",             "dorsal": 22, "posicion": "pivot",     "fecha_nacimiento": "1992-03-22"},
    {"nombre": "Damian Jones",            "dorsal": 30, "posicion": "pivot",     "fecha_nacimiento": "1995-06-30"},
    {"nombre": "Olivier Sarr",            "dorsal": 33, "posicion": "pivot",     "fecha_nacimiento": "1999-02-20"},
]

if __name__ == "__main__":
    for jugador in equipo:
        crear_jugador(
            jugador["nombre"],
            jugador["dorsal"],
            jugador["posicion"],
            jugador["fecha_nacimiento"]
        )