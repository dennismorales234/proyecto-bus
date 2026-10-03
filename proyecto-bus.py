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
# (14) GESTIÓN DE RUTAS
# ==========================================
def gestionar_rutas():
    while True:
        print("\n--- (14) GESTIÓN DE RUTAS ---")
        print("1. Incluir | 2. Mostrar | 3. Modificar | 4. Eliminar | 5. Regresar")
        op = input("Seleccione: ")
        rutas = leer_datos("rutas.txt")
        
        if op == "1":
            codigo = input("Código de ruta: ")
            if not existe_en_lista(codigo, rutas, 0):
                origen = input("Lugar de origen: ")
                destino = input("Lugar de destino: ")
                distancia = input("Distancia total (km): ")
                tarifa = input("Tarifa por kilómetro (colones): ")
                rutas.append([codigo, origen, destino, distancia, tarifa])
                guardar_datos("rutas.txt", rutas)
                print("Ruta registrada con éxito.")
            else:
                print("Error: Ya existe una ruta con este código.")
                
        elif op == "2":
            for r in rutas:
                print(f"Código: {r[0]} | Origen: {r[1]} | Destino: {r[2]} | Distancia: {r[3]}km | Tarifa: ₡{r[4]}")
                
        elif op == "3":
            codigo = input("Ingrese el código de la ruta a modificar: ")
            encontrado = False
            for i in range(len(rutas)):
                if rutas[i][0] == codigo:
                    rutas[i][1] = input("Nuevo lugar de origen: ")
                    rutas[i][2] = input("Nuevo lugar de destino: ")
                    rutas[i][3] = input("Nueva distancia total (km): ")
                    rutas[i][4] = input("Nueva tarifa por kilómetro: ")
                    guardar_datos("rutas.txt", rutas)
                    print("Ruta modificada con éxito.")
                    encontrado = True
                    break
            if not encontrado:
                print("Ruta no encontrada.")
                
        elif op == "4":
            codigo = input("Ingrese el código de la ruta a eliminar: ")
            paradas = leer_datos("paradas.txt")
            salidas = leer_datos("salidas.txt")
            
            # Validar si tiene paradas o salidas asignadas
            if existe_en_lista(codigo, paradas, 0) or existe_en_lista(codigo, salidas, 1):
                print("Error: No se puede eliminar. La ruta tiene paradas registradas o salidas programadas.")
            else:
                nuevas_rutas = []
                encontrado = False
                for r in rutas:
                    if r[0] != codigo:
                        nuevas_rutas.append(r)
                    else:
                        encontrado = True
                if encontrado:
                    guardar_datos("rutas.txt", nuevas_rutas)
                    print("Ruta eliminada con éxito.")
                else:
                    print("Ruta no encontrada.")
                    
        elif op == "5":
            break
# ==========================================
# (15) GESTIÓN DE PARADAS POR RUTA
# ==========================================
def gestionar_paradas():
    while True:
        print("\n--- (15) GESTIÓN DE PARADAS POR RUTA ---")
        print("1. Incluir | 2. Mostrar | 3. Modificar | 4. Eliminar | 5. Regresar")
        op = input("Seleccione: ")
        paradas = leer_datos("paradas.txt")
        rutas = leer_datos("rutas.txt")
        
        if op == "1":
            codigo = input("Código de ruta: ")
            if existe_en_lista(codigo, rutas, 0):
                orden = input("Número de orden: ")
                
                # Verificar que el orden no exista ya para esa ruta
                orden_existe = False
                for p in paradas:
                    if p[0] == codigo and p[1] == orden:
                        orden_existe = True
                        break
                
                if not orden_existe:
                    nombre = input("Nombre de la parada: ")
                    km = input("Kilómetro acumulado: ")
                    
                    # Validaciones de kilómetros
                    valido = True
                    if orden == "1" and km != "0":
                        print("Error: La primera parada (orden 1) debe tener kilómetro acumulado cero.")
                        valido = False
                    else:
                        # Verificar que el km sea creciente
                        for p in paradas:
                            if p[0] == codigo:
                                # Si hay una parada anterior, su km debe ser menor
                                if int(p[1]) < int(orden) and float(p[3]) >= float(km):
                                    print("Error: El kilómetro debe ser mayor que el de las paradas anteriores.")
                                    valido = False
                                    break
                                # Si hay una parada posterior, su km debe ser mayor
                                if int(p[1]) > int(orden) and float(p[3]) <= float(km):
                                    print("Error: El kilómetro debe ser menor que el de las paradas posteriores.")
                                    valido = False
                                    break
                    
                    if valido:
                        paradas.append([codigo, orden, nombre, km])
                        guardar_datos("paradas.txt", paradas)
                        print("Parada registrada con éxito.")
                else:
                    print("Error: Ya existe una parada con ese número de orden en esta ruta.")
            else:
                print("Error: El código de ruta no existe.")
                
        elif op == "2":
            for p in paradas:
                print(f"Ruta: {p[0]} | Orden: {p[1]} | Nombre: {p[2]} | Km: {p[3]}")
                
        elif op == "3":
            codigo = input("Ingrese el código de ruta: ")
            orden = input("Ingrese el número de orden de la parada a modificar: ")
            encontrado = False
            for i in range(len(paradas)):
                if paradas[i][0] == codigo and paradas[i][1] == orden:
                    paradas[i][2] = input("Nuevo nombre de la parada: ")
                    # Para simplificar y no romper el ciclo de validación creciente, 
                    # usualmente solo se modifica el nombre. Si modificas el km, 
                    # tendrías que aplicar las mismas validaciones de inclusión.
                    print("Parada modificada con éxito (solo nombre).")
                    guardar_datos("paradas.txt", paradas)
                    encontrado = True
                    break
            if not encontrado:
                print("Parada no encontrada.")
                
        elif op == "4":
            codigo = input("Ingrese el código de ruta: ")
            orden = input("Ingrese el número de orden a eliminar: ")
            nuevas_paradas = []
            encontrado = False
            
            for p in paradas:
                if p[0] == codigo and p[1] == orden:
                    encontrado = True
                else:
                    # Si es de la misma ruta y el orden es mayor al eliminado, reacomodamos restando 1
                    if p[0] == codigo and int(p[1]) > int(orden) and encontrado == False:
                        # Si todavía no lo hemos encontrado, significa que estamos iterando antes 
                        # del elemento a eliminar, no hacemos nada.
                        nuevas_paradas.append(p)
                    elif p[0] == codigo and int(p[1]) > int(orden):
                        p[1] = str(int(p[1]) - 1)
                        nuevas_paradas.append(p)
                    else:
                        nuevas_paradas.append(p)
                        
            if encontrado:
                guardar_datos("paradas.txt", nuevas_paradas)
                print("Parada eliminada y secuencia reacomodada con éxito.")
            else:
                print("Parada no encontrada.")
                
        elif op == "5":
            break
