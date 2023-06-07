from Inscripcion import Inscripcion

class TallerCapacitacion:
    def __init__(self,idTaller:int,nombreTaller,vacantes:int,montoInscripcion:int):
        self.__idTaller=idTaller
        self.__nombreTaller=nombreTaller
        self.__vacantes=vacantes
        self.__montoInscripcion=montoInscripcion
        self.__PerIns=[]
        
    def getNom(self):
        return self.__nombreTaller    
        
    def getIdTaller(self):
        return self.__idTaller
        
    def getMonto(self):
        return self.__montoInscripcion
        
    def modVacantes(self):
        self.__vacantes-=1
        
    def getInscripto(self):
        return self.__PerIns[-1] 
    
    def getInscriptos(self):
        return self.__PerIns
        
    def cargarInscripcion(self,persona):
        fecha=input("ingresar fecha de inscripcion: ")
        inscripto=Inscripcion(fecha,False,persona,self)
        self.__PerIns.append(inscripto)    
        
        
    def __str__(self):
        return f"{self.__idTaller:<10} {self.__nombreTaller} "
        