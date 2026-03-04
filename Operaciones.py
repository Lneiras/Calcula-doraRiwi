
import time

#colores
Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Reset = "\033[0m"

#suma
def suma():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    Suma = num1 + num2
    import time
    print("Calculando...")
    time.sleep(2)  # Pausa de 2 segundos
    print(f"{Verde}El resultado de la suma es: {Reset}", Suma)
    return f"{num1} + {num2} = {Suma}"

#resta
def resta():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    Resta = num1 - num2
    import time
    print("Calculando...")
    time.sleep(2)  # Pausa de 2 segundos
    print(f"{Verde}El resultado de la resta es: {Reset}", Resta)
    return f"{num1} - {num2} = {Resta}"

#multiplicación
def multiplicacion():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    Multiplicacion = num1 * num2
    import time
    print("Calculando...")
    time.sleep(2)  # Pausa de 2 segundos
    print(f"{Verde}El resultado de la multiplicación es: {Reset}", Multiplicacion)
    return f"{num1} * {num2} = {Multiplicacion}"  

#división
def division():
    while True:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if num2 <= 0:
            print(f"{Rojo}no es posible realizar esta operación{Reset}")
            continue
        else:
            Division = num1 / num2
            import time
            print("Calculando...")
            time.sleep(2)  # Pausa de 2 segundos
            print(f"{Verde}El resultado de la división es: {Reset}", Division)
            return f"{num1} / {num2} = {Division}" 
            break

#salir
def salir():
    print(f"{Magenta}\n Gracias por utilizar la calculadora{Reset}")
    