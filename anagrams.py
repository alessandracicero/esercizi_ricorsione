import copy


def anagrams(parola):
    soluzioni=[]
    ricorsione([],parola,soluzioni)

    return soluzioni
def ricorsione(parziale:list,rimanente:str,soluzioni:list):
    if len(rimanente)==0:
        soluzioni.append(copy.deepcopy(parziale))
        return
    else:
        for i in range(len(rimanente)):#prendo le varie lettere
            # e faccio il giochetto con tutte
            parziale.append(rimanente[i])#quando faccio liste, creare deep copy e emettere il pop
            nuovi_rimanenti= rimanente[:i]+rimanente[i+1:]
            ricorsione(parziale,nuovi_rimanenti,soluzioni)
            parziale.pop()

def anagrams_set(parola):
    soluzioni1=set()
    ricorsionestr("",parola,soluzioni1)

    return soluzioni1
def ricorsionestr(parziale1:str,rimanente:str,soluzioni1:list):
    if len(rimanente)==0:
        soluzioni1.add(copy.deepcopy(parziale1))
        return
    else:
        for i in range(len(rimanente)):#prendo le varie lettere
            nuovi_rimanenti= rimanente[:i]+rimanente[i+1:]
            ricorsionestr(parziale1+rimanente[i],nuovi_rimanenti,soluzioni1)
if __name__ == '__main__':
    print(anagrams_set('aaa'))