
#Linerar serarching algorithm using python

#Using pre-declared list
l=[3,4,6,2,5,1,7,10,45]
search=15
for i in range(len(l)):
    if l[i] == search:
        print('Found at position : ',i+1)
        break
else:
    print('Not found ')

#Taking input from the user
li=[]
for i in range (int (input('Enter the total number of elements : '))):
    li.append(int(input()))

find=int(input('Enter the element to be searched : '))
for i in range(len(li)) :
    if li[i] == find:
        print(f"Elelment found at position {i+1} ")
        break
else:
    print('Element not found')