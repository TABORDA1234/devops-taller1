class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}"