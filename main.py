from cProfile import label
from logging.handlers import RotatingFileHandler
from pickle import GLOBAL
from random import randrange
from struct import pack
from textwrap import fill
from tkinter import *

GAME_HEIGHT = 400
GAME_WIDTH = 200
BLOCK_SIZE = 20
PUNTUACION = 0
DIRECCION = ""
ROTATE = 0
FORMA = 0
SPEED = 300
# Posicion ficha jugador:
POSJUGADORX = 0
POSJUGADORY = 0

BACKGROUND_COLOUR = "green"
BLOCK_COLOUR = "grey"
USER_BLOCK_COLOUR = "red"

class Tetris():
    def __init__(self):
        self.listamapa = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        ]
        self.listamapa_usuario = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.cuadrado = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
        self.L = [[0, 3, 6, 7], [2, 5, 7, 8], [0, 1, 3, 6], [1, 2, 5, 8]]
        self.linea = [[0, 1, 2], [6, 7, 8], [0, 3, 6], [2, 5, 8]]
        self.Ldoble = [[0, 1, 4, 7, 8], [1, 2, 4, 6, 7], [0, 3, 4, 5, 8], [2, 3, 4, 5, 6]]
        self.formas = [self.cuadrado, self.L, self.linea, self.Ldoble]

def FormaAleatoria():
    global FORMA
    FORMA = randrange(0, 4)
        
def GuardarDatosForma(x, y):
    listayrotacion = tetris.formas[FORMA][ROTATE]# cogemos la lista aletoria con la forma y rotacion deseada
    print(str(listayrotacion))
    x_pixeles = x
    y_pixeles = y
    x_pixeles_f2 = x
    y_pixeles_f2 = y+1
    x_pixeles_f3 = x
    y_pixeles_f3 = y+2

    

    for i in listayrotacion: # miramos cada valor de esta lista
        if i == 0 or i == 3 or i == 6:
            x_pixeles = x

        if i == 1 or i == 4 or i == 7:
            x_pixeles = x + 1

        if i == 2 or i == 5 or i == 8:
            x_pixeles = x + 2

        if i >= 0 and i <= 2:
            # Gaurdamos la primera linea con valores 1 si el valor de nuestra "lista" forma es mayor que 1 
            tetris.listamapa_usuario[y_pixeles][x_pixeles] = 1
        elif i >= 3 and i <= 5:
            # Si el valor del la lista de la forma es mayor a 4 entonces es en la segunda linea ya que la forma es 4x4
            tetris.listamapa_usuario[y_pixeles_f2][x_pixeles] = 1
        elif i >= 6 and i <= 8:
            tetris.listamapa_usuario[y_pixeles_f3][x_pixeles] = 1



def ImprimirListaFondo():
    contador_columna = 0
    contador_fila = 0
    length = len(tetris.listamapa)
    for i in range(length):
        contador_fila = i

        for j in tetris.listamapa[i]:
            if j == 0:
                canvas.create_rectangle((contador_columna*20), (i*20), ((contador_columna*20)+BLOCK_SIZE), ((i*20)+BLOCK_SIZE), fill="grey")
                #tetris.cuadrados_canvas.append(cuadrado)
            elif j == 1:
                canvas.create_rectangle((contador_columna*20), (i*20), ((contador_columna*20)+BLOCK_SIZE), ((i*20)+BLOCK_SIZE), fill="green")
                #tetris.cuadrados_canvas.append(cuadrado2)
            contador_columna = contador_columna + 1
        contador_columna = 0

def ImprimirListaFrente():
    contador_columna = 0
    contador_fila = 0
    length = len(tetris.listamapa_usuario)
    for i in range(length):
        contador_fila = i
        for j in tetris.listamapa_usuario[i]:
            if j == 0:
                None # Haz nada si el valor de lista es 0
            elif j == 1:
                canvas.create_rectangle((contador_columna*20), (i*20), ((contador_columna*20)+BLOCK_SIZE), ((i*20)+BLOCK_SIZE), fill="red", tags="figurafrente")
                #tetris.cuadrados_canvas.append(cuadrado2)
            contador_columna = contador_columna + 1
        contador_columna = 0

def ColisionEntreListas(listafrente, listafondo):
    #Aqui comprobamos si alguna pieza de la lista colisiona con la lista del fondo con +1 vertical
    contador_columna = 0
    contador_fila = 0
    length = len(listafrente)# Contamos cuantas listas hay en la lista para saber las filas
    for i in range(length):
        contador_fila = i# i es filas

        for j in listafrente[i]:# miramos cada dato en la lista de frente con referncia a => i
            contador_columna = contador_columna + 1# contador de columnas
            #print(str(contador_fila) + " Y el dato es: " + str(j) + " Columna: " + str(contador_columna-1))
            if (j == 1 and j == listafondo[(contador_fila)+1][(contador_columna-1)]): # Miramos si el valor del dato es 1 y comprobamos si es tambien el caso en la lista del fondo pero con +1 verticalmente para ver si colisiona con la pieza de abajo
                return True
                break

        contador_columna = 0

