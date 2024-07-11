import re
import os
from collections import defaultdict
import tkinter as tk
from tkinter import simpledialog

def consolidar_archivos():
    contenido_consolidado = ''
    for archivo in os.listdir():
        if archivo.endswith('.nmap') or archivo.endswith('.txt'):
            with open(archivo, 'r', encoding='latin-1') as file:
                contenido_consolidado += file.read() + '\n\n'  # Añadir separación entre archivos
    return contenido_consolidado

def extract_tls_versions(datos, puerto_tcp):
    ip_regex = r'Nmap scan report for (.+?) \(([\d\.]+)\)'
    port_regex = rf'^{puerto_tcp}/tcp open'  # Asegurar coincidencia exacta al inicio de la línea
    tls_regex = r'(TLSv1\.[01]):\s+(\n|.)*?cipher preference: server'

    tls_v1_0_data = defaultdict(set)
    tls_v1_1_data = defaultdict(set)

    ip_matches = list(re.finditer(ip_regex, datos))

    for i, match in enumerate(ip_matches):
        ip_info = match.group(1)
        ip = match.group(2)
        start_index = match.end()
        end_index = ip_matches[i + 1].start() if i + 1 < len(ip_matches) else len(datos)
        ip_data = datos[start_index:end_index]

        port_matches = list(re.finditer(port_regex, ip_data, re.MULTILINE))

        for port_match in port_matches:
            port_info = port_match.group(0)
            port_start_index = port_match.end()
            port_end_index = ip_data.find('\n\n', port_start_index)
            port_end_index = port_end_index if port_end_index != -1 else len(ip_data)
            port_data = ip_data[port_start_index:port_end_index]

            tls_sections = re.findall(tls_regex, port_data)
            for tls_version, _ in tls_sections:
                if tls_version == 'TLSv1.0':
                    tls_v1_0_data[port_info].add(ip)
                elif tls_version == 'TLSv1.1':
                    tls_v1_1_data[port_info].add(ip)

    return tls_v1_0_data, tls_v1_1_data

def imprimir_resultados(tls_v1_0_data, tls_v1_1_data):
    for port_info in tls_v1_0_data:
        if tls_v1_0_data[port_info]:
            print(f'"{port_info}"')
            print("TLSv1.0")
            for ip in sorted(tls_v1_0_data[port_info]):
                print(ip)
            print()

    for port_info in tls_v1_1_data:
        if tls_v1_1_data[port_info]:
            print(f'"{port_info}"')
            print("TLSv1.1")
            for ip in sorted(tls_v1_1_data[port_info]):
                print(ip)
            print()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    puerto_tcp = simpledialog.askstring("Entrada", "Ingresa el puerto TCP que deseas revisar:")

    contenido_consolidado = consolidar_archivos()

    tls_v1_0_data_global, tls_v1_1_data_global = extract_tls_versions(contenido_consolidado, puerto_tcp)

    imprimir_resultados(tls_v1_0_data_global, tls_v1_1_data_global)

# Firma del creador
print("\nScript creado por Arturo Correa 'P4nth4 R31'")
