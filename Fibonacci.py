import time
from functools import lru_cache
from typing import Dict


class Fibonacci:
    def __init__(self):
        self.cache={0:0,1:1}
        self.ricorsione=0 # creo variabile per contare invocazioni
        self.ricorsioneCache=0


    def calcola_elemento_cache(self,n):
        #se ho gia la soluzione per questo n,
        # la prendo dalla cache
        if self.cache.get(n) is not None:
            return self.cache[n]
            #altrimento devo andare avanti
            # con la ricorsione
        else:
            self.ricorsioneCache+=1
            self.cache[n]=(self.calcola_elemento_cache(n-1)+
                           self.calcola_elemento_cache(n-2))
            return self.cache[n]



    def calcola_elemento(self,n):
        #caso terminale
        if n == 0:
            return 0
        #non terminale
        elif n == 1:
            return 1
        #caso ricorsivo
        else:
            self.ricorsione+=1
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

        pass
    @lru_cache#Memoization
    def calcola_elemento_lru(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)


if __name__ == '__main__':
    fib = Fibonacci()
    N = 10

    start = time.time()
    print(fib.calcola_elemento(N))
    print(fib.ricorsione)
    end = time.time()
    print(f"Elapsed time: {end - start}")#MOLTO LENTO
#calcolca ogni volta le stesse ose, vedi grafo sulle slide
#devoi memorizzare le somme di fibonacci precedentementre calcolate
#risparmio tempo e costo ma occupo memoria
    start = time.time()
    print(fib.calcola_elemento_cache(N))
    print(fib.ricorsioneCache) #usando cache invoco molto molto meno le funzioni
    # , faccio meno ricorsioni
    end = time.time()
    print(f"Elapsed time with cache: {end - start}")

#usando tool lru, crea da solo la cache
    start = time.time()
    print(fib.calcola_elemento_lru(N))
    end = time.time()
    print(f"Elapsed time with lru: {end - start}")

