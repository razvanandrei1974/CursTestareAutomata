# Varianta 2

# 4.Salvati fiecare cuvant din propozitia: “Ana s-a nascut in anul 1990 si acum are 33 de ani” in cate o adresa de memorie.
# 5.Printati propozitia de mai sus folosind trei tipuri diferite de printuri.

# nume="Ana"
# anul_nasterii= 1990
# varsta= 33
#
# print(f'{nume} s-a nascut in anul  {anul_nasterii} si acum are {varsta} de ani' )
# print(nume + " s-a nascut in anul " + str(anul_nasterii) + " si acum are " + str(varsta) + " de ani")
# print(nume,'s-a nascut in anul',anul_nasterii,'si acum are ',varsta, 'de ani')

#print("Info functia input()")
#input() =>> functia care ne ajuta sa preluam date de la tastura/de la utilizator
#datele preluate default sunt date de tip string
vanzator = input("Cum te numesti? ")
tip_imobil = input("Ce tip de imobil vrei sa vinzi? ")  # in variabila tip_imobil salvam datele preluate de la tastatura cu ajutorul functiei input(), aceste date vor fi de tip string
pret_vanzare = int(input("Care este pretul de vanzare? \n"))  # in variabila pret_vanzare salvam datele preluate de la tastatura cu ajutorul functiei input(), iar cu ajutorul functiei int() facem un type casting - modificam datele de tip string in date de tip int

print(f'{vanzator} are de vanzare un imobil de tip: {tip_imobil} si are pretul de vanzare {pret_vanzare} euro negociabil')