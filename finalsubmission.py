# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:52:42 2019

@author: Prateek Sharma
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:54:40 2019

@author: Prateek Sharma
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:37:26 2019

@author: Prateek Sharma
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:32:24 2019

@author: Prateek Sharma
"""

import tkinter
from tkinter import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

import time
import random
import sys
###############
#n=3
#dep=15
###############




################console###############
'''
print("select your options")
print("Option 1: Display the room environment")
print("Option 2: Find the path (action sequence) and path cost using T1")
print("Option 3: Find the path (action sequence) and path cost using T2")
print("Option 4: Show all results and graphs in the GUI.")
inp=int(input("enter :"))
'''
########################


##############################################






###############################
pathcost=0



#######  PREPROCESSING ################
#p=int(input("enter a number of dirt tiles::"))

def mainList(n):
    
    mainlist=[]

    for i in range(n*n):
        mainlist.append(0)
    
    mainlist.append(0)   
    mainlist.append(-1) 
    return mainlist
#mainlist=mainList()
############### END PREPROCESSING ########################



############### FUNCTIONS ####################
def DirtGenerator(mainlist,p):
    choices = list(range(n*n))
    random.shuffle(choices)
    #print(choices)

    for x in range(p):
        mainlist[choices[x]]=1
    return mainlist 
#lst=[]
#lst=DirtGenerator(mainlist,p)
#print(lst)

def GoalTest (lst):
    flag=0
    for i in range(n*n):
        if(lst[i]==1):
            flag=1
            break
    if(flag==1):
        return 0
    else:
        return 1
#explorelist=[0]*100
#explorelist[0]=1    

#sucking dust in first tile6   
#if(lst[0]==1):
#   lst[0]=0
def  nextState (lst, A):
    clst=[]
    clst=lst[:]
    ln=len(lst)+1
    lstp=lst[n*n+2:ln]
    if(A=='R' ):
        x=clst[n*n]+1
        if((clst[n*n]+1)%n==0 or x in lstp):
        
            clst[n*n]=-1
            clst.append(lst[n*n])
            
        else:
            clst[n*n]=clst[n*n]+1
            clst.append(lst[n*n])
            if(clst[clst[n*n]]==1):            
                clst[clst[n*n]]=0
            



    
    elif(A=='L'):
        
        x=lst[n*n]-1
        if((clst[n*n])%n==0 or x in lstp):
            clst[n*n]=-1
            clst.append(lst[n*n])


        else:
            clst[n*n]=clst[n*n]-1
            clst.append(lst[n*n])
            if(clst[clst[n*n]]==1):            
                clst[clst[n*n]]=0
            




    
    elif(A=='U'):
    
        x=lst[n*n]-n
        if((clst[n*n])<n or x in lstp):
            clst[n*n]=-1
            clst.append(lst[n*n])


        else:
            clst[n*n]=clst[n*n]-n
            clst.append(lst[n*n])
            if(clst[clst[n*n]]==1):            
                clst[clst[n*n]]=0
                

            


    
    elif(A=='D'):
    
        x=lst[n*n]+n
        if((clst[n*n])>=(n*n-n) or x in lstp):
            clst[n*n]=-1
            clst.append(lst[n*n])

     
        else:
            clst[n*n]=clst[n*n]+n
            clst.append(lst[n*n])
            if(clst[clst[n*n]]==1):            
                clst[clst[n*n]]=0



            
    return clst
################ END FUNCTIONS#######################3

#############################################
#print(lst)
#queue=[]
#startstate1=lst[:]
#queue.append(startstate1)
#goal=[]
#############################################3

################## FIUNCTIONS FOR IDFS ############3
dfs_nodes = [1]
def DFS(lt,depth):
    temp=[]
    temp = lt[:]

    if(temp[n*n]!=-1):
        if(GoalTest(temp)==1):
            goal.append(temp)
    
    l =nextState(temp,'L')
    tmp_n = dfs_nodes.pop()
    dfs_nodes.append(tmp_n+1)
    if l[n*n]!=-1 and not depth<=0 and len(goal)==0:
        
        

        DFS(l,depth-1)
    r = nextState(temp,'R')
    tmp_n = dfs_nodes.pop()
    dfs_nodes.append(tmp_n+1)
    if r[n*n]!=-1 and not depth<=0 and len(goal)==0:

        DFS(r,depth-1)
    u =  nextState(temp,'U')
    tmp_n = dfs_nodes.pop()
    dfs_nodes.append(tmp_n+1)
    if u[n*n]!=-1 and not depth<=0 and len(goal)==0:

        DFS(u,depth-1)
    d = nextState(temp,'D')
    tmp_n = dfs_nodes.pop()
    dfs_nodes.append(tmp_n+1)
    if d[n*n]!=-1 and not depth<=0 and len(goal)==0:

        DFS(d,depth-1)
def idfs(lst,dep,goal):
    k=0
    gstate=[]
    for i in range(dep):
        #gstate=[]
        DFS(lst,i)
        if(len(goal)!=0):
            gstate.append(goal[0])
            k=i
            break
    gstate.append([k])
    gstate.append(dfs_nodes)
    return gstate        
        
    
 ################################ END IDFS FUNCTIONS#############           
   ####################### BFS##################
def bfs(queue,n):
    k1=1
    k2=1
    g=[]
    while(queue):
        startstate=[]
        startstate=queue.pop(0)
        k1=k1-1
        
            
    
    
        if(GoalTest(startstate)==1):
            g.append(startstate)
            break
        else:
            if(startstate[n*n]!=-1):
                queue.append(nextState(startstate,'R'))
                k1=k1+1
                k2=k2+1
            if(startstate[n*n]!=-1):
                queue.append(nextState(startstate,'L'))
                k1=k1+1
                k2=k2+1
            if(startstate[n*n]!=-1):
                queue.append(nextState(startstate,'U'))
                k1=k1+1
                k2=k2+1
            if(startstate[n*n]!=-1):
                queue.append(nextState(startstate,'D'))
                k1=k1+1
                k2=k2+1
            

        startstate=None
    g.append([k1])
    g.append([k2])
        #startstate=None
    return g  
#############################################
        

############### LIST FOR PATH TRAVELLED ####################

def path(gstate,n):
     lst1=[]

     for i in range(n*n+2, len(gstate)) :
        lst1.append(gstate[i])
     lst1.append(gstate[n*n])
     return lst1
#lst1=path(gstate,n)  
#print(lst1)
'''  
lst1=[]
for i in range(n*n+2, len(gstate)) :
    lst1.append(gstate[i])
lst1.append(gstate[n*n])
'''    

################ END LIST #############################



####################################################



################## TKINTER ####################################################################3

#x=0
#y=0
#grd1=40
#size=n

#screen=tkinter.Tk()
#screen.configure(bg="black")


### CREATING CANVAS AND  GRID BOX ##############

#canvas=tkinter.Canvas(screen,width=2000, height=1000)
#canvas.config(background="white")

def gridbox(screen,x,y,size,gsize):
    g1=[[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            g1[i][j]=canvas.create_rectangle(x+j*gsize,y+i*gsize,x+gsize+j*gsize,y+gsize+gsize*i)
    return g1 

def gridbox1(screen,x,y,size,gsize):
    g1=[[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            g1[i][j]=canvas2.create_rectangle(x+j*gsize,y+i*gsize,x+gsize+j*gsize,y+gsize+gsize*i)
    return g1 

#if(inp==1):
#grd_1=gridbox(screen,x,y,size,grd1)       



###########################################3



######### CREATING  DIRT #################33
def dirtgui(lst,n,canvas):
    for i in range(n):
        for j in range(n):
            if(lst[i*n+j]==1):
                canvas.create_rectangle(j*grd1,i*grd1,grd1+j*grd1,grd1+i*grd1,fill = 'green')
#dirtgui(lst,n)
##############################################
def dirtgui1(lst,n,canvas):
    for i in range(n):
        for j in range(n):
            if(lst[i*n+j]==1):
                canvas.create_rectangle(size*grd2+20+j*grd2,i*grd2,grd2+size*grd2+20+j*grd2,grd2+i*grd2,fill = 'green')
                
                ##################


def createdirtenv(screen,x,y,size,grd1,lst,n,canvas):
    grd_1=gridbox(screen,x,y,size,grd1)       
    dirtgui(lst,n,canvas)
    canvas.pack()
    screen.mainloop()

    

    





###############
            
            
###############

#lst1=[0,1,4,7,8]


############# VACCUM CLEANER ################3
#o=canvas.create_oval(0,0,40,40,fill = 'red') 
###########################################################################################
#'''
#if(inp==1):
#canvas.pack()
#screen.mainloop()

#'''
##############  ACTIONS     ################
def rmov(o,g,screen,canvas):
    screen.update()
    time.sleep(1)
    canvas.move(o,g,0)
    
    screen.update()
def lmov(o,g,screen,canvas):
    screen.update()
    time.sleep(1)
    canvas.move(o,-g,0)
    screen.update()
def dmov(o,g,screen,canvas):
    screen.update()
    time.sleep(1)
    canvas.move(o,0,+g)
    screen.update()    
def umov(o,g,screen,canvas):
    screen.update()
    time.sleep(1)
    canvas.move(o,0,-g)
    screen.update()    
    
 #######################################  
    
#screen.update()  
#canvas.pack()
#mov(o,grd1) 
#if(lst[0]==1):
 #   canvas.create_rectangle(0,0,40,40,fill ="white")


###################### EXECUTING PATH FOR VACCUM CLEANER #############33 
def motion(lst1,o,screen,canvas,grd1,x,y,c): 
    for i in range(1,len(lst1)):
        if(lst1[i]-lst1[i-1]==1):
            rmov(o,grd1,screen,canvas) 
            canvas.create_line(x+(lst1[i-1]%size)*grd1 + grd1/2, y + (lst1[i-1]//size)*grd1 + grd1/2, x +(lst1[i]%size)*grd1 + grd1/2, y + (lst1[i]//size)*grd1 +grd1/2,fill=c)
        elif(lst1[i]-lst1[i-1]==-1):
            lmov(o,grd1,screen,canvas)    
            canvas.create_line(x+(lst1[i-1]%size)*grd1 + grd1/2, y + (lst1[i-1]//size)*grd1 + grd1/2, x +(lst1[i]%size)*grd1 + grd1/2, y + (lst1[i]//size)*grd1 +grd1/2,fill=c)

        elif(lst1[i]-lst1[i-1]==n):
            dmov(o,grd1,screen,canvas)    
            canvas.create_line(x+(lst1[i-1]%size)*grd1 + grd1/2, y + (lst1[i-1]//size)*grd1 + grd1/2, x +(lst1[i]%size)*grd1 + grd1/2, y + (lst1[i]//size)*grd1 +grd1/2,fill=c)

        elif(lst1[i]-lst1[i-1]==-n):
            umov(o,grd1,screen,canvas)
            canvas.create_line(x+(lst1[i-1]%size)*grd1 + grd1/2, y + (lst1[i-1]//size)*grd1 + grd1/2, x +(lst1[i]%size)*grd1 + grd1/2, y + (lst1[i]//size)*grd1 +grd1/2,fill=c)
            
    #time.sleep(2)
#motion(lst1)
'''
    if(lst[lst1[i]]==1 ):
        j=lst1[i]%3
        k=lst1[i]-j
        k=k/3            
       # canvas.create_rectangle(j*40,k*40,40+j*40,40+k*40,fill ="white")        
canvas.create_oval(j*40,k*40,40+j*40,40+k*40,fill ="red")
'''
#####################################################
def actionpath(lst1,dlst,n):
    apath=[]
    for i in range(len(lst1)):
        
        if(i==(len(lst1)-1)):
            if(dlst[lst1[i]]==1):
                apath.append('S')
        else: 
            if(dlst[lst1[i]]==1):
                apath.append('S')
            if((lst1[i+1]-lst1[i])==1):
                
                apath.append('R')
            if((lst1[i+1]-lst1[i])==-1):
                apath.append('L')
            if((lst1[i+1]-lst1[i])==n):
                apath.append('D')
            if((lst1[i+1]-lst1[i])==-n):
                apath.append('U')
            
             
    return apath         
def costpath(apath):
    cost=0
    for i in range(len(apath)):
        if(apath[i]=='S'):
            cost=cost+1
        else:
            cost=cost+2
    return cost        
#####################################################33
def writelist(lst,canvas,n,x,y,s):
    #s="R1:: "
   
    for i in range(len(lst)):
        s=s+lst[i]
        s=s+" "
   # l=2*len(s)
    #x=l+x    
        
        
    canvas.create_text(x,y,text=s,anchor="nw")

 ########################
      


#####################################3

#screen.mainloop()
################################END TKINTER#######################33
print("suggestions")
print("for a tile of side n, choose depth from n*(n-1) to n*n and n=<10")
print("examples")
print("for tile side 3,4 use depth=9 and depth=16 and dirt percentage upto 100")
print("for tile side 5 use depth=25  and dirt percentage upto 50")
print("for tile side 6 use depth=30  and dirt percentage upto 10")
print("for tile side 7,8,9  use depth=60-90  and dirt on 1 or 2 tiles")



print("select your options")
print("Option 1: Display the room environment")
print("Option 2: Find the path (action sequence) and path cost using T1")
print("Option 3: Find the path (action sequence) and path cost using T2")
print("Option 4: Show all results and graphs in the GUI.")
inp=int(input("enter the option (1 or 2 or3 or 4 )::"))
'''
n=e
p=int(input("enter a number of dirt tiles::"))
'''

n=int(input("enter n for n*n tile side length:"))
dep=int(input("depth for IDFS::"))
per=int(input("enter percentage of dirt tiles::"))
p1=(n*n*per)/100
p2=int(p1)
if(p1>p2):
    p=p2+1
else:
    p=p2    
#if(p==0):
 #   p=1
#print("p")
#print(p)
mainlist=mainList(n)
lst=[]
lst=DirtGenerator(mainlist,p)
dlst=lst[:]
if(lst[0]==1):
    lst[0]=0
queue=[]
startstate1=lst[:]
queue.append(startstate1)
goal=[]
t1dfs=time.time()
gstat=idfs(lst,dep,goal)
t2dfs=time.time()
timedfs=t2dfs-t1dfs
#print("timedfs")
#print(timedfs)

#print(timedfs)

#print("timedfs")

gstate=gstat[0][:]

t1bfs=time.time()
gstat1=bfs(queue,n)
t2bfs=time.time()
timebfs=t2bfs-t1bfs
#print(timebfs)
#print("timebfs")

gstate1=gstat1[0][:]

lst1=path(gstate,n)  
lst2=path(gstate1,n)

maxstackdfs=gstat[1][0]
maxquebfs=gstat1[1][0]
maxnodebfs=gstat1[2][0]

#print("maxquebfs")
#print(maxquebfs)

#print("maxnodebfs")

#print(maxstackdfs)


maxnodedfs=gstat[2][0]
#print("size")
nodemem=sys.getsizeof(lst)
#print(nodemem)
#print("dfsnode")
#print(dfsnodes)
if(maxquebfs>maxstackdfs):
    memdiff=maxquebfs*nodemem-maxstackdfs*nodemem
else:
    memdiff=maxstackdfs*nodemem-maxquebfs*nodemem
#print(memdiff)    
    

    

if(inp==2):
    apath=actionpath(lst1,dlst,n)
    print("Action path of Idfs:")
    print(apath)
    print("cost path of Idfs:")
    cost=costpath(apath)

    print(cost)    
if(inp==3):
    apath1=actionpath(lst2,dlst,n)
    print("Action path of Bfs:")
    print(apath1)
    print("cost path of Bfs:")
    cost1=costpath(apath1)

    print(cost1)    



 
    
x=0
y=0
grd1=35
size=n
grd2=35
x2=size*grd1+20
y2=0
'''
screen=tkinter.Tk()
canvas=tkinter.Canvas(screen,width=2000, height=1000)
canvas.config(background="white")
#createdirtenv(screen,x,y,size,grd1,lst,n)


grd_1=gridbox(screen,x,y,size,grd1)       
dirtgui(lst,n,canvas)
o=canvas.create_oval(0,0,40,40,fill = 'red') 
canvas.pack()

motion(lst1,o)
screen.mainloop()
'''
if(inp==1):
    screen=tkinter.Tk()
    canvas=tkinter.Canvas(screen,width=2000, height=1000)
    canvas.config(background="white")
    createdirtenv(screen,x,y,size,grd1,dlst,n,canvas)
    

      
   

if(inp==4):
    window = tkinter.Tk()
    window.geometry("1500x700")
    frame = tkinter.Frame(window)
    frame.pack(side = tkinter.RIGHT)
    frame1 = tkinter.Frame(window)
    frame1.pack(side = tkinter.TOP)
    frame2 = tkinter.Frame(window)
    frame2.pack(side = tkinter.LEFT)
    canvas1 = tkinter.Canvas(frame2, width = 600, height = 700 , bg = "lightgrey")
    canvas1.pack(side = tkinter.BOTTOM)
    canvas2 = tkinter.Canvas(frame, width = 800, height = 500,bg="lightgrey")
    canvas2.pack(side = tkinter.TOP)
    
    canvas2.create_text(10,600,text="GRAPH G3 FOR TIME(X) VS TILES(N*N)(Y)")
    idfstiles=[0.00099142536262,0.00099746453525,0.01563739776611328,0.06395888328552246
           ,0.05095481872558594,0.9681651592254639,2.5411579608917236]
    bfstiles=[0.000499938382727,0.0011928989819891,0.01634858685488888,0.05095505714416504
          ,0.042990922927856445,3.3687081336975098,14.630306720733643]
    tile=[3,4,5,6,7,8,9]
    
    idfsgraph2=[0.00412134349928,0.07190608978271484,0.03116011619567871,0.4870285987854004
            ,0.684995174407959,0.45858263969421387,1.9102814197540283,1.5366342067718506
            ,1.8237085342407227,3.8652753829956055,6.853026628494264,5.73137470600586,
            5.964636564254761,10.724948406219482,9.27123975753782,12.908725500106812,
            12.244277715682983,13.35518193244934]

    percentage=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]



    fig = Figure(figsize=(5, 2), dpi=100)
    t = np.arange(0, 3, .01)
    ax_1 = fig.add_subplot(121)
    ax_1.plot(tile, idfstiles)
    ax_1.plot(tile, bfstiles)
   

    ax_2 = fig.add_subplot(122)
    ax_2.plot(percentage, idfsgraph2)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    # canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
    apath=actionpath(lst1,dlst,n)
    apath1=actionpath(lst2,dlst,n)
    costdfs=costpath(apath)
    costbfs=costpath(apath)
    #print(apath)
   
   # o=canvas1.create_oval(0,0,grd1,grd1,fill = 'black')
####################################33
    tx=10
    ty=20
    s=30
    ss=30
    canvas1.create_text(tx,ty,text="CALCULATED VALUES FOR BFS",anchor="nw", fill='red',font=16)
    s1="R1::NUMBER OF NODES GENERATED IN BFS---"
    s1=s1+str(maxnodebfs)
    canvas1.create_text(tx,ty+s,text=s1,anchor="nw",fill='red')
    s2="R2::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"Bytes"
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red')
    s3="R3::MAXIMUM LENGTH OF QUEUE---"
    s3=s3+str(maxquebfs)
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s3,anchor="nw",fill='red')
    g1="G1::ACTION PATH---"
    ss=ss+s
    writelist(apath1,canvas1,n,tx,ty+ss,g1)
   #####################################3

    s4="R4:: COST OF BFS---"
    
    s4=s4+str(costbfs)
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s4,anchor="nw", fill='red')
    s5="R5::TIME OF BFS---"
    
    s5=s5+str(timebfs)
    s5=s5+" "
    s5=s5+"sec"
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s5,anchor="nw",fill='red')
    
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text="CALCULATED VALUES FOR IDFS",anchor="nw",fill='blue',font=16)

    s6="R6::MAXIMUM NODE GENERATED IN DFS---"
    s6=s6+str(maxnodedfs)
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s6,anchor="nw",fill='blue')
    s7="R7::MEMORY OF A NODE---"
    s7=s7+str(nodemem)
    s7=s7+" "
    s7=s7+"Bytes"
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s7,anchor="nw",fill='blue')
    s8="R8::MAXIMUM LENGTH OF STACK---"
    s8=s8+str(maxstackdfs)
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s8,anchor="nw",fill='blue')
    g2="G2::ACTION PATH OF IDFS---"
    ss=ss+s
    writelist(apath,canvas1,n,tx,ty+ss,g1)
   #####################################3

    s9="R9::COST OF IDFS---"
    
    s9=s9+str(costdfs)
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s9,anchor="nw",fill='blue')
    s10="R10::TIME OF IDFS---"
    
    s10=s10+str(timedfs)
    s10=s10+" "
    s10=s10+"sec"
    ss=ss+s
    canvas1.create_text(tx,ty+ss,text=s10,anchor="nw",fill='blue')
    
    s11="R11::MEMORY CONSUMED BY IDFS-MEMORY CONSUMED BY BFS(MEMORY DIFFERENCE) ---"
 
    s11=s11+str(memdiff)
    s11=s11+" "
    s11=s11+"Bytes"
    ss=ss+s
    
    canvas1.create_text(tx,ty+ss,text=s11,anchor="nw")
    ss=ss+s

    canvas1.create_text(tx,ty+ss,text="right side first grapgh G3",anchor="nw")
    ss=ss+s

    canvas1.create_text(tx,ty+ss,text="right side second graph G4",anchor="nw")

  
    #s="R1::"
    #writelist(maxnodebfs,canvas1,n,tx,ty+20,s)
   #####################################3
    grd_1=gridbox1(window,x,y,size,grd1) 
    grd_2=gridbox1(window,x2,y2,size,grd2)

    dirtgui(dlst,n,canvas2)
    dirtgui1(dlst,n,canvas2)
    #canvas2.create_text(10,(n+1)*grd1,text="IDS")
    canvas2.create_text(10,(n+1)*grd1,font=16,text="IDS",fill='blue',anchor="nw")

    canvas2.create_text(10+x2,(n+1)*grd1,font=16,text="BFS",fill='red',anchor="nw")

    o=canvas2.create_oval(0,0,grd1,grd1,fill = 'black')

    
    motion(lst1,o,window,canvas2,grd1,x,y,'blue')

   # grd_2=gridbox1(window,x2,y2,size,grd2)
    
    #dirtgui1(lst,n,canvas2)

    o1=canvas2.create_oval(x2+0,0,x2+grd1,grd1,fill = 'black') 

    motion(lst2,o1,window,canvas2,grd2,x2,y2,'red')
    tkinter.mainloop()
'''
    fig = Figure(figsize=(5, 2), dpi=100)
    t = np.arange(0, 3, .01)
    ax_1 = fig.add_subplot(121)
    ax_1.plot(t, 2 * np.sin(2 * np.pi * t))
    ax_2 = fig.add_subplot(122)
    ax_2.plot(t, 2 * np.sin(2 * np.pi * t))
    canvas = FigureCanvasTkAgg(fig, master=frame)
    # canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)
'''




   # tkinter.mainloop()
