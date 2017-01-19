from __future__ import print_function

import random
from compiler.ast import nodes
Inf=9999999999

class Node(object):
    def __init__(self,grid,y,x,power=1):
        if power>1:
            self.power=power
        elif power==1:
            global Inf
            self.power =Inf
        else:
            self.power=0
        self.grid=grid.grid
        self.visited=False
        self.x=x
        self.y=y
        self.neighbours=[]
        self.sent=False
        self.shortestpath=-1



    def fillneighbourloop(self,radius=20):

        for y in range((self.y-int(radius)),self.y+int(radius)+1):
            if y <0 or y>=len(self.grid):
                continue
            horiz=int(pow(pow(radius,2)-pow(y-self.y,2),0.5)+self.x)
            for x in range(self.x-(horiz-self.x),horiz+1):
                if x<0 or x>=len(self.grid[y]) or (x==self.x and y==self.y):
                    continue
                if type(self.grid[y][x]) is Node:
                    self.neighbours.append(self.grid[y][x])



    def sendto(self,destx,desty,nodes,canvas):
        global Inf
        minimumIndex=0
        while True:
            minimumvalue=Inf
            for i in range(len(nodes)):
                if nodes[i].power<minimumvalue and not(nodes[i].visited):
                    minimumIndex=i
                    minimumvalue=nodes[i].power
            if minimumvalue==Inf:
                return nodes[minimumIndex]
            if nodes[minimumIndex].x== destx and nodes[minimumIndex].y== desty:
                nodes[minimumIndex].power=minimumvalue
                #canvas.itemconfig(nodes[minimumIndex].circle,fill="red")
                return nodes[minimumIndex]
            nodes[minimumIndex].calcpower(canvas)

    def calcpower(self,canvas):
        self.visited=True
        # if self.power==0:
        #     canvas.itemconfig(self.circle,fill="red")
        for neighbour in self.neighbours:
            if(self.power+1<neighbour.power):
                neighbour.power=self.power+1


    def print_neighbours(self):
        print((str(self.power) + ":"), end="")
        for j in self.neighbours:
            print ((str(j.power) + " "), end="")
        print()

