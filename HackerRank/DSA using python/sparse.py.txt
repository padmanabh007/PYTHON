def matchingStrings(strings, queries):
    l=[]
    for i in queries :
        if i in strings :
            l.append(strings.count(i))
        else :
            l.append(0)
    return l
