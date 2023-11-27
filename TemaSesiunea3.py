'''
#1. Declarati o lista cu elemente multitype
#2. Declarati o lista goala
#3. Accesati orice element din lista pe baza de index
#4. Accesati pozitia unui element din lista pe baza functiei index()
#5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
#6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
#7. Numarati elementele dintr-o lista folosind functia len()
#8. Numarati de cate ori apare un anumit element in lista folosind functia count()
#9. Uniti doua liste folosind functia extend()
#10. Sortati lista folosind functia sort()
#11. Inversati continutul listei folosind functia reverse()
#12. Stergeti toate elementele din lista folosind functia clear()
'''

#LISTE
#1. Declarati o lista cu elemente multitype
lista = [1, 2, 3, 4, 5]
print(lista)
#2. Declarati o lista goala
list_goala = []
#3. Accesati orice element din lista pe baza de index
list[2]
print(lista[2])
#4. Accesati pozitia unui element din lista pe baza functiei index()
lista.index(3)
print(lista.index(3))
#5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
lista.append(4)
lista.append(4)
print (lista)
lista.insert(1,10)
print(lista)
#6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
lista.pop()
print(lista)
lista.remove(1)
print(lista)
#7. Numarati elementele dintr-o lista folosind functia len()
len(lista)
print(len(lista))
#8. Numarati de cate ori apare un anumit element in lista folosind functia count()
print(lista.count(4))
#9. Uniti doua liste folosind functia extend()
lista2 = [10, 12, 13, 14, 15]
lista.extend(lista2)
print(lista)
#10. Sortati lista folosind functia sort()
lista.sort()
print(lista)
#11. Inversati continutul listei folosind functia reverse()
lista.reverse()
print(lista)
#12. Stergeti toate elementele din lista folosind functia clear()
lista.clear()
print(lista)

'''
#1. Declarati un tuplu 
#2. Declarati un tuplu gol
#3. Accesati orice element din tuplu pe baza de index
#4. Accesati pozitia unui element din lista pe baza functiei index()
#5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu
#6. Folositi functia index() pentru a verifica pozitia la care se afla un anumit element in tuplu
#7. Incercati sa modificati un element din tuplu si observati rezultatele

'''
#1
persoana=('gen','numar','caz')
print(type(persoana))
#2
tuplu_gol=()
print(type(tuplu_gol))
#3
print(persoana[0])
#4
print(persoana.index('numar'))
#5
print(persoana.count('caz'))
#6
element_cautat='numar'
pozitie=element_cautat.index(element_cautat)
print(f'elementul {element_cautat} se afla la pozitia {pozitie} in tuplu')
#7 Tuplurile sunt imutabile nu se pot modifica


'''
#1. Declarati un set 
#2. Declarati un set gol
#3. Adaugati un element nou in set folosind functia add()
#4. Stergeti un element din set folosind functia pop() si respectiv functia remove(). Observati rezultatele
#5. Verificati daca un set este o subdiviziune a unui alt set (subset)
#6. Verificati daca un set contine toate elementele dintr-un alt set + alte elemente (superset)
#7. Verificati care sunt elementele comune intre doua seturi (intersection)
#8. Verificati diferenta intre doua seturi cu functia difference()
#9. Stergeti toate elementele dintr-un set folosind functia clear()

'''
#1
set={1,2,3}
#2
set_gol={}
#3
set.add(4)
print(set)
#4
set.pop() #se sterge aleatoriu
print(set)
set.remove(2) #stergem elementul 2 din set
print(set)
#5


#6


#7


#8
#Diferenta va contine toate elementele din set1_diferenta care nu sunt prezente in set2
set1_diferenta={1,2,3,4}
set2_diferenta={3,4,5,6}

diferenta=set1_diferenta.difference(set2_diferenta)
print(f'diferenta dintre set1 si set2 este {diferenta}')
#9
set.clear()
print(set)

'''
#1. Declarati un dictionar
#2. Declarati un dictionar gol
#3. Adaugati un element nou in dictionar folosind functia update() si respectiv pe baza de cheie
#4. Extrageti un element din dictionar folosind metoda get() si respectiv pe baza de cheie
#5. Stergeti un element din dictionar folosind functia pop() si respectiv functia popitem(). Observati rezultatele
#6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile din dictionar
#7. Stergeti toate valorile din dictionar folosind metoda clear()
'''
#1
Masini={
      "Scaune":"Piele",
      "Parbriz Incalzit":True,
       "Set Anvelope":True,
       "An Fabricatie":2014,
        "Marca":"BMW",
         "Pret":23000.00
}
#2
dictionar_gol={}
#3
Masini.update({"Model":"F30"})
Masini["Motorizare"]="Diesel"
print(Masini)
#4
print(Masini.get('Model'))
print(Masini['Motorizare'])
#5
Masini.pop('Motorizare') # am sterg cu ajutorul functiei pop pe baza de key
print(Masini)
Masini.popitem() #Mi-a sters ultimul key din dicitonar
print(Masini)
#6


#7
Masini.clear()
print(Masini)