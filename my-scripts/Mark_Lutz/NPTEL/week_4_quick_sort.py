def quick_sort(seq,l,r):
    if(r-l <= 1):
        return()

    yellow = l + 1

    for green in range(l+1,r):
        if(seq[green] <= seq[l]):
            (seq[yellow],seq[green]) = (seq[green],seq[yellow])
            yellow = yellow + 1


    (seq[l],seq[yellow-1]) = (seq[yellow-1],seq[l])

    quick_sort(seq,l,yellow-1)
    quick_sort(seq,yellow,r)



print(quick_sort([8,9,10,1,2,4,56,98,101],0,9))
