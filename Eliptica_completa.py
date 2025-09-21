# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
from scipy.special import ellipk
import math

# Lista para almacenar resultados
resultados = []

def calcular_integral():
    try:
        x_grados = float(entry_x.get())
        x_rad = math.radians(x_grados)
        k = math.sin(x_rad / 2)  # parámetro correcto para el péndulo
        if not (0 <= k < 1):
            raise ValueError("El valor de k = sin(x/2) debe estar en el rango [0, 1).")
        K = ellipk(k**2)
        T = 4 * K  # Período normalizado
        resultados.append((x_grados, k, K, T))
        tabla.insert("", "end", values=(
            f"{x_grados:.4f}", f"{k:.10f}", f"{K:.10f}", f"{T:.10f}"
        ))
        entry_x.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copiar_tabla():
    texto = "Ángulo (°)\tk\tK(k)\tT = 4·K(k)\n"
    for x, k, K, T in resultados:
        texto += f"{x:.4f}\t{k:.10f}\t{K:.10f}\t{T:.10f}\n"
    ventana.clipboard_clear()
    ventana.clipboard_append(texto)
    ventana.update()
    messagebox.showinfo("Copiado", "Tabla copiada al portapapeles. Puedes pegarla en cualquier editor de texto.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Integral Elíptica Completa y Período del Péndulo")

# Entrada de ángulo
frame_input = tk.Frame(ventana)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Ingrese ángulo máximo θ₀ (°):").pack(side=tk.LEFT)
entry_x = tk.Entry(frame_input, width=10)
entry_x.pack(side=tk.LEFT, padx=5)
tk.Button(frame_input, text="Calcular", command=calcular_integral).pack(side=tk.LEFT)
tk.Button(frame_input, text="Copiar tabla", command=copiar_tabla).pack(side=tk.LEFT, padx=5)

# Tabla de resultados
tabla = ttk.Treeview(ventana, columns=("x", "k", "K(k)", "T"), show="headings", height=8)
tabla.heading("x", text="Ángulo (°)")
tabla.heading("k", text="k = sin(x/2)")
tabla.heading("K(k)", text="K(k)")
tabla.heading("T", text="T = 4·K(k)")
tabla.column("x", width=100, anchor="center")
tabla.column("k", width=150, anchor="center")
tabla.column("K(k)", width=200, anchor="center")
tabla.column("T", width=200, anchor="center")
tabla.pack(pady=10)

# Ejecutar la interfaz
ventana.mainloop()