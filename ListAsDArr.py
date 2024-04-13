import ctypes
class myList:
    def __init__(self):
        self.size=1
        self.n=0
        self.Arr=self.__create(self.size) # makes a ctype array whose size is self.size
    def __create(self,capacity):
        return (capacity*ctypes.py_object)() #creates a static array with size capacity
    
    def length(self):
        return self.n

    def append(self,item):
        if self.n==self.size:
            #resize the array. to enter more elements on the already filled array
            self.__newSize(self.size*2)
        self.Arr[self.n]=item
        self.n=self.n+1
    def __newSize(self,newCap):
        NewArr=self.__create(newCap) # creation of the new array with the extra size
        self.size=newCap

        for i in range(self.n):
            NewArr[i]=self.Arr[i] #copy the content of the previous array into the new array
        self.Arr=NewArr
    
    def printList(self):
        result=''
        for i in range(self.n):
            result=result+str(self.Arr[i])+','
        return '[' + result[:-1] + ']'
    
    def __getVal__(self,index):
        if 0<=index<=self.n:
            return self.Arr[index]
        else:
            return "Index out of range"
    
    def pop(self):
        if(self.n==0):
            return "List is Empty"
        print(self.Arr[self.n-1])
        self.n=self.n-1
    def clear(self): #empties the list
        self.n=0
        self.size=0
    def find(self,num):
        for i in range(self.n):
            if(self.Arr[i]==num):
                return i
        return 'Value not present'
    def insert(self,pos,item):
        if self.n==self.size:
            self.__newSize(self.size*2)
        for i in range(self.n,pos,-1):
            self.Arr[i]=self.Arr[i-1]
        self.Arr[pos]=item

        self.n=self.n+1
    
    def delfromPos(self,pos):
        if 0<=pos<=self.n:
        
            for i in range(pos,self.n-1):
                self.Arr[i]=self.Arr[i+1]
            
            self.n=self.n-1 
        else:
            print("Index Error")
    def remove(self,item):
        pos=self.find(item)
      
        if type(pos)==int:
            self.delfromPos(pos)
        else:
            return pos


                
    
    

L=myList()
L.append("Hello")
L.append(3.4)
L.append(True)
L.append(100)
print(L.length()) # prints the length of the List using the length(not inbuilt in this case) function
print(L.printList()) # prints the list items 
print(L.__getVal__(1)) #prints the value at the given index


print(L.find(3.4))
print(L.printList())
L.remove(3.4)
print(L.printList())
