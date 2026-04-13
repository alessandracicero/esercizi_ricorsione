def binomiale(n,k):
    if k==0 or n==k:
        return 1
    else:
        return binomiale(n-1,k-1) + binomiale(n-1,k)

if __name__ == '__main__':
    n = 4

    k = 3
    print(binomiale(n,k))

#l'approccio e di immaginare di risolvere solo
#l'ultimo step, senza pensare a ciò che accade prima
#scaricando tutto alla chiamata successiva

#Non mettere variabili globali, piuttosto
#incapsulare tutto in una classe