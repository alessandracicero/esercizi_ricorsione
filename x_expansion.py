import copy
import self


class Xexpansion:
    def __init__(self):
        self.soluzioni = []
        self.soluzioniList = []



    def calcolaList(self,input):
        self.soluzioni = []

        self._ricorsioneList([],input)



    def calcola(self,input) :
        self.soluzioni.clear()
        self._ricorsione("",input)

    def _ricorsioneList(self,parziale:str,rimanenti:str):
       #caso terminale
       if  len(rimanenti)==0:
           print(parziale)
           self.soluzioniList.append(copy.deepcopy(parziale))
       else:#caso ricorsivo
           if rimanenti[0]=="X":
               #ciclare sui step possibili
               for c in ["0","1"]:
                   parziale.append(c)
                   self._ricorsioneList(parziale,rimanenti[1:])
                   parziale.pop()

           else:
               parziale.append(rimanenti[0])
               self._ricorsioneList(parziale,rimanenti[1:])

    def _ricorsione(self,parziale:str,rimanenti:str):
       #caso terminale
       if  len(rimanenti)==0:
           #print(parziale)
           self.soluzioni.append(parziale)
       else:#caso ricorsivo
           if rimanenti[0]=="X":
               self._ricorsione(parziale+'0',rimanenti[1:])
               self._ricorsione(parziale+'1',rimanenti[1:])
           else:self._ricorsione(parziale+rimanenti[0],rimanenti[1:])

    def x_explosion(self,input) :
        soluzioni2 = []

        def ricorsione(self,parziale:str,rimanenti:str):
       #caso terminale
            if  len(rimanenti)==0:
               print(parziale)
               self.soluzioni2.append(parziale)
            else:#caso ricorsivo
                if rimanenti[0]=="X":
                    self._ricorsione(parziale+'0',rimanenti[1:])
                    self._ricorsione(parziale+'1',rimanenti[1:])
                else:self._ricorsione(parziale+rimanenti[0],rimanenti[1:])
        ricorsione("",input)
        return soluzioni2

if __name__ == '__main__':
    sequence="01X0"
    xexp = Xexpansion()
    #metodo sol parzialicome string
    print(xexp.calcola(sequence))
    print(xexp.soluzioni)
    #medoto sol pariali in lista
