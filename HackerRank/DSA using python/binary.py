
#Python program to impliment in binary search 

#Using predeclared list
l=[2,3,4,7,8,9,10,12,15]
search=16
first=0
last=len(l)-1
mid=(last+first)//2
while last>=first:
    if l[mid] == search :
        print(f'Element found at position {mid+1}')
        break
    elif search<l[mid] :
        last=mid-1
        mid=(last+first)//2
    elif search>l[mid] :
        first=mid+1
        mid=(last+first)//2
else:
    print('Element not found ')

#Using recursion
def binary_search(arr,first,last,search) :
    if first<=last :
        mid=(first+last)//2
        if arr[mid]==search:
            print(f'Element found at position {mid+1}')  
        elif arr[mid]>search:
            binary_search(arr,first,mid-1,search)
        elif arr[mid]<search:
            binary_search(arr,mid+1,last,search)
    else:
        print('Element not found')

lr=[2,3,4,7,8,9,10,12,15]
search=1
first=0
last=len(lr)-1
binary_search(lr,first,last,search)



#Taking in put from the user
lu=[]
for i in range(int(input('Enter the number of elements : '))) :
    lu.append(int(input()))
search=int(input('Enter the element to be searched : '))
first=0
last=len(lu)-1
mid=(last+first)//2
while last>=first:
    if lu[mid] == search :
        print(f'Element found at position {mid+1}')
        break
    elif search<lu[mid] :
        last=mid-1
        mid=(last+first)//2
    elif search>lu[mid] :
        first=mid+1
        mid=(last+first)//2
else:
    print('Element not found ')

#This can also be done using recursion