# ==========================================
# (17) CONSULTAR HISTORIAL DE ABORDAJES
# ==========================================
def consultar_historial():
    print("\n--- (17) CONSULTAR HISTORIAL DE ABORDAJES ---")
    abordajes = leer_datos("abordajes.txt")
    salidas = leer_datos("salidas.txt")
    
    if not abordajes:
        print("No hay abordajes registrados.")
        return

    # Se solicitan los filtros (presionar Enter los ignora)[cite: 4]
    print("Filtros de búsqueda (presione Enter para omitir):")
    f_ruta = input("Ruta: ")
    f_fecha_salida = input("Fecha de salida (DD/MM/AAAA): ")
    f_fecha_reg_ini = input("Fecha de registro inicial (DD/MM/AAAA): ")
    f_fecha_reg_fin = input("Fecha de registro final (DD/MM/AAAA): ")
    f_parada = input("Número de orden de la parada de abordaje: ")

    total_pasajeros = 0
    total_monto = 0.0

    print("\n=== RESULTADOS DE BÚSQUEDA ===")
    for a in abordajes:
        # Formato de abordaje: [ID, Nombre, Num_Salida, Fecha_Reg, Hora_Reg, Parada_Origen, Parada_Destino, Cantidad, Monto][cite: 5]
        id_salida = a[2]
        
        # Cruzar datos con el archivo de salidas[cite: 4]
        datos_salida = []
        for s in salidas:
            if s[0] == id_salida:
                datos_salida = s
                break
        
        if not datos_salida:
            continue
            
        # Formato salida: [ID, Ruta, Unidad, Conductor, Fecha_Salida, H_Salida, H_Llegada][cite: 4]
        ruta = datos_salida[1]
        fecha_salida = datos_salida[4]
        unidad = datos_salida[2]
        conductor = datos_salida[3]
        h_salida = datos_salida[5]
        
        # Aplicación de filtros
        if f_ruta and ruta != f_ruta:
            continue
        if f_fecha_salida and fecha_salida != f_fecha_salida:
            continue
        if f_parada and a[5] != f_parada:
            continue
            
        # Filtro de rango de fechas usando la función auxiliar fecha_a_numero creada en la opción 16[cite: 4]
        if f_fecha_reg_ini or f_fecha_reg_fin:
            num_fecha_reg = fecha_a_numero(a[3])
            if f_fecha_reg_ini and num_fecha_reg < fecha_a_numero(f_fecha_reg_ini):
                continue
            if f_fecha_reg_fin and num_fecha_reg > fecha_a_numero(f_fecha_reg_fin):
                continue

        # Si supera los filtros, se muestra la información consolidada[cite: 4]
        print(f"ID Abordaje: {a[0]} | Pasajero: {a[1]} | Salida: {id_salida} | Ruta: {ruta}")
        print(f"   Fecha y Hora Salida: {fecha_salida} {h_salida} | Unidad: {unidad} | Cond: {conductor}")
        print(f"   Parada Abordaje: {a[5]} | Parada Destino: {a[6]} | Pasajeros: {a[7]} | Monto cancelado: ₡{a[8]}\n")
        
        total_pasajeros += int(a[7])
        total_monto += float(a[8])

    # Totales requeridos al final del listado[cite: 4]
    print("--------------------------------------------------")
    print(f"Total de pasajeros: {total_pasajeros}")
    print(f"Monto total acumulado: ₡{total_monto}")
    print("--------------------------------------------------")
    
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
        elif menu == "14":
            gestionar_rutas()
        elif menu == "15":
            gestionar_paradas()
        elif menu == "17":
            consultar_historial()
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
