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

    i = None
    aleatorio = rdm()
    acertado = False

    print("\n######################## Juego \"Adivina el Número\" ########################")
    print("\nEl juego consiste en encontrar el número que el programa elige de manera aleatoria antes de realizar "
          "8 intentos.\n"
          "Si lo consigues, GANAS; y si no lo consigues, PIERDES. Fácil, ¿verdad?\n"
          "Además, cada vez que le digas al programa un número que no sea el correcto,\n"
          "te dirá si el número que le has dicho es MAYOR o MENOR al número correcto. ¡Buena suerte!\n\n")

    for i in range(8):
        print(f'Intento Nº{i + 1}')
        try:
            numero = int(input("¿Cuál es el número oculto?\n"))
            if numero == aleatorio:
                acertado = True
                break
            elif numero > 100:
                print(f'Tu número {numero} es MAYOR que 100, no puedes pasar de ese límite (-1 intento :D)\n')
                continue
            elif numero > aleatorio:
                print(f'Tu número {numero} es MAYOR al número oculto, prueba con uno más bajo (-1 intento :D)\n')
                continue
            elif numero < 1:
                print(f'Tu número {numero} es MENOR que 1, no puedes pasar de ese límite (-1 intento :D)\n')
                continue
            else:
                print(f'Tu número {numero} es MENOR al número oculto, prueba con uno más alto (-1 intento :D)\n')
                continue
        except ValueError:
            if i == 7:
                print("Debes introducir un NÚMERO, no una letra.\n Ah! Y que sepas que te "
                      "has quedado sin intentos :)\n")
            else:
                print("Debes introducir un NÚMERO, no una letra.\n Ah! Y que sepas que acabas de gastar un intento, "
                      "te quedan: " + str(8 - (i + 1)) + " intentos ;P\n")
                continue

    if acertado:
        print(f'¡Enhorabuena! Has acertado el número oculto, y te ha llevado {i + 1} intento(s)\n')
    else:
        print(f'¡Más suerte la próxima! No has conseguido acertar el número oculto (que era {aleatorio}), inicia el '
              f'juego de nuevo y vuelve a intentarlo\n')

    print("\n######################## FIN DEL JUEGO ########################\n")


def rdm():
    return random.randint(1, 100)


if __name__ == "__main__":
    main()
