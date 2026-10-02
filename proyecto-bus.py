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
            datos_linea = linea.strip().split(";") 
            contenido.append(datos_linea) 
            linea = archivo.readline()
        archivo.close()
        return contenido
    except:
        return []

"""
 Nombre: existe_en_lista
 Entrada: elemento a buscar, la lista y el índice de la columna
 Salida: booleano (True si existe, False si no)
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
"""
def guardar_datos(nombre_archivo, matriz):
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    for fila in matriz:
        linea_texto = ""
        for i in range(len(fila)):
            if i == len(fila) - 1:
                linea_texto = linea_texto + str(fila[i])
            else:
                linea_texto = linea_texto + str(fila[i]) + ";"
        archivo.write(linea_texto + "\n")
    archivo.close()

"""
 Nombre: validar_acceso
 Entrada: ninguna (pide datos por teclado)
 Salida: booleano según éxito del login
"""
def validar_acceso():
    print("\n--- CONTROL DE ACCESO ---")
    u_input = input("Usuario: ")
    c_input = input("Clave: ")
    usuarios = leer_datos("acceso.txt")
    
    for u in usuarios:
        # Se usa .strip() para limpiar posibles espacios en la contraseña leída del disco
        if u[0].strip() == u_input and u[1].strip() == c_input:
            print("Acceso concedido.")
            return True
    print("Usuario o clave incorrectos.")
    return False

# ==========================================
# (11) GESTIÓN DE MODELOS
# ==========================================
def gestionar_modelos():
    while True:
        print("\n--- (11) GESTIÓN DE MODELOS DE AUTOBÚS ---")
        print("1. Incluir | 2. Mostrar | 3. Modificar | 4. Eliminar | 5. Regresar")
        op = input("Seleccione: ")
        modelos = leer_datos("modelos.txt")
        
        if op == "1":
            desc = input("Descripción del modelo: ")
            if not existe_en_lista(desc, modelos, 0):
                marca = input("Marca: ")
                asientos = input("Cantidad de asientos: ")
                pie = input("Cantidad de espacios de pie: ")
                # Se agrega como una sola fila (lista) para mantener la matriz correcta
                modelos.append([desc, marca, asientos, pie])
                guardar_datos("modelos.txt", modelos)
                print("Modelo registrado con éxito.")
            else:
                print("Error: El modelo ya existe.")
                
        elif op == "2":
            for mod in modelos:
                print(f"Modelo: {mod[0]} | Marca: {mod[1]} | Asientos: {mod[2]} | De pie: {mod[3]}")
                
        elif op == "3":
            desc = input("Ingrese la descripción del modelo a modificar: ")
            encontrado = False
            for i in range(len(modelos)):
                if modelos[i][0] == desc:
                    modelos[i][1] = input("Nueva Marca: ")
                    modelos[i][2] = input("Nuevos asientos: ")
                    modelos[i][3] = input("Nuevos espacios de pie: ")
                    guardar_datos("modelos.txt", modelos)
                    print("Modelo modificado con éxito.")
                    encontrado = True
                    break
            if not encontrado:
                print("Modelo no encontrado.")
                
        elif op == "4":
            desc = input("Ingrese la descripción del modelo a eliminar: ")
            unidades = leer_datos("unidades.txt")
            if existe_en_lista(desc, unidades, 1):
                print("Error: No se puede eliminar. El modelo está asignado a una unidad registrada.")
            else:
                nuevos_modelos = []
                encontrado = False
                for mod in modelos:
                    if mod[0] != desc:
                        nuevos_modelos.append(mod)
                    else:
                        encontrado = True
                if encontrado:
                    guardar_datos("modelos.txt", nuevos_modelos)
                    print("Modelo eliminado con éxito.")
                else:
                    print("Modelo no encontrado.")
                    
        elif op == "5":
            break

