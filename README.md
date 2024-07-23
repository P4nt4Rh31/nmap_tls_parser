# nmap_tls_parser

Nmap TLS parser

This script called "nmap_tls_parser.py" allows you to consolidate .nmap and .txt nmap scan files from "--script ssl-enum-ciphers" into a directory and extract information about the TLS 1.0 and 1.1 versions of specific ports. The script filters and displays only IPs and ports that exactly match the port specified by the user.

Characteristics

File Consolidation: The script consolidates all .nmap and .txt files into the current directory. TLS Extract: Extracts versions of TLSv1.0 and TLSv1.1 from the specified ports. Exact Filtering: Only displays ports that exactly match the port entered by the user. Simple user interface – uses a pop-up window for the user to enter the desired TCP port.

Use

Requirements

 Python 3.x
 Tkinter (included in most Python installations)

Facility

 1 Clone this repository or download the nmap_tls_parser.py file to your working directory:

git clone https://github.com/P4nt4Rh31/nmap_tls_parser.git
cd nmap_tls_parser

Execution

 1 Open a terminal and navigate to the directory containing nmap_tls_parser.py and the .nmap .txt files to process:

cd /path/to/your/directory/nmap_tls_parser

 2 Run the script:

python nmap_tls_parser.py file1.nmap file2.nmap file1.txt file2.txt

Output Example

If the port you entered is 443 and there is an IP with multiple TLS versions TLSv1.0 y TLSv1.1, you should see something like:

"443/tcp open"
TLSv1.0
192.168.10.10
....
....

"443/tcp open"
TLSv1.1
192.168.10.58
....

Script created by Arturo Correa 'P4nth4_R31'

=========================================================================================================================
Analizador TLS de Nmap

Este script llamado "nmap_tls_parser.py" permite consolidar archivos de escaneo nmap .nmap y .txt provenientes de "--script ssl-enum-ciphers" en un directorio y extraer información sobre las versiones TLS 1.0 y 1.1 de puertos específicos. El script filtra y muestra solo las IP y los puertos que coinciden exactamente con el puerto especificado por el usuario.

Características

Consolidación de archivos: el script consolida todos los archivos .nmap y .txt en el directorio actual. Extracto de TLS: extrae versiones de TLSv1.0 y TLSv1.1 de los puertos especificados. Filtrado exacto: solo muestra los puertos que coinciden exactamente con el puerto ingresado por el usuario. Interfaz de usuario simple: utiliza una ventana emergente para que el usuario ingrese el puerto TCP deseado.

Usar

Requisitos

 Pitón 3.x
 Tkinter (incluido en la mayoría de las instalaciones de Python)

Instalación

 1 Clona este repositorio o descarga el archivo nmap_tls_parser.py a tu directorio de trabajo:

clon de git https://github.com/P4nt4Rh31/nmap_tls_parser.git
CD nmap_tls_parser

Ejecución

 1 Abra una terminal y navegue hasta el directorio que contiene nmap_tls_parser.py y los archivos .nmap .txt para procesar:

cd /ruta/a/su/directorio/nmap_tls_parser

 2 Ejecute el script:

Python nmap_tls_parser.py archivo1.nmap archivo2.nmap archivo1.txt archivo2.txt

Ejemplo de salida

Si el puerto que ingresaste es 443 y hay una IP con múltiples versiones de TLS TLSv1.0 y TLSv1.1, deberías ver algo como:

"443/tcp open"
TLSv1.0
192.168.10.10
....
....

"443/tcp open"
TLSv1.1
192.168.10.58
....

Script created by Arturo Correa 'P4nth4_R31'
