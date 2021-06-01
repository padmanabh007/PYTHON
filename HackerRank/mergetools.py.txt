def merge_the_tools(string, k):
    
    for i in range(0,len(string),k) :
        sm=''
        st=''
        s=string[i:k+i:]
        for j in s :
            if j not in st :
                sm=sm+j
            st=st+j
        print(sm)
                
        
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)