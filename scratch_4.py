# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=a+b
# print((c))
# except EOFError as e:
#     print(e)
#     print("EOF when reading input")
dict={"name":"meerab"}
print(dict)




# try:
#        l=[]
#        l1=[5,7,6,8,7]
#        l2=[20,0,5]
#        for i in l1:
#            for j in l2:
#                l.append(i/j)
#            print(l)
# except (IndexError,ArithmeticError) as e:
#        print(e)








# a=("counterrevolution")
# b=("counter")
# c=("resolution")
# if len(a)==len(b)+len(c):
#     print("The number of characters in the word counterrevolution is equal to the sum of the number of characters"
#           "in words counter and resolution.""")
# else:
#     print("The number of characters in the word counterrevolution is not equal to the sum of the number of characters"
#           "in words counter and resolution.""")












# if "misinterpretation"<"misrepresentation":
#     print("It appear earlier in dictionary")
# else:
#     print("It appear later in dictionary")
#
#


# print()
# try:
#     def (test):
#         print("Test function")
# except IndentationError as e:
#     print(e)
# finally:
#     print("End of the day")










# try:
#     file=open("D:/ab.txt")
#     text=file.read()
#     file.close()
# except IOError as e:
#     print(e)
# finally:
#     print("End of the day")














# import math
# for i in range(4):
#    r=10
#    x=int(input("enter x_coordinate: "))
#    y=int(input("enter y_coordinate: "))
#    print((x,y))
#    r=math.sqrt(x**2+y**2)
#    if r < 10:
#      print(True)
#    else:
#       print(False)




# try:
#     file=int(input("enter a:"))
#     text=int(input("enter b:"))
# except IOError as e:
#     print(e)
# finally:
#     print("End of the day")










# t=tuple()
# x=list(t)
# num=int(input("Enter the no of provinces pakistan have: "))
# for i in range(num):
#     a=input("Enter the provinces of pakistan: ")
#     x.append(a)
# z=tuple(x)
# print(z)















# a=("counterrevolution")
# b=("counter")
# c=("resolution")
# if len(a)==len(b)+len(c):
#     print("The number of characters in the word counterrevolution is equal to the sum of the number of characters"
#           "in words counter and resolution.""")
# else:
#     print("The number of characters in the word counterrevolution is not equal to the sum of the number of characters"
#           "in words counter and resolution.""")








# a= ("ﬂoccinaucinihilipiliﬁcation")
# x=(tuple(list(a)))
# if "o" in x:
#     print("The letter e appear in the word ﬂoccinaucinihilipiliﬁcation")
# else:
#     print("The letter e does not appear in the word ﬂoccinaucinihilipiliﬁcation")

print()





# a=("anachronistically")
# b=("counterintuitive")
# x=len(a)
# y=len(b)
# print("The no of characters in",a,"has",x-y,"more characters than in",b,".")
#
#
#
#
# print()
# print()




# radius=10
# t=(5,4)
# a=[]
# no=int(input("Enter value:"))
# for i in range(no):
#     x=input("enter x")
#     y = input("enter y")
#     a.append(x)
#     a.append(y)
#     print(a)
#     d=tuple(a)
#     print(d)











# Sample = [(2, 3), (4, 7), (8, 11), (3, 6)]
# x=max(Sample)
#
# y=min(Sample)
# print("The maximum value is: ",x)
# print("The maximum value is: ",y)
#







# def abc(file):
#     file=open(text)
#     content=file.read()
#     words=content.split()
#     for i in words:
#         if i==4:
#             x=i.replace(i,"xxxx")
# text=input("Enter file name: ")
# (abc(text))



print()

# def make_list(no_of_families):
#     l={}
#     lst=[]
#     for i in range(no_of_families):
#         print(" ")
#         a=input(str("Enter Family name: "))
#         n=int(input("Enter no of family members: "))
#         for j in range(n):
#             lst.append(input("Enter family members: "))
#         l[a]=lst
#     return (l)
# def common_guest(a,b):
#     number=0
#     lst=[]
#     for x,y in a.items():
#         for i,j in b.items():
#             if x==i:
#                 for k in y:
#                     for l in j:
#                         if k==l:
#                             if k not in lst:
#                                 lst.append(k)
#                                 number += 1
#                             else:
#                                 continue
#     print("Members: ",lst,"\n","Number of common members:",number)

# print("PARENT'S LIST: ")
# parents_list= make_list(3)
# print()
# print("MY GUEST ARE: ")
# my_list=make_list(2)
# print("PARENT'S LIST",parents_list,"\n","MY GUEST LIST",my_list)
# print("\n","COMMON GUESTS: ")
# common_guest(parents_list,my_list)







































