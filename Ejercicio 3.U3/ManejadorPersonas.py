from Persona import Persona

class ManejadorPersona:
    def __init__(self):
        self.__personas=[]
        
    def cargarPersonas(self):
        nombre=input("ingrese nombre de la persona: ")
        direccion=input("ingrese direccion: ")
        dni=input("ingrese dni: ")
        persona=Persona(nombre,direccion,dni)
        self.__personas.append(persona)
        return persona