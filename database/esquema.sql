-- jugadores
CREATE TABLE jugadores (
    id              SERIAL PRIMARY KEY,
    nombre          TEXT NOT NULL,
    dorsal          INTEGER NOT NULL,
    posicion        TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    estado          TEXT NOT NULL DEFAULT 'disponible'
);

-- partidos
CREATE TABLE partidos (
    id              SERIAL PRIMARY KEY,
    rival           TEXT NOT NULL,
    fecha           DATE NOT NULL,
    competicion     TEXT NOT NULL,
    local_visitante TEXT NOT NULL
);

-- convocatorias
CREATE TABLE convocatorias (
    partido_id      INTEGER NOT NULL,
    jugador_id      INTEGER NOT NULL,
    PRIMARY KEY (partido_id, jugador_id),
    FOREIGN KEY (partido_id) REFERENCES partidos(id),
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
);

-- minutos_jugados
CREATE TABLE minutos_jugados (
    partido_id      INTEGER NOT NULL,
    jugador_id      INTEGER NOT NULL,
    minutos         INTEGER NOT NULL,
    cuartos_jugados INTEGER NOT NULL,
    PRIMARY KEY (partido_id, jugador_id),
    FOREIGN KEY (partido_id) REFERENCES partidos(id),
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
);

-- alertas_carga
CREATE TABLE alertas_carga (
    id                   SERIAL PRIMARY KEY,
    jugador_id           INTEGER NOT NULL,
    fecha                DATE NOT NULL,
    motivo               TEXT NOT NULL,
    minutos_acumulados   INTEGER NOT NULL,
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
);