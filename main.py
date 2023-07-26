from flask import Flask, render_template
#Se define un objeto de la clase flask
app = Flask(__name__)

#Creacion de ruta con ayuda de la palabra route
@app.route('/hola')
#Función
def hola():
    return 'Hola'
#creación de otra ruta
@app.route('/paises')
def paises():
    '''Lista en python'''
    #Se crea la lista
    '''paises = [
        'Colombia',
        'Perú',
        'Argentina',
        'Chile',
        'Bolivia',
        'Brasil',
        'Honduras'
    ]'''
    
    #Multilistas
    """paises = [
        [
            'Colombia',
            'Brasil',
            'Chile'
        ],
        [
            'Corea',
            'China',
            'Japón'
        ],
        [
            'Irlanda',
            'Francia',
            'España'
        ],
        [
            'Nigeria',
            'Egipto',
            'Congo'
        ]
    ]"""
    
    
    #Diccionario
    
   '''paises = [
        [
            {
                "nombre" : "América",
                "paises" : [
                    "Colombia",
                    "Perú",
                    "Brasil"
                ]
            }    
        ],
        [
        {
                "nombre" : "Europa",
                "paises" : [
                    "Francia",
                    "Italia",
                    "Irlanda"
                ]
            }    
        ],
        [
            {
                "nombre" : "Asia",
                "paises" : [
                    "Japón",
                    "China",
                    "Corea"
                ]
            }
        ],
        [
            {
                "nombre" : "África",
                "paises" : [
                    "Nigeria",
                    "Egipto",
                    "Congo"
                ]
            } 
        ]
    ]'''
    
    '''variables de conteo para cada continente'''
    '''contador_paises_america = 0
    for pais in paises[0][0]["paises"]:
        contador_paises_america = contador_paises_america + 1
    
    contador_paises_europa = 0
    for pais in paises[1][0]["paises"]:
        contador_paises_europa = contador_paises_europa + 1
    
    contador_paises_asia = 0
    for pais in paises[2][0]["paises"]:
        contador_paises_asia = contador_paises_asia + 1
    
    contador_paises_africa = 0
    for pais in paises[3][0]["paises"]:
        contador_paises_africa = contador_paises_africa + 1'''
    
    #ESTRUCTURA TAREA 
    continentes = [
        {
            "nombre" : "America",
            "paises" : [
                { 
                    "nombre" : "Colombia", 
                    "capital" : "Bogotá",
                    "moneda" : "Peso",
                    "poblacion" : 52,
                    "superficie" : 1142 
                },
                { 
                    "nombre" : "Perú",
                    "capital" : "Lima",
                    "moneda" : "Sol",
                    "poblacion" : 34,  
                    "superficie" : 1285
                },
                { 
                    "nombre" : "Brasil",
                    "capital" : "Brazilia",
                    "moneda" : "Real Brasileño",
                    "poblacion" : 214,  
                    "superficie" : 8 
                }
            ]
        },
        {
            "nombre" : "Europa",
            "paises" : [
                {
                    "nombre" : "Francia",
                    "capital" : "Paris",
                    "moneda" : "Euro",
                    "poblacion" : 68,
                    "superficie" : 551
                },
                {
                    "nombre" : "Italia",
                    "capital" : "Roma",
                    "moneda" : "Euro",
                    "poblacion" : 59,
                    "superficie" : 302 
                },
                {
                    "nombre" : "Irlanda",
                    "capital" : "Dublín",
                    "moneda" : "Euro",
                    "poblacion" : 5,
                    "superficie" : 70 
                }
            ]
        },
        {
            "nombre" : "Asia",
            "paises" : [
                {
                    "nombre" : "Japón",
                    "capital" : "Tokio",
                    "moneda" : "Yen",
                    "poblacion" : 125,
                    "superficie" : 378
                },
                {
                    "nombre" : "China",
                    "capital" : "Hong-Kong",
                    "moneda" : "Yuan",
                    "poblacion" : "1412 miles de millones",
                    "superficie" : 9600 
                },
                {
                    "nombre" : "Corea",
                    "capital" : "Seúl",
                    "moneda" : "Won",
                    "poblacion" : 52,
                    "superficie" : 100 
                }
            ]
        },
        {
            "nombre" : "África",
            "paises" : [
                {
                    "nombre" : "Nigeria",
                    "capital" : "Abuya",
                    "moneda" : "Naira",
                    "poblacion" : 214,
                    "superficie" : 923
                },
                {
                    "nombre" : "Egipto",
                    "capital" : "El Cairo",
                    "moneda" : "Libra Egipcia",
                    "poblacion" : 109,
                    "superficie" : 1002 
                },
                {
                    "nombre" : "Congo",
                    "capital" : "Brazzaville",
                    "moneda" : "Franco Congoleño",
                    "poblacion" : 6,
                    "superficie" : 2345 
                }
            ]
        }
    ]
    
    '''variables de conteo para cada continente'''
    contador_paises_america = 0
    for pais in paises[0]["continentes"]:
        contador_paises_america = contador_paises_america + 1
    
    contador_paises_europa = 0
    for pais in paises[1]["continentes"]:
        contador_paises_europa = contador_paises_europa + 1
    
    contador_paises_asia = 0
    for pais in paises[2]["continentes"]:
        contador_paises_asia = contador_paises_asia + 1
    
    contador_paises_africa = 0
    for pais in paises[3]["continentes"]:
        contador_paises_africa = contador_paises_africa + 1
    
    user = 'Zuly Ballesteros'
    #Para que retorno a una vista
    return render_template('paises_lista.html', 
                           user = user, 
                           continentes = continentes,
                           america = contador_paises_america, 
                           europa = contador_paises_europa,
                           asia = contador_paises_asia,
                           africa = contador_paises_africa)

