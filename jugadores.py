from conexion import obtener_conexion

def crear_jugador(nombre, dorsal, posicion, fecha_nacimiento, estado="disponible"):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO jugadores (nombre, dorsal, posicion, fecha_nacimiento, estado)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
        """,
        (nombre, dorsal, posicion, fecha_nacimiento, estado)
    )

    nuevo_id = cursor.fetchone()[0]
    conexion.commit()

    cursor.close()
    conexion.close()

    print(f"Jugador '{nombre}' creado con id {nuevo_id}")
    return nuevo_id


def listar_jugadores():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, dorsal, posicion, fecha_nacimiento, estado FROM jugadores ORDER BY dorsal;")
    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return filas


def actualizar_jugador(jugador_id, nombre=None, dorsal=None, posicion=None, fecha_nacimiento=None):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        UPDATE jugadores
        SET nombre = COALESCE(%s, nombre),
            dorsal = COALESCE(%s, dorsal),
            posicion = COALESCE(%s, posicion),
            fecha_nacimiento = COALESCE(%s, fecha_nacimiento)
        WHERE id = %s;
        """,
        (nombre, dorsal, posicion, fecha_nacimiento, jugador_id)
    )

    conexion.commit()
    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        print(f"No se encontró ningún jugador con id {jugador_id}")
    else:
        print(f"Jugador {jugador_id} actualizado correctamente")


def cambiar_estado(jugador_id, nuevo_estado):
    estados_validos = ("disponible", "lesionado", "sancionado")
    if nuevo_estado not in estados_validos:
        print(f"Estado no válido. Usa uno de: {estados_validos}")
        return

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE jugadores SET estado = %s WHERE id = %s;",
        (nuevo_estado, jugador_id)
    )

    conexion.commit()
    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        print(f"No se encontró ningún jugador con id {jugador_id}")
    else:
        print(f"Jugador {jugador_id} marcado como '{nuevo_estado}'")


if __name__ == "__main__":
    pass