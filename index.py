
# name = input("Как вас зовут? ")
# print("Привет " + name)
# num_1 = int(input("Enter first number: "))
# num_2 = input("Enter first number: ")
# res = num_1 + int(num_2)
# print(res)
# Res = 'Shohruh '
# Res *= 5
# print(Res)



                        # Shartli operator
# num = input("What is your name?: ")
# if num == "Shohruh":
#     print("Salom ho'jayin\n")
# elif num == "Baxodir":
#     print("Salom Shohruhning adasi ")
# else: print("You are not Shohruh!!!")


# number = int(input("Enter number: "))
#
# if number > 0:
#     print("Siz 0 dan katta son kiritdingiz!!!")
#     if number > 10:
#         print("SIz 10 dan ham katta son kiritdingiz")
#     else: print("Siz 10 dan kichik lekin 0 dan katta son kirtdingiz")
# else:
#     print("Siz 0 dan kichik son kiritdingiz")


# number = int(input("Son kiriting: "))
# little = str(number - 20)
# big = str(20 - number)
# if number > 20:
#     print("Siz 20 dan " + little + " ta katta son kiritdingiz")
# else:
#     print("Siz 20 dan " + big + " ta kichkina son kiritdingiz" )


# car = input("Say me you car name: ")
# A = "True" if car == "Nexia" else "False"
# print(A)


                            #Random
# import random
# print(random.randrange(5,10))


                            #LOOPS
# i = 0
# while i < 10:
#     i += 2
#     print(i)

# i = 2000
# while i > 100:
#     i /= 2
#     print(i)
#
# for x in range(6):
#     print(x)

# for j in "hello world":
#     print(j * 2, end='')

# for i in "hello world":
#     if i == 'w':
#         break
#     print(i*3, end='')

                                #List tipa massiv
# # a = [a + b for a in "list" if a != "s" for b in "soup" if b!= "u"]
# # print(a)
#
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
# print(l.pop(2))        # listdagi elementning indexi bo'yicha o'chiradi , agar parametr ko'rsatilmasa oxirgi elementini o'chiradi
# print(l.index(56))   #ko'rsatilgan element nechinchi indexdaligini chiqaradi
# print(l.count(47))      # ko'rsatilgan elementning listdagi soni nechtaligini chiqaradi
# l.sort()        # sortirovka bo'yicha chiqaradi
# print(l)
# l.reverse()     # sortning teskarisiga chiqaradi
# print(l)
# l.clear()       # listning ichini polnisti tozalab tashlaydi
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
# print(l)
# print(l[:])
#


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
# a = ('hello world', 'dwd', 34)
# print(a)
#
# x = ("apple", "banana", "cherry")
# y = list(x)
# print(y)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)
#
# tuple = (32, 45, 'ls')
# print(tuple.__len__())


                                # dict -- slovar yoki obyekt
#
# a = {'one' : 1, 'two' : 2}
# print(a['two'])
#
# b = dict([(2 , 3), (5, 6)])
# print(b)
#
# c = dict.fromkeys(['a', 'b'], 2)
# print(c)
#
# d = {a: a ** 2 for a in range(10, 20)}
# print(d)
#
# person = {'name' : {"first_name" : 'Shohruh', "last_name" : "Masharipov", "middle_name" : "Baxodirovich"},
#           'adress' : ["Tashkent", "Almazar", "Qora-qamish 1/2" ],
#           'phone' : {"mobile_phone" : "998909757651", "mobile_phone_2" : "998946160682"}
#           }
#
# print(person["name"]['middle_name'])
#
# z = person['adress']
# print(z)
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
# a = ['r', 's', 'w', 'a', 's', 'w']
# print(a)
# s = set(a)
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

# def Myfunctions(*a):
#     if a[0].__len__() > a[1].__len__():
#         print(a + "Salom")
#     elif a[0].__len__() > a[1].__len__():
#         print(a + "sizga salom yo'q")
#     elif a[1].__len__() == a[0].__len__():
#         print(a[2] + ", qizlarga alohida salom!!!")
# #

# Myfunctions("Shohruh","Baxodir","Malohat")

# def func (*fruits):
#     print("Judayam shirin " + fruits[2])
# func('Banan', 'peach', 'strawberry')


