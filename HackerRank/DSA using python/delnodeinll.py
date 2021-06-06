
#Delete node from a particlar position

def deleteNode(llist, position):
    itr=llist
    if position==0 :
        llist=llist.next
        return llist
    c=0
    while itr.next!=None :
        node=itr
        itr=itr.next
        if c==position-1 :
            node.next=itr.next
            break
        c=c+1
    return llist
        