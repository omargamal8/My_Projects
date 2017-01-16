from __future__ import print_function
from Nodes import *


class Gridd:
    def __init__(self, y, x):
        self.grid = []
        self.visited=[]
        for i in range(y):
            self.grid.append([])
            self.visited.append([])
            for j in range(x):
                self.grid[i].append([])
                self.visited[i].append(False)



    def printgrid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if type(self.grid[y][x])is Node:
                    #print(self.grid[y][x].power, end='   ')
                    print(1, end='   ')

                else:
                    print(0, end='   ')
            print()

    def printgrid_transmission(self,srcx,srcy,destx,desty):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if type(self.grid[y][x])is Node:
                    if y==srcy and x==srcx:
                        print(self.grid[y][x].power, end='<S  ')
                    elif y==desty and x==destx:
                        print(self.grid[y][x].power, end='<D  ')
                    else:
                        if(self.grid[y][x].power<9999999999):
                            print(self.grid[y][x].power, end='    ')
                        else:
                             print('N', end='    ')

                else:
                    print(0, end='    ')
            print()
