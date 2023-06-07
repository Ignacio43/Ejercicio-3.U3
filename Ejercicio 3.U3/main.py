
from ManejadorTaller import ManejadorTaller
from ManejadorInscripciones import ManejadorInscripccion
from ManejadorPersonas import ManejadorPersona
        
if __name__=='__main__':
    manejaTaller=ManejadorTaller()
    manejaTaller.cargarTalleres()
    
    manejaPersona=ManejadorPersona()
    
    manejaInscripcion=ManejadorInscripccion()
    
    print("1.     Cargar los datos de los talleres")
    print("2.     Inscribir una persona en un taller")
    print("3.     Consultar inscripción")
    print("4.     Consultar inscriptos")
    print("5.     Registrar pago")
    print("6.     Guardar inscripciones")
    
    op=int(input("ingrese opcion a cargar: "))
    
    while op != 0:
        if op == 1:
            persona=manejaPersona.cargarPersonas()
            manejaTaller.mostrarTalleres()
            buscaTaller=input("ingrese nombre del taller que desea")
            taller=manejaTaller.TallerElegido(buscaTaller)
            
            taller.cargarInscripcion(persona)
            manejaInscripcion.cargarInscripto(taller)
        elif op == 2:
            dni=input("ingrese dni de la persona buscada: ")
            manejaInscripcion.buscaPersona(dni)
        elif op == 3:
            identificadorTaller=int(input("ingrese identificador de taller a buscar:  "))
            taller=manejaTaller.buscarId(identificadorTaller)
            manejaTaller.listarAlumnos(taller)
        elif op == 4:
            dni=int(input("ingrese dni de la persona: "))
            manejaInscripcion.registrarPago(dni)
        elif op == 5:
            manejaInscripcion.crearArchivo()
        else:
            print("opcion incorrecta .")
        
        print("1.     Cargar los datos de los talleres")
        print("2.     Inscribir una persona en un taller")
        print("3.     Consultar inscripción")
        print("4.     Consultar inscriptos")
        print("5.     Registrar pago")
        print("6.     Guardar inscripciones")
        
        op=int(input("ingrese opcion a cargar: "))
        