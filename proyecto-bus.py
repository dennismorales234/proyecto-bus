

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
"""
# Nombre: existe_en_lista
# Entrada: elemento a buscar, la lista y el índice de la columna
# Salida: booleano (True si existe, False si no)
# Restricciones:
"""

def existe_en_lista(elemento, lista, indice):
    
    encontrado = False
    for sublista in lista:
        if sublista[indice] == elemento:
            encontrado = True
            break
    return encontrado
"""
 Nombre: guardar_datos
 Entrada: nombre del archivo (str) y la matriz de datos
 Salida: ninguna (escribe en disco)
 Restricciones: la matriz debe ser una lista de lista
"""
def guardar_datos(nombre_archivo, matriz):
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    for fila in matriz:
        linea_texto = ""
        for i in range(len(fila)):
            if i == len(fila) - 1:
                linea_texto = linea_texto + fila[i]
            else:
                linea_texto = linea_texto + fila[i] + ";"
        archivo.write(linea_texto + "\n")
    archivo.close()


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
        if opcion == "11":
            return gestionar_modelos()
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

def gestionar_modelos():
    while True:
        print("\n--- GESTIÓN DE TIPOS (MODELOS) ---")
        print("1. Incluir modelo | 2. Mostrar modelos | 3. Regresar")
        op = input("Seleccione: ")
        modelos = leer_datos("modelos.txt")
        
        if op == "1":
            nombre = input("Nombre de la marca: ")
            if not existe_en_lista(nombre, modelos, 0):
                modelos = modelos + [[nombre]]
                e = input("Asientos : ")
                t = input("Asientos pie: ")
                modelos = modelos + [[ e, t]]
                guardar_datos("modelo.txt", modelos)
                print("Modelo registrado.")
            else: print("Error: Modelo ya existe.")
        elif op == "2":
            for mod in modelos:
                print(f" Modelo: {mod[1]} | Asientos: {mod[2]} Asientos pie {mod[2]}")
        elif op == "3": break
           

def menu_administrativo():
    
    print( "(11) Gestión de modelos de autobús" )
    print( "(12) Gestión de unidades" )
    print( "(13) Gestión de conductores" )
    print( "(14) Gestión de rutas" )
    print( "(15) Gestión de paradas por ruta" )
    print( "(16) Programación de salidas" )
    print( "(17) Consultar historial de abordajes" )
    print( "(18) Regresar al menú principal" )

    menu = input("seleccione ")

    if menu == "18":
        return menu_principal()
    if menu == "11":
        return gestionar_modelos()
if __name__ == "__main__":
    menu_principal()
    