# def hexASCII(l):
#     l=list(l)
#     d={}
#     print("\n","Correspondance between the lowercase characters in the alphabet and the hexadecimal representation: ",)
#     for i in l:
#         d[i]=(hex(ord(i)))
#     for x,y in d.items():
#         print(x," : ",y)
# hexASCII(input(str("Enter the alphabets to get the hexadecimal representation of their ASCII code: ")))




































# def make_list(no_of_families):
#     l={}
#     lst=[]
#     for i in range(no_of_families):
#         print(" ")
#         a=input(str("Enter Family name: "))
#         n=int(input("Enter no of family members: "))
#         for j in range(n):
#             lst.append(input("Enter family members: "))
#         l[a]=lst
#     return (l)
# def common_guest(a,b):
#     number=0
#     lst=[]
#     for x,y in a.items():
#         for i,j in b.items():
#             if x==i:
#                 for k in y:
#                     for l in j:
#                         if k==l:
#                             if k not in lst:
#                                 lst.append(k)
#                                 number += 1
#                             else:
#                                 continue
#     print("Members: ",lst,"\n","Number of common members:",number)
#
# print("PARENT'S LIST: ")
# parents_list= make_list(3)
# print()
# print("MY GUEST ARE: ")
# my_list=make_list(2)
# print("PARENT'S LIST",parents_list,"\n","MY GUEST LIST",my_list)
# print("\n","COMMON GUESTS: ")
# common_guest(parents_list,my_list)













# a = {"Monday": "burger", "Tuesday": "biryani", "Wednesday": "pizza", "Thursday": "aloo", "Friday": "keema"}
# b = {"dish":"keema", "dish1": "aloo" ,"dish2": "korma", "dish3": "pasta" ,"dish4": "burger"}
# for a, b in zip(a.values(), b.values()):
#      if a == b:
#         print("The dishes cook this week that i like are: ",b)
# l=[]
# l.append(b)
# for i in l:
#   print(l,end="")













# def duplicate(file):
#     content=file.read()
#     words=content.split()
#     for i in words:
#         if words.count(i)>1:
#             return("TRUE")
#         else:
#             return("FALSE")
#
# file1=open("D:\duplicate.txt")
# file2=open("D:\duplicate1.txt")
# print("For duplicate.txt: ",duplicate(file1))
# print("For duplicate1.txt: ",duplicate(file2))
#












# def distribution(grades):
#     file=open(a)
#     data=file.read()
#     words =[data.count("A1"), data.count("A2"), data.count("A3"), data.count("B1"), data.count("B2"), data.count("B3")]
#     return (words)
# a=input("Enter the file name: ")
# print("The student who got A1 grades are",distribution(a)[0])
# print("The student who got A2 grades are",distribution(a)[1])
# print("The student who got A3 grades are",distribution(a)[2])
# print("The student who got B1 grades are",distribution(a)[3])
# print("The student who got B2 grades are",distribution(a)[4])
# print("The student who got B3 grades are",distribution(a)[5])














# hockey=set()
# for j in range(1,22):
#     hockey.add(j)
# both_set=set()
# for k in range(1,22):
#     both_set.add(k)
# hockeyonly=hockey-both_set
# cricket=u-hockeyonly
# cricketonly=cricket-both_set
# print("NO of students playing cricket only is",len(cricketonly))

















# U = {"ali", "malaika", "meerab", "khurram", "ayesha", "laiba", "bisma", "sarah", "maya", "nabia", "zohan",
#      "aliza", "arham", "shazain", "mehwish", "hamna", "areeba", "aqib", "aqsa", "alishba", "zain", "maha", "wajeeha",
#      "zoha", "almirah",
#      "fatima", "urooj", "dania", "sania", "yussra", "ahmed", "azam", "maryum", "faraz", "farah", "sana", "tania",
#      "moiz", "naveed", "asad"}
# A = {"laiba", "bisma", "sarah", "maya", "nabia", "zohan", "mehwish", "hamna", "areeba", "aqib", "aqsa", "alishba",
#      "urooj", "dania", "sania", "yussra", "wajeeha", "faraz", "moiz", "naveed", "asad"}
# B = {"malaika", "shazain", "ali", "tania", "meerab", "khurram", "ayesha", "aliza", "farah", "maha"}
# C = U.difference(A)
# print(C)
# D = B.union(C)
# print(D)





















# french=set(range(11))
# spanish=set(range(10))
# english=set(range(25))
# english_french=set(range(17))
# spanish_french=set(range(9))
# english_spanish=set(range(20))
# total=set(range(120))
# neither=set(range(20))
# print("Student speaking English and Spanish but not French",len(english_spanish))
# print("Student speaking neither English,Spanish nor French",len(neither))
# print("Student speaking French but neither English nor Spanish ",len(french))
# print("Student speaking only one of the three",len(english)+len(spanish)+len(french))
# print("Student speaking English and Spanish but not French",len(english_spanish)+len(english_french)+len(spanish_french))


















