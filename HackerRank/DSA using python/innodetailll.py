#Insert node at tail of a linked list

def insertNodeAtTail(head, data):
    node=SinglyLinkedListNode(data)
    itr=head
    if head==None:
        return node
    while itr.next!=None :      
        itr=itr.next
    itr.next=node
    return head
    