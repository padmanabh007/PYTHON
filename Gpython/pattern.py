n=int(input('Enter the number of rows of * required '))

for i in range(1,n+1):
    if i%2==0:
        s=int((n-i)/2)
        for j in range(2):
            print(" "*s,"*"*i)
