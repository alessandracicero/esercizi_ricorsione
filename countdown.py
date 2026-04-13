from time import sleep
from turtledemo.round_dance import stop


def contdown(n):
    while n >=0:
        print(n)
        sleep(1)    #crea pausa
        n -= 1
def contdown_ricorsive(n):
    #condizione terminale:
    if n==0:
        print("STOP")
    #condizione non terminale
    else:
        print(n)
        #sleep(1)
        contdown_ricorsive(n-1)

if __name__== '__main__':
    N=10
    #contdown(N)
    if N>0:
        contdown_ricorsive(N)
    #andando a debuggare la riga sopra si crea stack delle funzioni chiamate
    #chiamera tante funzioni diverse quanto è il numero del countdowm
