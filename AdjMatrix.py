from queues import queue

class Graph:
    def __init__(self, v):
        self.matrix = [[0 for _ in range(v)] for _ in range(v)]
        self.v = v

    def addEdge (self, source, destination):
        self.matrix [source] [destination] = 1
        self.matrix [destination] [source] = 1


    def printGraph (self):
        for i in range (len(self.matrix)):
            print (i," is connected to:", end="")  
            for j in range (len (self.matrix)):
                if self.matrix [i] [j] !=0:
                    print (j, ", ", end="")
            print ("")

    def bfs (self):
        q = queue()
        visited = [False]*self.v
        q.enqueue(source)
        visited [source]= True
        while not q.isEmpty():
            x= q.dequeue()
            print (x)
            for j in range (self.v):
                if self.matrix [x] [j]!=0 and not visited [j]:
                    q.enqueue(j)
                    visited [j]= True

    def dfs (self, source):
        visited = [False]*self.v
        self.depthFirstSearch(source, visited)

    def depthFirstSearch (self, source, visited):
        print (source)
        visited [source]= True
        for j in range (self.v):
            if self.matrix [source] [j]!=0 and not visited [j]:
                self.depthFirstSearch (j, visited)





g= Graph (6)
g.addEdge (0,1)
g.addEdge (0,2)
g.printGraph ()
                
                