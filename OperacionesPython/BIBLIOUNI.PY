from datetime import datetime, timedelta


class Autor:

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: [nombre = {self.nombre}, nacionalidad = {self.nacionalidad}]")


class Pagina:

    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar_pagina(self):
        print(f"Pagina: [numero = {self.numero}, contenido = {self.contenido}]")


class Libro:

    def __init__(self, titulo, isbn, contenido_inicial):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        self.paginas.append(Pagina(1, contenido_inicial))

    def crear_pagina(self, numero, contenido):
        p = Pagina(numero, contenido)
        self.paginas.append(p)

    def mostrar_info(self):
        print(f"Libro: [titulo = {self.titulo}, isbn = {self.isbn}]")

    def leer(self):
        for pagina in self.paginas:
            pagina.mostrar_pagina()

    def get_titulo(self):
        return self.titulo


class Estudiante:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Estudiante: [codigo = {self.codigo}, nombre = {self.nombre}]")

    def get_nombre(self):
        return self.nombre


class Horario:

    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrar_horario(self):
        print(
            f"Horario: [Dias de apertura = {self.dias_apertura}, "
            f"Apertura = {self.hora_apertura}, "
            f"Cierre = {self.hora_cierre}]"
        )


class Prestamo:

    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=7)

    def mostrar_info(self):
        print(
            f"El estudiante: {self.estudiante.get_nombre()}, "
            f"se presto el libro: {self.libro.get_titulo()}"
        )


class Biblioteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = None

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def agregar_horario(self, dias_apertura, hora_apertura, hora_cierre):
        h = Horario(dias_apertura, hora_apertura, hora_cierre)
        self.horario = h

    def prestar_libro(self, estudiante, libro):
        if libro in self.libros:
            p = Prestamo(estudiante, libro)
            self.prestamos.append(p)
            p.mostrar_info()
        else:
            print("El libro no esta disponible en la biblioteca")

    def mostrar_estado(self):
        print(
            f"Biblioteca: [nombre = {self.nombre}, "
            f"libros = {len(self.libros)}, "
            f"autores = {len(self.autores)}, "
            f"prestamos = {len(self.prestamos)}]"
        )

        if self.horario is not None:
            self.horario.mostrar_horario()
        else:
            print("Horario: [Sin asignar]")

    def cerrar_biblioteca(self):
        print("La Biblioteca se cerro")
        self.prestamos.clear()


# =========================
# Aplicacion principal
# =========================

if __name__ == "__main__":

    # Libros
    l1 = Libro("Indigno de ser humano", "978-0811204811", "Cuaderno 1")
    l2 = Libro("Crónica de una muerte anunciada", "978-0307388946", "Capitulo 1")
    l3 = Libro("El Principito", "978-0156012195", "Capitulo I")

    # Solo unas páginas para probar
    l1.crear_pagina(70, "Cuaderno 2")
    l2.crear_pagina(35, "Capitulo 2")
    l3.crear_pagina(15, "Capitulo IV")

    # Mostrar funcionamiento
    l1.mostrar_info()
    l2.leer()

    # Estudiantes
    e1 = Estudiante("1895348", "Moises Mariño")
    e2 = Estudiante("2039485", "Belen Quispe")

    # Autores
    a1 = Autor("Osamu Dazai", "Japones")
    a2 = Autor("Gabriel Garcia Marquez", "Colombiano")

    # Biblioteca
    b1 = Biblioteca("Biblioteca Central - UMSA")

    b1.agregar_horario("Lunes a Viernes", "08:00", "21:00")

    # Agregar datos para probar
    b1.agregar_libro(l1)
    b1.agregar_libro(l2)

    b1.agregar_autor(a1)
    b1.agregar_autor(a2)

    # Mostrar estado
    b1.mostrar_estado()

    # Prestamos
    b1.prestar_libro(e1, l1)
    b1.prestar_libro(e2, l2)