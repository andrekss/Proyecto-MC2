from xml.etree.ElementTree import *
from tkinter import filedialog

class Carga:
    def __init__(self):
        self.vertices = []
        self.EnlacesV = []
        self.Ascendente = True
        self.ruta = ''

    def LeerXML(self):
      self.ruta = filedialog.askopenfilename() #jalamos la ruta
      #self.ruta='/Users/gmg/Desktop/Nueva carpeta (3)/Ejercicio1.xml'  # se necesita una ruta del archivo
      if self.ruta != '':
        try:
         Arbol = parse(self.ruta) #cargamos el archivo en la variable Arbol
         raiz = Arbol.getroot() #entramos a la raíz de todo el archivo que sería Entrada
         contador = 0 
         for lista in raiz: # empezamos a recorrer cada lista del arbol 
            if contador == 0:
               
               if lista.text == 'si':
                  self.Ascendente = False
               if lista.text == 'no':
                  self.Ascendente = True

            elif contador == 1:# lista de vértices
                for vertice in lista:
                    self.vertices.append(vertice.text) # agregamos el vertice en la lista
            elif contador ==2: # ciclamos a la siguiente lista 
                for unidad in lista:
                    Enlaces = []  # hacemos un arreglo para cada unidad
                    for enlaces in unidad: 
                        Enlaces.append(enlaces.text) # agregamos cada enlace  
                    self.EnlacesV.append(Enlaces) #y guardamos ala lista de la unidad respectiva    

            contador+=1    
        except:
         pass  
        
        '''       
        print('---Vertices---')
        for i in range(len(self.vertices)):
            print(self.vertices[i])
        print('-->Enlaces<--')
        for i in range(len(self.EnlacesV)):
            print('unidad',i)
            for j in range(len(self.EnlacesV[i])):
                print(self.EnlacesV[i][j]) '''

