# Archivo principal para ejecutar la aplicación

from modelo.empleado import Empleado, EmpleadoTiempoCompleto
from servicio.gestion_empleados import mostrar_salario

def main():
    # Creación de instancias de las clases
    empleado1 = Empleado("Yurak", 1200)
    empleado2 = EmpleadoTiempoCompleto("Melissa", 1500, 300)

    # Demostración del funcionamiento del programa
    mostrar_salario(empleado1)
    print("------------------")
    mostrar_salario(empleado2)

if __name__ == "__main__":
    main()
