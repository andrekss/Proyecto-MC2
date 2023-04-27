from tkinter import *
from CargarXML import *
from Algoritmo import *
import sys

car = Carga()

ancho = 15
alto = 2
centrado = 180
inicial = 70

selector = Tk()

Opciones = Label(selector, text="Algoritmo Busqueda a Profundidad")
Opciones.config(font=("Times New Roman",16))
Opciones.pack()

selector.geometry("500x300+450+100") 
selector.title("Proyecto 1")
selector.config(bg="orange")

archivo = Button(selector, text="Cargar")
archivo.config(font=("Arial",13),width=ancho,height=alto,command=car.LeerXML )

Ayuda = Button(selector, text="Resultado")                                           # si es false será Ascendente, de lo contrario irá descendente
Ayuda.config(font=("Arial",13),width=ancho,height=alto,command=lambda:algoritmo(car.vertices,car.EnlacesV,car.Ascendente).Ejecutar())

salir = Button(selector, text="Salir")
salir.config(font=("Arial",13),width=ancho,height=alto,command=sys.exit) 

archivo.place(x=centrado,y=inicial)
Ayuda.place(x=centrado,y=2*inicial)
salir.place(x=centrado,y=3*inicial)


selector.mainloop()