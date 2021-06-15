#Array data structure using python

l=[]  #Declaring a list to store values in the array
for i in range(int(input("Enter the number of elements required : "))):
    l.append(int(input(f"Enter the {i+1} element : ")))

#to print all the elements
print(*l)


#SORTING using python inbuilt function
l.sort()
print(*l)

#Sorting without using inbuilt python functions
for i in range(len(l)-1):
    for j in range(i,len(l)-1):
        if l[j]>l[j+1] :
            l[j],l[j+1]=l[j+1],l[j]

print(*l)

#Enter the elements to be find
find=int(input("Enter the elements to search : "))
for i in l :
    if i==find:
        print(f"Element find at position {l.index(i)}")
        break
else:
    print("Element not found")

#Enter the elements to delete
delete=int(input("Enter the elements to delete : "))
for i in l :
    if i==delete:
        l.pop(l.index(i))
        print('Deleted')
        break
else:
    print("Wrong input for delete ")
        
        
print(*l)
