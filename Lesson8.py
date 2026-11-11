# Task 1 - hangman game

# puzle = "token pirata de fortnite"
# mi_solucion = "***** ****** ** ********"
# vidas = 10
# letras_correctas = []
# letras_incorrectas = []
# while vidas > 0 and puzle != mi_solucion:
#     print(mi_solucion)
#     intento = input("Escribe una nueva letra:\n")
#     if len(intento) == len(puzle):
#         temporal = mi_solucion
#         mi_solucion = intento
#         print("Intentas adivinar la solución... y tu intento es...")
#         if mi_solucion == puzle:
#             print("Correcto.")
#         else:
#             print("Incorrecto.")
#             vidas -= 1
#             print("Esto no está en el juego. Quedan " + str(vidas) + " vidas.")
#             mi_solucion = temporal
#     else:
#         encontrado_algo = False
#         for i in range(len(puzle)):
#             if puzle[i] == intento:
#                 lista_mi_solucion = list(mi_solucion) # Convertir cadena a lista
#                 lista_mi_solucion[i] = intento
#                 mi_solucion = "".join(lista_mi_solucion) # Unir lista en cadena
#                 encontrado_algo = True
#         if not encontrado_algo:
#             letras_incorrectas.append(intento)
#             vidas -= 1
#             print("Esto no está en el juego. Quedan " + str(vidas) + " vidas.")
#         else:
#             letras_correctas.append(intento)
#         print("Lista de letras correctas: " + str(letras_correctas))
#         print("Lista de letras incorrectas: " + str(letras_incorrectas))
# if vidas > 0:
#     print("¡Enhorabuena!")
# else:
#     print("Quizás la próxima vez..\n")

# Task 2 - find quadrant based on coordinates
# x_pos = int(input("What is the x position?\n"))
# y_pos = int(input("What is the y position?\n"))
# if x_pos >=0:
#     if y_pos >=0:
#         print("The coordinate point is in the first quadrant.")
#     else:
#         print("The coordinate point is in the fourth quadrant.")
# else:
#     if y_pos >=0:
#         print("The coordinate point is in the second quadrant.")
#     else:
#         print("The coordinate point is in the third quadrant.")

# Task 3 - greatest common divisor
# number_1 = int(input("What is the first number?\n"))
# number_2 = int(input("What is the second number?\n"))
# gcd = 1
# for i in range(1,number_1+1):
#     if number_1 % i == 0 and number_2 % i == 0:
#         gcd = i
# print("The greatest common divisor of " + str(number_1) + " and " + str(number_2) + " is " + str(gcd) + ".")

# Task 4 - prime factors of a number
# number = int(input("Give me a number:\n"))
# i = 2
# prime_factors = []
# while number > 1:
#     while number % i == 0:
#         number /= i
#         prime_factors.append(i)
#     i += 1
# print(prime_factors)

# Task 5 - least common multiple - without finding all the prime factors
# num_1 = int(input("What is the first number?\n"))
# num_2 = int(input("What is the second number?\n"))
# if num_1 > num_2:
#     lcm = num_1
# else:
#     lcm = num_2
# while not (lcm % num_1 == 0 and lcm % num_2 == 0):
#     lcm += 1
# print("The least common multiple of " + str(num_1) + " and " + str(num_2) + " is " + str(lcm) + ".")

# Task 6 - binary numbers
# print(bin(42))
# print(type(bin(42)))
# print(bin(42)[2:])
# print(int(bin(42)[2:]))

# Task 7 - solving equations with quadratic formula - ax^2+bx+c
# print("You have the following equation: ax^2+bx+c = 0\n "
#       "Tell me the a,b,c, parameters and i'll tell you the possible x values.")
# a = int(input("What is the value of a?\n"))
# b = int(input("What is the value of b?\n"))
# c = int(input("What is the value of c?\n"))
# if b**2-4*a*c > 0: # Discriminante
#     x_1 = (-b + (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
#     x_2 = (-b - (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
#     print("The roots of the equation are: " + str(x_1) + " and " + str(x_2) + ".")
# elif b**2-4*a*c < 0:
#     print("The equation has no real roots.")
# else:
#     x_1 = (-b + (b ** 2 - 4 * a * c) ** 1 / 2) / (2 * a)
#     print("There is only one root which is: " + str(x_1) + ".")