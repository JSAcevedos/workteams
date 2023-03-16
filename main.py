#Implementación de los nodos
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Implementación de la lista enlazada
class linkedList:
    
    def __init__(self):
      self.head = None
      self.tail = None
    
    def pushback(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def popback(self):
        if self.tail is None:
            print("ERROR: Empty list")
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            temp = current_node.data
            current_node.next = None
            self.tail = current_node
            return temp


    def print(self):
        if self.head is None:
            print("ERROR: Empty list")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
	

list = input().split()
length = len(list) - 1
students = linkedList()
workTeams = linkedList()

for i in range(int(length/2) + 1):
    j = length - i
    students.pushback(list[i])
    students.pushback(list[j])

students.print()



#Avila Bermudez Cardenas Ramos Rodriguez Valencia