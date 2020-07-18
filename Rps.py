import random as r

Comp=0
User=0

#Welcoming User
print("Welcome To ROCK PAPER SCISSORS")
points=int(input("How many times you would like to play against the computer "))

#Loop for the points entered by the user
for i in range(1,points+1):
    print("Enter your choice\n")
    choice=int(input("1.Rock\n2.Paper\n3.Scissors "))
    n=r.randrange(1,4,1)
    
    #Code for compairing user's and Computer's input
    if n==1:
        print("Compuer Entered Rock ")
        if(choice==1):
            print("TIE No Points")
        elif(choice==2):
            print("You Scored")
            User=User+1
        else:
            print("Computer scored")
            Comp=Comp+1
    if n==2:
        print("Compuer Entered Paper ")
        if(choice==1):
            print("Computer scored")
            Comp=Comp+1
        elif(choice==2):
            print("TIE No Points")
        else:
            print("You Scored")
            User=User+1
    if n==3:
        print("Compuer Entered Scissors ")
        if(choice==1):
            print("You Scored")
            User=User+1
        elif(choice==2):
            print("Computer scored")
            Comp=Comp+1
        else:
            print("TIE No Points")
print("Computer  YOU")
print(Comp,"     ",User)

#Compairing points and declaring the winner
if(Comp>User):
    print('Computer wins')
elif(User>Comp):
    print('You Win')
else:
    print('TIE')
