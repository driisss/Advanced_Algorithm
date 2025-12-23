class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stk = [0] * capacity
        self.top = -1
     
        