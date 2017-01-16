
from grid import *
import random
from Tkinter import*
nodes=[]
GridSizeY=100
GridSizeX=100
Range=20
root = Tk()
canvas=Canvas(root,width=500,height=600)
powercount=0
class WorkSpace:
    def GUI(self):


        canvas.pack()
        scale=4
        global Range
        for node in nodes:
            circle=canvas.create_oval(node.x*scale,node.y*scale,node.x*scale+10,node.y*scale+10,fill="green")
            node.circle=circle
            range_indicator=canvas.create_oval((node.x-Range)*scale,(node.y-Range)*scale,(node.x+Range)*scale+10,(node.y+Range)*scale+10)

            circle=canvas.create_oval(10,500,20,510,fill="red")
            canvas.create_text(50,505,text="Source")
            circle = canvas.create_oval(10, 520, 20, 530, fill="green")
            canvas.create_text(60, 525, text=" Destination")
            circle = canvas.create_oval(10, 540, 20, 550, fill="yellow")
            canvas.create_text(45, 545, text="Path")

    def fillchoiceArray(self,array,nodes_no,gridsize):
        for i in range(nodes_no):
            array.append(1)
        for i in range(int(gridsize-nodes_no)):
            array.append(0)
    def insertnodes(self,mygrid):
        grid=mygrid
        mygrid=mygrid.grid
        nodes_no=int(input("enter the number of Nodes"))
        choiceArray=[]
        nodescount=0
        global GridSizeX
        global GridSizeY
        gridsize=GridSizeX*GridSizeY
        self.fillchoiceArray(choiceArray,nodes_no,gridsize)
        for y in range(len(mygrid)):
            for x in range(len(mygrid[0])):
                rand = random.choice(choiceArray)
                if rand and nodescount<nodes_no:
                    nodescount+=1
                    choiceArray.pop(0)
                    temp_node = Node(grid,y,x)
                    global nodes
                    nodes.append(temp_node)
                    mygrid[y][x]=temp_node
                    del temp_node
                else:
                    choiceArray.pop(len(choiceArray)-1)
                    mygrid[y][x]=0
                    # TODO fill Neighbours
    def insertnodesmanually(self,mygrid):
        temp=mygrid
        mygrid=mygrid.grid
        for y in range(len(mygrid)):
            for x in range(len(mygrid[0])):
                pow=input()
                if int(pow):
                    temp_node=Node(temp,y,x)
                    global nodes
                    nodes.append(temp_node)
                    mygrid[y][x]=temp_node
                    del temp_node
                else:
                    mygrid[y][x]=0
    def __init__(self):
        global GridSizeX
        global GridSizeY
        self.mygrid= Gridd(GridSizeY,GridSizeX)
        self.insertnodes(self.mygrid)
        #self.mygrid.printgrid()
        for i in nodes:

            i.fillneighbourloop(Range)
            #i.print_neighbours()                                           #print neighbours
        self.GUI()
        for i in range(0,1000) :
            for node in nodes:
                node.power=Inf
                node.visited=False
                canvas.itemconfig(node.circle,fill="blue")
            src=random.randint(0, len(nodes)-1)
            while True:
                recv=random.randint(0,len(nodes)-1)
                if not(recv==src):
                    break
            src_node=nodes[src]
            recv_node=nodes[recv]

            # srcx=int(input())
            # srcy=int(input())
            # destx=int(input())
            # desty=int(input())
            # src_node=self.mygrid.grid[srcy][srcx]
            # recv_node=self.mygrid.grid[desty][destx]
            src_node.power=0
            path=nodes[src].sendto(nodes[recv].x,nodes[recv].y,nodes,canvas)
           # self.mygrid.printgrid_transmission(src_node.x,src_node.y,recv_node.x,recv_node.y)
            print ">>>>"+str(path.power)
            finalnode=path

            if(finalnode.power<Inf):
                global powercount
                powercount+=(finalnode.power*2)
                canvas.itemconfig(finalnode.circle,fill="yellow")
                while not (finalnode.power==0):

                    for node in finalnode.neighbours:
                        if(node.power== finalnode.power-1):
                            if(node.power==0):
                                finalnode = node
                                break
                            canvas.itemconfig(node.circle,fill="yellow")
                            finalnode=node
                #canvas.itemconfig(finalnode.circle,fill= "red")

            end="end"

        canvas.itemconfig(src_node.circle, fill="red")
        canvas.itemconfig(recv_node.circle, fill="green")
        print "The Average Power = "+str(powercount/1000)
        root.mainloop()
