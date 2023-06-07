class Persona:
    def __init__(self,nombre,direccion,dni):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__dni=dni
        
    def getDni(self):
        return self.__dni
    
    def __str__(self):
        return f"{self.__nombre:<20}{self.__direccion:<30}{self.__dni}"