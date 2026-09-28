#PRUEBA PROYECTO
def experimento(nuevo):
    print( "(1) Opciones Administrativas" )
    print( "(2) Opciones de Usuario" )
    print( "(3) Salir")

    opcion = input("seleccione ")

    if opcion == "1":
        validar_acceso()
        
    elif opcion == "2":
        menu_usuario() 
    elif opcion == "3":
        print("Cerrando sistema... ¡Buen viaje!")
           
def validar_acceso():
    usuario = input("usuario ")
    clave = input("clave ")
    contra = "pperez"
    if not usuario == contra: #and clave != "1234":
        print("no eres un admin fuchele")
    else:
        menu_administrativo()
def menu_administrativo():
    print ("alto pro")
    
    print( "(11) Gestión de modelos de autobús " )
    print( "(12) Gestión de unidades" )
    print( "(13) Gestión de conductores")

    menu = input("seleccione ")

    
