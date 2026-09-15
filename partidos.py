from conexion import obtener_conexion
from jugadores import cambiar_estado

def crear_partido(rival, fecha, competicion, local_visitante):
    competiciones_validas = ("liga", "copa", "playoff", "amistoso")
    if competicion not in competiciones_validas:
        print(f"Competición no válida. Usa una de: {competiciones_validas}")
        return None

    if local_visitante not in ("local", "visitante"):
        print("local_visitante debe ser 'local' o 'visitante'")
        return None

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO partidos (rival, fecha, competicion, local_visitante)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """,
        (rival, fecha, competicion, local_visitante)
    )

    nuevo_id = cursor.fetchone()[0]
    conexion.commit()

    cursor.close()
    conexion.close()

    print(f"Partido vs {rival} ({fecha}) creado con id {nuevo_id}")
    return nuevo_id


def listar_partidos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, rival, fecha, competicion, local_visitante FROM partidos ORDER BY fecha;")
    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return filas


def convocar_jugador(partido_id, jugador_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # 1. Comprobar el estado del jugador antes de convocarlo
    cursor.execute("SELECT nombre, estado FROM jugadores WHERE id = %s;", (jugador_id,))
    resultado = cursor.fetchone()

    if resultado is None:
        print(f"No existe ningún jugador con id {jugador_id}")
        cursor.close()
        conexion.close()
        return

    nombre, estado = resultado

    if estado != "disponible":
        print(f"{nombre} no puede ser convocado: está marcado como '{estado}'")
        cursor.close()
        conexion.close()
        return

    # 2. Si está disponible, insertarlo en la convocatoria
    try:
        cursor.execute(
            "INSERT INTO convocatorias (partido_id, jugador_id) VALUES (%s, %s);",
            (partido_id, jugador_id)
        )
        conexion.commit()
        print(f"{nombre} convocado correctamente al partido {partido_id}")
    except Exception as error:
        conexion.rollback()
        print(f"No se pudo convocar a {nombre}: {error}")
    finally:
        cursor.close()
        conexion.close()


def listar_convocatoria(partido_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT j.id, j.nombre, j.dorsal, j.posicion
        FROM convocatorias c
        JOIN jugadores j ON j.id = c.jugador_id
        WHERE c.partido_id = %s
        ORDER BY j.dorsal;
        """,
        (partido_id,)
    )
    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return filas


if __name__ == "__main__":
    pass