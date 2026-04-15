def dichotomic(inputlist,num):
    #caso terminal
    if len(inputlist)==1:
        if inputlist[0]==num:
            return True
        else:
            return False
    #caso ricorsivo
    else:
        index = len(inputlist)//2
        return (dichotomic(inputlist[:index],num)
                or  dichotomic(inputlist[index:],num))


if __name__ == '__main__':
    sequence=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(dichotomic(sequence, 4))
    print(dichotomic(sequence, 11))
