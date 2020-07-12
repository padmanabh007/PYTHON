#map is a handy funcion
def even_odd(n):
    if n%2==0:
        print('The number {} is even'.format(n))#return inside the funcion does not print any value
    else:
       print('The number {} is odd'.format(n))
#def main():
    #n=int(input('Enter the number '))
    #p=even_odd(n)
    #print(p)
#if __name__=='__main__':
    #main()


lst=[1,2,3,4,5,6,7,8,9,24,56,78]#to find which number is odd and even for iteration it will take more time for that we use map function
p=list(map(even_odd,lst))#make to perform the funcion easier we can get rid of the iteration
print(p)
#o/p
#The number 1 is odd
#The number 2 is even
#The number 3 is odd
#The number 4 is even
#The number 5 is odd
#The number 6 is even
#The number 7 is odd
#The number 8 is even
#The number 9 is odd
#The number 24 is even
#The number 56 is even
#The number 78 is even