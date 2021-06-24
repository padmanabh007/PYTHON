
#Insertionsort using python
l=[5,12,6,7,8,23,48,96,1,3,9]

for i in range(1,len(l)) :
    m=l[i]
    j=i-1
    while j>=0 and m<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=m
print(l) 

#Taking input from the user
n=int(input('Ente the totel number of elements : '))
lu=list(map(int,input(f'Enter {n} element : ').split()))
if n==len(lu) :
    for i in range(1,n) :
        ma=lu[i]
        j=i-1
        while j>=0 and ma<lu[j] :
            lu[j+1]=lu[j]
            j=j-1
        lu[j+1]=ma
    print(*lu)
else:
    print('Elements is not equal to the length you entered ')
