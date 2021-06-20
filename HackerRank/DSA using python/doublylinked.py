#Doubly linked list using python

#Cerating node of a  doubly linked list
class Node:
    def __init__(self,data) :
        self.data=data
        self.nextnode=None
        self.prevnode=None

#class for doubly linked list operations
class Doublyll:

    #Delaring head for the linked list
    def __init__(self):
        self.head=None
    
    #Inserting at the beginning 
    def insert_at_beg(self,data) :
        node=Node(data)
        if self.head is None:
            self.head=node
        else :
            node.nextnode=self.head
            self.head.prevnode=node
            self.head=node

    #Inserting at particular position 
    def insert_at_pos(self,data, pos):
        node=Node(data)
        if self.head is None:
            self.head=node
        else :
            itr=self.head
            p=1
            while itr.nextnode is not None:
                if p==pos :
                    node.nextnode=itr
                    node.prevnode=itr.prevnode
                    itr.prevnode.nextnode=node
                    itr.prevnode=node
                    break
                p+=1
                itr=itr.nextnode
            else:
                node.nextnode=itr
                node.prevnode=itr.prevnode
                itr.prevnode.nextnode=node
                itr.prevnode=node

    #Inserting at end 
    def insert_at_end(self,data) :
        node=Node(data)
        if self.head is None:
            self.head=node
        else :
            itr=self.head
            while itr.nextnode is not None:
                itr=itr.nextnode
            node.prevnode=itr
            itr.nextnode=node

    #Inserting using value best works on sorted linked list
    def insert_use_value(self,val) :
        node=Node(val)
        if self.head is None:
            self.head=node
        elif self.head.data >val:
            node.nextnode=self.head
            self.head.prevnode=node
            self.head=node
        else:
            itr=self.head
            while itr.nextnode is not None :
                if itr.data > val :
                    node.nextnode=itr
                    node.prevnode=itr.prevnode
                    itr.prevnode.nextnode=node
                    itr.prevnode=node
                    break
                itr=itr.nextnode
            else :
                itr.nextnode=node
                node.prevnode=itr




    #Delete from beginning
    def del_at_beg(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            itr=self.head
            self.head=self.head.nextnode
            itr.nextnode=None
            self.head.prevnode=None
    
    #Delete from end
    def del_at_end(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            itr=self.head
            while itr.nextnode is not None:
                itr=itr.nextnode
            itr.prevnode.nextnode=None
            itr.prevnode=None 

    #Delete from a position
    def del_at_pos(self,pos) :
        if self.head is None:
            print('Linked list is empty')
        else:
            itr=self.head
            p=1
            while itr.nextnode is not None :
                if p == pos:
                    itr.prevnode.nextnode=itr.nextnode
                    itr.nextnode.prevnode=itr.prevnode
                    itr.prevnode,itr.nextnode=None,None
                    break
                itr=itr.nextnode
                p+=1
 
    #Delete using values 
    def del_use_val(self,val):
        if self.head is None:
            print('Linked list is empty')
        elif self.head.data==val:
            itr=self.head
            self.head=self.head.nextnode
            itr.nextnode=None
        else:
            itr=self.head
            while itr.nextnode is not None:
                if itr.data == val:
                    itr.nextnode.prevnode=itr.prevnode
                    itr.prevnode.nextnode=itr.nextnode
                    itr.prevnode,itr.nextnode=None,None
                    break
                itr=itr.nextnode
            else:
                itr.prevnode.nextnode=itr.nextnode
                itr.prevnode=None

    #Sorting
    def sort_dl(self) :
        if self.head is None:
            print('Linked list is empty')
        else:
            l=[]
            itr=self.head
            while itr:
                l.append(itr.data)
                itr=itr.nextnode
            
            l.sort()
            itr=self.head
            while itr:
                itr.data=l.pop(0)
                itr=itr.nextnode
            

    #Reversing
    def revese_dl(self):
        if self.head is None:
            print('Linked list is empty ')
        else:
            itr=self.head
            while itr.nextnode is not None :
                prev=itr.prevnode
                itr.prevnode=itr.nextnode
                itr.nextnode=prev
                itr=itr.prevnode
            itr.nextnode=itr.prevnode
            itr.prevnode=None
            self.head=itr



    #Printing the linked list    
    def printdl(self):
        if self.head is None:
            print('Empty linked list')
        else :
            itr=self.head
            while itr.nextnode is not None:
                print(f"{itr.data}-->",end='')
                itr=itr.nextnode
            print(itr.data)
    

if __name__=='__main__':
    dl=Doublyll()
    dl.insert_at_beg(1)
    dl.insert_at_beg(3)
    dl.insert_at_beg(2)
    dl.insert_at_pos(4,3)
    dl.insert_at_end(20)
    dl.insert_at_end(22)
    dl.insert_use_value(6)
    dl.printdl()
    dl.sort_dl()
    dl.printdl()
    dl.del_at_beg()
    dl.del_at_end()
    dl.del_at_pos(2)
    dl.del_use_val(6)
    dl.printdl()
    dl.revese_dl()
    dl.printdl()