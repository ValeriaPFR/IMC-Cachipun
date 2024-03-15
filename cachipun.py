# Importar el módulo random desde la librería de Python, para generar resultados aleatorios
import random
""""Se define una clase en Python llamada Cachipún/sin tilde, 
una clase es una especie de plantilla para crear objetos, que agrupa o 'encapsula' datos y comportamientos 
relacionados entre sí """
class Cachipun:
    #Se define el método juego, "jugar()" en este caso, que agrupa la lógica del juego. 
    """Self indica que se solicitará primero al usuario que ingrese su opción"""
    def jugar(self):
        # Definir las opciones disponibles en el juego
        opciones = ["piedra", "papel", "tijera"]
        # Solicitar la jugada del usuario, se debe escribir la palabra corespondiente a la opción elegida
        jugada_usuario = input("Ingrese su jugada (piedra, papel o tijera): ").lower()
        # Verificar si la jugada del usuario es válida en caso de ingresar otra opción, ej. "taza" marca un error
        if jugada_usuario not in opciones:
            print("Argumento inválido: Debe ser piedra, papel o tijera.")
            return self.jugar() #Vuelve a pedir al usuario una opción válida
        
        # Generar aleatoriamente la jugada de la computadora
        jugada_computador = random.choice(opciones)
        
        # Muestra las jugadas realizadas
        print(f"Tu jugaste {jugada_usuario}")
        print(f"Computador jugó {jugada_computador}")

    """Interpretación de resultados"""
        # Determinar el resultado del juego
        if jugada_usuario == jugada_computador:
            print("¡Empate!")  # Si las jugadas son iguales, es un empate
        elif (jugada_usuario, jugada_computador) in [("piedra", "tijera"), ("papel", "piedra"), ("tijera", "papel")]:
            print("¡Usuario ganó!")  # Si el usuario gana, muestra un mensaje de victoria
        else:
            print("¡Computador ganó!")  # Si la computadora gana, muestra un mensaje de derrota

"""Se termina de encapsular los datos del juego. Con las siguientes líneas de código se da por terminada la clase ingresada al inicio"""
    juego = Cachipun()
    juego.jugar() 