# ==========================================
# (12) GESTIÓN DE UNIDADES
# ==========================================
def gestionar_unidades():
    while True:
        print("\n--- (12) GESTIÓN DE UNIDADES ---")
        print("1. Incluir | 2. Mostrar | 3. Modificar | 4. Eliminar | 5. Regresar")
        op = input("Seleccione: ")
        unidades = leer_datos("unidades.txt")
        modelos = leer_datos("modelos.txt")
        
        if op == "1":
            placa = input("Placa de la unidad: ")
            if not existe_en_lista(placa, unidades, 0):
                modelo = input("Modelo (debe estar registrado): ")
                if existe_en_lista(modelo, modelos, 0):
                    anio = input("Año: ")
                    empresa = input("Empresa operadora: ")
                    unidades.append([placa, modelo, anio, empresa])
                    guardar_datos("unidades.txt", unidades)
                    print("Unidad registrada con éxito.")
                else:
                    print("Error: El modelo indicado no existe en el sistema.")
            else:
                print("Error: Ya existe una unidad con esta placa.")
                
        elif op == "2":
            for uni in unidades:
                print(f"Placa: {uni[0]} | Modelo: {uni[1]} | Año: {uni[2]} | Empresa: {uni[3]}")
                
        elif op == "3":
            placa = input("Ingrese la placa de la unidad a modificar: ")
            encontrado = False
            for i in range(len(unidades)):
                if unidades[i][0] == placa:
                    nuevo_modelo = input("Nuevo Modelo: ")
                    if existe_en_lista(nuevo_modelo, modelos, 0):
                        unidades[i][1] = nuevo_modelo
                        unidades[i][2] = input("Nuevo Año: ")
                        unidades[i][3] = input("Nueva Empresa operadora: ")
                        guardar_datos("unidades.txt", unidades)
                        print("Unidad modificada con éxito.")
                    else:
                        print("Error: El modelo indicado no existe.")
                    encontrado = True
                    break
            if not encontrado:
                print("Unidad no encontrada.")
                
        elif op == "4":
            placa = input("Ingrese la placa de la unidad a eliminar: ")
            salidas = leer_datos("salidas.txt")
            if existe_en_lista(placa, salidas, 2):
                print("Error: No se puede eliminar. La unidad está asignada a una salida programada.")
            else:
                nuevas_unidades = []
                encontrado = False
                for uni in unidades:
                    if uni[0] != placa:
                        nuevas_unidades.append(uni)
                    else:
                        encontrado = True
                if encontrado:
                    guardar_datos("unidades.txt", nuevas_unidades)
                    print("Unidad eliminada con éxito.")
                else:
                    print("Unidad no encontrada.")
                    
        elif op == "5":
            break

# ==========================================
# (13) GESTIÓN DE CONDUCTORES
# ==========================================
def gestionar_conductores():
    while True:
        print("\n--- (13) GESTIÓN DE CONDUCTORES ---")
        print("1. Incluir | 2. Mostrar | 3. Modificar | 4. Eliminar | 5. Regresar")
        op = input("Seleccione: ")
        conductores = leer_datos("conductores.txt")
        
        if op == "1":
            cedula = input("Cédula: ")
            if not existe_en_lista(cedula, conductores, 0):
                nombre = input("Nombre completo: ")
                licencia = input("Tipo de licencia: ")
                fecha_vence = input("Fecha vencimiento licencia (DD/MM/AAAA): ")
                jornada = input("Jornada máxima diaria (horas): ")
                conductores.append([cedula, nombre, licencia, fecha_vence, jornada])
                guardar_datos("conductores.txt", conductores)
                print("Conductor registrado con éxito.")
            else:
                print("Error: Ya existe un conductor con esa cédula.")
                
        elif op == "2":
            for cond in conductores:
                print(f"Cédula: {cond[0]} | Nombre: {cond[1]} | Licencia: {cond[2]} | Vence: {cond[3]} | Jornada: {cond[4]}h")
                
        elif op == "3":
            cedula = input("Ingrese la cédula del conductor a modificar: ")
            encontrado = False
            for i in range(len(conductores)):
                if conductores[i][0] == cedula:
                    conductores[i][1] = input("Nuevo Nombre: ")
                    conductores[i][2] = input("Nuevo Tipo de licencia: ")
                    conductores[i][3] = input("Nueva Fecha vencimiento (DD/MM/AAAA): ")
                    conductores[i][4] = input("Nueva Jornada máxima (horas): ")
                    guardar_datos("conductores.txt", conductores)
                    print("Conductor modificado con éxito.")
                    encontrado = True
                    break
            if not encontrado:
                print("Conductor no encontrado.")
                
        elif op == "4":
            cedula = input("Ingrese la cédula a eliminar: ")
            salidas = leer_datos("salidas.txt")
            if existe_en_lista(cedula, salidas, 3):
                print("Error: No se puede eliminar. El conductor está asignado a una salida programada.")
            else:
                nuevos_conductores = []
                encontrado = False
                for cond in conductores:
                    if cond[0] != cedula:
                        nuevos_conductores.append(cond)
                    else:
                        encontrado = True
                if encontrado:
                    guardar_datos("conductores.txt", nuevos_conductores)
                    print("Conductor eliminado con éxito.")
                else:
                    print("Conductor no encontrado.")
                    
        elif op == "5":
            break

# ==========================================
# MENÚS PRINCIPALES
# ==========================================
def menu_administrativo():
    while True:
        print("\n--- MENÚ ADMINISTRATIVO ---")
        print("(11) Gestión de modelos de autobús")
        print("(12) Gestión de unidades")
        print("(13) Gestión de conductores")
        print("(14) Gestión de rutas")
        print("(15) Gestión de paradas por ruta")
        print("(16) Programación de salidas")
        print("(17) Consultar historial de abordajes")
        print("(18) Regresar al menú principal")

        menu = input("Seleccione: ")

        if menu == "11":
            gestionar_modelos()
        elif menu == "12":
            gestionar_unidades()
        elif menu == "13":
            gestionar_conductores()
        elif menu == "18":
            break
        else:
            print("Opción en construcción o inválida.")

def menu_usuario():
    print("\n--- MENÚ DE USUARIO ---")
    print("Opciones de usuario en construcción...")
    # Aquí irían las opciones 21 a 24

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
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
