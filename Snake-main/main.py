import turtle                           #La libreria turtle ayuda a construir la interfaz gráfica
import time                             #Para obtenier el tiempo
import random                           #Para usar numeros random

posponer = 0.1
puntaje = 0
maxPuntaje = 0

#Configuración
window = turtle.Screen()                #Crea una ventana nueva
window.title('Snake')                   #Ponemos titulo
window.bgcolor('#353535')               #Color de fondo
window.setup(width=600,height=600)      #Redimensionar pantalla
window.tracer(0)                        #Ayuda a hacer la animación mas placentera
