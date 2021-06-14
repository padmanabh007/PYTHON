n=[]
for i in range(int(input())) :
    n.append(input())
n3=[]
n2=[]
for i in n :
    if i not in n3 :
        n3.append(i)
        n2.append(n.count(i))
print(len(n3))
print(*n2)