'''
- ako zelim testirati svoj kod, moram pokrenuti ovaj modul: from bla import *
- i onda probati nekoliko primjera tj. pozvati par funkcija
- u ovom slucaju je sve trivijalno, ali moze biti slucajeva kada ce cak i jedna funkcija biti kompleksna i tricky
- tada bi trebali proci svaki moguci slucaj na nacin da se svaki put poziva funkcija
- zato se koristi unittest
'''

def isInList(elem, list):
	return elem in list

def isEven(x):
	return x % 2 == 0

def plusOne(n):
	return n + 1