# dog=set(range(1,3))|set(range(7,13))|set(range(24,49))|set(range(49,99))
# cat=set(range(3,7))|set(range(7,13))|set(range(24,49))|set(range(99,165))
# fish=set(range(1,3))|set(range(7,13))|set(range(3,7))|set(range(13,23))
# other=set(range(145,199))
# onlydog=dog-(cat|fish)
# onlycat=cat-(dog|fish)
# onlyfish=fish-(dog|cat)
# total=(((dog|cat)|fish)|other)
# print("The purchase for a dog product are:",len(onlydog))
# print("The purchase for a cat product are:",len(onlycat))
# print("The purchase for a dog or fish product are:",len(onlydog|onlyfish))
# print("The total purchases are:",len(total))
#
















# def distribution(grades):
#     file=open(a)
#     data=file.read()
#     words =[data.count("A1"), data.count("A2"), data.count("A3"), data.count("B1"), data.count("B2"), data.count("B3")]
#     # words = data.count("A3")
#     return (words)
#
# a=input("Enter the file name: ")
# print("The student who got A1 grades are",distribution(a)[0])
# print("The student who got A2 grades are",distribution(a)[1])
# print("The student who got A3 grades are",distribution(a)[2])
# print("The student who got B1 grades are",distribution(a)[3])
# print("The student who got B2 grades are",distribution(a)[4])
# print("The student who got B3 grades are",distribution(a)[5])


















# def stat(a):
#    file=open(text)
#    content=file.read()
#    words=content.split()
#    lines=content.split("\n")
#    # return  (words,lines)
#    print("Number of character are:", len(content))
#    print("Number of character are:", len(words))
#    print("Number of character are:", len(lines))
# text=input("Enter file name: ")
# stat(text)
#
# print()
# def distribution(grades):
#     file=open(a)
#     data=file.read()
#     words =[data.count("A1"), data.count("A2"), data.count("A3"), data.count("B1"), data.count("B2"), data.count("B3")]
#     # words = data.count("A3")
#     return (words)
# a=input("Enter the file name: ")
# print("The student who got A1 grades are",distribution(a)[0])
# print("The student who got A2 grades are",distribution(a)[1])
# print("The student who got A3 grades are",distribution(a)[2])
# print("The student who got B1 grades are",distribution(a)[3])
# print("The student who got B2 grades are",distribution(a)[4])
# print("The student who got B3 grades are",distribution(a)[5])






# from random import*
# Students=["Meerab","Ayesha","Malaika","Khurram","Maya"]
# l=[]
# for i in range (5):
#     a=Students.pop()
#     l.append(a)
# print("The students applying for scholarship are:",l)
# x=sample(l,2)
# print("The two student who got scholarship are:",x)
# #




print("\n")




# def phone_directory(no):
#     phone_book = {}
#     for i in range(no):
#         name = str(input("Enter name:")).title()
#         phone_num = int(input("Enter number:"))
#         print()
#         phone_book[name] = phone_num
#     return phone_book
#
#
# num = int(input("Enter how many numbers you want to enter:"))
# phone_book = phone_directory(num)
# print(phone_book)
#
#
# def delete(book, no_1):
#     for i in range(no_1):
#         name_1 = str(input("Enter name you want to delete:")).title()
#         if name_1 in book.keys():
#             book.pop(name_1)
#         else:
#             print("Number not in the phonebook")
#     return book
#
#
# num_1 = int(input("How many num you want to delete:"))
# del_num = delete(phone_book, num_1)
# print("Member in phone directory after deleting are:")
# print(del_num)
# print("Total number of members in phonebook are:",end="")
# total=len(del_num)
# print(total)
























# family = {1: {"name": "meerab", "f_name": "tahir", "m_name": "fozia", "s_name": "malaika", "s_name": "ayesha",
#               "b_name": "khurram"}}
# print(family)
# print()
# maternal = {2: {"grand mother": "yasmin", "grand father": "mehrkhan", "uncle": ("usama", "imran"), "aunt": ("fiza", "tayyaba")}}
# paternal = {3: {"grand mother": "ameer", "grand father": "maqbool hussain", "uncle": ("zubair", "shoaib"),
#                 "aunt": ("nadia", "aasia")}}
# family.update(maternal)
# family.update(paternal)
# print("The family after updating is:")
# print(family)
#
# print("\n")
















def phone_directory(no):
    phone_book = {}
    for i in range(no):
        name = str(input("Enter name:")).title()
        phone_num = int(input("Enter number:"))
        print()
        phone_book[name] = phone_num
    return phone_book


