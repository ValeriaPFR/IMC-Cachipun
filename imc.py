""""#Crear un programa que calcule el IMC de una persona"""
""""Palabra clave def: define una tarea específica. Es decir calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la altura en metros.
    Fórmula: IMC = peso (kg) / (altura (m) ** 2)
    
    El código se divide en 4 partes:
    1-> Definir el problema al que busca otorgar solución este código.
    2-> Calcular el IMC
    3-> Interpretar el resultado de acuerdo a la escala.
    4-> Mostrar resultado al usuario/a    
    
    La función main() encierra las funciones que se ejecutarán en el programa. Es decir, al usar la función def main() estamos 80
    
    """
def calcular_imc(peso, estatura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la altura en centímetros para lo que se divide por 100 para la conversión de unidades de medida.
    Fórmula: IMC = peso (kg) / ((altura (cm) / 100) ** 2)
    Al tener múltiples opciones de interpretación, entonces luego del if, se usa elif, para finalizar con else
    """
    imc = peso / ((altura / 100) ** 2)
    
    if imc < 18.5:  
        interpretacion = "Bajo peso"
    elif imc < 25:
        interpretacion = "Peso normal"
    elif imc < 30:
        interpretacion = "Sobrepeso"
    elif imc < 35:
        interpretacion = "Obesidad grado I"
    elif imc < 40:
        interpretacion = "Obesidad grado II"
    else:
        interpretacion = "Obesidad grado III"
        
    return imc, interpretacion

def main():
    # Ingrese el peso en kilogramos
    peso = float(input("Ingrese su peso en kilogramos: "))
    
    # Ingrese la altura en centímetros
    altura = float(input("Ingrese su altura en centímetros: "))
    
    # Calcula el IMC y su interpretación
    imc, interpretacion = calcular_imc(peso, altura)
    
    # Muestra el resultado extrapolado con 2 decimales
    print(f"Su IMC es: {imc:.2f}")
    print(f"Interpretación: {interpretacion}")


if __name__ == "__main__":
    main()
 