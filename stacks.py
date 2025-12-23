class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stk = [0] * capacity
        self.top = -1
        
    def push(self, data):
        if (self.isFull()):
            print ("Stack Overflow")
        else:
            self.top  = self.top + 1
            self.stk [self.top]= data 
            
    def pop (self):
        if (self.isEmpty ()):
            print ("Stack Underflow")
            return -1
        tmp = self.stk[self.top]
        self.top = self.top - 1
        return tmp
    
    def peek (self):
        return self.stk[self.top]
    
       
    def isFull(self):
        return self.top == self.capacity - 1              
    
    def isEmpty (self):
        return self.top == -1
    
stk = Stack(5)
stk.push(10)
stk.push(20)
print(stk.pop())  # Output: 20




