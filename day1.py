# -*- coding: utf-8 -*-

a = 1
print (type(a))

a = "sample text"
print (type(a))

a = 1.0
print (type(a))

pi = 3.14
print (type(a))

myChar = 'a'
print (type(myChar))

#p0
imie= "Anna"
adres_zamieszkania = "Nieznana 20"
#adres-zamieszkania = „Nieznana 20”;
drugie_imię = "Beata"
#3ulubionePotrawy = „x, y, z”
#and = 51
and_Dana = 1023
And = "hello"
#twoje zainteresowania = „nurkowanie”
twoje2samochody = "v, m"
śćółżęąćł = ":-)"
twojaSzczesliwaLiczbaKtoraWylosowanoSpecjalnieDlaCiebie= 5


"""
    doakdaw
    dadafwad
"""

#p0a

a = 45
print (type(a))

a = "Szkolenia"
print (type(a))

a = 23.5
print (type(a))

a = "Test"
print (type(a))

a = '?'
print (type(a))


#######################
#Syntax
#######################

a = 1
b = '1'
c = 1.0

a = 20
print(a)


#######################
#Tuple
#######################

a = (1,2,3)
print(type(a))

print (a[0])
print (a[1])
print (a[2])

a = (1,2,3,'s','a','m','p','l','e')
print (type(a))

print (a[4])

#one element tuple
a = (1,)
print(type(a))

#TUPLE IS IMMUTABLE!
#a[0] = 4

a = 1,2,3,4,'s','a','m','p','l','e'
print(type(a))

#a = tuple (1,2,3)
#print(type(a))

#######################
#List
#######################

a = [1,2,3,4,5,'s','a','m','p','l','e']
print (type(a))

print
var = a[6]
#podmiana wartosci pod indeksem drugim
a[2] = 'nowa'
print (a)
#dodanie nowej wartosci na koncu listy
a.append('nowa2')
print (a)
#dodanie wartosci na wybranej pozycji
a.insert (2,'nowa3')
print(a)

del a[0]
print (a)
#sprawdzanie długości listy
print (len(a))

a_tuple = tuple(a)
print (type(a_tuple))

#####################
a = 1
b = 2

a,b = b,a


print(a) #2
print(b) #1


a = [1,2,3,4,5,'s','a','m','p','l','e']

#for each
for elem in a:
    print (elem)

a = list(range(1,10,1)) ;    #< )
print (a)



for elem in a:
    print(elem)

my_list = [1,2,'log',4,5,'s','a','m','p','l','e']
counter = 0
for elem in a:
    print(my_list[counter])
    counter +=1

my_tuple = ('a','b','c')

for elem in my_tuple:
    print(elem)

a = list(range(1,3)) #<)
print(a)
counter = 0
for elem in a:
    print(my_tuple[counter])
    counter +=1

a =['a','b','c','d','e']

for elem in a:
    print(elem)


my_lst = list(range(7,10,1))
print(my_lst) #[7,8,9]
counter = 0
for elem in my_lst:
    print(a[counter])
    counter = counter +1

a = [1,2,3,4,5]
for elem in a:
    print(elem * 2)

a = ['a','b','c']
for elem in a:
    print(elem * 2)

a = [1,2,3,4,5,6,7,8,9,10]
a = list(range(1,11,1))

new_list = []
new_list2 = []
for elem in a:
    if elem > 3:
        new_list.append(elem)
    else:
        new_list2.append(elem)
print(new_list)
print(new_list2)

a = [1,2,3,4,5,6,7,8,9,10]

new_lst = []
for elem in a:
    if elem %2 == 0:
        new_lst.append(elem)
print(new_lst)

a = "sample text"
for letter in a:
    print(letter)

counter = 0
while counter<5:
    print(counter)
    counter +=1 # counter = counter +1

counter = 0
while counter < 4:
    print(counter)
    counter +=1

#while 1==1: #pętla w nieskończoność, #break - kończy pętlę, można dodać warunek
    print("...")
    counter = 4
    if counter >0:
        break
    counter =-1

if 1<2:
    pass

#######################
#set
#######################

a = [1,1,1,2,3,4,5]
b = 'sample text'
c = (1,2,1,2,3)

a_set = set(a)
print(type(a_set))
b_set = set(b)
print(type(b_set))
c_set = set(c)
print(type(c_set))

print(a_set)
print(b_set)
print(c_set)

for elem in a_set:
    if elem ==1:
        print("ok istnieje")