# def function(x):
#     def add(a):
#         return x + a
#     return add

# test = function(100)
# print(test(200))

# def func(r, w, y=7):
#     res = r + w
#     res *= y
#     return res
# print(func(2,4,5))

# def func(*args):      # parametrda * bilan kelsa nechta argument olishini farqi yoq, hohlaganicha oladi
#     return args
# print(func(1,3,4))


# def myfunc(**args):    # если будет 2 звездочки это возврашает обьекть
#     return args
# print(myfunc(a=5, b=3, c="dw"))


# add = lambda x, y: x * y      # lambda  bitta qatorga yoziladigan funksiyaning bir turi
# print(add(3, 4))
# print(add('q', 4))

# print((lambda x, y: x + y)(4, 7))

# fun = lambda *args: args
# print(fun(2, 56 , 76.45))


                            # try - except 

# x = int(input("Son kiriting: "))
# y = int(input("Son kiriting: "))

# try:
#    res =  x / y                         # qlishga harakat qiladi
# except ZeroDivisionError:                       # Xatolarni kutib oladi ya'ni xato nomi yoziladi 
#     print("Siz 0 ga bo'ldingiz bu mumkin emas")
#     res = 0
# else:
#     print("Siz to'gri kiritidingiz")       # Xato bo'lmasa ishlaydi
# finally:
#     print("Hammasi ishlayabdi 100%")           # Xato bo'lsin bo'lmasin har qanday vaziyatda ishlaydi
# print(res)



                                # Files
# f = open('text.txt', 'r+',)   # agar r+ bo'lsa o'qish ham yozish ham mumkin

# print(f.read( ))         # to'liq fileni ichidagi yozuvni ekranga chiqaradi

# print(f.read(5))     # ichidagi parametr nechta harf chiqarishi yoki o'qishini bildiradi

# print(f.readline())    # qatorri to'liq chiqaradi

# for i in f:
#     print(i)       # for qlib o'qib olish ujun rejim faqat 'r' ya'ni read bo'lishi kerak

# f.write('Bu yana man\nikkinchi qator')
# f.close()               # har doim fileni ochgandan so'ng uni yopish kerak


                                    
                                    
                                    
                                    # Menedjer content with....as

# with open('test2.txt', 'wt', encoding='utf-8') as inFile:
#     num = int(input())
#     line = str('1/ ' + str(num) + ' = ' + str(1/ num))
#     print(line)
#     inFile.write(line)

                                    # import module from....

# import time
# import sys
# import random as r           #randomni r sifatida ishlatssa bo'ladi
# from m import module as m           #papkani ichida bo'lsa from bilan topib olinadi
# from module2 import plus as p, kopaytirish as k        # agar moduleni ichidagi bitta yoki bir nechta funkiyalarni ishlatmoqchi bo'lsak fromdan foydalaniladi
# try:
#     import nomodule
# except ImportError:
#     print("bunday module mavjud emas")

# print(m.minus(5,3))
# print(p(6,8))
# print(r.randrange(0,10))
# print(sys.platform)




                                # OOP python

# class Person:
#     name = "Shohruh"
#     age = 22
    
#     def set(self, name, age):
#         self.name = name
#         self.age = age

# David = Person()
# David.set("David", 42)
# print(David.name + " " + str(David.age)) 

                                

                                
                                    # Nasl olish, inkapsulyatsiya, polimorfizm

# class Person:
#     name = "Shohruh"
#     age = 22
#     pol = 'male'
    
#     def set(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol

# class Student (Person):
#     course = 1

# igor = Student()
# igor.set("Igor", 19, 'male')
# igor.course = 2
# print(igor.age)

# David = Person()
# David.set("David", 42, 'female')
# print(David.name + " " + str(David.age)) 


# __set yoki _set bu inkapsulyatsiya



                                    # Konstruktor

# class Person():
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol

#     def set(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol

# class Student (Person):
#     course = 1

# igor = Student("Igor", 19, 'male')
# # igor.set("Igor", 19, 'male')
# igor.course = 2
# print(igor.age)

# David = Person("David", 42, 'female')
# # David.set("David", 42, 'female')
# print(David.name + " " + str(David.age))