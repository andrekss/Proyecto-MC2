from graphviz import *

class algoritmo:
    def __init__(self,Vertices,Enlaces,MayorOMenor):
        self.Vertices = Vertices
        self.Enlaces = Enlaces
        self.dot = Digraph(comment='Grafo', format='pdf')
        self.Pasos = True
        self.pasos = [] # arreglo con el paso a paso del algoritmo
        self.ordenar = []
        self.Menor = 0
        self.Abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.MayorOMenor = MayorOMenor
        
    def Ejecutar(self):
       
       self.LetrasANumeros()
       it = 0
       #Paso 1:  Seleccionamos la etiqueta del vértice con el valor numérico mas pequeño existente
       verticesOrdenados = sorted(self.Vertices,reverse=self.MayorOMenor)# ordenamos de menor a mayor los vértices 
       self.pasos.append(verticesOrdenados[0])    # colocamos el vértice del primer paso 
       self.Menor = self.Vertices.index(verticesOrdenados[0]) # necesitamos el índice para el vértice self.menors
    
       while self.Pasos: 
        #Paso 2
        self.PasoRecursivo(it,True,0)
        it +=1 

       self.NumerosALetras() 
       self.Graficar(True)
       print('Pasos')
       p = 1
       for i in self.pasos:
        print(str(p)+')',i)
        p+=1
       
        
    def Graficar(self,resultados):
       
       for i in range(len(self.Vertices)):
        color = 'yellow'
        if self.pasos[0] == self.Vertices[i]:
           color = 'blue'
        self.dot.node(f'{self.Vertices[i]}', shape='circle', width = '0.1', height= '0.1',fillcolor=f'{color}', style="filled")
       
       conexionesHechas = []
       if resultados:
          for i in range(len(self.pasos)):
            if (i+1) <len(self.pasos): 
             if self.VerificarRepetidos(i+1,self.pasos,True):
              self.dot.edge(f'{self.pasos[i]}',f'{self.pasos[i+1]}',arrowhead='none',color = 'red')
              conexionesHechas.append(f'{self.pasos[i]},{self.pasos[i+1]}') #hecha asi
              conexionesHechas.append(f'{self.pasos[i+1]},{self.pasos[i]}') # o viceversa 
             else:
               continue  

       for i in range(len(self.Enlaces)):  #unidad
          for j in range(len(self.Enlaces[i])):
             pasar = True
             for k in conexionesHechas:
                if f'{self.Vertices[i]},{self.Enlaces[i][j]}' == k or f'{self.Enlaces[i][j]},{self.Vertices[i]}' == k:
                   pasar = False
             if pasar:        
              self.dot.edge(f'{self.Vertices[i]}',f'{self.Enlaces[i][j]}',arrowhead='none',color = 'black')
              conexionesHechas.append(f'{self.Vertices[i]},{self.Enlaces[i][j]}') #hecha asi
              conexionesHechas.append(f'{self.Enlaces[i][j]},{self.Vertices[i]}') # o viceversa
       
       color = 'blue'
       self.dot.node('Inicio', shape='box', width = '0.1', height= '0.1',fillcolor=f'{color}', style="filled")
       self.dot.render('Grafo', view=True)

    def LetrasANumeros(self):      
        for i in range(len(self.Vertices)):
         for j in range(len(self.Abecedario)):
                if self.Vertices[i] == self.Abecedario[j]:
                    self.Vertices[i] = j     
        
        for i in range(len(self.Enlaces)):  #unidad
          for j in range(len(self.Enlaces[i])):
            for k in range(len(self.Abecedario)):
                if self.Enlaces[i][j] == self.Abecedario[k]:
                    self.Enlaces[i][j] = k           

        #self.Imprimir()    

    def Imprimir(self):
        for i in self.Vertices:
            print('vértice '+str(i))

        for i in range(len(self.Enlaces)):
            print('unidad',str(i))
            for j in range(len(self.Enlaces[i])):
                print(self.Enlaces[i][j])

    def VerificarRepetidos(self,i,ordenar,Graficar):
          for j in range(len(self.pasos)):
            if j== i and Graficar:
               break
            if self.pasos[j] == ordenar[i]:

                return False   # si se repite
          return True  # no se repite

    def Retroceso(self):
        i = len(self.pasos)-1
        self.para = True
        while self.para:
            self.Menor = self.Vertices.index(self.pasos[i])
            self.ordenar = sorted(self.Enlaces[self.Menor],reverse=self.MayorOMenor)
            self.PasoRecursivo(1,False,self.pasos[i])
            if i == 0:
                break
            i-=1

    def PasoRecursivo(self,it,mas,actual):
        if it == 0:
         self.ordenar = sorted(self.Enlaces[self.Menor] ,reverse=self.MayorOMenor)  
        
        else:
            #Paso 2 y seguimos la recursividad
            if mas:
             indiceFinal = len(self.pasos)-1
             self.Menor = self.Vertices.index(self.pasos[indiceFinal]) #conseguimios el índice del ultimo paso
             self.ordenar = sorted(self.Enlaces[self.Menor],reverse=self.MayorOMenor) 

        for i in range(len(self.Enlaces[self.Menor])):
          if self.VerificarRepetidos(i,self.ordenar,False):  
           if mas ==False:
            self.pasos.append(actual) 
           self.pasos.append(self.ordenar[i])
           if mas == False:
              self.para = False
              self.Pasos = True
           break 
          elif i == (len(self.Enlaces[self.Menor])-1):
            if mas: 
             self.Pasos = False
             self.Retroceso()
             
            break        

    def NumerosALetras (self):
        
        for i in range(len(self.pasos)):
            for j in range(len(self.Abecedario)):
                if self.pasos[i] == j:
                    self.pasos[i] = self.Abecedario[j]

        for i in range(len(self.Vertices)):
           for j in range(len(self.Abecedario)):
             if self.Vertices[i] == j:
                self.Vertices[i] = self.Abecedario[j]  

        for i in range(len(self.Enlaces)):  #unidad
          for j in range(len(self.Enlaces[i])):
            for k in range(len(self.Abecedario)):
                if self.Enlaces[i][j] == k:
                    self.Enlaces[i][j] = self.Abecedario[k]                        
                