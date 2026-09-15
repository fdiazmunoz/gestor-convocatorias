from partidos import crear_partido

partidos = [
    # Pretemporada / amistosos
    {"rival": "Unicaja",           "fecha": "2026-09-01", "competicion": "amistoso", "local_visitante": "local"},
    {"rival": "Partizan Belgrado", "fecha": "2026-09-05", "competicion": "amistoso", "local_visitante": "visitante"},
    {"rival": "Baskonia",          "fecha": "2026-09-10", "competicion": "amistoso", "local_visitante": "local"},

    # Liga regular
    {"rival": "Gran Canaria",        "fecha": "2026-10-04", "competicion": "liga", "local_visitante": "local"},
    {"rival": "Joventut Badalona",   "fecha": "2026-10-11", "competicion": "liga", "local_visitante": "visitante"},
    {"rival": "Valencia Basket",     "fecha": "2026-10-18", "competicion": "liga", "local_visitante": "local"},
    {"rival": "Unicaja",             "fecha": "2026-10-25", "competicion": "liga", "local_visitante": "visitante"},
    {"rival": "San Pablo Burgos",    "fecha": "2026-11-01", "competicion": "liga", "local_visitante": "local"},
]

if __name__ == "__main__":
    ids_creados = []
    for p in partidos:
        nuevo_id = crear_partido(p["rival"], p["fecha"], p["competicion"], p["local_visitante"])
        ids_creados.append(nuevo_id)

    print("\nIDs de partidos creados:", ids_creados)