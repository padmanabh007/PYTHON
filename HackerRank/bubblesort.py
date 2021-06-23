
#Bubble sort using python


l=[4,7,8,9,2,0,1,11,32,10]
for i in range(len(l)) :
    for j in range(0,len(l)-i-1) :
        if l[j+1]<l[j]:
            l[j],l[j+1]=l[j+1],l[j]

print(*l)


#Taking input from user and sorting
lu=[]
for i in range(int(input('Enter the number of elements to sort : '))) :
    lu.append(int(input()))

for i in range(len(lu)) :
    for j in range(0,len(lu)-i-1) :
        if lu[j+1]<lu[j] :
            lu[j],lu[j+1]=lu[j+1],lu[j]

print(*lu)