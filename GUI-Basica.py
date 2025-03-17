import tkinter as tk
from tkinter import messagebox

class DataApp:
    def __init__(self, master):
        # Configuración de la ventana principal
        self.master = master
        master.title("Aplicación de Gestión de Datos")  # Título descriptivo

        # Marco superior para organizar etiqueta, campo de texto y botón "Agregar"
        self.top_frame = tk.Frame(master)
        self.top_frame.pack(pady=10)

        # Etiqueta instructiva
        self.label = tk.Label(self.top_frame, text="Ingrese información:")
        self.label.pack(side=tk.LEFT, padx=5)

        # Campo de texto para la entrada del usuario
        self.entry = tk.Entry(self.top_frame, width=30)
        self.entry.pack(side=tk.LEFT, padx=5)

        # Botón "Agregar" que permite agregar la información ingresada
        self.add_button = tk.Button(self.top_frame, text="Agregar", command=self.add_item)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Lista para mostrar los datos agregados
        self.listbox = tk.Listbox(master, width=50)
        self.listbox.pack(pady=10)

        # Botón "Limpiar" para borrar la información mostrada en la lista
        self.clear_button = tk.Button(master, text="Limpiar", command=self.clear_list)
        self.clear_button.pack(pady=5)

    def add_item(self):
        """
        Función que se ejecuta al presionar el botón 'Agregar'.
        Verifica que el campo de texto no esté vacío, agrega el dato a la lista,
        y luego limpia el campo de entrada.
        """
        data = self.entry.get()
        if data.strip() != "":
            self.listbox.insert(tk.END, data)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese algún texto.")

    def clear_list(self):
        """
        Función que se ejecuta al presionar el botón 'Limpiar'.
        Borra todos los elementos de la lista.
        """
        self.listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
