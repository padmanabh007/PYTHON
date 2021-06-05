#Function to print elements in a linkedlist


def printLinkedList(head):
    itr=head
    while itr :
        print(itr.data)
        itr=itr.next
