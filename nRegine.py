import copy
from datetime import datetime
from dataclasses import dataclass


@dataclass
class nQueens():



   def __init__(self):
       self.nSoluzioni= 0
       self.nChiamare = 0
       self.soluzioni=[]
#==============================APPROCCIO 2==================================================================================
# Rappresentiamo soluzione come vettore di N regine
# ognuno rappresentante una regina come riga e colonna
   def solve2(self,N):
       self.nSoluzioni = 0
       self.nChiamare = 0
       self.soluzioni=[]

       self._ricorsione2([],N)

   #parziale è un vettore di coppie riga-colonna

   def _ricorsione2(self,parziale,N):
       self.nChiamare+=1
       #caso terminale, ho messo N regine
       if len(parziale)==N:
           if self.is_nuova_soluzione(parziale):
               self.nSoluzioni+=1
               self.soluzioni.append(copy.deepcopy(parziale))
          # print(parziale)
        #caso ricorsivo: ho messo meno di N regine
       else:
           for i in range(N):
               for j in range(N):
                   nuovaQ=(i,j)
                   #verifico se la nuova regina sia ammissibile
                   if self.stepIsValid(nuovaQ,parziale):
                   # aggiungere alla soluzione parziale
                       parziale.append(nuovaQ)
                       #andare avanti con nuova ricorsione
                       self._ricorsione2(parziale,N)
                       #backtracking
                       parziale.pop()

    #confrontiamo la potenziale soluzione con tutte quelle gia trovate,
    # se è diversa restituiamo True altrimenti False
   def is_nuova_soluzione(self,parziale)->bool:
       N = len(parziale)
       for soluzione in self.soluzioni:
           counter=0
           for regina in parziale:
               if regina in soluzione:
                   counter += 1
           if counter==N:
               return False
       return True




   def is_soluzione(self,possible_soluzione:list):
       for i in range(len(possible_soluzione)-1):
           for j in range(i+1,len(possible_soluzione)):
               if not self.is_ammissibile(possible_soluzione[i],possible_soluzione[j]):
                   return False
       return True

    #funzione che verifica se la nuova regina sia ammissibile
       # rispetto la attuale soluzione parziale
   def stepIsValid(self,nuova_regina,parziale:list):
       for regina in parziale:
           if not self.is_ammissibile(nuova_regina,regina):
               return False
       return True




   def is_ammissibile(self, reg1, reg2)->bool:
      # 1) Verifico riga, se non va bene ritorno False
      # 2) Verifico colonna, se non va bene ritorno False
      # 3) Verificp diagolane 1, se non va bene ritorno False
      # per fare questa verifica devo controllare che
      # colonna di reg1 - riga  di reg1==
      # colonna di reg2 - riga  di reg2
      # 4) Verifico digonale 2, se non va bene ritorno False
      # 5) Se jop passato tutti i controlli ritorno True
        if reg1[0]==reg2[0]:
            return False
        elif reg1[1]==reg2[1]:
            return False
        elif reg1[1]==reg2[1] and reg1[0]==reg2[0]:
            return False
        elif (reg1[1]-reg1[0]) == (reg2[1]-reg2[0]):
            return False
        elif (reg1[0] + reg1[1]) == (reg2[1]+reg2[0]):
            return False
        else:
            return True



if __name__ == "__main__":
    nreg=nQueens()
    timeStart = datetime.now()
    nreg.solve2(5)
    timeEnd = datetime.now()

    print(f"Ho impiegato: {timeEnd-timeStart}")
    print(f"Ho trovato {nreg.nSoluzioni} soluzioni possibili")
    print(f"Ho effettuato {nreg.nChiamare} chiamate")
    print(nreg.soluzioni)