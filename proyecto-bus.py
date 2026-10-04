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
# FUNCIONES AUXILIARES PARA SALIDAS
# ==========================================

# Convierte "HH:MM" a un número de minutos (ej. "06:30" -> 390)
def tiempo_a_minutos(hora_str):
    partes = hora_str.split(":")
    return int(partes[0]) * 60 + int(partes[1])

# Convierte "DD/MM/AAAA" a un número "AAAAMMDD" para poder comparar fechas con < o >
def fecha_a_numero(fecha_str):
    partes = fecha_str.split("/")
    return int(partes[2] + partes[1] + partes[0])

# Genera el código automático S001, S002, etc.
def generar_id_salida(salidas):
    if len(salidas) == 0:
        return "S001"
    # Tomamos el último ID y le sumamos 1
    ultimo_id = salidas[-1][0]
    numero = int(ultimo_id[1:]) + 1
    
    if numero < 10:
        return "S00" + str(numero)
    elif numero < 100:
        return "S0" + str(numero)
    else:
        return "S" + str(numero)

# Valida todas las reglas de negocio antes de registrar o modificar
def validar_reglas_salida(ruta, unidad, conductor, fecha, h_salida, h_llegada, salidas, conductores, id_ignorar=""):
    min_salida = tiempo_a_minutos(h_salida)
    min_llegada = tiempo_a_minutos(h_llegada)
    
    # 1. La hora de llegada debe ser posterior a la de salida
    if min_llegada <= min_salida:
        print("Error: La hora estimada de llegada debe ser posterior a la de salida.")
        return False
        
    duracion_nueva = (min_llegada - min_salida) / 60.0
    
    # Buscar datos del conductor para validarlo
    datos_cond = []
    for c in conductores:
        if c[0] == conductor:
            datos_cond = c
            break
            
    if not datos_cond:
        print("Error: El conductor seleccionado no existe en el sistema.")
        return False
        
    # 2. Licencia vencida
    if fecha_a_numero(datos_cond[3]) < fecha_a_numero(fecha):
        print("Error: La licencia del conductor está vencida para la fecha de la salida.")
        return False

    horas_acumuladas = 0.0
    
    for s in salidas:
        # Si estamos modificando, ignoramos la salida actual
        if s[0] == id_ignorar:
            continue
            
        # Si la salida analizada es en la misma fecha, comprobamos traslapes
        if s[4] == fecha:
            s_min_sal = tiempo_a_minutos(s[5])
            s_min_lle = tiempo_a_minutos(s[6])
            
            # Condición de traslape: inicio1 < fin2 y fin1 > inicio2
            hay_traslape = (min_salida < s_min_lle) and (min_llegada > s_min_sal)
            
            # 3. Traslape de unidad
            if s[2] == unidad and hay_traslape:
                print("Error: La unidad seleccionada ya tiene una salida que se traslape en ese horario.")
                return False
                
            # 4. Traslape de conductor
            if s[3] == conductor:
                if hay_traslape:
                    print("Error: El conductor seleccionado ya tiene una salida que se traslape en ese horario.")
                    return False
                # Si no hay traslape pero es el mismo día, sumamos sus horas
                horas_acumuladas += (s_min_lle - s_min_sal) / 60.0
                
    # 5. Jornada máxima
    if horas_acumuladas + duracion_nueva > float(datos_cond[4]):
        print(f"Error: Asignar esta salida excede la jornada máxima diaria del conductor ({datos_cond[4]} horas).")
        return False

    return True

