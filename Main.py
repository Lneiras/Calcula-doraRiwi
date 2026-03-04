#Colores
from Operaciones import suma, resta, multiplicacion, division, salir
from Historial import mostrar_historial, eliminar_historial

Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Reset = "\033[0m"


#calculadora 

def menu():
    print("=" * 50)
    print(f"{Cian}              Operaciones disponibles:{Reset}")
    print("=" * 50)
    print(f"{Azul}\n 1. Sumar{Reset}",
    f"{Azul} 2. Restar{Reset}",
    f"{Azul} 3. Multiplicar{Reset}",
    f"{Azul} 4. Dividir{Reset}",
    f"{Azul} 5. Salir{Reset}",
    f"{Azul} 6. Ver historial{Reset}",
    f"{Azul} 7. Limpiar historial{Reset}",
    sep="\n")

def main():
    print("\n" + "=" * 50)
    print(f"{Magenta}             Bienvenido a tu calculadora{Reset}")

    historial_global = []

    while True:
            menu()
            operacion = int(input(f"{Blanco}\n Que operacion deseas realizar?:  {Reset}"))
            if operacion == 1:
                resultado = suma()
                historial_global.append((f"Sumaste", resultado))
            elif operacion == 2:
                resultado = resta()
                historial_global.append((f"Restaste", resultado))
            elif operacion == 3:
                resultado = multiplicacion()
                historial_global.append((f"Multiplicaste", resultado))
            elif operacion == 4:
                resultado = division()
                historial_global.append((f"Dividiste", resultado))
            elif operacion == 5:
                salir()
                break
            elif operacion == 6:
                mostrar_historial(historial_global)
            elif operacion == 7:
                eliminar_historial(historial_global)
            else:
                print(f"{Rojo}Operacion no valida{Reset}")

main()