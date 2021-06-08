
#Minion Game

def minion_game(string):
    Stuart=0
    Kevin=0
    ss=[]
    sk=[]
    for i in range(len(string)) :
        if string[i] in 'AEIOU' :
            Kevin=Kevin+len(string)-i
        else :
            Stuart=Stuart+len(string)-i
    if Stuart>Kevin :
        print('Stuart',Stuart)
    elif Kevin>Stuart:
        print('Kevin',Kevin)
    else :
        print('Draw')   
