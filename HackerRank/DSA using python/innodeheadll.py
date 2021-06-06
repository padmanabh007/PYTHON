
#Insert node at head of a linked list
def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    if llist == None :
        return node
    else :
        node.next=llist
    return node
        