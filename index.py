
# name = input("Как вас зовут?")
# print("Привет" + name)
# num_1 = int(input("Enter first number: "))
# num_2 = input("Enter first number: ")
# res = num_1 + int(num_2)
# Res = 'Shohruh'
# Res *= 5
# print(Res)
# print(res)



                        # Shartli operator
# num = input("What is your name?: ")
# if num == "Shohruh":
#     print("Salom ho'jayin\n")
# elif num == "Baxodir":
#     print("Salom Shohruhning adasi ")
# else: print("You are not Shohruh!!!")


# number = int(input("Enter number: "))

# if number > 0:
#     print("Siz 0 dan katta son kiritdingiz!!!")
#     if number > 10:
#         print("SIz 10 dan ham katta son kiritdingiz")
#     else: print("Siz 10 dan kichik lekin 0 dan katta son kirtdingiz")
# else:
#     print("Siz 0 dan kichik son kiritdingiz")

# name = input("Mevaning ismini kiriting: ")
# A = "Ha Olma" if name == "Olma" else "Olma emas"
# print(A)


                            #Random
# import random
# print(random.randrange(80,100))


                            #LOOPS
# i = 0
# while i < 10:
#     print(i)
#     i += 2
#
# i = 2000
# while i > 100:
#     i /= 2
#     print(i)
#
# for x in range(6):
#     print(x)

# for j in "hello world":
#     print(j * 2 , end='')
# for i in "hello world":
#     if i != 'w':
#         break
#     print(i*3, end='')

                                #List
# a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
# print(a)

# l = []
#
# l.append(23)   # element qo'shadi
# l.append(34)
# l.append('b')
# b = [47,68]
# l.extend(b)    # list elementlarini qo'shadi
# l.insert(1, 56)  # listning 1 chi elementiga 56 ni qo'yadi va list 1 taga suriladi
# l.remove(34)    # listdagi ko'rsatilgan elementni o'chiradi
# print(l)
# l.pop(2)        # listdagi elementning indexi bo'yicha o'chiradi , agar parametr ko'rsatilmasa oxirgi elementini o'chiradi
# print(l.index(56))   #ko'rsatilgan element nechinchi indexdaligini chiqaradi
# print(l.count(47))      # ko'rsatilgan elementning listdagi soni nechtaligini chiqaradi
# l.sort()        # sortirovka bo'yicha chiqaradi
# l.reverse()     # sortning teskarisiga chiqaradi
# l.clear()       # listning ichini polnisti tozalab tashlaydi
#
#
# print(l)



                                        # Index

# l = [21, 'sd', 34, 56.56]
#
# i = 0
# while i<4:
#     print(l[i])
#     i += 1
#
# print(l[:])



                            # Tub sonni topish

# N = int(input("Nechchigacha bo'lgan tub sonlarni topmoqchisiz ? :"))
# for i in range(2, N + 1):
#     tubson = True
#     for j in range(2, i):
#         if i % j == 0:
#             tubson = False
#             break
#     if tubson == True:
#         print("{} - tub son".format(i))


                    #Touple (Kortej) Listdan farqi uni keyin o'zgartirib bo'lmaydi va kam joy egallaydi xotiradan

# a = (32, 56.56, 'b')
# b = [32, 56.56, 'b']
#
# print(a.__sizeof__())
# print(b.__sizeof__())
#
# a =('hello world', 'dwd', 34)
# print(a)

# x = ("apple", "banana", "cherry")
# y = list(x)
# print(y)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)

# tuple = (32, 45, 'ls')
# print(tuple.__len__())


                                # dict -- slovar yoki obyekt

# a = {'one' : 1, 'two' : 2}
# print(a['two'])
#
# b = dict([(2 , 3), (5, 6)])
# print(b)
#
# c = dict.fromkeys(['a', 'b'] , 1)
# print(c)
#
# d = {a : a ** 2 for a in range(10,20)}
# print(d)
#
# person = {'name' : {"first_name" : 'Shohruh', "last_name" : "Masharipov", "middle_name" : "Baxodirovich"},
#           'adress' : ["Tashkent", "Almazar", "Qora-qamish 1/2" ],
#           'phone' : {"mobile_phone" : "998909757651", "mobile_phone_2" : "998946160682"}
#           }
#
# print(person["name"]['middle_name'])
#
# x = person.get("phone")
# print(x)


                                        # Set and frozenset
#set bilan frozensetni farqi frozensetni o'zgartiirib bo'lmaydi

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# print(type(set1))
#
# set1.union(set2)
# print(set1)
#
# a = ['r','s','w','a','s','w']
# print(a)
# s = set (a)
# print(s)
#
# a = {32, 43, 56, 74,48}
# x = {43, 12, 90, 32}
# print(a.isdisjoint(x))      #isdisjoint metodi agar 2 ta setni ichidagi elementlar ichida bittaham bir xili bo'lmasa True qaytaradi
#
# a.update(x)            #update funksiyasi 2 ta setda bor yo'gini olib bir biriga qoshadi borini qaytarmaydi
# print(a)
#
# a.intersection_update(x)    # updateni teskarisi faqat 2 tasida ham borini chiqaradi ekvivalent
# print(a)



                                        # Functions (def,lambda, return)
#
# def Myfunctions(*a):
#     if a[0].__len__()>a[1].__len__():
#         print(a + "Salom")
#     elif a[0].__len__()>a[1].__len__():
#         print(a + "sizga ga salom yo'q")
#     elif a[1].__len__()==a[0].__len__():
#         print(a[2] + " qizlarga alohida salom!!!")
# #
#
# Myfunctions("Shohruh","Baxodir","Malohat")
#
# def func (*fruits):
#     print("Judayam shirin " + fruits[2])
# func('Banan', 'peach', 'strawberry')
#
#
# def function(x):
#     def add(a):
#         return x + a
#     return add
#
# test = function(100)
# print(test(200))
#
# def func(r, w, y=2):
#     res = r + w
#     res *= y
#     return res
# print(func(2,4,5))
#
def func(*args):      # parametrda * bilan kelsa nechta argument olishini farqi yoq, hohlaganicha oladi
    return args
print(func(1,3,4))
                                # Archa yulduzcha
# N = int(input("Nechta qator: "))
# for i in range(1, N + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

                                #Heart Yulduzchalari
# for row in range(6):
#     for column in range(7):
#         if (row == 0 and column % 3 != 0) or (row == 1 and column % 3 ==0 ) or (row - column == 2) or (row + column == 8):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()
