
#Multidiensional array using python

l=[]
nrows=int(input("Enter number of rows : "))
ncolumns=int(input("Enter number of columns : "))

#Insertion
for i in range(nrows):
    rowl=[]
    for j in range(ncolumns) :
        rowl.append(int(input(f"Enter a[{i+1}][{j+1}] : ")))
    l.append(rowl)


#To print the 2d array
for i in l:
    print(i)


#To find position of a number in a array
Find=int(input("Enter the element to search : "))
F=False
for i in range(nrows) :
    for j in range(ncolumns):
        if l[i][j]==Find:
            print(f"Find at position a[{i+1}][{j+1}]")
            F=True
            break
    if F:
        break
else:
    print("Element not found")


#To Delete
Delete=int(input("Enter the element to delete : "))
F=False
for i in range(nrows) :
    for j in range(ncolumns):
        if l[i][j]==Delete:
            print("Deleted")
            l[i][j]=0 #Deleted position is replaced by 0
            F=True
            break
    if F:
        break
else:
    print("Wrong input to delete")

print(*l)


#To insert
Yn=input('Want to change any elemnt (y,n) ').lower()
if Yn=='y' :
    row,col=int(input('Row = ')),int(input('Column = '))
    element=int(input("Enter the element "))
    l[row-1][col-1]=element
    print("New array : ",*l)