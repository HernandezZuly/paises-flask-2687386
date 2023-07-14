from flask import Flask
#Se define la variabe con un objeto de la clase flask
app = Flask(__name__)

#Creacion de ruta
@app.route('/')
#Función
def index():
    return 'Hola 2687386'