#ricorsione: definizione che richiama se stessa
#funzione, un metodo è ricorsivo quando il metodo richiama se stesso
#crea una struttura circolare

#l'obiettivo è di scomporre il problema fino a quando scomponibile,
#quando creo un metodo, chiamerà se stesso "scomposto"
#creando ricorsioni fin quando possibile

#alla fine di ogni funzione ricorsiva, la funzione richiama se stessa
#pianificando il termine della ricorsione
#sys.getrecursionlimit()-->crea limite di ricorsione per evitare loop

#una funzione iterativa può essere sempre modificata in una ricorsiva
#si usa:
#divide et impera-->dividere il problema P in i problemi Qi, della stessa
#                   natura di P, risolvere i Qi priblemi e unire
#                   le soluzioni dei sotto problemi
#Exploration-->procedura per cui si esplorano tutte le possibili soluzioni
#              e si cerca la soluzine migliore, si usa all'esame e
#              consiste nell'esplorazione di ub grafo
#Strutture dati ricorsive--> data una lista e un input list, si aggiunge alla lista
#                            il primo elemento della input, eliminandolo
#                            fin quando input non sarà vuota
#inserire SEMPRE if ed else--> altrimenti si crea una ricorsione infinita
#LISTE ANNIDATE-->


#ESISTE TOOL PER CREARE DELLE MEMORIE CACHE @lru_cache
#
#