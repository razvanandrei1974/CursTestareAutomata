"""Rezolvari - Exercitii: Sesiune curs _1.1"""


'''
Activitati sesiune: 
Creati o variabila care sa stocheze cu ce va ocupati in momentul asta
Creati cateva constante care sa stocheze fiecare, pe rand, numele vostru, data nasterii, data la care v-ati inscris la curs. De ce le-am creat ca si constante in loc de variabile? Valorile se vor da de la tastatura prin intermediul functiei input. 
Definiti o noua variabila numita procent_invatare care va stoca un procent ce va descrie nivelul de informatii pe care credeti ca ati ajuns sa le stapaniti de la inceputul cursului de testare manuala si pana acum (ca un fel de auto-evaluare). 
Definiti o noua variabila care sa se numeasca sunt_pregatit_de_examen si care sa stocheze valoarea corespunzatoare. 
Ce tip de data are fiecare din cele create?
Printati pe ecran intr-o singura propozitie toate informatiile de mai sus folosind trei tipuri de printare. Ce observati in fiecare caz? Cum am putea sa rezolvam eventualele probleme?
Definiti o noua constanta care sa reprezinte valoarea unei excursii pe care ati achizitionat-o recent si respectiv una care sa stocheze un eventual discount pe care l-ati avut (daca nu a existat, acesta va fi 0). 
Valorile se for da de la tastatura. In final, veti calcula valoarea finala a calatoriei folosind pretul de baza al biletului si valoarea discountului. Ce trebuie sa ii faceti functiei input pentru ca acest exercitiu sa functioneze?
Adaugati comentarii inaintea fiecarei linii de cod si explicati ce face

'''
ocupatie = "programator"
NUME = input("Care este numele tau? ")  # date de tip string
DATA_NASTERII = input("Care data nasterii? ")  # date de tip string
DATA_INSCRIERE_CURS = input("La ce data te-ai inscris la curs? ")  # date de tip string
procent_invatare = 90  # date de tip int
sunt_pregatit_de_examen = True # date de tip bool

# afisam pe ecran info utilizand functia print() si folosind metoda f-string
print(f'Ma numesc {NUME} si sunt nascuta in {DATA_NASTERII}. M-am inscris la curs in {DATA_INSCRIERE_CURS}, sunt {ocupatie} si dupa finalizarea cursului de Testare Manuala ma simt pregatita in proportie de {str(procent_invatare)}%. Sunt pregatita pentru examen: {str(sunt_pregatit_de_examen)}  ')
# afisam pe ecran info utilizand functia print() si folosind concatenarea de stringuri
print('Ma numesc' + NUME +' si sunt nascuta in ' + DATA_NASTERII + '. M-am inscris la curs in ' + DATA_INSCRIERE_CURS + ', sunt ' + ocupatie + ' si dupa finalizarea cursului de Testare Manuala ma simt pregatita in proportie de ' + str(procent_invatare) + '%. Sunt pregatita pentru examen:  ' + str(sunt_pregatit_de_examen))
# afisam pe ecran info utilizand functia print() si insiruirea de carac.
print('Ma numesc', NUME, ' si sunt nascuta in ',  DATA_NASTERII,  '. M-am inscris la curs in ',  DATA_INSCRIERE_CURS,  ', sunt ',  ocupatie,  ' si dupa finalizarea cursului de Testare Manuala ma simt pregatita in proportie de ',  procent_invatare, '%. Sunt pregatita pentru examen:  ',  sunt_pregatit_de_examen)


VALOARE_EXCURSIE = int(input('Care este pretul pentru excursiei achizitionate? \n'))
DISCOUNT = VALOARE_EXCURSIE * (int(input('Care este discount-ul de care ati beneficiat? \n')))/100
valoare_finala = VALOARE_EXCURSIE - DISCOUNT

print(f"Valoarea initiala a excursiei este de {VALOARE_EXCURSIE} lei iar la momentul achizitiei am primit un discount de {DISCOUNT} lei asa ca in final am primit {valoare_finala}lei")
"""
EX1: 
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
"""
print("ex 1 - rezolvare")
latime = 10  # rezolvarea pentru a
descriere = "patrat" # rezolvarea pentru b
pret = 10.5 # rezolvarea pentru c
discount = 0.75 # rezolvarea pentru c
valoare = True # rezolvarea pentru d

print(latime) # rezolvarea pentru e
print(descriere) # rezolvarea pentru e
print(pret) # rezolvarea pentru e
print(discount) # rezolvarea pentru e
print(valoare) # rezolvarea pentru e

"""
EX2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10.
"""
print("ex 2 - rezolvare")
unghiul_a = unghiul_b = 45 # am declarat si initializat doua variabile unghiul_a si unghiul_b care au date de tip int si avem aceaasi valoare


"""
EX3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite.
"""

print("ex 3 - rezolvare")

oras, judet = "Cluj-Napoca", "Cluj"  # am declarat si initializat doua variabile oras si judet care au date de tip string diferite


"""
EX4: Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
"""
print("ex 4 - rezolvare")
nume, pret = "Maria", 13
print(nume, " si-a cumparat un meniu cu doar ",  pret,  "lei.")

"""
EX5:
a. Defineste doua variabile: nume (string) si varsta (int).
b. Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
"""
print("ex 5 - rezolvare")
nume, varsta = "Ioana", 23
print(f"{nume} are varsta de {varsta} ani.")


"""
EX6:
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
"""
print("ex 6 - rezolvare")
nr_strada = 10 # am declarat si initializat o variabila nr_strada in care avem date de tip int
print("a. variabila de tip int: ", nr_strada)
print(type(nr_strada))
suprafata = 125.45 # am declarat si initializat o variabila suprafata in care avem date de tip float
print("b. variabila de tip float: ", suprafata)
print(type(suprafata))
strada = "Mircea Eliade" # am declarat si initializat o variabila strada in care avem date de tip string
print("c. variabila de tip string: ", strada)
print(type(strada))
deschis = True  # am declarat si initializat o variabila deschis in care avem date de tip bool
print("d. variabila de tip bool: ", deschis)
print(type(deschis))


"""
EX7: 
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
"""
print("ex 7 - rezolvare")
aria1 = 20
print(type(aria1))
aria2 = float(aria1)
print(type(aria2))

"""
EX8:
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
"""
print("ex 8 - rezolvare")
luna1 = "11"
print(type(luna1))
luna2 = int(luna1)
print(type(luna2))
"""
EX9: Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
print("ex 9 - rezolvare")
produs = input("Nume produs: \n")
print(f"Duminica la pranz am iesit la restaurant si am mancat {produs}.")


"""
EX10: Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
"""
print("ex 10 - rezolvare")
pret = float(input(f"Care a fost pretul ce l-ai dat pentru {produs}: "))
print(f"Pretul a fost doar de {pret} lei.")








