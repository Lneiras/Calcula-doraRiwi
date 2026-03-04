import os

def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' es para Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')