num = int(input("Enter how many numbers you want to enter:"))
phone_book = phone_directory(num)
print(phone_book)


def delete(book, no_1):
    for i in range(no_1):
        name_1 = str(input("Enter name you want to delete:")).title()
        if name_1 in book.keys():
            book.pop(name_1)
        else:
            print("Number not in the phonebook")
    return book


num_1 = int(input("How many num you want to delete:"))
del_num = delete(phone_book, num_1)
print("Member in phone directory after deleting are:")
print(del_num)
print("Total number of members in phonebook are:",end="")
total=len(del_num)
print(total)








import random

player1 = []
player2 = []
for i in range(2):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    player1.append(dice1)
    player2.append(dice2)
print("player1 turns are:", player1)
print("player2 turns are:", player2)

print()

file = open("C:\lab1.txt", "r")
data = file.read()
words = data.split()
x = len(data)
y = len(words)
print("Total characters are:", x)
print("Total words are:", y)

# import pygame
#
# pygame.init()
#
# screen=pygame.display.set_mode((800,600))
#
# pygame.display.set_caption("Space Hub")
# icon = pygame.image.load('space alien.png')
# pygame.display.set_icon(icon)
#
# running=True
# while running:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
#
#         pygame.display.update()


import random

# def rolldice(dice1,dice2):
# dice1=["1","2","3","4","5","6"]
# dice2=["1","2","3","4","5","6"]
# print(random.sample(dice1,2))
# print(random.sample(dice2,2))


# Students=["Meerab","Ayesha","Malaika","Khurram","Maya"]
# l=[]
# for i in range (5):
# a=Students.pop()
# l.append(a)
# print("The students applying for scholarship are:",l)
# x=sample(l,2)
# print("The two student who got scholarship are:",x)

print("\n")
# Cities=["Karachi","Lahore","Peshawar","Quetta","Islamabad","Hyderabad"]
# shuffle(Cities)
# print(Cities)


print("\n")

# import pyodbc
# from tkinter import*
# from tkinter import messagebox


# label1=Label(text="NAME",width=15,bg='pink',pady=10,padx=10).grid(row=1,column=0)
# label2=Label(text="ADDRESS",width=15,bg='pink',pady=10,padx=10).grid(row=2,column=0)
# entry1=Entry(bg='pink').grid(row=1,column=2)
# entry2=Entry(bg='pink').grid(row=2,column=2)
# button=Button(text="Display",bg='pink',command=display).grid(row=5,column=2)

# m.mainloop()


a = {"dish": "keema", "dish1": "biryani", "dish2": "pizza", "dish3": "aloo", "dish4": "burger"}
b = {"dish": "keema", "dish1": "aloo", "dish2": "korma", "dish3": "pasta", "dish4": "burger"}
for a, b in zip(a.items(), b.items()):
    if a == b:
        print("ok")
        print("The dishes cook this week that i like are: ")
        print(b)
else:
    print("not")

family = {1: {"name": "meerab", "f_name": "tahir", "m_name": "fozia", "s_name": "malaika", "s_name": "ayesha",
              "b_name": "khurram"}}
print(family)
print()
maternal = {2: {"grand mother": "yasmin", "grand father": "mehrkhan", "uncle": ("usama", "imran"), "aunt": ("fiza", "tayyaba")}}
paternal = {3: {"grand mother": "ameer", "grand father": "maqbool hussain", "uncle": ("zubair", "shoaib"),
                "aunt": ("nadia", "aasia")}}
family.update(maternal)
family.update(paternal)
print("The family after updating is:")
print(family, sep="\n")
for k, v in family.items():
    print(k, ":", v)

pets = {"dogs", "cats", "fish"}
num = int(input("The no of product sell in 4 hours: "))
a = input("Enter the pet name: ")
l = []
for i in range(num):
    a = int(input("Enter the no of purchases: "))
    l.append(a)
print(l)
print(sum(l))

U = {"ali", "malaika", "meerab", "khurram", "ayesha", "laiba", "bisma", "sarah", "maya", "nabia", "zohan",
     "aliza", "arham", "shazain", "mehwish", "hamna", "areeba", "aqib", "aqsa", "alishba", "zain", "maha", "wajeeha",
     "zoha", "almirah",
     "fatima", "urooj", "dania", "sania", "yussra", "ahmed", "azam", "maryum", "faraz", "farah", "sana", "tania",
     "moiz", "naveed", "asad"}
A = {"laiba", "bisma", "sarah", "maya", "nabia", "zohan", "mehwish", "hamna", "areeba", "aqib", "aqsa", "alishba",
     "urooj", "dania", "sania", "yussra", "wajeeha", "faraz", "moiz", "naveed", "asad"}
