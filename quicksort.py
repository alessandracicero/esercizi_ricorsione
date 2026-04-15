def quick_sort(arr):
    #caso terminale
    if len(arr) <= 1:
        return arr

    #caso ricorsivo
    else:
        #scelgo pivot
        #se non ho info della listra, prendo uno a caso es il primo
        pivot = arr[0]
        #divido sequence seconfo pivot
        seq_smaller=[]
        seq_larger=[]
        seq_pivot=[]
        for x in arr:
            #caso 1 il numero è minore del pivot
            if x < pivot:
                seq_smaller.append(x)
            #caso 2 numero uguale al pivot
            elif x==pivot:
                seq_pivot.append(x)
            #caso 3 numero più grande del pivot
            else:
                seq_larger.append(x)
        return(quick_sort(seq_smaller) + [pivot] + quick_sort(seq_larger))
    #la soluazione è data da ordinare il vettore dei più piccoli+ il vettore =pivot,
    # + ordinare il vettore dei più grandi ordinato


if __name__ == '__main__':
    arr = [1, 3, 5, 5,6,82,2, 6, 4]

    print(quick_sort(arr))