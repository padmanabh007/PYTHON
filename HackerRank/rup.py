
#To find the runner up

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
     
    maxa=max(arr)
    mina=min(arr)
    for i in arr :
        if i>maxa :
            maxa=i
      
    for i in arr :
        if i>mina and i<maxa :
            mina=i 
        
    print(mina)