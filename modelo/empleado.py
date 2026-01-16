# Clase base Empleado
# Aquí se aplican los conceptos de:
# - Encapsulación
# - Herencia
# - Polimorfismo

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario  # Atributo protegido (encapsulación)

    # Acceder al salario
    def get_salario(self):
        return self._salario

    # Sobrescritura (polimorfismo)
    def calcular_salario(self):
        return self._salario


# Clase derivada que hereda de Empleado
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    # Polimorfismo: se sobrescribe calcular_salario
    def calcular_salario(self):
        return self._salario + self.bono
