import tkinter as tk

# Crear una ventana con Tkinter
root = tk.Tk()
root.title("Expresiones del Robot")

# Crear un lienzo para dibujar en la ventana
canvas = tk.Canvas(root, width=800, height=480, bg='black')
canvas.pack()

# Colores en formato hexadecimal
eye_color_normal = "#60D8F0"  # Azul claro para los ojos normales
eye_color_happy = "#60D8F0"  # Azul claro para los ojos felices
eye_color_sad = "#60D8F0"  # Azul más oscuro para los ojos tristes
eye_color_serious = "#60D8F0"  # Azul claro para la cara seria
eye_color_mad = "#60D8F0"  # Azul claro para la cara seria
eye_color_thinking = "#60D8F0"  # Azul para la expresión de pensar


def draw_eyes(expression="normal"):

    # Limpiar el lienzo
    canvas.delete("all")

    if expression == "normal":
        # Ojos normales: Círculos
        canvas.create_oval(180, 190, 330, 340, fill=eye_color_normal)  # Ojo izquierdo
        canvas.create_oval(470, 190, 620, 340, fill=eye_color_normal)  # Ojo derecho


    elif expression == "happy":
        # Ojos felices: Media luna curva hacia arriba
        # Ojo izquierdo
        canvas.create_arc(180, 190, 330, 340, start=0, extent=180,
                        fill=eye_color_happy, outline="")
        # Ojo derecho
        canvas.create_arc(470, 190, 620, 340, start=0, extent=180,
                        fill=eye_color_happy, outline="")


    elif expression == "sad":
        # Ojos tristes: Media luna muy pronunciada hacia abajo
        # Ojo izquierdo
        canvas.create_arc(180, 190, 330, 340, start=200, extent=180,
                        fill=eye_color_sad, outline="")
        # Ojo derecho
        canvas.create_arc(470, 190, 620, 340, start=160, extent=180,
                        fill=eye_color_sad, outline="")


    elif expression == "serious":
        # Ojos serios: Media luna hacia abajo
        # Ojo izquierdo
        canvas.create_arc(180, 190, 330, 340, start=180, extent=180,
                        fill=eye_color_serious, outline="")
        # Ojo derecho
        canvas.create_arc(470, 190, 620, 340, start=180, extent=180,
                        fill=eye_color_serious, outline="")


    elif expression == "mad":
        canvas.create_arc(180, 190, 330, 340, start=160, extent=180,
                        fill=eye_color_mad, outline="")
        # Ojo derecho
        canvas.create_arc(470, 190, 620, 340, start=200, extent=180,
                        fill=eye_color_mad, outline="")


    elif expression == "thinking":
            # Ojos pensando: Ojos semi-cerrados y ligeramente inclinados hacia arriba
            # Ojo izquierdo (semi-cerrado hacia arriba)
        canvas.create_arc(180, 200, 330, 330, start=0, extent=180,
                        fill=eye_color_thinking, outline="")
        # Ojo derecho (semi-cerrado hacia arriba)
        canvas.create_arc(470, 200, 620, 330, start=0, extent=180,
                        fill=eye_color_thinking, outline="")


draw_eyes("normal")

# Cambiar la expresión a "feliz" después de 2 segundos
root.after(2000, lambda: draw_eyes("happy"))

# Cambiar la expresión a "triste" después de 4 segundos
root.after(4000, lambda: draw_eyes("sad"))

# Cambiar la expresión a "seria" después de 6 segundos
root.after(6000, lambda: draw_eyes("serious"))

root.after(8000, lambda: draw_eyes("mad"))

root.after(10000, lambda: draw_eyes("thinking"))

# Ejecutar la ventana de Tkinter
root.mainloop()
