#def even_odd(n):#from which the elements which are tue is only printed
    #if n%2==0:
        #return True #return inside the funcion does not print any value

#to applt these funcion for the list  of elementswe use
lst=[1,2,3,4,5,6,7,8,9,0]
#p=list(filter(even_odd,lst))
#print(p)
#o/p
#[2, 4, 6, 8, 0] will print only the values whose values are true

#using lambda function inside the list
p=list(filter(lambda n: n%2==0,lst))
print(p)
#o/p
#[2, 4, 6, 8, 0] is the output which is get insted of using a long function

#using map insted of using filter
p=list(map(lambda n: n%2==0,lst))
print(p)
#o/p
#[False, True, False, True, False, True, False, True, False, True] is the output
