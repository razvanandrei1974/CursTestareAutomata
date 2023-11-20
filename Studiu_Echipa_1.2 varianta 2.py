# Tema 1.2
# 17 Noiembrie 2023

# 1.Definiti o adresa de memorie care sa salveze data curenta. Va fi o variabila sau o constanta?

data_curenta="19 Noiembrie 2023" #Am declarat si initializat variabila, deci este variabila
type(data_curenta) #Cu ajutorul Functiei type(variabila) putem afla tipul de data folosit.
print(data_curenta) # am printat

# 2.Identificati tipul de data pe care il are variabila pe care ati definit-o folosind una din functiile invatate la curs
data_curenta="19 Noiembrie 2023"
print(type(data_curenta)) #am printat variabila cu functia "type"

# 3.Definiti alte cateva variabile care sa stocheze cursul la care sunteti, ce zi este si la ce sesiune de curs sunteti.
curs="Testare Automata" #variabila tip curs
zi="vineri" #variabila zi
sesiune_curs=1 #variabila sesiune_curs1
data_curs="17 Noiembrie 2023" # variabila data cursului

# Am printat folosind metoda cu formatare
print(f'Particip la cursul de {curs} in ziua de {zi} la sesiunea {sesiune_curs}, in data de {data_curs}')

# 4.Salvati fiecare cuvant din propozitia: “Ana s-a nascut in anul 1990 si acum are 33 de ani” in cate o adresa de memorie.

cuvant2="s-a"  #am declarat si initializat variabila cuvant_2
cuvant1="Ana"  #am declarat si initializat variabila cuvant_1
cuvant3="nascut" #am declarat si initializat variabila cuvant_3
cuvant4="in" #am declarat si initializat variabila cuvant_4
cuvant5="anul" #am declarat si initializat variabila cuvant_5
cuvant6=1990 #am declarat si initializat variabila cuvant_6
cuvant7="si" #am declarat si initializat variabila cuvant_7
cuvant8="acum" # #am declarat si initializat variabila cuvant_8
cuvant9="are" #am declarat si initializat variabila cuvant_9
cuvant10=33 #am declarati s initializat variabila cuvant_10
cuvant11="de" #am declarat si initializat variabila cuvant_11
cuvant12="ani" #am declarat si initializat variabila cuvant_12
#
# #Am printat folosind concatenarea
print( cuvant1 + " " + cuvant2 + " " + cuvant3 + " " + cuvant4 + " " + cuvant5 + " " + str(cuvant6) + " " + cuvant7 + " " + cuvant8 + " " + cuvant9 + " " + str(cuvant10) + " " + cuvant11 + " " + cuvant12)

#Am printat folosind metoda printare cu formatare
print(f'{cuvant1} {cuvant2} {cuvant3} {cuvant4} {cuvant5} {cuvant6} {cuvant7} {cuvant8} {cuvant9} {cuvant10} {cuvant11} {cuvant12}')

#Am printat folosind metoda a-3-a
print(cuvant1,cuvant2,cuvant3,cuvant4,cuvant5,cuvant6,cuvant7,cuvant8,cuvant9,cuvant10,cuvant11,cuvant12)

# Varianta 2
nume="Ana"
anul_nasterii= 1990
varsta= 33

# 5.Printati propozitia de mai sus folosind trei tipuri diferite de printuri.

#Am printat folosind concatenarea

print(f'{nume} s-a nascut in anul {anul_nasterii} si acum are {varsta} de ani' )

#Am printat folosind metoda printare cu formatare
print(nume + " s-a nascut in anul " + str(anul_nasterii) + " si acum are " + str(varsta) + " de ani")

#Am printat folosind metoda a-3-a
print(nume,'s-a nascut in anul',anul_nasterii,'si acum are',varsta,'de ani')

# 6.Declarati cateva alte adrese de memorie la alegere si initializati-le folosind functia input.
nume_utilizator = input("Care este numele de utilizator ? \n") # Variabila "Nume Utilizator"
data_nasterii = input("Care este data nasterii ? \n") # Variabila "Data nasterii utilizatorului"
adresa = input("Care este adresa din actul de identitate ? \n") # Variabila "Adresa utilizatorului"
oras = input("Care este orasul din actul de identitate ? \n") # Variabila "Orasul utilizatorului"
judet = input("Care este judetul din actul de identitate ? \n") # Variabila "Judet utilizatorului"
pin = int(input("Care este pin-ul ? \n")) # Variabila "PIN-ul utilizatorului"
telefon_mobil= int(input("Care este numarul de telefon mobil ? \n")) # Variabila "Numarul de telefon mobil al utilizatorului"
email = input("Care este adresa de e-mail ? \n") # Variabila "Email-ul utilizatorului"
parola = input("Care este parola ? \n ") # Variabila "Parola utilizatorului"


nume_utilizator = "Razvan1974" # Variabila "Nume Utilizator"
data_nasterii = "27 August 1974 " # Variabila "Data nasterii utilizatorului"
adresa = "Strada Ciocarliei, nr.5 " # Variabila "Adresa utilizatorului"
oras = "Resita " # Variabila "Orasul utilizatorului"
judet = "Caras Severin " # Variabila "Judet utilizatorului"
pin = 123456 # Variabila "PIN-ul utilizatorului"
telefon_mobil= 774903493  # Variabila Numarul de telefon mobil al utilizatorului"
email = "razvan.ungar@gmail.com " # Variabila "Email-ul utilizatorului"
parola = "Bnc123654@" # Variabila "Parola utilizatorului"

# Am printat prin metoda printare cu formatare

print(f'Numele de utilizator este {nume_utilizator}, nascut in data {data_nasterii}, locuieste la adresa {adresa}, in orasul {oras}, judetul {judet}.PIN-ul utilizatorului este {pin}, telefonul mobil este {telefon_mobil}, adresa de email este {email},parola este {parola}')

# 7.Adaugati comentarii la fiecare linie de cod cu explicatii cu privire la ce ati facut la fiecare

