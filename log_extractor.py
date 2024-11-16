import re
import json
import matplotlib.pyplot as plt
from collections import Counter  # Usamos Counter para contar elementos fácilmente

# Expresiones regulares para extraer información del log
# Esta expresión regular busca direcciones IP en formato 'xxx.xxx.xxx.xxx'
ip_pattern = r"\d+\.\d+\.\d+\.\d+"

# Esta expresión regular busca los métodos HTTP comunes como GET, POST, PUT y DELETE
method_pattern = r"(GET|POST|PUT|DELETE)"

# Función que lee el archivo de log y extrae las IPs y los métodos HTTP
def analizar_log(ruta_archivo):
    logs = []  # Creamos una lista vacía para guardar los datos extraídos
    with open(ruta_archivo, 'r') as archivo:  # Abrimos el archivo de log en modo lectura
        for linea in archivo:
            ip = re.search(ip_pattern, linea)  # Buscamos una dirección IP en la línea
            method = re.search(method_pattern, linea)  # Buscamos un HTTP
            if ip and method:
                logs.append({"ip": ip.group(), "method": method.group()})  # Añadimos los datos a la lista
    return logs  # Retornamos la lista de logs extraídos

# Función para guardar los datos extraídos en formato JSON
def guardar_json(data, ruta_salida):
    with open(ruta_salida, 'w') as json_file:  # Abrimos un archivo JSON para escribir los datos
        json.dump(data, json_file, indent=4)  # Guardamos los datos en el archivo con formato legible

# Función para generar un gráfico de barras mostrando los métodos HTTP
def mostrar_grafico_metodos(logs):
    methods = [log['method'] for log in logs]  # Extraemos HTTP de los logs
    method_counts = Counter(methods)  # Contamos cuántas veces aparece HTTP
    # Generamos el gráfico de barras
    plt.bar(method_counts.keys(), method_counts.values(), color='skyblue')
    plt.title('Distribución de Métodos HTTP')  # Título del gráfico
    plt.xlabel('Métodos HTTP')  # Etiqueta del eje X
    plt.ylabel('Frecuencia')  # Etiqueta del eje Y
    plt.show()  # Mostramos el gráfico

# Función para generar un gráfico de barras mostrando las IP
def mostrar_grafico_ips(logs):
    ips = [log['ip'] for log in logs]  # Extraemos todas las IP de los logs
    ip_counts = Counter(ips)  # Contamos cuántas veces aparece cada IP
    # gráfico de barras
    plt.bar(ip_counts.keys(), ip_counts.values(), color='lightgreen')
    plt.title('Frecuencia de Accesos por IP')  # Título del gráfico
    plt.xlabel('Dirección IP')  # Etiqueta del eje X
    plt.ylabel('Frecuencia de Accesos')  # Etiqueta del eje Y
    plt.xticks(rotation=90)  #  del eje X para que se vean mejor
    plt.show()

# Ruta del archivo de log y archivo de salida
ruta_log = "access.log"  # Ruta del archivo de logs
ruta_json = "logs.json"  # Ruta del archivo donde guardaremos el JSON con los datos extraídos

# Llamamos a la función para analizar los logs y extraer los datos=
logs_extraidos = analizar_log(ruta_log)

# Si se han extraído logs, los guardamos en un archivo JSON y generamos los graficos
if logs_extraidos:
    guardar_json(logs_extraidos, ruta_json)  #  datos extraídos en JSON
    mostrar_grafico_metodos(logs_extraidos)  # grafico HTTP
    mostrar_grafico_ips(logs_extraidos)  #  grafico de las IP


