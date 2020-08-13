import os, sys, time
from time import sleep

logo = ("""
01.Perkalian
02.Pembagian
03.Pengurangan
04.Penambahan
00.Info Tools
#Nurchan
""")
logo2 = ("""
INI ADALAH KALKULATOR PERKALIAN
#Nurchan""")

logo3 = ("""
INI ADALAH KALKULATOR PEMBAGIAN
#Nurchan""")

logo4 = ("""
INI ADALAH KALKULATOR PENGURANGAN
#Nurchan""")

logo5 = ("""
INI ADALAH KALKULATOR PENAMBAHAN
#Nurchan""")

logo6 = ("""
AUTHOR = NurChan & Safar
Support = Cinta :v
Tools = Kalkulator
NB: Doakan kami langgeng :v""")
def menu():
	os.system('clear')
	print(r"##### Tools Kalkulator #####")
	print(logo)
	print('='*30)
	nurchtan = input("Pilih No : ")
	if nurchtan =="1" or nurchtan=="01":
		perkalian()
	elif nurchtan =="02" or nurchtan=="2":
		pembagian()
	elif nurchtan =="03" or nurchtan=="3":
		pengurangan()
	elif nurchtan =="04" or nurchtan=="4":
		penambahan()
	elif nurchtan =="0" or nurchtan=="00": 
		info()
	elif nurchtan =="":
		print("Masukan angkanya")
		sleep(2)
		menu()
	
def perkalian():
	try:
		os.system('clear')
		print(logo2)
		print('='*30)
		a = int(input("Masukan Nilai A : "))
		b = int(input("Masukan Nilai B : "))
		c = a * b
		print("Nilai A = " +str(a))
		print("Nilai B = " + str(b))
		print("Nilai A * B = " + str(c)) 
		print('='*30)
		pilih = input('Apakah Anda mau melakukan Lagi? Y/N : ')
		if pilih =="y" or pilih =="Y":
			menu()
		else:
			pass
	except ZeroDivisionError:
		print("Kelemahan system jni jumblah angka tidak dapat di bagi 0 ")
		sleep(2)
	except ValueError:
		print("Yang harus di masukan adalah angka")
		sleep(2)
		perkalian()


def pembagian():
	try:
		os.system('clear')
		print(logo3)
		print('='*30)
		a = int(input("Masukan Nilai A : "))
		b = int(input("Masukan Nilai B : "))
		c = a / b
		print("Nilai A = " +str(a))
		print("Nilai B = " + str(b))
		print("Nilai A / B = " + str(c)) 
		print('='*30)
		pilih = input('Apakah Anda mau melakukan Lagi? Y/N : ')
		if pilih =="y" or pilih =="Y":
			menu()
		else:
			pass
	except ZeroDivisionError:
		print("Kelemahan system jni jumblah angka tidak dapat di bagi 0 ")
		sleep(2)
		pembagian()
	except ValueError:
		print("Yang harus di masukan adalah angka")
		sleep(2)
		pembagian()

def pengurangan():
	try:
		os.system('clear')
		print(logo4)
		print('='*30)
		a = int(input("Masukan Nilai A : "))
		b = int(input("Masukan Nilai B : "))
		c = a - b
		print("Nilai A = " +str(a))
		print("Nilai B = " + str(b))
		print("Nilai A - B = " + str(c)) 
		print('='*30)
		pilih = input('Apakah Anda mau melakukan Lagi? Y/N : ')
		if pilih =="y" or pilih =="Y":
			menu()
		else:
			pass
	except ZeroDivisionError:
		print("Kelemahan system jni jumblah angka tidak dapat di bagi 0 ")
		pengurangan()
		sleep(2)
	except ValueError:
		print("Yang harus di masukan adalah angka")
		sleep(2)
		pengurangan()


def penambahan():
	try:
		os.system('clear')
		print(logo5)
		print('='*30)
		a = int(input("Masukan Nilai A : "))
		b = int(input("Masukan Nilai B : "))
		c = a + b
		print("Nilai A = " +str(a))
		print("Nilai B = " + str(b))
		print("Nilai A + B = " + str(c)) 
		print('='*30)
		pilih = input('Apakah Anda mau melakukan Lagi? Y/N : ')
		if pilih =="y" or pilih =="Y":
			menu()
		else:
			pass
	except ValueError:
		print("Yang harus di masukan adalah angka")
		sleep(2)
		penambahan()

def info():
	os.system('clear')
	print(logo6)
	print('='*30)
	pilih = input("Balik Kemenu?  Y/N : ")
	if pilih =="y" or pilih =="Y":
		menu()
	else:
		pass
menu()

