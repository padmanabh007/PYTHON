
#Delete duplicate value in liked list

def removeDuplicates(llist):
    itr=llist
    l=[]
    #
    while itr:
        l.append(itr.data)
        itr=itr.next
    s=list(set(l))
    itr=llist
    for i in range(len(s)):
        itr.data=s[i]
        prev=itr
        itr=itr.next
    prev.next=None
    return llist