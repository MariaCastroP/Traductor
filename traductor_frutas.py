import tkinter as tk
from tkinter import messagebox

 #lista de frutas 
frutas = {
    "manzana": "apple",
    "plátano": "banana",
    "naranja": "orange",
    "uva": "grape",
    "fresa": "strawberry",
    "pera": "pear",
    "piña": "pineapple",
    "mango": "mango",
    "sandía": "watermelon",
    "melón": "melon",
    "cereza": "cherry",
    "limón": "lemon",
    "papaya": "papaya",
    "durazno": "peach",
    "ciruela": "plum",
    "kiwi": "kiwi",
    "granada": "pomegranate",
    "arándano": "blueberry",
    "frambuesa": "raspberry",
    "mora": "blackberry",
    "coco": "coconut",
    "higo": "fig",
    "mandarina": "tangerine",
    "toronja": "grapefruit",
    "guayaba": "guava",
    "lichi": "lychee",
    "maracuyá": "passion fruit",
    "arándano rojo": "cranberry",
    "tamarindo": "tamarind",
    "chayote": "chayote"
}


ventana = tk.Tk()
ventana.title("Traductor de Frutas")
ventana.geometry("400x300")
ventana.resizable(False, False)

tk.Label(
    ventana,
    text="Escribe el nombre de la fruta en ESPAÑOL\ny presiona Traducir",
    font=("Arial", 11),
    fg="blue"
).pack(pady=10)

entrada = tk.Entry(ventana, width=30, font=("Arial", 12))
entrada.pack(pady=10)

resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 14),
    fg="green"
)
resultado.pack(pady=10)

def traducir():
    palabra = entrada.get().lower().strip()

    if palabra == "":
        messagebox.showerror("Error", "Escribe una fruta")
        return

    if palabra in frutas:
        resultado.config(text=f"Inglés: {frutas[palabra]}")
    else:
        resultado.config(text="Fruta no encontrada")

  tk.Button(
    ventana,
    text="Traducir",
    command=traducir,
    width=15,
    bg="green",
    fg="white"
).pack(pady=10)

ventana.mainloop()
