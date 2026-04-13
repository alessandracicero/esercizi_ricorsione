def count_leaf_nodes(input_list):
    #condizinoe terminale
    if len(input_list) == 0:
        return 0
    #non terminale
    else:
        counter = 0
        for node in input_list:
            #checklist element is a list
            #se è una lista, contiamo gli elementi tramite una ricorsione
            if type(node) == list:
                counter += count_leaf_nodes(node)
                #altrimenti aggiungi +1, cioè se il mio elemento è una lista mi richiami,
                # vedi quanti elementi ci sono nella sotto lista e li aggiungi,
                # altrimenti è un elemento quindi conto un +1
            else:
                counter += 1
        return counter



if __name__ == '__main__':
    names = ['Adam',['Bob',['Chet', 'Cat'],['Barb', 'Bert'], 'Alex'],['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names))