import tkinter as tk
from tkinter import scrolledtext, messagebox

import io
import sys

from antlr4 import CommonTokenStream, InputStream
from ArduinoMexaLexer import ArduinoMexaLexer
from ArduinoMexaParser import ArduinoMexaParser

from parser import run_parser      # parser corregido
from visitor import TraductorArduinoVisitor


terminal_visible = True


def ejecutar_codigo():
    salida_texto.config(state='normal')
    salida_texto.delete("1.0", tk.END)

    code = texto_codigo.get("1.0", tk.END)


    if not code:
        messagebox.showwarning("Advertencia", "El área de código está vacía.")
        return

    try:
        # Redirigir stdout para capturar salida del parser
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        codigo_arduino = run_parser(code)

        # Recuperar la salida del parser/AST
        salida_parser = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Dentro de la función ejecutar_codigo() en main.py

        # ... (código existente para mostrar el código en la terminal) ...
        salida_texto.insert(tk.END, str(codigo_arduino))

        try:
            nombre_archivo = "sketch_arduino_mexa.ino"

            # Usamos 'with open' para asegurar que el archivo se cierre automáticamente
            with open(nombre_archivo, "w", encoding="utf-8") as archivo_arduino:
                archivo_arduino.write(str(codigo_arduino))


            salida_texto.insert(tk.END, f"\n\n Archivo '{nombre_archivo}' creado con éxito en la carpeta actual.\n")

        except Exception as e:

            salida_texto.insert(tk.END, f"\n\n ERROR al escribir el archivo: {e}\n")


        salida_texto.insert(tk.END, salida_parser)
        salida_texto.config(state='disabled')

    except Exception as e:
        salida_texto.config(state='normal')
        salida_texto.insert(tk.END, f"⚠️ Error al procesar el código:\n{e}")
        salida_texto.config(state='disabled')


def limpiar_campos():
    salida_texto.config(state='normal')
    texto_codigo.delete("1.0", tk.END)
    salida_texto.delete("1.0", tk.END)
    salida_texto.config(state='disabled')

def toggle_terminal():
    global terminal_visible
    if terminal_visible:
        salida_label.pack_forget()
        salida_texto.pack_forget()
        boton_toggle_terminal.config(text="Mostrar Terminal")
    else:
        salida_label.pack(padx=10, pady=5, anchor="w")
        salida_texto.pack(padx=10, pady=(0, 10), expand=True, fill="both")
        boton_toggle_terminal.config(text="Ocultar Terminal")
    terminal_visible = not terminal_visible


# ================================
#          INTERFAZ TKINTER
# ================================

ventana = tk.Tk()
ventana.title("ArduinoLite IDE")
ventana.geometry("800x600")

top_frame = tk.Frame(ventana)
top_frame.pack(fill="x", padx=10, pady=5)

etiqueta = tk.Label(top_frame, text="Código:", font=("Arial", 10, "bold"))
etiqueta.pack(side="left")

botones_frame = tk.Frame(top_frame)
botones_frame.pack(side="right")

btn_style = {
    "bg": "white",
    "highlightthickness": 2,
    "highlightbackground": "black",
    "font": ("Arial", 10, "bold"),
    "padx": 10,
    "pady": 3
}

boton_ejecutar = tk.Button(botones_frame, text="Ejecutar", fg="green",
                           command=ejecutar_codigo, **btn_style)
boton_ejecutar.pack(side="left", padx=5)

boton_limpiar = tk.Button(botones_frame, text="Limpiar", fg="#5a7ca5",
                          command=limpiar_campos, **btn_style)
boton_limpiar.pack(side="left", padx=5)

boton_toggle_terminal = tk.Button(botones_frame, text="Ocultar Terminal",
                                  command=toggle_terminal, **btn_style)
boton_toggle_terminal.pack(side="left", padx=5)

# Área de código
texto_codigo = scrolledtext.ScrolledText(ventana, font=("Consolas", 10, "italic bold"))
texto_codigo.pack(padx=10, pady=5, expand=True, fill="both")

# Área terminal
salida_label = tk.Label(ventana, text="Terminal:", font=("Arial", 10, "bold"))
salida_label.pack(padx=10, pady=5, anchor="w")

salida_texto = scrolledtext.ScrolledText(ventana, font=("Consolas", 10))
salida_texto.pack(padx=10, pady=(0, 10), expand=True, fill="both")
salida_texto.config(state='disabled')

ventana.mainloop()
