# Task 1 - print number using for loop
# for i in range(10):
#     print(i)

# Task 2 - print positive number using for loop
# for i in range(1,11):
#     print(i)

# Task 3 - print even number using for loop
# for i in range(2,101,2):
#     print(i)

# Task 4 - for loop on strings
# for i in "Hello World!":
#     print(i)

# Task 5 - multiplication table
# num = int(input("Give me a number and i'll show you its multiplication table: "))
# for i in range(1,11,1):
#     print(str(i) + " * " + str(num) + " = " + str(i*num))

# # Task 6 - decryption with for loop
# encrypted_message = "Mlye mnsa msel eiesp iYnogs huinktaigle  mKoirrnai.n gI.’ mJ u3s3t  yleiakres  ao lbda.b yM,y  Ih owuaskee  iusp  iwni tthhoeu tn oarntyh efaastti gsueec toiro ns torfe sMso riino ht,h ew hmeorren ianlgl.  tIh ew avsi ltloalsd  atrhee,r ea nwde rIe  anmo  niosts umeasr raite dm.y  Il awsotr kc haesc ka‑nu pe.m pIl’omy eter yfionrg  tthoe  eKxapmlea iYnu  tdheapta rIt’mme nat  psetrosroens ,w haon dw iIs hgeest  thoo mlei veev ear yv edrayy  qbuyi e8t  PlMi faet.  tIh et alkaet ecsatr.e  In odto nt’ot  tsrmooukbel,e  bmuyts eIl fo cwciatshi oannayl leyn edmriiensk,.  lIi’kme  iwni nbneidn gb ya n1d1  lPoMs,i nagn,d  tIh amta kweo usludr ec aIu sgee tm ee itgoh tl ohsoeu rssl eoefp  salte enpi,g hnto.  mTahtatte ri sw hhaotw.  IA fdteearl  hwaivtihn gs oac igeltays,s  aonfd  wIa rkmn omwi ltkh aatn di sd owihnagt  abbroiuntg st wmeen thya pmpiinnuetsess.  oAfl tshtoruegthc,h eisf  bIe fwoerree  gtooi nfgi gthot ,b eId ,w oIu ludsnu’atl llyo shea vteo  naon ypornoeb."
# decrypted_message = ""
# for i in range(0,len(encrypted_message)):
#     if i % 2 == 0:
#         decrypted_message += encrypted_message[i]
# for i in range(0,len(encrypted_message)):
#     if i % 2 == 1:
#         decrypted_message += encrypted_message[i]
# print(encrypted_message)
# print(decrypted_message)

# "Hee lalnod,  Im ya mn a1m7e  yiesa rGse oorlgd"
# "Mdy,  nJaammee si sB oBnodn."
# "Wyh earne  eclaenp hIa nbtu?"

# Task 7 - encryption with for loop
# new_decrypted_message = input("Introduce el mensaje a cifrar: ")
# print(new_decrypted_message)
# first_half = new_decrypted_message[:(len(new_decrypted_message)+1)//2] # +1 para grantizar que la primera mitad sea la más larga en caso de longitud impar
# second_half = new_decrypted_message[(len(new_decrypted_message)+1)//2:]
# new_encrypted_message = ""
# for i in range((len(new_decrypted_message)+1)//2):
#     new_encrypted_message += first_half[i]
#     if i < len(second_half):
#         new_encrypted_message += second_half[i]
# print(new_encrypted_message)

# Task 8 - Generating numbers with for loop and add them to a list
# list_1 = []
# for i in range(50):
#     list_1.append(i)
# print(list_1)

# Task 9 - Generate numbers with for loop which start with 9 to 99
# list_1 = []
# for j in range(9, 99):
#     list_1.append(j)
# print(list_1)

# Task 10 - Generate numbers with for loop from 7 to -20
# list_1 = []
# for k in range(7, -20, -1):
#     list_1.append(k)
# print(list_1)

# Task 11 - Check that a given name is in the list with for loop
# names = ["Anna", "David", "George", "Alex", "Felix", "Mike"]
# chosen_name = input("Give me a name:\n")
# in_the_list = False
# for item in names:
#     if chosen_name.lower() == item.lower():
#         in_the_list = True
#
# if in_the_list:
#     print("Yes! This name is in the list!")
# else:
#     print("No, this name is NOT in the list...")

# Task 12 - generate multiplaction tables and print them one by one
# numbers = []
# for i in range(1,11):
#     for j in range(1,11):
#         numbers.append(i*j)
# print(numbers)
# # j = 0
# for i in range(10):
#     print(numbers[i*10:(i*10)+10])
#     # j += 1
