DROP TABLE IF EXISTS valores;

CREATE TABLE valores (
    id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_sensor REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);