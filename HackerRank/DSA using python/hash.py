
#Hash Table using python


#Using dictionary
prices={'march':1200,'April':1400}
for i ,j in prices.items():
    print(i,'=',j)


#Function to getting hash value of a particular key for eg
'''
def get_hash_value(key):
    hashval=0
    for char in key:
        hashval+=ord(char)
    return hashval%100

val=get_hash_value('march')
print(val)
'''

#Implementing hash table
class HashTable :
    def __init__(self) :
        self.MAX=100                      #IT is the maximum number of elemets in the hash table 
        self.arr=[[] for i in range(self.MAX)] #Inseting values inside the array using list comprehension and each value to 'NONE' to avoid collision we make it as []

    #Hash table creation
    def get_hash_value(self,key) :
        hashval=0
        for char in key:
            hashval+=ord(char)
        return hashval%self.MAX

    def __setitem__(self,key,value) :
        h=self.get_hash_value(key)
        self.arr[h].append({key:value})

    def __getitem__(self,key) :
        val=self.get_hash_value(key)
        for i in self.arr[val] :
            s=list(i.keys())
            if s == [key]:
                return i[key]

    def __delitem__(self,key):
        val=self.get_hash_value(key)
        self.arr[val]=None

    #Fixing collision

    
ht=HashTable()
ht['1']=1200
ht['2']=1300
ht['140']=1400
print(ht['1'])
print(ht['140'])
print(ht.arr)