def BloqueFueraMapaDerecha(listafrente):
    #En esta funcion comprobaremos cada bloque individual si esta fuera del mapa horizontalmente a la derecha
    contador_columna = 0
    contador_fila = 0
    length = len(listafrente)# Contamos cuantas listas hay en la lista para saber las filas
    for i in range(length):
        contador_fila = i# i es filas => vertical

        for j in listafrente[i]:# miramos cada dato en la lista de frente con referncia a => i

            if j == 1 and contador_columna == 9:
                return True
                break
            contador_columna = contador_columna + 1# contador de columnas
        contador_columna = 0

def BloqueFueraMapaIzquierda(listafrente):
    #En esta funcion comprobaremos cada bloque individual si esta fuera del mapa horizontalmente a la izquierda
    contador_columna = 0
    contador_fila = 0
    length = len(listafrente)# Contamos cuantas listas hay en la lista para saber las filas
    for i in range(length):
        contador_fila = i# i es filas => vertical

        for j in listafrente[i]:# miramos cada dato en la lista de frente con referncia a => i
            if (j == 1) and (contador_columna == 0):
                return True
                break
            contador_columna = contador_columna + 1# contador de columnas
        contador_columna = 0

def ColisionDentroLista(listafrente, listafondo):
    contador_columna = 0
    contador_fila = 0
    length = len(listafrente)# Contamos cuantas listas hay en la lista para saber las filas
    for i in range(length):
        contador_fila = i# i es filas => vertical

        for j in listafrente[i]:# miramos cada dato en la lista de frente con referncia a => i
            contador_columna = contador_columna + 1# contador de columnas
            #print(str(contador_fila) + " Y el dato es: " + str(j) + " Columna: " + str(contador_columna-1))
            if (j == 1 and j == listafondo[(contador_fila)][(contador_columna-1)]): # Miramos si el valor del dato es 1 y comprobamos si es tambien el caso en la lista del fondo pero con +1 verticalmente para ver si colisiona con la pieza de abajo
                return True
                break
        contador_columna = 0

def ListaFrenteColisionaFinal(listafrente, listafondo):
    contador_columna = 0
    contador_fila = 0
    length = len(listafrente)# Contamos cuantas listas hay en la lista para saber las filas
    for i in range(length):
        contador_fila = i# i es filas

        for j in listafrente[i]:# miramos cada dato en la lista de frente con referncia a => i
            contador_columna = contador_columna + 1# contador de columnas
            #print(str(contador_fila) + " Y el dato es: " + str(j) + " Columna: " + str(contador_columna-1))
            # tambien vamos a aprovechar este codigo para una vez comprobado si hay colision entre las dos listas de manera verical comprobar si algun elemento de la lista usuario esta en la ultima fila la (19)
            if j == 1 and i == 19:
                print("Colision ultima fila!")
                return True
                break
        contador_columna = 0

def left(event):
    global DIRECCION
    DIRECCION = "left"

def right(event):
    global DIRECCION
    DIRECCION = "right"

def rotate(event):
    global ROTATE
    ROTATE = ROTATE + 1
    if ROTATE > 3:
        ROTATE = 0

def EliminarContenidoLista():
    #Eliminamos todo el contenido de la lista mapa jugador
    contador = 0
    filas = len(tetris.listamapa_usuario)
    for i in range(filas):
        for j in tetris.listamapa_usuario[i]:
            if j == 1:
                tetris.listamapa_usuario[i][contador] = 0
            contador = contador + 1
        contador = 0
    canvas.delete("figurafrente")

def NuevaPieza():
    global POSJUGADORX
    global POSJUGADORY
    POSJUGADORY = 0
    POSJUGADORX = 4

def LineaCompleta():
    global PUNTUACION
    total = 0
    vertical = len(tetris.listamapa)
    for j in range(vertical):
        for i in tetris.listamapa[j]:
            total = total + i
            if total >= 10:
                print("llega aqui")
                PUNTUACION = PUNTUACION + 1
                tetris.listamapa.pop(j)
                tetris.listamapa.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        total = 0

