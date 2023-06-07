import csv
from TallerCapacitacion import TallerCapacitacion
import numpy as np
from Inscripcion import Inscripciones 

      
class ManejadorTaller:
    def __init__(self):
        self.__talleres=np.array([],dtype=TallerCapacitacion)
        
    def cargarTalleres(self):
        archivo=open("talleres.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            taller=TallerCapacitacion(int(fila[0]),fila[1],int(fila[2]),int(fila[3]))
            self.__talleres=np.append(self.__talleres,taller)
        archivo.close()
        
    def mostrarTalleres(self):
        for i in self.__talleres:
            print(i)
            
    def TallerElegido(self,taller):
        i=0
        while i<len(self.__talleres) and self.__talleres[i].getNom()!=taller:
            i+=1
        if i<len(self.__talleres):
            return self.__talleres[i]
        
    def buscarId(self,idTaller):
        i=0
        while i<len(self.__talleres)and self.__talleres[i].getIdTaller()==idTaller:
            i+=1
        if i<len(self.__talleres):
            return self.__talleres[i]
    
    def listarAlumnos(self,taller):
        Inscripciones=taller.getInscriptos()
        for inscripto in Inscripciones:
            persona=inscripto.getPersona()
            print(f"{persona}")