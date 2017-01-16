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

    def fillneighbour(self,x,y,dist=20):
        if(x<0 or x>=len(self.grid[0]) or y<0 or y>=len(self.grid)):
            return
        coverage = pow((pow(abs(x - self.x), 2) + pow(abs(y - self.y), 2)), 0.5)

        if(coverage>dist):
            return
        if(self.visited[y][x]):
            return
        self.visited[y][x]=True

        if type(self.grid[y][x]) is Node:
            self.neighbours.append(self.grid[y][x])
            self.grid[y][x].neighbours.append(self)
        self.fillneighbour(x + 1, y,dist)
        self.fillneighbour(x - 1, y,dist)
        self.fillneighbour(x, y + 1,dist)
        self.fillneighbour(x, y - 1,dist)
        self.fillneighbour(x-1, y - 1, dist)
        self.fillneighbour(x-1, y + 1, dist)
        self.fillneighbour(x+1, y - 1, dist)
        self.fillneighbour(x+1, y + 1, dist)
        self.visited[y][x]=False
        return

    def fillneighbourloop(self,radius=20):

        for y in range((self.y-int(radius)),self.y+int(radius)+1):
            if y <0 or y>=len(self.grid):
                continue
            if(pow(radius,2)-pow(y-self.y,2)<0):
                holymoly=True
            horiz=int(pow(pow(radius,2)-pow(y-self.y,2),0.5)+self.x)
            for x in range(self.x-(horiz-self.x),horiz+1):
                if x<0 or x>=len(self.grid[y]) or (x==self.x and y==self.y):
                    continue
                if type(self.grid[y][x]) is Node:
                    self.neighbours.append(self.grid[y][x])


    def fillneighbours2(self,currx,curry,dist=2):
        boolreturn =False
        if(currx==1 and curry==3):
            boolreturn=False
        if(currx<0 or currx>=len(self.grid[0]) or curry<0 or curry>=len(self.grid) or (currx==self.x and curry== self.y)):
            return

        if (currx == self.x)  or (curry==self.y):
            if(currx==self.x):
                coverage=abs(curry-self.y)
            else:
                coverage=abs(currx-self.x)
        else:
            coverage= pow((pow(abs(currx-self.x),2)+pow(abs(curry-self.y),2)),0.5)

        if(coverage>dist):
            return None

        if(type(self.grid[curry][currx])is Node):
            if self.grid[curry][currx] not in self.neighbours:
                self.neighbours.append(self.grid[curry][currx])

            else:
                 return

        else:
            if self.grid[curry][currx]==1:
                return
            else:
                self.grid[curry][currx]=1

        self.fillneighbours2(currx + 1, curry,dist)
        self.fillneighbours2(currx - 1, curry,dist)
        self.fillneighbours2(currx, curry + 1,dist)
        self.fillneighbours2(currx, curry - 1,dist)
        self.fillneighbours2(currx-1, curry - 1, dist)
        self.fillneighbours2(currx-1, curry + 1, dist)
        self.fillneighbours2(currx+1, curry - 1, dist)
        self.fillneighbours2(currx+1, curry + 1, dist)

        if type (self.grid[curry][currx]) is int:
            self.grid[curry][currx]=0
        return

    # def sendtoNode(self,destx,desty):
    #     shortest=9999999999999999
    #     if self.x==destx and self.y==desty:
    #         return 0
    #     else:
    #         if self.sent:
    #             return 9999999999999999
    #         self.sent=True
    #         for neighbour in self.neighbours:
    #             if(neighbour.shortestpath==-1):
    #                 pathlength= neighbour.sendtoNode(destx,desty)
    #             else:
    #                 pathlength=neighbour.shortestpath
    #
    #             if pathlength<shortest:
    #                 shortest=pathlength
    #
    #         self.sent = False
    #         self.shortestpath=1+shortest
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

