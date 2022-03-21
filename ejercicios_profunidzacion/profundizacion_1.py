# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia


- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('Ingrese el primer número que desea operar:')
numero_1 = int(input())
print('Ingrese el segundo número que desea operar:')
numero_2 = int(input())
print('Ingrese la operacion que desea realizar indicando:\nA) Suma\nB) Resta\nC) Multiplicación\nD) División\nE) Exponente/Potencia:')
operación_1 = str(input())
while operación_1 != "a" and operación_1 != "A" and operación_1 != "b" and operación_1 != "B" and operación_1 != "c" and operación_1 != "C" and operación_1 != "d" and operación_1 != "D" and operación_1 != "e" and operación_1 != "E":
    print('Error Ingrese la operacion que desea realizar indicando:\nA) Suma\nB) Resta\nC) Multiplicación\nD) División\nE) Exponente/Potencia:')
    operación_1 = str(input())
if operación_1 == "a" or operación_1 =="A": 
    print("la suma entre",numero_1,"y",numero_2,"es:", numero_1+numero_2)
if operación_1 == "b" or operación_1 =="B":
    print("la resta entre",numero_1,"y",numero_2,"es:", numero_1-numero_2)
if operación_1 == "c" or operación_1 =="C":
    print("la multiplicación entre",numero_1,"y",numero_2,"es:", numero_1*numero_2)
if operación_1 == "d" or operación_1 =="D":
    print("la división entre",numero_1,"y",numero_2,"es:", numero_1/numero_2)
if operación_1 == "e" or operación_1 =="E":
    print("la potencia entre",numero_1,"y",numero_2,"es:", numero_1**numero_2)

    
              


