# Task 1 - while loop that repeats forever - comment this task later so you don't run into infinite loop later
number = 1
# while True:
#     print(number)
#     number += 1

# Task 2 - print only the first 10 integers and calculate the sum of these numbers
number_2 = 1

# Con while
# sum = 0
# while number_2 < 11:
#     print(number_2)
#     sum += number_2
#     number_2 += 1
# print(sum)

# Con for
# suma = 0
# for number_2 in range(1, 11): #number 2 es nuestra "i"
#     print(number_2)
#     suma += number_2
# print(suma)

# Task 3 - number of digits in a number
# num = 9845198
# count = 0
# while num != 0:
#     num //= 10 # División sin decimales
#     count+= 1
# print("Number of digits: ", count)

# Task 4 - number guessing game
# num = 42
# guessnum = int(input("How many guesses should we have?\n"))
# guess = 0
# while guessnum > 0 and  guess != num:
#     guess = int(input("Take a guess:\n"))
#     if guess > num:
#         print("I thought of a smaller number.")
#     elif guess < num:
#         print("I thought of a bigger number.")
#     guessnum -= 1
#     print("You have " + str(guessnum) + " chances left.")
# if guess == num:
#     print("Congratulations, I thought of " + str(guess) + " indeed.")
# else:
#     print("Maybe next time. The number I thought was " + str(num) + ".")

# Task 5 - display the Fibonacci series
# counter = 10
# num1 = 0
# num2 = 1
# print("Fibonacci sequence:")
# while counter > 0:
#     print(str(num1))
#     temp = num1 + num2
#     num1 = num2
#     num2 = temp
#     counter -= 1

# Task 6 - nursery rhyme
# i = 0
# times = int(input("How many times you want to say it? "))
# word = "If you happy and you know it..."
# while i < times:
#     do_something = input("Do something: ")  # Clap your hand
#     print("%s \n%s" %(word, do_something))
#     i += 1

# Ejercicio de Pucci - prime number from 1 to 100
# number = 2
# counter = 2
# isPrime = True
# while number < 100:
#     counter = 2
#     isPrime = True
#     while counter < number:
#         if number % counter == 0:
#             # print(str(number) + " es divisible entre " + str(counter))
#             isPrime = False
#         counter += 1
#     if isPrime:
#         print(number)
#         # print(str(number) + " es primo")
#     number += 1

# # Triángulo
# # Pista --> print("@" * 5)
# longitud = int(input("Introduce la longitud máxima del patrón: "))
#
# i = 1
# while i <= longitud:
#     print("*" * i)
#     i += 1
#
# i = longitud - 1
# while i >= 1:
#     print("*" * i)
#     i -= 1