#Stack using array

l=[]
top=0
for i in range(int(input('Enter the number of elements in the stack : '))):
    l.append(int(input()))


yn=input('Do you want to remove an element from the stack (y/n) ').lower()
if yn=='n' :
    quit()
else:
    print(l.pop())
    print("remaing elements in list ->",*l)



#Using linked list

class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.top=None
        self.head=None
        
    def push(self,data) :
        node=Node(data)
        if self.top is None:
            self.head=node
            self.top=node
        else :
            self.top.next=node
            self.top=self.top.next

    def pop(self):
        if self.top is None:
            print('Empty stack ')
        else :
            itr=self.head
            while itr.next is not None:
                prev=itr
                itr=itr.next
            self.top=prev
            self.top.next=None


    def printstack(self) :
        if self.head is None:
            print('Empty stack')
        else :
            itr=self.head
            while itr.next is not None :
                print(f"{itr.data}-->",end='')
                itr=itr.next
            print(itr.data)

if __name__=="__main__":
    l=linkedlist()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.printstack()
    l.pop()
    l.printstack()
