# Archivo encargado de la lógica del sistema

def mostrar_salario(empleado):
    # Se demuestra polimorfismo,ya que funciona con cualquier tipo de Empleado
    print(f"Empleado: {empleado.nombre}")
    print(f"Salario total: {empleado.calcular_salario()}")
