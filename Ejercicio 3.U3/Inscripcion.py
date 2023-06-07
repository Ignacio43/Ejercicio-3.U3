  
class Inscripccion:
    def __init__(self,fechaInscripcion,pago:bool,persona:object,taller:object):
        self.__fechaInscripcion=fechaInscripcion
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller
        
    def getFecha(self):
        return self.__fechaInscripcion    
        
    def setPago(self,pago):
        self.__pago=pago     
    
    def getPago(self):
        return self.__pago    
        
    def getPersona(self):
        return self.__persona 
        
    def getTaller(self):
        return self.__taller