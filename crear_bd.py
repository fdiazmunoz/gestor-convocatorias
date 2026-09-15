from conexion import obtener_conexion
import os

RUTA_ESQUEMA = os.path.join("database", "esquema.sql")

def crear_base_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    with open(RUTA_ESQUEMA, "r", encoding="utf-8") as archivo:
        script_sql = archivo.read()

    cursor.execute(script_sql)
    conexion.commit()

    cursor.close()
    conexion.close()
    print("Tablas creadas correctamente en PostgreSQL.")

if __name__ == "__main__":
    crear_base_datos()