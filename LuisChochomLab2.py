class SensorPresion:
    # Atributos de clase para toda la planta
    LIMITE_PELIGRO = 200 
    total_lecturas = 0    

    #constructor recibe el nombre del sensor y la presión inicial
    def __init__(self, nombre, presion_inicial):
        self.nombre = nombre
        # Atributo privado para evitar acceso directo y forzar el uso de los decoradores
        self.__presion = 0 
        
        # Al asignar aquí, se dispara automáticamente el @presion.setter
        self.presion = presion_inicial
        
        # Incremento del contador global
        SensorPresion.total_lecturas += 1

    # Decorador para lectura (Getter) para obtener el valor de presión de forma controlada
    @property
    def presion(self):
        return self.__presion

    # Decorador para validación (Setter) esto se realiza para evitar que se asignen valores negativos a la presión, lo cual no tendría sentido físico
    @presion.setter
    def presion(self, valor):
        # Bloquea valores negativos y asigna 0 en su lugar
        if valor >= 0:
            self.__presion = valor
        else:
            print(f"Advertencia: Presión negativa detectada en {self.nombre}. Se asignará 0.")

# --- LÓGICA PRINCIPAL ---

#Creación de una lista para almacenar los objetos de tipo SensorPresion, extraidos del archivo registros.txt
lista_sensores = []

print("MONITOREO INDUSTRIAL")
print("Cargando datos de presión...")

# 1. Lectura del archivo registro.txt y creación de objetos SensorPresion
# Se debe asegurar que registros.txt exista en la carpeta
with open("registros.txt", "r") as datos:
    #Se recorre el archivo registros.txt de dos en dos lineas, la primera es el nombre del sensor y la segunda es el valor de presión
    for linea_nombre in datos:
        #Con strip() se eliminan los espacios en blanco al inicio y al final de la linea.
        nombre = linea_nombre.strip()
        
        #Capturamos el valor de presión en la siguiente línea, si no hay más líneas, se rompe el ciclo
        linea_presion = datos.readline()
        if not linea_presion:
            break
            
        # Conversión de texto a entero. Convertimos el valor de presion a un numero entrero.
        valor_presion = int(linea_presion.strip())
        
        # Creación del objeto. Creamos un nuevo objeto de tipo SensorPresion con el nombre y el valor de presion, que se extraen desde el archivo registros.txt. Luego, se agrega el nuevo objeto a la lista de sensores.
        nuevo_sensor = SensorPresion(nombre, valor_presion)
        lista_sensores.append(nuevo_sensor) 

# 2. Análisis y Generación de Alertas. Creacion de archivo de alertas.txt
with open("alertas.txt", "w") as archivo_salida: 
    archivo_salida.write("REPORTE DE INCIDENCIAS - CALDERAS CRITICAS")
    archivo_salida.write("\n-------------------------------------------\n")
    
    contador_alertas = 0
    #Recorremos con un for los datos de los sensores en la lista creada, comprobamos si la presion supera el limite de peligro, si es asi se registra una alerta en el archivo alertas.txt
    for sensor in lista_sensores:
        # Usamos el decorador property para comparar
        if sensor.presion > SensorPresion.LIMITE_PELIGRO:
            estado = "¡PELIGRO!"
            contador_alertas += 1
            # Registro en el archivo de auditoría
            archivo_salida.write(str(contador_alertas) + ". " + sensor.nombre + "\n")
        else:
            estado = "Seguro"
        
        print("Analizando: " + sensor.nombre + " | Estado: " + estado)

# 3. Resumen final
print("[AUDITORÍA] Se han generado alertas en el archivo 'alertas.txt'")
print("[RESUMEN] Total de sensores procesados: " + str(SensorPresion.total_lecturas) + ".")