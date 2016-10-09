import sys
class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList(object):
    head = None
    tail = None
    
    def createNewNode(self, data): return Node(data, None, None)
    def inputNumber(self):x = input('enter the Number to insert');return int(x)
    
    def insert(self, data):
        newNode = self.createNewNode(data)
        ##print(" inside insert %s" % (str(data)))
        if self.head is None:
            print("Inserting first node")
            self.head = self.tail = newNode
        elif newNode.data < self.head.data:
            print("Inserting second node")
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode   
        elif newNode.data > self.tail.data:
            print("Inserting last node")
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            print("Inserting node at a position")
            findNode = self.head
            while findNode is not None:
                if newNode.data==findNode.data:
                    print("That's a duplicate. try Again")
                    break
                elif newNode.data < findNode.data:
                    print("The value is lesser, inserting before %d" % (findNode.data))
                    newNode.next = findNode
                    newNode.prev = findNode.prev
                    findNode.prev.next = newNode
                    break
                findNode = findNode.next
                  
    def delete(self, data):
        print ("Inside delete %s" % (str(data)))
    def search(self,data):
        print ("Inside search %" % (str(data)))
    def printList(self):
        print ("Inside print")
        current_node = self.head
        while current_node is not None:
            ##current_node.data
            ##print (current_node.prev.data) if hasattr(current_node.prev, "data") else None,
            print (current_node.data)
            ##print (current_node.next.data) if hasattr(current_node.next, "data") else None
 
            current_node = current_node.next
        print ("*"*50)
            

dObject = DoubleLinkedList()
def inputChoice(default="1"):
    userChoice = input( """\t1. Insert  a number\n\t2. Delete a number\n\t3. Search for a number\n\t4. Print the List\n\t5. Exit""")
    if userChoice == '1':
        data = dObject.inputNumber()
        dObject.insert(data)
    elif userChoice == '2':
        data = dObject.inputNumber()
        dObject.delete(data)
    elif userChoice == '3':
        data = dObject.inputNumber()
        dObject.search(data)
    elif userChoice == '4':
        dObject.printList()
    elif userChoice == '5':
        print ("bye Bye !!")
        sys.exit(0)

while True:   
    inputChoice()




        