B = {"malaika", "shazain", "ali", "tania", "meerab", "khurram", "ayesha", "aliza", "farah", "maha"}
C = U.difference(A)
print(C)
D = B.union(C)
print(D)

print("\n")

s = {"burger", "pizza", "pasta", "biryani", "korma", "colddrink"}
print("The avalible items are:", s)
l = []
l1 = []
no = int(input("Enter the no of item :"))
print()
for i in range(no):
    item = str(input("Enter the items you want to purchase: ")).lower()
    s.remove(item)
    print("Enter the number of", item, "you purchased:", end="")
    num = int(input())
    l1.append(num)

    global price
    if item == 'burger':
        price = 150
    elif item == 'pizza':
        price = 300
    elif item == 'pasta':
        price = 200
    elif item == 'biryani':
        price = 100
    elif item == 'korma':
        price = 100
    elif item == 'colddrink':
        price = 120

    p = price * num
    l.append(p)
    print('item:', item, " ", 'price', price, " ", 'total price:', p, " ", "no of", item, "bought:", num)

print("The total amount is:", sum(l))
print("The remaining items are: ", s)
print("Maximum amount of items sold are:", max(l1))
print("Mininmum amount of items sold are:", min(l1))
print("Total amoumt of items sold are:", sum(l1))

print("\n")

U = {"ali", "malaika", "meerab", "khurram", "ayesha", "laiba", "bisma", "sarah", "maya", "nabia", "zohan",
     "aliza", "arham", "shazain", "mehwish", "hamna", "areeba", "aqib", "aqsa", "alishba", "zain", "maha", "wajeeha",
     "zoha", "almirah",
     "fatima", "urooj", "dania", "sania", "yussra", "ahmed", "azam", "maryum", "faraz", "farah", "sana", "tania",
     "moiz", "naveed", "asad"}
A = {"laiba", "bisma", "sarah", "maya", "nabia", "zohan", "mehwish", "hamna", "areeba", "aqib", "aqsa", "alishba",
     "urooj", "dania", "sania", "yussra", "wajeeha", "faraz", "moiz", "naveed", "asad"}
B = {"laiba", "zohan", "aqib", "faraz", "hamna", "ali", "malaika", "meerab", "khurram", "ayesha"}
C = U.difference(A)
print(C, sep='\n')

s1 = set()
num = int(input("How many dishes do you like? "))
for i in range(num):
    dishes = input("Enter the dishes: ")
    s1.add(dishes)
print("The favourite dishes are:", s1)
for i in range(num):
    s2 = s1.pop()
    print(s1)

print("\n")

s1 = {'malaika', 'meerab', 'ayesha', 'khurram', 'abiha'}
s2 = set()
for i in range(2):
    a = input("enter the student: ")
    s2.add(a)
    s1.remove(a)
print("the student who left NED are:", s2)
print("The remaining students are: ", s1)

print("\n")


def month(m):
    months = ("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec").split(" ")
    return (months[m - 1])


n = int(input("enter num from 1-12:"))
print("The month is:", month(n))

print("\n")


def team(a):
    print("How do you spell winner?\nI know,I know!")
    print(" ".join(a.upper()))
    print("And that's how you spell winner!")
    print(f'Go', a.title(), '!')


a = input("enter team name: ")
team(a)

print("\n")

a = 6
b = 7
c = (a + b) / 2
print(c)
inventory = ['papers', 'staples', 'pencils']
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
full_name = (first + ' ' + middle + ' ' + last)
print(full_name)

print("\n")

l1 = [2, 1, 3, 5, 4, 3, 8]
print(l1.pop(0))
(l1.remove(4))
print(l1)
(l1.insert(1, 9))
print(l1)
(l1.extend([10, 11]))
print(l1)
(l1.sort())
print(l1)

print("\n")
import time

print(time.strftime('%A,%b/%d/%y', time.localtime()))
print(time.strftime('%I:%M %p Central Daylight Time %b/%d/%y', time.localtime()))
print(time.strftime('I will meet you on, %A,%b/%d at %I:%M %p', time.localtime()))

print("\n")


def even(a):
    for i in range(1, a + 1):
        if (i % 2 == 0 or i % 3 == 0):
            print(i, end=" ")


a = int(input("enter the integer:"))
even(a)

print("\n")


def cheer(a):
    print("How do you spell winner?\nI know, I know!")
    print(a.upper(), "!")
    print("And that's how you spell winner!")
    print(f'Go', a.title(), '!')


a = input("enter team name: ")
cheer(a)

print("\n")


def team(a):
    a = input("enter team name: ")
    print("cheer", a,
          "How do you spell winner? ,\n, I know, I know!",
          a.upper(), sep=' ')
    print("and that's how you spell winner")
    print(f'Go', a, '!')


