from turtle import *
from freegames import vector

#Dibuja un línea del punto start al punto end
def line(start, end):
    "Draw line from start to end."
    up()#Deja de dibujar la línea actual
    goto(start.x, start.y)#Posiciona el inicio de la línea en las coordenadas start
    down()#Inicia una nueva línea
    goto(end.x, end.y)#Dibuja una línea a las ccordenadas finales

#Dibuja un cuadrado cuyo lado es del tamaño de la diferencia entre las coordenadas x de start y end
def square(start, end):
    "Draw square from start to end."
    up()#Deja de dibujar la línea actual
    goto(start.x, start.y)#Posiciona el inicio de la línea en las coordenadas start
    down()#Inicia una nueva línea
    begin_fill()#Iniciar una figura
    #Dibuja cada uno de los lados
    for count in range(4):
        forward(end.x - start.x)#Dibuja una línea con la longitud dada
        left(90)#Gira 90° a la izquierda

    end_fill()#Terminar figura

#Dibujo un círculo con altura de la diferencia entre las coordenadas en y & un ancho de la diferencia entre las coordenadas en x
def circles(start, end):
    "Draw circle from start to end."
    up() #Deja de dibujar la línea actual
    goto(start.x, start.y) #Posiciona el inicio de la línea en las coordenadas start
    down() #Inicia una nueva línea
    begin_fill()#Iniciar una figura
    circle(end.x - start.x) #Iniciar una figura con el radio elegido
    end_fill()#Terminar figura

#Dibuja un rectangulo
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()#Deja de dibujar la línea actual
    goto(start.x, start.y)#Posiciona el inicio de la línea en las coordenadas start
    down()#Inicia una nueva línea
    sizes=[end.x-start.x,
           end.y-start.y] #Un array con las posibles longitudes
    begin_fill()#Iniciar una figura
    #Dibuja cada uno de los lados
    for i in range(4):
        forward(sizes[i%2])#Elegir las longitudes de forma alternada
        left(90)#Girrar a la izquierda
    end_fill()#Terminar figura

#Dibujo un triángulo recto, cuyos lados iguales son la diferencia entre las coordenadas en x de start y end
def triangle(start, end):
    "Draw triangle from start to end."
    up()#Deja de dibujar la línea actual
    goto(start.x, start.y)#Posiciona el inicio de la línea en las coordenadas start
    down()#Inicia una nueva línea
    sizes=[end.x-start.x,
           end.x-start.x,
           (end.x-start.x)*(2**(1/2))] #Un array con las posibles longitudes
    angles=[90,45+90,90] #Un array con los posibles ángulos
    begin_fill()#Iniciar una figura
    for i in range(3):
        forward(sizes[i])#Elegir la longitud correspondiente
        left(angles[i])#Gira a la izquierda con el ángulo correspondiente
    end_fill()#Terminar figura

#Guarda la posición del mouse cuando se de click
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']#Guardar el valor actual de start

    if start is None:#Si está vacio, por lo tanto, es el primer click
        state['start'] = vector(x, y)#Guardarlo
    else:#Si es el segundo click
        shape = state['shape']#Guardar la figura seleccionada
        end = vector(x, y)#Guardar la posición actual como end
        shape(start, end)#Generar la figura seleccionada
        state['start'] = None#Reinicializar el valor
#Cambiar un valor de un parámetro del diccionario
def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}#Incializar diccionario
setup(420, 420, 370, 0)#Crear ventana
onscreenclick(tap)#Guardar el click
listen()#Detectar entradas de teclado
onkey(undo, 'u')
#Cambios de color
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'),'Y')
onkey(lambda: color('pink'),'P')

#Cambios de figura
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circles), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()#Finalizar