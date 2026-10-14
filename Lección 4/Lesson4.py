# Task 1 - Arithmetic operators
# print(5 + 5)
# print(6 - 4)
# print(9 * 10)
# print(9 / 3)
# print(9 / 2)
# print(7 % 4)
# print(3 ** 3)
# print(99 / 4)
# print(99 // 4)


# Task 2 - Assignment operators
# num = 8
# print(num)
# num += 7
# print(num)
# num -= 6
# print(num)
# num *= 5
# print(num)
# num /= 4
# print(num)
# num **= 2
# print(num)

# Task 3 - Comparison operators
# print(5 < 4)
# print(32 > 9)
# print(9 == 45)
# print(9 * 5 == 45)

# Task 4 - Identity operator
# Working but the IDE gives us an error
# print(9999999999999 is 9999999999999)
# print(8 is 9)
# print(6 is "peach")

# a = int("999999999")
# b = int("999999999")
# print(a == b)  # True (porque sus valores son iguales)
# print(a is b)  # False (porque están en sitios distintos de la memoria)

# lista_a = [1, 2, 3]
# lista_b = [1, 2, 3]
# lista_c = lista_a  # lista_c "copia" la referencia al mismo objeto
# # 1. Comparar contenido (==)
# print(lista_a == lista_b)  # True -> Tienen los mismos elementos adentro.
# # 2. Comparar identidad física en memoria (is)
# print(lista_a is lista_b)  # False -> Aunque tienen lo mismo, son DOS listas distintas creadas en sitios diferentes de la memoria RAM.
# # 3. ¿Cuándo da True con 'is'?
# print(lista_a is lista_c)  # True -> 'lista_c' apunta exactamente al mismo objeto en la memoria que 'lista_a'.

# Task 5 - membership operator

# z1 = 'H'
# z2 = 'K'
# z3 = "world"
# word = "Hello world"
# print(z1 in word)
# print(z2 in word)
# print(z3 in word)

# Task 6 - use operators in if statements
# a1 = 4
# a2 = 7
# if a1 < a2:
#     print(str(a1) + " is smaller than " + str(a2))
# if a1 ** a2 == a2 ** a1:
#      print(str(a1) + "^" + str(a2) + " equals to " + str(a2) + "^" + str(a1))
# if a1 ** a2 != a2 ** a1:
#      print(str(a1) + "^" + str(a2) + " not equals to " + str(a2) + "^" + str(a1))

# Task 7 - email address validity
# address = "hskull55@logiscool.com"
# if "@" in address and ( address.endswith(".com") or address.endswith(".es")):
#     print("Valid address")
# else:
#     print("Invalid address")

# Task 8 - value of a number
# number = float(input("Enter a number!\n"))
# if number >= 0:
#     if number == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")

# Task 9 - which one is the greatest
# a = float(input("Enter the first number!\n"))
# b = float(input("Enter the second number!\n"))
# c = float(input("Enter the third number!\n"))
# if a > b:
#     if a > c:
#         print(str(a) + " is the greatest number.")
#     elif c > a:
#         print(str(c) + " is the greatest number.")
#     else:
#         print("There are multiple greatest numbers here.")
# elif b > a:
#     if b > c:
#         print(str(b) + " is the greatest number.")
#     elif c > b:
#         print(str(c) + " is the greatest number.")
#     else:
#         print("There are multiple greatest numbers here.")
# else:
#     if c > b:
#         print(str(c) + " is the greatest number.")
#     else:
#         print("There are multiple greatest numbers here.")


# numeros = [
#     float(input("Enter the first number!\n")),
#     float(input("Enter the second number!\n")),
#     float(input("Enter the third number!\n")),
# ]
#
# mayor = max(numeros)
#
# if numeros.count(mayor) > 1:
#   print("There are multiple greatest numbers here.")
# else:
#   print(f"{mayor} is the greatest number.")
#   print("%s is the greatest number." % mayor)
#   print("%f is the greatest number." % mayor)

# Task 10 - I thought of an animal
# animal_leg = int(input("Has 2 or 4 legs?"))
# animal_fly = input("Can fly? (yes/no)")
# animal_swim = input("Can swim? (yes/no)")
# if animal_leg == 2:
#     if animal_fly.lower == "yes":
#         if animal_swim.lower == "yes":
#             print("It's an atlantic puffins")
#         else:
#             print("It's a pidgeon")
#     elif animal_fly.lower == "no":
#         if animal_swim.lower == "yes":
#             print("It's a penguin")
#         else:
#             print("It's a kiwi")
#
# elif animal_leg == 4:
#     if animal_fly.lower == "yes":
#         if animal_swim.lower == "yes":
#             print("There is no such animal...(except a pegasus)")
#         else:
#             print("It's a butterfly")
#     elif animal_fly.lower == "no":
#         if animal_swim.lower == "yes":
#             print("It's a horse")
#         else:
#             print("It's a camel")