print("\n")


def even(n):
    print('i%2==0 i%3==0')
    formatstr = '{0:2d}'
    for i in range(1, 17):
        print(i % 2 == 0, i % 3 == 0)


message = 'The secret of message is that it is secret'
length = len(message)
count = message.count('secret')
censored = message.replace('secret', 'xxxxxx')
print("The length of message is: ", length)
print("The occurence of count is: ", count)
print("After changing secret with xxxxxx: ", censored)

print("\n")
print("\n")

first = 'John'
last = 'Doe'
street = 'Main Street'
number = '123'
city = 'Anycity'
state = 'AS'
zipcode = '09876'
print(first, last)
print(street, number)
print(city, ",", state, zipcode, )

print("\n")
print("\n")
print("\n")
forecast = "It will be a sunny day today"
count = forecast.count('day')
weather = forecast.find('sunny')
change = forecast.replace('sunny', 'cloudy')
print("The occurance of day is: ", count)
print("The index where substring sunny start: ", weather)
print("After changing sunny with cloudy: ", change)

print("\n")

lst = []
num = int(input("enter the no of element: "))
for i in range(num):
    lst.append(int(input("Enter the element: ")))
print(lst)
if len(lst) % 2 == 0:
    import math

    a = int(math.ceil(num) / 2)
    print(lst[a], 'find at index', lst.index(lst[a]))
else:
    a = int((num) / 2)
    print(lst[a], 'find at index', lst.index(lst[a]))

print("\n")

lst = []
num = int(input("enter the no of element: "))
for i in range(num):
    lst.append(int(input("Enter the element: ")))
    print(lst)
lst.sort(reverse=True)
print(lst)

print("\n")

lst = []
num = int(input("enter the no of element: "))
for i in range(num):
    lst.append(int(input("Enter the element: ")))
print(lst)
for i in range(0, len(lst)):
    if len(lst) % 2 == 0:
        import math

        a = (math.ceil(num) / 2)
        print(lst[a], 'find at index', lst.index[a])
    else:
        a = (math.ceil(num) / 3)
        print(lst[a], 'find at index', lst.index(lst[a]))

lst = []
num = int(input("enter the no of element: "))
for i in range(num):
    lst.append(int(input("Enter the element: ")))
    print(lst)
m = (int(len(lst) / 2))
print(lst[m])

print("\n")
lst = []
num = int(input("enter the no of element: "))
for i in range(num):
    lst.append(int(input("Enter the element: ")))
for i in range(len(lst) - 1):
    for j in range(len(lst) - 1):
        if lst[j] < lst[j + 1]:
            temp = lst[j + 1]
            lst[j + 1] = lst[j]
            lst[j] = temp
    print(lst)

print("\n")
lst = []
num = int(input("enter the no of element: "))
for i in range(num):
    lst.append(int(input("Enter the element: ")))
print(lst)
for i in range(0, len(lst)):
    if len(lst) % 2 == 0:
        print(lst.pop(int(num / 2)))

print("\n")

for i in range(2):
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))
    x1 = (B + (B ** 2 - 4 * A * C) ** 0.5) / 2 * A
    x2 = (B - (B ** 2 - 4 * A * C) ** 0.5) / 2 * A
    if A == 0:
        print("The equation cannot be solved as there is zero in division")
    else:
        print(x1, x2)

print("\n")

i = 0
while i <= 5:
    j = 0
    while j <= 14:
        print('*', end=" ")
        j = j + 1
    print()
    i = i + 1

i = 0
while i <= 5:
    j = 0
    while j <= 14:
        print(" ", end=" ")
        j = j + 1
    i = i + 1
    j = 0
    while j <= 14:
        j = j + 1
        print("*", end=" ")
    print()


def mataddition(a, b):
    z = [[0, 0],
         [0, 0]]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                z[i][j] += a[i][k] * b[k][j]
    print()
    for i in z:
        print(i)


x = [[2, 3],
     [4, 6]]
y = [[4, 5],
     [9, 8]]
z = [[0, 0],
     [0, 0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j] += x[i][k] * y[k][j]
print()
for i in z:
    print(i)

print("\n")

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=' ')
    print()

print("\n")
months_L = ['Jan', 'Feb', 'Mar', 'May']
months_T = ('Jan', 'Feb', 'Mar', 'May')
months_L.insert(3, 'Apr')
print(months_L)
months_L.append('Jun')
print(months_L)
months_L.pop()
print(months_L)
months_L.remove('Feb')
print(months_L)

print("\n")

a = 6
b = 7
c = (a + b) / 2
inventory = ['paper', 'staples', 'pencils']
first = 'John'
middle = 'Firtzgerald'
last = 'Kennedy'
name = first + ' ' + middle + ' ' + last
print(c)
print(name)

