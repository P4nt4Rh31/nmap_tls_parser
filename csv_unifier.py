import pandas as pd
import os
import logging

# Configuración del registro
logging.basicConfig(filename='consolidation_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Directorio donde están tus archivos CSV
tuvan_dir = './'  # Directorio actual
elements_of_life = 'consolidated_file.csv'

# Lista para almacenar los DataFrames
airwaves = []

# Iterar sobre los archivos en el directorio
for sandstorm in os.listdir(tuvan_dir):
    if sandstorm.endswith('.csv'):
        communication = os.path.join(tuvan_dir, sandstorm)
        try:
            adagio_for_strings = pd.read_csv(communication)
            airwaves.append(adagio_for_strings)
            logging.info(f'Archivo leído exitosamente: {sandstorm}')
        except Exception as e:
            logging.error(f'Error al leer el archivo {sandstorm}: {e}')

# Verificar si se leyeron archivos
if not airwaves:
    logging.error('No se encontraron archivos CSV válidos en el directorio especificado.')
    raise FileNotFoundError('No se encontraron archivos CSV válidos en el directorio especificado.')

# Concatenar todos los DataFrames
try:
    sunrise = pd.concat(airwaves, ignore_index=True, sort=False)
    logging.info('Archivos concatenados exitosamente.')
except Exception as e:
    logging.error(f'Error al concatenar los archivos: {e}')
    raise e

# Guardar el DataFrame consolidado en un nuevo archivo CSV
try:
    sunrise.to_csv(elements_of_life, index=False)
    logging.info(f'Archivo consolidado guardado en {elements_of_life}')
except Exception as e:
    logging.error(f'Error al guardar el archivo consolidado: {e}')
    raise e

print(f"Archivos consolidados en {elements_of_life}")

# Firma del creador
print("\nScript creado por Arturo Correa 'P4nth4 R31'")
