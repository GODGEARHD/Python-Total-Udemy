 nombre = input("¿Cuál es tu nombre?\n")

ventas = input("¿Cuántas ventas has realizado este mes?\n")

comisiones = (int(ventas) * 13) / 100

print("Hola " + nombre + ", las comisiones que te corresponden por tus " + ventas + "€ en ventas son de "
      + str(comisiones) + "€")
