def hourglassSum(arr):
    l=[]
    for i in range(len(arr)-2):
        s=0
        for j in range(len(arr)-2):
            s=0
            s=sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
            l.append(s)
    return(max(l))