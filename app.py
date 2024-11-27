import sqlite3
from flask import Flask, request

def init_db():
    conn = sqlite3.connect('sensor.sqlite')
    c = conn.cursor()
    # Crear la tabla si no existe
    c.execute('''
              CREATE TABLE IF NOT EXISTS valores (
              id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
              valor_sensor REAL NOT NULL,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
              ''')
    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente")

app = Flask(__name__)
with app.app_context():
        init_db()



@app.route('/mediciones', methods=['POST'])
def mediciones():
    valor_sensor = request.form.get('valor_sensor', type=float)
    if valor_sensor is not None:
        conn = sqlite3.connect('sensor.sqlite')
        c = conn.cursor()
        c.execute("INSERT INTO valores (valor_sensor) VALUES (?)", (valor_sensor,))
        conn.commit()
        conn.close()
        return 'Datos registrados correctamente'
    else:
        return 'No se recibió ningún valor de sensor'

if __name__ == '__main__':
    with app.app_context():
            init_db()
    app.run(host='0.0.0.0', port=5000)
