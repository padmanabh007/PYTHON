# Merge sort using python

def mergesort(li) :
    if len(li)>1 :
        mid=len(li)//2
        L=li[:mid:]
        R=li[mid::]
        mergesort(L)
        mergesort(R)
        i,j,k=0,0,0
        while i<len(L) and j<len(R) :
            if L[i]<R[j] :
                li[k]=L[i]
                i+=1
            else :
                li[k]=R[j]
                j+=1
            k+=1

        while i<len(L) :
            li[k]=L[i]
            i+=1
            k+=1
        while j<len(R) :
            li[k]=R[j]
            j+=1
            k+=1
        

li=[2,8,3,5,11,0,13,28,21,12,23,26]
mergesort(li)
print(*li)

#Taking input from the user 
lu=[]
for i in range(int(input("Enter number of elemets to be inserted "))):
    lu.append(int(input()))
print(*lu)
mergesort(lu)
print(*lu)