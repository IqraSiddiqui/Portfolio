#------------IMPLEMENTATION OF INTELLIGENT WATER DROP ALGORITHM---------------------#

#Reference:  https://pdfs.semanticscholar.org/9d61/b5d40f561a08657e75350c58a0e842be00c7.pdf

N= #set of nodes from user
E= #set of edges from user

import random
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#helper functions:
def addNodes(G, nodes):
    for i in nodes:
        G[i]=[]
    return(G)
def addEdges(G, edges, directed):
    if directed==False:
        for i in G:
            ans=[]
            for j in edges:
                if j[0]==i:
                    ans.append(j[1])
                elif j[1]==i:
                    ans.append(j[0])
            G[i]=ans
    else:
        for i in G:
            ans=[]
            for j in edges:
                if j[0]==i:
                    ans.append(j[1])
            G[i]=ans
    return(G)

def adjlist(V,E):
    G={}
    addNodes(G, V)
    addEdges(G,E,False)
    return(G)
#---------------------------------------------------------------------------------        
#---------------------------------------------------------------------------------

def initializeIWD(Niwd):
    iwd={} #it will hold key as the iwd and its value as a list in the form [soil,velocity,visited]
    for i in range(Niwd):
            
            val=[]
            val.append(0)
            val.append(iniVel)

            visited=[]
            visit=random.choice(graph.keys()) #Step 3
            visited.append(visit) #Step 4
            val.append(visited)

            iwd[i]=val
    return(iwd)
    

def probabilityJ(i,j,temp[i],soil):
    sigma_i_k=0
    for k in graph:
        if k not in temp[i]:
            sigma_i_k = sigma_i_k + f_soil(i,k,temp[i],soil)
    return(f_soil(i,j,temp[i],soil)/sigma_i_k)
            
            
def g_soil(i,j,temp[i],soil):
    mini=1000000000000000000000000000000
    for l in graph:
        if l not in temp[i]:
            if soil[i][l]<mini:
                mini=soil[i][l]
    if mini>=0:
        return(soil[i][l])
    else:
        return(soil[i][l]-mini)
    
def f_soil(i,j,temp[i],soil):
    epsilon_s= 0.0001
    return(1/(epsilon_s+g_soil(i,j,temp[i],soil)))

def HUD(graph):
    return

#----------------------------------------------------------------------------------------------------    
    


graph=adjlist(N,E) 
def IWD(graph):
    soil={} #soil on path from some node to another

    #Step 1
    Ttb= -1000000000000000000000000000000
    Niwd=len(graph)
    
    av=1
    bv=0.01
    cv=1
    
    asoil=1
    bsoil=0.01
    csoil=1
    
    pn=0.9
    piwd=0.9
    
    iniSoil=10000
    iniVel=200

    itercount=0
    itermax=1000
    
   for iwd in range(len(graph)):
        soil[iwd]={}
        for j in graph[iwd]:
            soil[iwd][j]=iniSoil

    while itercount<itermax:
        iwd=initializeIWD(Niwd) #Step 2
        for i in range(Niwd):
            
