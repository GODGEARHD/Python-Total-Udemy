"""
juego de adivinar el numero

numero aleatorio entre 1 y 100

8 intentos en total

posibles flujos:

    1.- numero erroneo, MENOR que el elegido

    2.- numero erroneo, MAYOR que el elegido

    3.- numero MENOR que 1 o MAYOR que 100

    4.- numero correcto

se debe contar el numero de intentos, ya que si se realizan los 8 intentos (el maximo),
el programa debe terminar, indicandole al usuario que el juego acabo y que lo perdio

ademas, si el programa entra en el 4º flujo (numero correcto, el usuario gana el juego),
se le debe notificar al jugador cuantos intentos le ha llevado
"""

import random


def main():
    print("######################## Juego \"Adivina el Número\" ########################")
    aleatorio = rdm()


def rdm():
    return random.randint(1, 100)


if __name__ == "__main__":
    main()