print("\n")

i = 0
while i <= 5:
    j = 0
    while j <= 14:
        print('*', end=" ")
        j = j + 1
    print()
    i = i + 1
k = 0
while k <= 5:
    m = 0
    while m <= 14:
        print("    \t", '*', end=" ")
        m = m + 1
    print()
    k = k + 1
i = 0
while i <= 5:
    j = 0
    while j <= 14:
        print('*', end=" ")
        j = j + 1
    print()
    i = i + 1

print("\n")

for i in range(11, 42, 5):
    print(i, end=" ")
print("\n")
for i in range(3, 34, 5):
    print(i, end=" ")
print("\n")
for i in range(20, 10, -3):
    if i > 11:
        print(i, end=" ")
        print(i, end=" ")
    else:
        print(i)

print("\n")

import math

for i in range(2):
    r = float(input("Enter radius of the circle in (centimeter):"))
    w = float(input("Enter angular speed of the circle in (rev\min):"))
    r1 = r / 100
    w1 = w / 60
    w2 = w1 * 6.28
    linearvelocity = r1 * w2
    print("the linearvelocity of a circle in meter/sec,is", linearvelocity)

print("\n")

# Nested loop
for i in range(4):
    for j in range(14):
        print('*', end=' ')
    print()
for i in range(4):
    for j in range(4, i):
        print('*', end=' ')
    for j in range(28):
        print('', end=' ')
    for j in range(14):
        print('*', end=' ')
    print()

import math

A = int(input("Enter a : "))
B = int(input("Enter b : "))
C = int(input("Enter c : "))
x1 = (B + (B ** 2 - 4 * A * C) ** 0.5) / 2 * A
x2 = (B - (B ** 2 - 4 * A * C) ** 0.5) / 2 * A
print(x1, x2, sep=',')

print("\n")

std = ["MEERAB", "TAHIR", 19, "PL", "FIT", "FE", "CALCULUS", "DS", 90, 89, 85, 92, 87, 500, 443, 88.6, "Aone"]
print("Printing student data.......")
print(
    "Name : %s,Father name : %s,Roll no : %d,Subject1 :%s,Subject2 :%s,Subject3 :%s,Subject4 :%s,Subject5 :%s,Marks1 :%d,Marks2 :%d,Marks3 :%d"
    "\n Marks4 :%d,Marks5 :%d,Totalmarks :%d,Obtainedmarks :%d,Percantage :%f,Grade :%s" % (
        std[0], std[1], std[2], std[3], std[4], std[5], std[6], std[7],
        std[8], std[9], std[10], std[11], std[12], std[13], std[14], std[15], std[16]))

print("\n")
print("\n")

s = input("Enter string : ")
s = s.casefold()
srever = reversed(s)
if list(s) == list(srever):
    print("Its  palindrome")
else:
    ("Its not palindrome")

print("\n")

i = -1
while i <= 97:
    i = i + 2
    print(i, end=' ')

print("\n")
print("\n")
print("\n")

months_L = ['Jan', 'Feb', 'Mar', 'May']
months_T = ('Jan', 'Feb', 'Mar', 'May')
months_L.insert(3, 'Apr')
print(months_L)
months_L.append('Jun')
print(months_L)
months_L.pop()
print(months_L)
months_L.remove('Feb')
print(months_L)

print("\n")
print("\n")
text = input("enter the names: ")
for word in text:
    if word[0] in 'abcdefghijklm':
        print(word)

print("\n")

import math

for i in range(4):
    l = float(input("Enter length in feets: "))
    a = float(input("Enter angle in degree: "))
    radian = math.pi * a / 180
    height = l * math.sin(radian)
    print("the height of ladder is", height)

print("\n")

l1 = [2, 4, 56, 7, 22, 6]
for i in range(len(l1) - 1):
    for j in range(len(l1) - 1):
        if l1[j] > l1[j + 1]:
            temp = l1[j + 1]
            l1[j + 1] = l1[j]
            l1[j] = temp
print(l1)

print("\n")

for i in range(11, 42, 5):
    print(i, end=' ')
print("\n")
for i in range(3, 34, 5):
    print(i, end=' ')
print("\n")
for i in range(20, 10, -3):
    print(i, end=' ')
    print(i, end=' ')

print("\n")
print("\n")
print("\n")

n = int(input("Enter 4 no integer: "))
a = int(n / 1000)
b = int((n % 1000) / 100)
c = int((n % 100) / 10)
d = int((n % 10) / 1)
print(a)
print(b)
print(c)
print(d)


def xmult(p, q):
    l = []
    for i in l1:
        for j in l2:
            l.append(i * j)
    return l


