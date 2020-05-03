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
            val.append(iniVel)          # velocity is set to Initial Velocity. All IWDs are set to have zero amount of soil. 

            visited=[]
            visit=random.choice(graph.keys()) #Step 3  (Spread the IWDs randomly on the nodes of the graph as their first visited nodes)
            visited.append(visit) #Step 4   (Update the visited node list of each IWD to include the nodes just visited)
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
    """Initialisation of static parameters. The graph (N, E) of
    the problem is given to the algorithm. The quality of the
    total-best solution TTB is initially set to the worst value:
    ( ) TB q T = −∞ . The maximum number of iterations
    itermax is specified by the user. The iteration count
    itercount is set to zero.
    The number of water drops NIWD is set to a positive
    integer value, which is usually set to the number of
    nodes Nc of the graph.
    For velocity updating, the parameters are 1 v a = ,
    .01 v b = and 1 v c = . For soil updating, 1 s a = , .01 s b =
    and 1 s c = . The local soil updating parameter ρn ,
    which is a small positive number less than one, is set as 
    ρn = . The global soil updating parameter ρ IWD ,
    which is chosen from [0, 1], is set as 0.9 ρ IWD = .
    Moreover, the initial soil on each path (edge) is denoted
    by the constant InitSoil such that the soil of the path
    between every two nodes i and j is set by
    soil i j InitSoil (, ) = . The initial velocity of each IWD is
    set to InitVel. Both parameters InitSoil and InitVel are
    user selected and they should be tuned experimentally
    for the application. Here, InitSoil = 10000 and
    InitVel = 200. For the IWD-MKP, InitVel = 4 is used,
    which is the same value used in Shah-Hosseini (2008)"""
    #Step 1
    Ttb= -1000000000000000000000000000000           #total best solution set to worst value
    Niwd=len(graph)                                 #number of water drops
    
    av=1                #velocity parameters a, b, c
    bv=0.01
    cv=1
    
    asoil=1             #soil parameters a, b, c
    bsoil=0.01
    csoil=1
    
    pn=0.9          #local soil parameter is set to less than 1
    piwd=0.9            #global soil parameter
    
    iniSoil=10000       #initial soil
    iniVel=200      #intial velocity 

    itercount=0             #iteration count is set to zero
    itermax=1000
    
   for iwd in range(len(graph)):
        soil[iwd]={}
        for j in graph[iwd]:
            soil[iwd][j]=iniSoil

    while itercount<itermax:
        """Initialisation of dynamic parameters. Every IWD has a
        visited node list ( ) V IWD c , which is initially empty:
        V IWD c ( ) = { } . Each IWD’s velocity is set to InitVel.
        All IWDs are set to have zero amount of soil."""
        iwd=initializeIWD(Niwd) #Step 2
        for i in range(Niwd):
            
