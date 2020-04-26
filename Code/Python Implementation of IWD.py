#------------IMPLEMENTATION OF INTELLIGENT WATER DROP ALGORITHM---------------------#

#Reference:  https://pdfs.semanticscholar.org/9d61/b5d40f561a08657e75350c58a0e842be00c7.pdf

N= #set of nodes from user
E= #set of edges from user

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


def soil(i,j):
    pass
    
    




graph=adjlist(N,E) 
def IWD(graph):
    temp={} #a temperoray dictionary having key as iwd and value as the visited node list of each iwd
    
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
    
    for i in range(len(graph)):
        #Step 2
        visited=[] 
        Soil=0
        Vel=iniVel
        #Step 3
        lst=list(graph.keys())
        #Step 4
        visited.append(lst[i])
        temp[i]=visited

    #Step 5.1

    
    
        

    

    
        

        
 
        
        
            
        
        
        
        
