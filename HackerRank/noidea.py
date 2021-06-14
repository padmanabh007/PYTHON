if __name__ == "__main__" :
    m,n=map(int , input().split())
    ar=set(map(int,input().split()))
    a=set(map(int,input().split()))
    b=set(map(int,input().split()))
    h=len(ar.intersection(a))-len(ar.intersection(b))
    print(h)
    