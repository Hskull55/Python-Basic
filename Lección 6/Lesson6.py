# Task 1 - create a list with manually added items and print these elements. These elements be random names

names = ["Anna", "Elizabeth", "George", "Tom", "Adam", "Chris"]
# print(names)
# print(type(names))

# Task 2 - using the len() function on list
# print("The length of your list is: " + str(len(names)))

# Task 3 - print out the first, last and a chosen element from the list
# print(names[0]) # first
# print(names[-1]) # last
# print(names[-2]) # chosen

# Task 4 - List Slicing
# print(names[0:3])
# print(names[:2])
# print(names[3:-1])
# print(names[3:])

# EXTRA

# length = len(names)
#
# while True:
#     user_input = input("Introduce un índice: ")
#
#     # Comprobamos si es un número positivo o un número negativo válido
#     if user_input.isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
#         index = int(user_input)
#
#         # Comprobamos que esté dentro del rango de la lista
#         if -length <= index <= length - 1:
#             print(names[index])
#             break
#         else:
#             print("El número no es un índice válido para esta lista.")
#     else:
#         print("La entrada no es correcta.")

# Task 5 - using loop to print each element from the list
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1

# Task 6 - create a new list and fill it with the first 50 positive integers with a loop
# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(i)
#     i += 1
# print(numbers)

# Task 7 - create a new list, which contains the first 20 odd numbers
# odd_numbers = []
# even_numbers = []
# i = 0
# while i < 20:
#     if i % 2 == 1:
#         odd_numbers.append(i)
#     else:
#         even_numbers.append(i)
#     i += 1
# print("Odd numbers: " + str(odd_numbers))
# print("Even numbers: " + str(even_numbers))

# Task 8 - Switch two list elements each other
# list_1 = [1,2,3,4,5]
# list_2 = [11,23,34,45,57]
# print("List 1 before switch: %s" %list_1)
# print("List 2 before switch: %s" %list_2)
# print("-" * 40)
#
# i = 0
# while i < 5: # Debería ser un len(list_1), realmente ni eso
#     temp = list_1[i]
#     list_1[i] = list_2[i]
#     list_2[i] = temp
#
#     i += 1
#
# print("List 1 after switch: %s" %list_1)
# print("List 2 after switch: %s" %list_2)

# Task 9 - insert items into a list
# insertList = []
# insertList.insert(0,"Logiscool")
# insertList.insert(1,"fun")
# insertList.insert(1,"is")
# insertList.insert(5,"everyone") # Como es mayor que la longitud de la lista, se pone al final
# insertList.insert(3,"for")
# print(insertList)

# Task 10 - deleting items from a list
# girl_names = ["Anne", "Elizabeth", "Elon", "Sophie", "Hannah"]
# boy_names = ["Thomas", "George", "Rick", "Olivia", "Noah", "Olivia"]
# print(girl_names)
# print(boy_names)
# print("-" * 40)
# girl_names.pop(2)
# boy_names.remove("Olivia") # Remove solo borra la primera
# print(girl_names)
# print(boy_names)
# print("-" * 40)
# borrado = boy_names.pop(-1)
# print("Se ha eliminado " + borrado)
# print(boy_names)

# Task 11 - summa of number items
# numberList = [1,40,523,6851,0,346,321,8,1,457,123]
# i = 0
# sum_of_numbers = 0
# while i < len(numberList):
#     sum_of_numbers += numberList[i]
#     i += 1
# print(sum_of_numbers)

# Task 12 - occurrences in the list
# repeatList = [1, 0, 1, 2, 0, 2, 2, 1, 0, 1, 2, 1, 1, 1, 0]
# i = 0
# occurrences = 0
# value = int(input("What value are we looking for?\n"))
# while i < len(repeatList):
#     if repeatList[i] == value:
#         occurrences += 1
#     i += 1
# print("The number " + str(value) + " appears " + str(occurrences) + " times in the list.")
