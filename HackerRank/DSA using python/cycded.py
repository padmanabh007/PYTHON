
#Cycle detection in liked list

def has_cycle(head):
    itr=head
    l=[]
    while itr and itr not in l:
        if itr.next==None :
            return 0
        l.append(itr)
        itr=itr.next
    return 1
