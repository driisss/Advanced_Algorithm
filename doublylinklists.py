class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.dummyhead = Node(0)
        self.dummytail = Node(0)
        
    def insNode (self, data):
        newnode = Node(data)
        if (self.dummyhead.next == None):
            self.dummyhead.next = newnode
            newnode.prev = self.dummyhead
            newnode.next = self.dummytail
            self.dummytail.prev = newnode
        else:
            newnode.prev = self.dummytail.prev
            newnode.next = self.dummytail
            self.dummytail.prev.next = newnode
            self.dummytail.prev = newnode 