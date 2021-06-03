def mergeLists(head1, head2):
    itr1=head1
    l=[]
    while itr1.next!=None :
        l.append(itr1.data)
        itr1=itr1.next 
    itr1.next=head2
    while itr1.next!=None :
        l.append(itr1.data)
        itr1=itr1.next
    l.append(itr1.data)
    print(l)
    l.sort()
    itr=head1
    i=0
    while itr :
        itr.data=l[i]
        itr=itr.next
        i+=1
    return head1