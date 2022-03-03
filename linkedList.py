import time
from array import *

def showingArray(processID,arrayToDelete):
    print("this reruns the program because IO for the print statement slowed down \nthe program so this makes it run faster and faster than the linkedlist")
    for x in arrayToDelete:
        print(x)
    print("before array is told to delete processID", processID)
    count = 0
    for a in arrayToDelete:
        if(a[0] == processID):
            break
        else:
            count = count + 1
    #del arrayToDelete[count]
    for g in range(len(arrayToDelete)):
        if(g != count):
            continue
        else:
            for h in range(len(arrayToDelete[g])):
                arrayToDelete[g][h] = None
#                for h in range(len(arrayToDelete[g])):
#                        arrayToDelete[g][h] = None   
                             
    #above code deletes the child process from the array index
    #change this to just empty the slots

    for i in range(len(arrayToDelete)):
        if(g == count):
            continue
        else:
            for j in range(len(arrayToDelete[i])):
                    if(arrayToDelete[i][j] == processID):
                        arrayToDelete[i][j] = None
 
    for x in arrayToDelete:
        print(x)
    print("after")
def arrayDel(processID,arrayToDelete):
    count = 0
    for a in arrayToDelete:
        if(a[0] == processID):
            break
        else:
            count = count + 1
    #del arrayToDelete[count]
    for g in range(len(arrayToDelete)):
        if(g != count):
            continue
        else:
            for h in range(len(arrayToDelete[g])):
                arrayToDelete[g][h] = None
#                for h in range(len(arrayToDelete[g])):
#                        arrayToDelete[g][h] = None   
                             
    #above code deletes the child process from the array index
    #change this to just empty the slots

    for i in range(len(arrayToDelete)):
        if(g == count):
            continue
        else:
            for j in range(len(arrayToDelete[i])):
                    if(arrayToDelete[i][j] == processID):
                        arrayToDelete[i][j] = None
    addChild(3,arrayToDelete)
def addChild(processID, arrayToAdd):
    #adding child
    arrayToAdd[2][0] = 3
    arrayToAdd[2][1] = 1
    arrayToAdd[2][2] = None
    arrayToAdd[2][3] = 2
    arrayToAdd[1][2] = 3

 
class Node:
  
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next
    

class LinkedList:
  def __init__(self):  
    self.head = None
    self.start = 0
    
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
      self.start = self.start + 1
    else:
      self.head = newNode
  def destroy(self):
    #while (self.head != None and self.start != 0):
      if(self.head != None and self.start != 0):
        temp = self.head
        self.head = self.head.next
        temp = None
        self.start = self.start -1
        LL.destroy()
      #else:
          #print("at the start: ", self.head.data)

  def countList(self):
    countlist = 0
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
        countlist = countlist + 1
      print("nodes in the list: ", countlist + 1)
  def printLL(self):
    array = []
    current = self.head
    while(current):
      array.append(current.data)
      current = current.next
    print(array)
    print("number of nodes: ", self.start + 1)


LL = LinkedList()
LL2 = LinkedList()
#for i in range(0,100):
    #LL.insert(i)

tic = time.perf_counter()
for x in range(1,1000000):
    LL.insert(0)
    LL.insert(0)# creates 1st child of PCB[0] at PCB[1]
    LL.insert(0)# creates 2nd child of PCB[0] at PCB[2]
    LL.insert(2)# creates 1st child of PCB[2] at PCB[3]
    LL.insert(0)# creates 3rd child of PCB[0] at PCB[4]
    LL.destroy()
toc = time.perf_counter()
ms = (toc - tic) 
print(f"linked list completed in ",ms," seconds")
tec = time.perf_counter()
twoDArray = [[1,0,None,None], [2,1,3,None], [3,1,None,2], [4,0,None,None]]
for i in range(0,1000000):
    arrayDel(3,twoDArray)
tac = time.perf_counter()
ps = (tac - tec)  

print(f"array completed in ",ps," seconds")

#twoDArray = [[1,0,None,None], [2,1,3,None], [3,1,None,2], [4,0,None,None]]
#showingArray(3,twoDArray)
#  
#    LL.insert(0)# creates 1st child of PCB[0] at PCB[1]
#    LL.insert(0)# creates 2nd child of PCB[0] at PCB[2]
#    LL.insert(2)# creates 1st child of PCB[2] at PCB[3]
#    LL.insert(0)# creates 3rd child of PCB[0] at PCB[4]
#    LL.destroy()
#
#    3. 
#    on average 2 seconds is saved when the program is ran 1000000 times
#
#
#
#
#
#
#