# ==========================================
# (16) PROGRAMACIÓN DE SALIDAS
# ==========================================
def gestionar_salidas():
    while True:
        print("\n--- (16) PROGRAMACIÓN DE SALIDAS ---")
        print("1. Incluir | 2. Mostrar | 3. Modificar | 4. Eliminar | 5. Regresar")
        op = input("Seleccione: ")
        
        salidas = leer_datos("salidas.txt")
        rutas = leer_datos("rutas.txt")
        unidades = leer_datos("unidades.txt")
        conductores = leer_datos("conductores.txt")
        
        if op == "1":
            print("\nListas disponibles:")
            print("Rutas registradas:", end=" ")
            for r in rutas: print(r[0], end=" | ")
            print("\nUnidades registradas:", end=" ")
            for u in unidades: print(u[0], end=" | ")
            print("\nConductores registrados:", end=" ")
            for c in conductores: print(c[0], end=" | ")
            print("\n")
            
            ruta = input("Código de ruta: ")
            unidad = input("Placa de la unidad: ")
            conductor = input("Cédula del conductor: ")
            
            # Validar existencia básica
            if existe_en_lista(ruta, rutas, 0) and existe_en_lista(unidad, unidades, 0) and existe_en_lista(conductor, conductores, 0):
                fecha = input("Fecha de salida (DD/MM/AAAA): ")
                h_salida = input("Hora de salida (HH:MM): ")
                h_llegada = input("Hora estimada de llegada (HH:MM): ")
                
                if validar_reglas_salida(ruta, unidad, conductor, fecha, h_salida, h_llegada, salidas, conductores):
                    nuevo_id = generar_id_salida(salidas)
                    salidas.append([nuevo_id, ruta, unidad, conductor, fecha, h_salida, h_llegada])
                    guardar_datos("salidas.txt", salidas)
                    print(f"Salida {nuevo_id} programada con éxito.")
            else:
                print("Error: La ruta, unidad o conductor indicados no existen en el sistema.")
                
        elif op == "2":
            for s in salidas:
                print(f"Salida: {s[0]} | Ruta: {s[1]} | Unidad: {s[2]} | Cond: {s[3]} | Fecha: {s[4]} | Horario: {s[5]} - {s[6]}")
                
        elif op == "3":
            num_salida = input("Ingrese el número de salida a modificar (ej. S001): ")
            encontrado = False
            
            for i in range(len(salidas)):
                if salidas[i][0] == num_salida:
                    print("Ingrese los nuevos datos (presione Enter para mantener listas, o escriba los nuevos):")
                    n_ruta = input(f"Nueva ruta ({salidas[i][1]}): ") or salidas[i][1]
                    n_unidad = input(f"Nueva unidad ({salidas[i][2]}): ") or salidas[i][2]
                    n_conductor = input(f"Nuevo conductor ({salidas[i][3]}): ") or salidas[i][3]
                    n_fecha = input(f"Nueva fecha ({salidas[i][4]}): ") or salidas[i][4]
                    n_h_salida = input(f"Nueva hora salida ({salidas[i][5]}): ") or salidas[i][5]
                    n_h_llegada = input(f"Nueva hora llegada ({salidas[i][6]}): ") or salidas[i][6]
                    
                    if existe_en_lista(n_ruta, rutas, 0) and existe_en_lista(n_unidad, unidades, 0) and existe_en_lista(n_conductor, conductores, 0):
                        # Aplicar de nuevo las validaciones, enviando el ID actual para que se ignore a sí mismo en el chequeo
                        if validar_reglas_salida(n_ruta, n_unidad, n_conductor, n_fecha, n_h_salida, n_h_llegada, salidas, conductores, id_ignorar=num_salida):
                            salidas[i][1] = n_ruta
                            salidas[i][2] = n_unidad
                            salidas[i][3] = n_conductor
                            salidas[i][4] = n_fecha
                            salidas[i][5] = n_h_salida
                            salidas[i][6] = n_h_llegada
                            guardar_datos("salidas.txt", salidas)
                            print("Salida modificada con éxito y validaciones superadas.")
                    else:
                        print("Error: Algún dato de ruta, unidad o conductor no existe.")
                    
                    encontrado = True
                    break
                    
            if not encontrado:
                print("Salida no encontrada.")
                
        elif op == "4":
            num_salida = input("Ingrese el número de salida a eliminar (ej. S001): ")
            abordajes = leer_datos("abordajes.txt")
            
            # Verificar que no tenga abordajes registrados
            if existe_en_lista(num_salida, abordajes, 2):
                print("Error: No se puede eliminar. La salida tiene abordajes registrados.")
            else:
                nuevas_salidas = []
                encontrado = False
                for s in salidas:
                    if s[0] != num_salida:
                        nuevas_salidas.append(s)
                    else:
                        encontrado = True
                
                if encontrado:
                    guardar_datos("salidas.txt", nuevas_salidas)
                    print("Salida eliminada con éxito.")
                else:
                    print("Salida no encontrada.")
                    
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

    # Se solicitan los filtros (presionar Enter los ignora)
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
        elif menu == "16":
            gestionar_salidas()
        elif menu == "17":
            consultar_historial()
        elif menu == "18":
            break
        else:
            print("Opción en construcción o inválida.")

# ==========================================
# (21) CONSULTA DE SALIDAS
# ==========================================
def consulta_salidas():
    print("\n--- (21) CONSULTA DE SALIDAS ---")
    salidas = leer_datos("salidas.txt")
    rutas = leer_datos("rutas.txt")
    unidades = leer_datos("unidades.txt")
    modelos = leer_datos("modelos.txt")
    abordajes = leer_datos("abordajes.txt")

    print("Filtros de búsqueda (presione Enter para omitir):")
    f_ruta = input("Ruta: ")
    f_origen = input("Lugar de origen: ")
    f_destino = input("Lugar de destino: ")
    f_fecha = input("Fecha de salida (DD/MM/AAAA): ")

    print("\n=== SALIDAS PROGRAMADAS ===")
    for s in salidas:
        id_salida = s[0]
        cod_ruta = s[1]
        placa_unidad = s[2]
        fecha_salida = s[4]
        h_salida = s[5]
        h_llegada = s[6]

        # Aplicar filtros directos de salida[cite: 5]
        if f_ruta and cod_ruta != f_ruta:
            continue
        if f_fecha and fecha_salida != f_fecha:
            continue

        # Obtener datos de la ruta[cite: 3]
        origen, destino = "", ""
        for r in rutas:
            if r[0] == cod_ruta:
                origen = r[1]
                destino = r[2]
                break
                
        # Aplicar filtros de ruta[cite: 5]
        if f_origen and origen != f_origen:
            continue
        if f_destino and destino != f_destino:
            continue

        # Calcular capacidad de la unidad[cite: 2, 5]
        cod_modelo = ""
        for u in unidades:
            if u[0] == placa_unidad:
                cod_modelo = u[1]
                break
                
        capacidad_total = 0
        for m in modelos:
            if m[0] == cod_modelo:
                capacidad_total = int(m[2]) + int(m[3]) # Asientos + De pie
                break

        # Calcular espacios ocupados revisando abordajes[cite: 5]
        ocupados = 0
        for a in abordajes:
            if a[2] == id_salida:
                ocupados += int(a[7])
                
        disponibles = capacidad_total - ocupados

        print(f"Salida: {id_salida} | Ruta: {cod_ruta} ({origen} - {destino})")
        print(f"   Fecha: {fecha_salida} | Hora: {h_salida} a {h_llegada}")
        print(f"   Unidad: {placa_unidad} | Capacidad: {capacidad_total} | Ocupados: {ocupados} | Disponibles: {disponibles}\n")
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