print(1 in a)

a = {1,1,2,3}
print(a)

a.add(4)    #dodawanie elementów do zbioru
print(a)

a.remove(1)     #usuwanie elementów ze zbioru
print(a)

#animal list
animal = ['cat', 'dog', 'rabbit', 'rabbit', 'guinea pig']

animal.remove('rabbit')

a = [1,1,1,2,3,4]
for elem in a:
    print(a), elem
    if elem == 1:
        a.remove(1)
print(a)

a = [1,2,3,4,5]
for elem in a:
    a.pop()
print(a)


a = [1,2,3]
#frozenset is immutable
a_set = frozenset(a)

#######################
#Dictionary
#######################

numbers = {
    'a': 2,
    "b": 3,
    'c': 4
}
print(numbers)
print(type(numbers))
print(numbers['b'])

print(numbers.keys())
print(numbers.values())
print(numbers.items())

items = numbers.items()
for item in items:
    print(item[0])
    print(item[1])

#slices
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0:3:1])
print(a[0:7:2])  #ostatnia wartość to krok - tutaj co drugą liczbę wybieramy

print(a[len(a) -1])
print(a[-1])
print(a[-1:-4:-1])
print(a[::])
print(a[::-1])

text = "sample text"
textList = text.split(" ")
print(textList)

print("|".join(textList))

a = "sample text"
print(a[::-1])

#p0c

zmienna_1 = 'ciekawe'
zmienna_2 = 'programowanie'
zmienna_3 = 'jest'
zmienna_4 = 'wciagające'
zmienna_5 = 'I'

a = [zmienna_2 + " " + zmienna_3 + " " + zmienna_1 + " " + zmienna_5 + " " + zmienna_4]
print(a)

#p7d
czas = 45

#kolorowa
print((2*45)/5)

#czarno-biała
print((45*8)/2)

a = 1
print(str(a))

print(str (1) + 'a')

#p10
brutto = 1000
VAT1 = 0.03
VAT2 = 0.07
VAT3 = 0.23

print(round(brutto * (VAT1+1),2))
print(round(brutto * (VAT2+1),2))
print(round(brutto * (VAT3+1),2))


#p11
Chleb = 1.99
Mleko = 2.5
Cukierki = 12.99

print(2 * Chleb + 0.5 * Mleko + 0.3 * Cukierki)


a = 0o11
print(a)

a = 0o27
print(a)

bool(7)
#p22
a = 'Adam'
b = 'Kowalski'
c = str('35')
d = 'Młodszy inżynier procesu'
e = str('6000')

print (10 * ("Pan " + a + " " + b + "(" +"wiek: " + c + ")" + "pracuje na stanowisku: " + d + "(pensja: " + e + " " +"brutto)"))


#a = input("enter number 1")
#b = input("enter number 2")
#print(a + b)

a = 257
b = 257

print(a is b)
print(id(a))
print(id(b))

#p22a
a = 500
b = 200

c = 500 + b + (0.5 * (a + b))
print(c)
b1 = b + (0.5 * c)
b2 = b1 + (0.5 * b1)
b3 = b2 + (0.5 * b2)
b4 = b3 + (0.5 * b3)
b5 = b4 + (0.5 * b4)

d = a + b2
print(d)
e = a + b3
print(e)
f = a + b4
print(f)
g = a + b5
print(g)


#p25
WynNetto = 5500
Godziny = 168
print(round(5500/168,2))
wynBrutto = 1.23 * WynNetto
print((round (wynBrutto/Godziny, 2)))


#p27
a = bool(0)
b = bool(0)
c = bool(1)

W1 = (not a) and (not b) and (not c)
W2 = (not a) and (not b) and (c)
W3 = (not a) and (b) and (not c)
W4 = (a) and (not b) and (not c)
F = (W1) or (W2) or (W3) or (W4)

print(F)

#p36
#imie = input("wczyta napis")
#print(30 * (imie + "\n"))

#p37
#a = input("długość podstawy")
#h = input("wysokość")

#pole = (0.5 * int(a) * int(h))

#print(pole)

a = "sample"
print(a[2])

print(a.capitalize())

a = "aaaaabbbbbcccc"
dictionary = dict()
for letter in a:
    if letter in dictionary:
        dictionary[letter] +=1
    else:
        dictionary[letter] =1
print(dictionary)

a = dict()
print(type(a))
a['a'] = 2
print(a)
print(a['a'])






