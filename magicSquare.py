import copy
from time import time


class QuadratoMagico():

    def __init__(self,N):
        self.N=N


    # soluzione del quadrata magico rappresentato da un vettore di N^2 elementi,
    # ogni elemento rappresenta una cella del quadrato,
    # ed il suo valore è il numer all'interno della cella

    def risolvi_quadrato(self):
        self.n_chiamate=0
        self.n_soluzione=0
        self.soluzioni=[]
        self._ricorsione([], set(range(1, self.N*self.N+1)))


    def _ricorsione(self,parziale, rimanenti):
        self.n_chiamate+=1
        #caso terminale
        if len(parziale) == self.N*self.N:
             if self.is_valid(parziale):
                self.soluzioni.append(copy.deepcopy(parziale))
                self.n_soluzione += 1
        else:
             for numero in rimanenti:
                     #1)aggiungere numero parziale
                parziale.append(numero)
                     #1b) tolgo numero appena inserito dai rimanenti
                if self.is_parziale_valid(parziale):
                    nuovo = copy.deepcopy(rimanenti)
                    nuovo.remove(numero)
                         #2) amdare avanti nella ricorsione
                    self._ricorsione(parziale,nuovo)
                # 3) backtracking
                parziale.pop()

    def stampa_quadrato(self,soluzione):
        print("------------------------")
        for riga in range(self.N):
            print(soluzione[riga * self.N:(riga + 1) * self.N])
        print("------------------------")

    def is_valid(self,potenziale_soluzione):
        numero_magico =self.N*(self.N*self.N+1)/2
        # 1) controllare righe
        for id_riga in range(self.N):
            riga = potenziale_soluzione[id_riga*self.N:(id_riga+1) * self.N]
            if sum(riga)!=numero_magico:
                return False
        # 2) controllare colonne
        for id_col in range(self.N):
            col = potenziale_soluzione[id_col: (self.N-1)*self.N + id_col +1:self.N]
            if sum(col)!=numero_magico:
                return False
        # 3) cotrollare diagonale 1
        for id_diag1 in range(self.N):
            diag1 = potenziale_soluzione[0:self.N**2 +1 :self.N+1]
            if sum(diag1)!=numero_magico:
                return False
        # 4) controllare diagonale 2
        somma = 0
        for indice in range(self.N):
            somma += potenziale_soluzione[(indice*self.N) + ( self.N-1 - indice)]
        if somma!=numero_magico:
            return False
        # 5) passati tutti i controlli, possiamo tornare True
        return True

    def is_parziale_valid(self, potenziale_soluzione):
        numero_magico = self.N * (self.N * self.N + 1) / 2
        # 1) controllare righe
        n_righe= len(potenziale_soluzione)//self.N

        for id_riga in range(n_righe):
            riga = potenziale_soluzione[id_riga * self.N:(id_riga + 1) * self.N]
            if sum(riga) != numero_magico:
                return False
        # 2) controllare colonne
        n_col =max( len(potenziale_soluzione)-self.N*(self.N-1),0)
        for id_col in range(n_col):
            col = potenziale_soluzione[id_col: (self.N - 1) * self.N + id_col + 1:self.N]
            if sum(col) != numero_magico:
                return False
        # 3) cotrollare diagonale 1
       # for id_diag1 in range(self.N):
        #    diag1 = potenziale_soluzione[0:self.N ** 2 + 1:self.N + 1]
         #   if sum(diag1) != numero_magico:
         #       return False
        # 4) controllare diagonale 2
       # somma = 0
      #  for indice in range(self.N):
        #    somma += potenziale_soluzione[(indice * self.N) + (self.N - 1 - indice)]
       # if somma != numero_magico:
       #     return False
        # 5) passati tutti i controlli, possiamo tornare True
        return True

if __name__=="__main__":
    qM=QuadratoMagico(3)
    start_time= time()
    qM.risolvi_quadrato()
    end_time= time()
    print(f"Tempo impiegato:{end_time-start_time}")
    print(f"Ho effettuato {qM.n_chiamate} chiamate al metodo")
    print(f"Ho ottenuto {qM.n_soluzione} soluzioni")
    for sol in qM.soluzioni:
        qM.stampa_quadrato(sol)
