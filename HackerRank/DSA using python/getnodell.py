
#Get node value of a linked list

def getNode(llist, positionFromTail):
    itr=llist
    l=[]
    while itr :
       l.append(itr.data)
       itr=itr.next 
    return (l[len(l)-positionFromTail-1])