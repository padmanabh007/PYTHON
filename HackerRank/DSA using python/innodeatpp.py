#func to insertnode at particular position

def insertNodeAtPosition(llist, data, position):
    node=SinglyLinkedListNode(data)
    itr=llist
    if position==0 :
        node.next=llist
        llist=node
        return llist
    c=1   
    while c < position :
        itr=itr.next
        c=c+1
    node.next=itr.next
    itr.next=node
    return llist