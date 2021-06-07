def compare_lists(llist1, llist2):
    itr1,itr2=llist1,llist2
    c1,c2=0,0
    while itr1 is not None and itr2 is not None:
        if itr1.data!=itr2.data :
            return 0
        if itr1.next!=None :
            c1+=1
        if itr2.next!=None :
            c2+=1
        itr1=itr1.next
        itr2=itr2.next
    if c1==c2 :
        return 1
    else :
        return 0
    