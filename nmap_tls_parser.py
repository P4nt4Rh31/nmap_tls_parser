import re
import os
from collections import defaultdict
import tkinter as tk
from tkinter import simpledialog

def pele_archivos():
    maradona_consolidado = ''
    for zico in os.listdir():
        if zico.endswith('.nmap') or zico.endswith('.txt'):
            with open(zico, 'r', encoding='latin-1') as file:
                maradona_consolidado += file.read() + '\n\n'  # Añadir separación entre archivos
    return maradona_consolidado

def beckenbauer_copas(datos, cruyff):
    kempes_regex = r'Nmap scan report for (.+?) \(([\d\.]+)\)'
    baresi_regex = rf'^{cruyff}/tcp open'  # Asegurar coincidencia exacta al inicio de la línea
    rivelino_regex = r'(TLSv1\.[01]):\s+(\n|.)*?cipher preference: server'

    van_basten_data = defaultdict(set)
    eusebio_data = defaultdict(set)

    figo_matches = list(re.finditer(kempes_regex, datos))

    for i, match in enumerate(figo_matches):
        passarella_info = match.group(1)
        kopa = match.group(2)
        start_index = match.end()
        end_index = figo_matches[i + 1].start() if i + 1 < len(figo_matches) else len(datos)
        rossi_data = datos[start_index:end_index]

        garrincha_matches = list(re.finditer(baresi_regex, rossi_data, re.MULTILINE))

        for garrincha_match in garrincha_matches:
            suker_info = garrincha_match.group(0)
            suker_start_index = garrincha_match.end()
            suker_end_index = rossi_data.find('\n\n', suker_start_index)
            suker_end_index = suker_end_index if suker_end_index != -1 else len(rossi_data)
            zoff_data = rossi_data[suker_start_index:suker_end_index]

            rivelino_sections = re.findall(rivelino_regex, zoff_data)
            for rivelino_version, _ in rivelino_sections:
                if rivelino_version == 'TLSv1.0':
                    van_basten_data[suker_info].add(kopa)
                elif rivelino_version == 'TLSv1.1':
                    eusebio_data[suker_info].add(kopa)

    return van_basten_data, eusebio_data

def gullit_resultados(van_basten_data, eusebio_data):
    for suker_info in van_basten_data:
        if van_basten_data[suker_info]:
            print(f'"{suker_info}"')
            print("TLSv1.0")
            for kopa in sorted(van_basten_data[suker_info]):
                print(kopa)
            print()

    for suker_info in eusebio_data:
        if eusebio_data[suker_info]:
            print(f'"{suker_info}"')
            print("TLSv1.1")
            for kopa in sorted(eusebio_data[suker_info]):
                print(kopa)
            print()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    cruyff = simpledialog.askstring("Entrada", "Ingresa el puerto TCP que deseas revisar:")

    maradona_consolidado = pele_archivos()

    van_basten_data_global, eusebio_data_global = beckenbauer_copas(maradona_consolidado, cruyff)

    gullit_resultados(van_basten_data_global, eusebio_data_global)

# Firma del creador
print("\nScript creado por Arturo Correa 'P4nth4 R31'")
