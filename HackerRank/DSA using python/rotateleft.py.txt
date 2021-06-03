def rotateLeft(d, arr):
    for i in range(d) :
        c=arr.pop(0)
        arr.append(c)
    return arr