def GameOver(listafondo):
    #Aqui miramos si algun elemento de la lista fondo llega al nivel 3 de altura lo cual el juego acaba
    vertical = len(listafondo)
    total = 0
    for j in range(vertical):
        for i in listafondo[j]:
            total = total + i
            if total == 3 and j < 4:
                #Game over
                return True
        total = 0

def Ganas():
    if PUNTUACION == 10:
        canvas.delete(ALL)
        canvas.create_text(200, 200, fill="green", font=("consolas", 70), text="HAS GANADO!")

def ElementosListaALista():
    #En esta funcion el objetivo es coger todos los elementos de la lista mapa usuario y copiarlos al la => lista fondo
    contador = 0
    filas = len(tetris.listamapa_usuario)
    for i in range(filas):
        for j in tetris.listamapa_usuario[i]:
            if j == 1:
                tetris.listamapa[i][contador] = 1
            contador = contador + 1
        contador = 0


def BucleJuego():
    global POSJUGADORY # referencia a todas nuestras variables y strings globales
    global POSJUGADORX
    global DIRECCION

    GameOver(tetris.listamapa)

    if ListaFrenteColisionaFinal(tetris.listamapa_usuario, tetris.listamapa) == True:
        ElementosListaALista()
        EliminarContenidoLista()
        LineaCompleta()
        FormaAleatoria()
        NuevaPieza()

    if ColisionEntreListas(tetris.listamapa_usuario, tetris.listamapa) == True:
        ElementosListaALista()
        LineaCompleta()
        FormaAleatoria()
        NuevaPieza()
    

    #Limpieza de nuevo ciclo en pantalla eliminamos lista del usuario y liberamos ram de las imagenes de todo
    canvas.delete(ALL)
    EliminarContenidoLista() # Eliminamos contenido de la lista si hay algun 1 ahora es 0
    ImprimirListaFondo() # Imprimos 1 de la => lista fondo

    POSJUGADORY = POSJUGADORY + 1 #cada turno se mueve 1 movimiento abajo
    GuardarDatosForma(POSJUGADORX, POSJUGADORY)

    if (DIRECCION == "left"):
        if BloqueFueraMapaIzquierda(tetris.listamapa_usuario) == True: # En caso que uno de los bloques este en el borde no permitimos mover 
            None
        else:
            POSJUGADORX = POSJUGADORX - 1
            EliminarContenidoLista()
            GuardarDatosForma(POSJUGADORX, POSJUGADORY)
            DIRECCION = ""
            if ColisionDentroLista(tetris.listamapa_usuario, tetris.listamapa) == True:
                POSJUGADORX = POSJUGADORX + 1 #Revertimos cambio en caso que al mover el bloque del jugaodr entre dentro de otra pieza de la lista del fondo
                EliminarContenidoLista()
                GuardarDatosForma(POSJUGADORX, POSJUGADORY)
    elif DIRECCION == "right":
        if BloqueFueraMapaDerecha(tetris.listamapa_usuario) == True: # En caso que uno de los bloques este en el borde no permitimos mover 
            None
        else:
            POSJUGADORX = POSJUGADORX + 1
            EliminarContenidoLista()
            GuardarDatosForma(POSJUGADORX, POSJUGADORY)
            if ColisionDentroLista(tetris.listamapa_usuario, tetris.listamapa) == True:
                POSJUGADORX = POSJUGADORX - 1 #Revertimos cambio en caso que al mover el bloque del jugaodr entre dentro de otra pieza de la lista del fondo
                EliminarContenidoLista()
                GuardarDatosForma(POSJUGADORX, POSJUGADORY)
            DIRECCION = ""


    GuardarDatosForma(POSJUGADORX, POSJUGADORY) # Guardamos ficha jugador en la lista del usuario

    ImprimirListaFrente() # Imprimimos la lista de usuario
    canvas.create_text(300, 100, fill="red", font=("consolas", 15), text="Puntuacion: " + str(PUNTUACION))
    if GameOver(tetris.listamapa) == True:
        canvas.delete(ALL)
        canvas.create_text(200, 200, fill="red", font=("consolas", 40), text="GAME OVER")
    elif PUNTUACION == 10:
        Ganas()
    else:
        window.after(SPEED, BucleJuego)


tetris = Tetris()

window = Tk()
window.title("Tetris Juego")
window.resizable(False, False)
foto = PhotoImage(file="tetrislogo2.png")
window.iconphoto(False, foto)
canvas = Canvas(window, height=GAME_HEIGHT-1, width=(GAME_WIDTH*2)-1, bg="blue")
canvas.pack()

label = Label(window, text=("Puntacion:" + str(PUNTUACION)))

FormaAleatoria()
BucleJuego()

window.update()
window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", rotate)

window.mainloop()