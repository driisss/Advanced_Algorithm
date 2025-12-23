class Nqueen: #exam ma aauda solve vanne wala samma matra garne safe wala pardaina exam ma but assignment tira chai paryooooo
    def solveNqueen(self,n):
        board = [["." for _ in range(n)] for _ in range(n)]
        result=[]
        self.solve(0,board,result,n)


    def solve (self,col,board,result,n):
        if col==n:
            #save board solution in theb result
            pass
        for row in range(n):
            if self.issafe(row,col,board,n):
                board[row][col]="Q"
                self.solve(col+1,board,result,n)
                board[row][col]="."

    def issafe(self,row,col,board,n):
        #check horizontally
        for j in range (n):
            if board [row] [j]=="Q":
                return False
            
        #check vertically
        for i in range (n):
            if board [i] [col]=="Q":
                return False
                
        #checking diagonally upwards left
        i = row
        j = col
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i-=1
            j-=1

        #checking diagonally upwards right
        i = row
        j = col
        while i>=0 and j<n:
            if board[i][j]=="Q":
                return False
            i-=1
            j+=1

        #checking diagonally downwards left
        i = row 
        j = col
        while i<n and j>=0:
            if board[i][j]=="Q":
                return False
            i+=1
            j-=1 

        #checking diagonally downwards right
        i = row
        j = col
        while i <n and j<n:
            if board [row][col] == "Q":
                return False
            i+=1
            j+=1

        return True
    
    
    
    

