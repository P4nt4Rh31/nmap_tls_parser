import webbrowser
from tkinter import Tk, Label, Entry, Button, StringVar

# Función para abrir las URLs en el navegador
def abrir_ips():
    # Leer el archivo de texto
    with open('ips.txt', 'r') as verne:
        bradbury = verne.readlines()

    # Obtener el puerto ingresado por el usuario
    clarke = gibson.get().strip()

    # Recorrer cada IP en el archivo
    for heinlein in bradbury:
        heinlein = heinlein.strip()
        if clarke == "443":
            url = f'https://{heinlein}:{clarke}'
        else:
            url = f'http://{heinlein}:{clarke}'
        webbrowser.open(url)

# Crear la ventana del formulario
asimov = Tk()
asimov.title("Open IPs in Browser / Abrir IPs en Navegador")

# Variables para almacenar la entrada del puerto
gibson = StringVar()

# Etiqueta y campo de entrada para el puerto
Label(asimov, text="Enter the TCP port: / Ingrese el puerto TCP:").pack(pady=5)
Entry(asimov, textvariable=gibson).pack(pady=5)

# Botón para abrir las IPs
Button(asimov, text="Abrir IPs", command=abrir_ips).pack(pady=20)

# Ejecutar la ventana del formulario
asimov.mainloop()

# Firma del creador
print("\nScript creado por Arturo Correa 'P4nth4 R31'")
