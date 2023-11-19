# print("Rezolvare exercitiu 1")
#
# latime = 10
# descriere = "cerc"
# pret = 10.5
# discount = 0.75
# initializat = True
#
# print(latime)
# print(descriere)
# print(pret)
# print(discount)
# print(initializat)
#
# # concatenarea stringurilor
#
# forma =" cerc"
# culoare =" roz"
# forma_geometrica = forma + culoare
# print(forma + culoare)
# print(forma_geometrica)
# print( "Detalii forma geometrica " + forma + culoare )
#
# #Concatenare f-string
#
# print(f"Detalii forma geometrica {forma} {culoare}")
# print(f"Detalii forma geometrica {forma, culoare}")
#
# diametru=16
# print(f"Diametrul cercului este de {diametru}")
# print(f"Avem un{forma} de culoare{culoare} cu diametru{diametru}")
#
# # casting
# print("Info functia type()")
# anotimp="vara"
# print(type(anotimp))
#
# # type casting
# print("Info type casting")
# lungime1=15
# lungime2="15"
# print(type(lungime1))
# print(type(lungime2))
# lungime2=int(lungime2)
# print(type(lungime2))
#
# # functia INPUT
#
# print("Info functia input()")
#
# vanzator = input("Cum te numesti? ")
# tip_imobil = input("Ce tip de imobil vrei sa vinzi? ")
# pret_vanzare = int(input("Care este pretul de vanzare? \n"))
#
# print(f'{vanzator} are de vanzare un imobil de tip{tip_imobil} la pretul de vanzare{pret_vanzare}')

# Activitati sesiune

ocupatie = "tester"
nume = input("Scrie numele tau")
Data_nasterii = input(" Scrie data nasterii" )
Data_inscrierii_la_Curs = input( "Scrie data la care te-ai inscis la curs")
procent_invatare = 90
sunt_pregatit_de_examen = True

#print("Ma numesc " + nume , + " sunt nascut in data " + Data_nasterii + " si m-am inscris la curs la data de " + str("Data_inscrierii_la_Curs") + " Dupa terminarea cursului de TM sunt pregatit in procent de " + str("procent_invatare") + "Sunt pregatit de examen" + str("sunt_pregatit_de_examen"))

print(f'Ma numesc :{nume}')
print(f'Sunt nascut in data :{Data_nasterii}')
print(f'M-am inscris la curs la data de :{Data_inscrierii_la_Curs}')
print(f'Dupa terminarea cursului de TM sunt pregatit in procent de :{procent_invatare}%')
print(f'Sunt pregatit de examen :{sunt_pregatit_de_examen}')

#
VALOARE_EXCURSIE = int(input("valoare excursie: "))
DISCOUNT = VALOARE_EXCURSIE * (int(input("discount: ")))/100
valoare_finala =int(input(VALOARE_EXCURSIE - DISCOUNT))
PRINT("valoare_finala")
