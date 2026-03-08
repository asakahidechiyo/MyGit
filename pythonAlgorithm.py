import numpy as np

class SeqList:
    def __init__(self,size=100):
        self.MAXSIZE=size
        self.length=0
        self.data=[None for x in range(0,self.MAXSIZE)]

    def _resize(self):
        oldMaxsize=self.MAXSIZE
        self.MAXSIZE=oldMaxsize*2
        newData=[None for i in range(self.MAXSIZE)]
        for i in range(self.length):
            newData[i]=self.data[i]
        self.data=newData
        print(f"SeqList has resized: {oldMaxsize}->{self.MAXSIZE}")

    def isFull(self):
        if self.length>=self.MAXSIZE:
            return True
        return False
        
    def isEmpty(self):
        if self.length==0:
            return True
        return False

    def append(self,value):
        if(self.isFull()):
            self._resize()
        self.data[self.length]=value
        self.length+=1

    def find(self,value):
        if self.isEmpty():
            return False
        for i in range(self.length):
            if self.data[i]==value:
                return True
        return False
    
    def getByIndex(self,index):
        if not isinstance(index,int):
            raise TypeError
        if self.isEmpty():
            return None
        return self.data[index]
    
    def insert(self,index,value):
        if self.isFull():
            self._resize()
        if not isinstance(index,int):
            raise TypeError
        if index>self.length or index<0:
            raise AttributeError("Trying to insert into a not-exist place")
        for iCurrentIndex in range(self.length,index,-1):
            self.data[iCurrentIndex]=self.data[iCurrentIndex-1]
        self.data[index]=value
        self.length+=1
        return True

    def display(self):
        if self.isEmpty():
            print("SeqList is empty")
            return True
        print(*(self.data[:self.length]), sep=" ", end="\n", flush=True)
        return True

initLength=input("Enter init data, which is the MAXSIZE of SeqList:")
myList=SeqList(int(initLength))
for i in range(int(initLength)):
    myList.append(i)
myList.display()
rawInput=input("Enter insert index and value:")
iInsertIndex,nValue=rawInput.split()
myList.insert(int(iInsertIndex),int(nValue))
myList.display()
input("请按回车继续...")