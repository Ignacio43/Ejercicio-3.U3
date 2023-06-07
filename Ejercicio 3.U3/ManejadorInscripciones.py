from Inscripcion import Inscripccion
import numpy as np

class ManejadorInscripccion:
    def __init__(self):
        self.__inscripciones=np.array([],dtype=Inscripccion)
        
    def cargarInscripto(self,taller):
        self.__inscripciones=np.append(self.__inscripciones,taller.getInscripto())
        
    def buscaPersona(self,dni):
            for inscripto in self.__inscripciones:
                persona=inscripto.getPersona()
                if persona.getDni()==dni:
                    taller=inscripto.getTaller()
                    print(f"Nombre Taller:{taller.getNom()}  ")
                    if inscripto.getPago()==False:
                        print(f"Monto Adeudado:{taller.getMonto()} ")
                    else:
                        print("No adeuda nada")
    
    def registrarPago(self,dni):
        for inscripto in self.__inscripciones:
            persona=inscripto.getPersona()
            if persona.getDni()==dni:
                inscripto.setPago(True)
        
    def crearArchivo(self):
        archivo=open("datos.csv","w")
        archivo.write("DNI;idTaller;fecha Inscripcion;pago") 
        for inscripto in self.__inscripciones:
            persona=inscripto.getPersona()
            taller=inscripto.getTaller()
            archivo.write(f"{persona.getDni()}  {taller.getIdTaller()}  {inscripto.getFecha()}  {inscripto.getPago()}")    
        archivo.close()
        