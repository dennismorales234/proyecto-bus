

"""
 Nombre: leer_datos
 Entrada: nombre del archivo (str)
 Salida: matriz con los datos del archivo
 Restricciones: el archivo debe existir o retornará lista vacía
"""
def leer_datos(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        contenido = []
        linea = archivo.readline()
        while linea != "":
            # .strip() elimina el salto de línea al final y .split(";") separa el usuario de la clave
            datos_linea = linea.strip().split(";") 
            
            # .append() agrega la lista [usuario, clave] entera creando una matriz
            contenido.append(datos_linea) 
            
            linea = archivo.readline()
        archivo.close()
        return contenido
    except:
        return []

def menu_principal():
    while True:
        print("\n=== SISTEMA DE BUSES TEC ===")
        print("1. Opciones Administrativas")
        print("2. Opciones de Usuario")
        print("3. Salir")
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            if validar_acceso():
                menu_administrativo()
        elif opcion == "2":
            menu_usuario() 
        elif opcion == "3":
            print("Cerrando sistema... ¡Buen viaje!")
            break
           
"""
 Nombre: validar_acceso
 Entrada: ninguna (pide datos por teclado)
 Salida: booleano según éxito del login
 Restricciones: requiere archivo acceso.txt con datos válidos
"""
def validar_acceso():
    print("\n--- CONTROL DE ACCESO ---")
    u_input = input("Usuario: ")
    c_input = input("Clave: ")
    usuarios = leer_datos("acceso.txt")
    
    for u in usuarios:
        if u[0] == u_input and u[1] == c_input:
            print("Acceso concedido.")
            return True
    print("Usuario o clave incorrectos.")
    return False
def menu_administrativo():
    print ("alto pro")
    
    print( "(11) Gestión de modelos de autobús " )
    print( "(12) Gestión de unidades" )
    print( "(13) Gestión de conductores")

    menu = input("seleccione ")

    
if __name__ == "__main__":
    menu_principal()
    
