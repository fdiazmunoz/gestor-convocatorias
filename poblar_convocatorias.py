from partidos import convocar_jugador

# Partido 1 (vs Unicaja) - se quedan fuera: 13, 14, 15, 16
convocatoria_partido_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Partido 2 (vs Partizan) - se quedan fuera: 1, 2, 9, 10
convocatoria_partido_2 = [3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16]

# Partido 3 (vs Baskonia) - se quedan fuera: 5, 6, 11, 12
convocatoria_partido_3 = [1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 15, 16]

if __name__ == "__main__":
    for jugador_id in convocatoria_partido_1:
        convocar_jugador(1, jugador_id)

    for jugador_id in convocatoria_partido_2:
        convocar_jugador(2, jugador_id)

    for jugador_id in convocatoria_partido_3:
        convocar_jugador(3, jugador_id)