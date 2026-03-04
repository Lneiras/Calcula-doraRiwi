Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Reset = "\033[0m"

# Función para mostrar el historial
def mostrar_historial(lista_historial):
    print(f"\n{Amarillo}=== HISTORIAL DE OPERACIONES ==={Reset}")
    if not lista_historial:
        print(f"{Rojo}El historial está vacío.{Reset}")
    else:
        for i, registro in enumerate(lista_historial, 1):
            print(f"{Cian}{i}. {registro}{Reset}")

# Función para eliminar el historial
def eliminar_historial(lista_historial):
    lista_historial.clear()
    print(f"\n{Rojo}Historial eliminado correctamente.{Reset}")