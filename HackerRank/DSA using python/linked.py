
#SinglyLinked list using python

#Creating node of a linkedlist
class Node :
    def __init__(self,data):
        self.data=data
        self.link=None

#Singly liked list
class singlyLl:
    
    #Declaring head
    def __init__(self):
        self.head=None


    #Inserting at the beginning of the linkedlist
    def insert_at_beg(self,data):
        node=Node(data)
        node.link=self.head
        self.head=node

    #Inserting at particular position
    def insert_at_pos(self,data,pos) :
        if self.head == None:
            self.head=Node(data)
            
        else :
            node=Node(data)
            itr=self.head
            p=1
            while itr.link != None:
                if p == pos-1 :
                    node.link=itr.link
                    itr.link=node
                    break
                pos+=1
                itr=itr.link
            else:
                itr.link=node
            
    #Insert at end of a linked list
    def insert_at_end(self,data):
        node=Node(data)
        if self.head == None:
           self.head=node
           return
        else :
            itr=self.head
            while itr.link!=None:
                itr=itr.link
            itr.link=node
            
            
    #To insert using values
    def insert_use_values(self,value) :
        node=Node(value)
        if self.head is None:
            head=Node
        elif self.head.data > value :
            node.link=self.head
            self.head=node
        else :
            itr=self.head
            while itr.link is not None:
                prev=itr
                itr=itr.link
                if itr.data > value :
                    node.link=itr
                    prev.link=node
                    break  
            else:
                itr.link=node

                
                
    #Delete at the beginning 
    def delete_at_beg(self) :
        if self.head is None:
            print('No elements to delete ')
        else :
            itr=self.head
            self.head=itr.link
            itr.link=None
    
    #Delete from a position
    def delete_at_pos(self,pos) :
        if self.head is None:
            print('No elements to delete ')
        else :
            itr=self.head
            p=1
            while itr.link is not None:
                prev=itr
                itr=itr.link
                if p==pos-1 :
                    prev.link=itr.link
                    itr.link=None
                    break
                p+=1
            else :
                prev.link=None

    #Delete at the end
    def delete_at_end(self):
        if self.head is None:
            print('No elements to delete ')
        else :
            itr=self.head
            while itr.link is not None:
                prev=itr
                itr=itr.link
            prev.link=None

    

    #Printing the linkedlist values
    def printll(self) :
        if self.head==None :
            print('No elemnts in the linked list ')
            return
        else :
            itr=self.head
            while itr.link!=None:
                print (f"{itr.data}-->",end='')
                itr=itr.link
            print(itr.data)

#Main function
if __name__ == '__main__':
    l=singlyLl()
    l.insert_at_beg(5)
    l.insert_at_beg(2)
    l.insert_at_beg(3)
    l.printll()
    l.insert_at_end(10)
    l.printll()
    l.insert_at_pos(12,2)
    l.printll()
    l.delete_at_beg()
    l.printll()
    l.delete_at_pos(2)
    l.printll()
    l.delete_at_end()
    l.printll()
   
