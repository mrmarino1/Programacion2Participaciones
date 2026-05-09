import tkinter as tk
from tkinter import messagebox


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcular las 4 operaciones")
        self.root.geometry("1000x700")
        self.root.configure(bg="#ffff99")

        # ================= HEADER =================
        header = tk.Frame(root, bg="#0033cc", bd=3, relief="raised")
        header.pack(fill="x")

        titulo = tk.Label(
            header,
            text="Aplicacion",
            font=("Consolas", 32, "bold"),
            fg="white",
            bg="#0033cc"
        )
        titulo.pack(pady=10)

        # ================= CONTENIDO =================
        frame = tk.Frame(root, bg="#ffff99")
        frame.pack(pady=20)

        # Numero 1
        lbl_n1 = tk.Label(
            frame,
            text="Numero 1:",
            font=("Consolas", 18),
            bg="#ffff99"
        )
        lbl_n1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.txtN1 = tk.Entry(frame, font=("Consolas", 18), width=20)
        self.txtN1.grid(row=0, column=1, padx=10, pady=10)

        # Numero 2
        lbl_n2 = tk.Label(
            frame,
            text="Numero 2:",
            font=("Consolas", 18),
            bg="#ffff99"
        )
        lbl_n2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.txtN2 = tk.Entry(frame, font=("Consolas", 18), width=20)
        self.txtN2.grid(row=1, column=1, padx=10, pady=10)

        # Resultados
        lbl_resultados = tk.Label(
            frame,
            text="Resultados",
            font=("Consolas", 20, "bold"),
            bg="#ffff99"
        )
        lbl_resultados.grid(row=2, column=0, columnspan=2, pady=15)

        # Suma
        lbl_suma = tk.Label(
            frame,
            text="Suma",
            font=("Consolas", 16),
            bg="#ffff99"
        )
        lbl_suma.grid(row=3, column=0, padx=10, pady=5)

        self.txtSuma = tk.Entry(frame, font=("Consolas", 12), width=30)
        self.txtSuma.grid(row=4, column=0, padx=10, pady=5)

        # Resta
        lbl_resta = tk.Label(
            frame,
            text="Resta",
            font=("Consolas", 16),
            bg="#ffff99"
        )
        lbl_resta.grid(row=3, column=1, padx=10, pady=5)

        self.txtResta = tk.Entry(frame, font=("Consolas", 12), width=30)
        self.txtResta.grid(row=4, column=1, padx=10, pady=5)

        # Multiplicacion
        lbl_producto = tk.Label(
            frame,
            text="Multiplicacion",
            font=("Consolas", 16),
            bg="#ffff99"
        )
        lbl_producto.grid(row=5, column=0, padx=10, pady=5)

        self.txtProducto = tk.Entry(frame, font=("Consolas", 12), width=30)
        self.txtProducto.grid(row=6, column=0, padx=10, pady=5)

        # Division
        lbl_division = tk.Label(
            frame,
            text="Division",
            font=("Consolas", 16),
            bg="#ffff99"
        )
        lbl_division.grid(row=5, column=1, padx=10, pady=5)

        self.txtDivision = tk.Entry(frame, font=("Consolas", 12), width=30)
        self.txtDivision.grid(row=6, column=1, padx=10, pady=5)

        # ================= BOTONES =================
        btn_frame = tk.Frame(root, bg="#ffff99")
        btn_frame.pack(pady=20)

        btn_calcular = tk.Button(
            btn_frame,
            text="CALCULAR",
            font=("Consolas", 20),
            bg="#ccffff",
            width=15,
            command=self.calcular
        )
        btn_calcular.grid(row=0, column=0, padx=20)

        btn_salir = tk.Button(
            btn_frame,
            text="SALIR",
            font=("Consolas", 20),
            bg="#ccffff",
            width=15,
            command=root.quit
        )
        btn_salir.grid(row=0, column=1, padx=20)

    # ================= FUNCION CALCULAR =================
    def calcular(self):
        try:
            n1 = float(self.txtN1.get())
            n2 = float(self.txtN2.get())

            suma = n1 + n2
            resta = n1 - n2
            producto = n1 * n2

            self.txtSuma.delete(0, tk.END)
            self.txtSuma.insert(0, f"La suma es: {suma}")

            self.txtResta.delete(0, tk.END)
            self.txtResta.insert(0, f"La resta es: {resta}")

            self.txtProducto.delete(0, tk.END)
            self.txtProducto.insert(0, f"La multiplicacion es: {producto}")

            self.txtDivision.delete(0, tk.END)

            if n2 != 0:
                division = n1 / n2
                self.txtDivision.insert(0, f"La division es: {division}")
            else:
                self.txtDivision.insert(
                    0,
                    "La division entre 0 es imposible"
                )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese numeros validos"
            )


# ================= MAIN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()