l1 = []
s = int(input("enter no of integers: "))
print("The integers are 'l1' ")
for i in range(s):
    a = int(input())
    l1.append(a)

l2 = []
s = int(input("enter no of integers: "))
print("The integers are 'l1' ")
for i in range(s):
    a = int(input())
    l2.append(a)

print("the product of integer:", xmult(l1, l2))

print('\n')

i = 0
while i <= 10:
    def factorial(x):
        a = 1
        for i in range(x, 1, -1):
            a = a * i
        return a


    i = i + 1
    print(i, "!=", factorial(i))

print("\n")
print("\n")

# nested loop
for i in range(10):
    for j in range(i, 9):
        print('*', end='')
    print()

print("\n")

l1 = [11, 23, 38, 49, 56, 69]
print(l1[::-3])

for i in range(5):
    for j in range(i + 1):
        print(' ', end=' ')
    for j in range(i, 4):
        print('*', end=' ')
    for j in range(i, 5):
        print('*', end=' ')
    print()

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
print(l1 is l2)

x = input("enter string")
for i in x:
    if i in 'aeiouAEIOU':
        print(i, "\t", x.index(i))

a = [1, 2, 3, 4]
b = [5]

a.pop(3)
a.append(b)
print(a)
a.extend(b)
print(a)

a = 9
b = 8
a, b = b, a
print(a)
print(b)

a = [1, 2, 3, 4]
a[2] = 6
print(a)

for i in range(20, 1, -2):
    print(i)

print("\n")

l1 = ['apple', 'mango', 'grapes', 'apple']
l2 = 'banana'
l1.append(l2)
l1.insert(0, 'guava')
print(l1.index('apple'))
print(l1)
print(l1.count('apple'))
print(l1.pop())
x = 34
y = 'meerab'
z = 3.5675
print(int(z))
print(complex(z))
print(type(x))
print(type(y))
print(type(z))


def update(l2):
    l1[0] = 5
    l1[1] = 4
    return (l2)


l1 = [1, 2, 3]
update(l1)
print('l1 is now', (l1))

l1 = [1, 2, 3]
l2 = 'a'
if l2 in l1:
    print('true')
print(l1 * 2)
print(l1[2])
print(sum(l1))
print(len(l1))

s1 = 'bat'
s2 = 'rat'
s3 = 'kat'
print((s1, s2, s3))
print(s1 * 10, sep='  ')
print(s1, s2 * 2, s3 * 3, sep='  ')

a = 3
b = 4
c = a * a + b * b
print(c)

print(7 // 3 == 1 + 1)
print(7 // 8)

g = 'hello world'
h = 'hello' * 2
print(h[0])
print(len(g))
if h not in g:
    print('true')
else:
    print('false')

print(3 * 'A')

import math

x = 2
x = 3
print(x == 3)
print(x)
print(3 + 5 == 6 + 7)
print(2 < 3)
print(math.fabs(-2))
s = 'use'
t = 'oil'
print(s < t)
print(s + '   ' + t)

print((1 + 2) * 3)
print(math.ceil(5.9))
print(5.09876543211234565667)

a = str(input("enter name"))
l1 = ['musial', 'aaraon', 'william', 'gehrig']
if a in l1:
    print("one of top 5 baseball players,ever!")

hit = int(input("enter hit"))
shield = int(input("enter shield"))
if hit >= 10 and shield == 0:
    print("you can escape")
else:
    pass

last = 'Smith'
first = 'John'
middle = 'Paul'
print(last, "\t", first, "\t", middle)

l2 = ['It ', 'will', 'be', ' a', 'sunny', 'day', 'today']
l3 = [(l2.count('day'))]
print(l3)
print(l2[4])
l2.insert(4, 'cloudy')
print(l2)


def swapPosition(list1):
    list[0], list[3] = list[3], list[0]
    return list


list = ['Ava', 'Eleanor', 'Clare', 'Sarah']
list0, list3 = 0, 3
print(swapPosition(list))

for i in range(6):
    for j in range(i, 5):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for i in range(i + 1):
        print("*", end=" ")
    print()

print("\n")

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l1.pop(1)
print(l1)
l1.remove(3)
print(l1)
l1.pop()
print(l1)
l1.clear()
print(l1)

l1 = [23, 87, 90, 65, 74, 80, 69, 43, 56]
a = [32]
l1.append(a)
l1.extend(a)
l1.insert(1, a)
l1.remove(90)
l1.pop(1)
print(l1)

print(l1[::])
print(l1[::-1])
print(l1[:2])
print(l1[0:5:2])
print(l1[:5:])
print(l1[3:])
print(l1[:3])
print(l1[-4:-2])
print(l1[4:-2])
print(l1[3:-2])

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()
