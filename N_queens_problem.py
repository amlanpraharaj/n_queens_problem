
# coding: utf-8

# In[14]:

import numpy as np


# In[23]:

class Nqueen:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for i in range(self.size)] for j in range(self.size)]
    
    def valid_move(self, row, col):
        # Check this row on left side
        for i in range(col):
            if self.grid[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
            if self.grid[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i,j in zip(range(row,self.size,1), range(col,-1,-1)):
            if self.grid[i][j] == 1:
                return False
        return True
                
    def solve(self, col):
        if col >= self.size:
            return True
        
        for i in range(self.size):
            if(self.valid_move(i, col)):
                self.grid[i][col] = 1
                
                if(self.solve(col + 1)):
                    return True
                
                self.grid[i][col] = 0
        return False


# In[27]:

#initialize instance
board = Nqueen(18)


# In[28]:

board.solve(0)


# In[29]:

board.grid


# In[ ]:



