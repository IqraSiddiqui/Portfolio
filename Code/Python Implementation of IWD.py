
#------------IMPLEMENTATION OF INTELLIGENT WATER DROP ALGORITHM---------------------#

#Reference:  https://pdfs.semanticscholar.org/9d61/b5d40f561a08657e75350c58a0e842be00c7.pdf


import random
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

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
#helper functions for IWD:
def initializeIWD(Niwd,iniVel,iniSoil):
    soiliwd={}
    visitiwd={}
    veliwd={}
    lst=list(graph.keys())
    for i in range(Niwd):
            soiliwd[i]=iniSoil      #All IWDs are set to have Initial Soil which is 0. 
            veliwd[i]=iniVel    # velocity is set to Initial Velocity.          

            visited=[]
            visit=lst[i] #Step 3  (Spread the IWDs randomly on the nodes of the graph as their first visited nodes)
            visited.append(visit)
            visitiwd[i]=visited #Step 4   (Update the visited node list of each IWD to include the nodes just visited)
    
    return(soiliwd,visitiwd,veliwd)
            
def g_soil(i,j,visited,soil):
    mini=1000000000000000000000000000000
    for l in graph:
        if l not in visited:
            if soil[i][l]<mini:
                mini=soil[i][l]
    if mini>=0:
        return(soil[i][l])
    else:
        return(soil[i][l]-mini)
    
def f_soil(i,j,visited,soil):
    epsilon_s= 0.0001
    return(1/(epsilon_s+g_soil(i,j,visited,soil)))

def probabilityJ(visited,i,j,soil):
    sigma_i_k=0
    for k in graph:
        if k not in visited:
            sigma_i_k = sigma_i_k + f_soil(i,k,visited,soil)
    return(f_soil(i,j,visited,soil)/sigma_i_k)
    

def HUD(i,node_j,soil):
    HUD = soil[i][node_j]  #more the soil on a path, greater is the heuristic undersirability i.e. HUD. HUD varies from problem to problem. For example in solving TSP the HUD can be taken as distance. 
    return HUD   

def time(i,j,vel,HUD):
    	return HUD/vel 

def q(visited,soil):
    total=0
    pre=visited[len(visited)-1]
    for node in visited:
        now=node
        total=total+soil[pre][now]
        pre=now
    return(1/total)    


#---------------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------------    

#------------------------------------------------------------------------------
#    IMPLEMENTATION with input as UN-WEIGHTED graph
#------------------------------------------------------------------------------

graph=adjlist(N,E) #unweighted, undirected
def iwd(graph):
    soil={} #soil on path from some node to another
    
    #Step 1
    #Ttb= -999         total best solution set to worst value
    Niwd=len(graph)                                 #number of water drops
    
##    av=1                #velocity parameters a, b, c
##    bv=0.01
##    cv=1
    
##    asoil=1             #soil parameters a, b, c
##    bsoil=0.01
##    csoil=1
    
##    pn=0.9          #local soil parameter is set to less than 1
##    piwd=0.9            #global soil parameter
    
    iniSoil=10000       #initial soil
    iniVel=200      #intial velocity


    itercount=0             #iteration count is set to zero
    itermax=1000

    highest=0

    lst=list(graph.keys())
    for node in (graph):
        soil[node]={}
        for neighbour in graph:
            if neighbour in graph[node]:
                soil[node][neighbour]=iniSoil
            else:
                soil[node][neighbour]=0
    
    while itercount<itermax:
        soiliwd,visitiwd,veliwd=initializeIWD(Niwd,iniVel,iniSoil) #Step 2
       
        quality = []
        probability = {}
        
        for i in range(Niwd):
           

            node_j = False
            # Step 5.1 
            node=lst[i]
            for j in graph[node]:
                if j not in visitiwd[i]:
                    probability[j] = int(probabilityJ(visitiwd[i], lst[i], j, soil))
                    
                    temp=visitiwd[i]
                    temp.append(j)
                    visitiwd[i]=temp  # add newly visited node j to visited

            random_number=random.random()
            probability_sum=0
            
            for k in probability:       #this loop is verifying that the selected node j satisfy all constraints of the problem. It varies from problem to problem. Here we have taken a dummy constraint.   
                if random_number > probability_sum and random_number < probability_sum+probability[k]: 
                    node_j = True
                    j=k
                    break
                else:
                    node_j=False
                probability_sum = probability_sum + probability[k]


            # Step 5.2 
            u_v = veliwd[i] + 1 / (0.01 + 1 * soil[lst[i]][j] ** 2)   #u_v = updated velocity 
            veliwd[i]=u_v

            # Step 5.3 
            ds = 1/(0.01 + 1 * time(i,j,veliwd[i],HUD(lst[i],j,soil)) ** 2)         #ds = delta soil 
            # Step 5.4 
            soil[lst[i]][j] = (1 - 0.9) * soil[lst[i]][j] - 0.9 * ds
            soiliwd[i] =  soiliwd[i] + ds                 #updated soil                   
            quality.append(q(visitiwd[i],soil))

            
    # Step 6  
        best_qual = max(quality)
        location=quality.index(best_qual)
    # Step 7
        visit=visitiwd[location]
        i=visit[len(visit)-1]
        for j in visit:
            soil[i][j]=(1+0.9)*soil[i][j]-0.9*(1/(Niwd-1))*soiliwd[location]
            i=j
    # Step 8
        if highest>best_qual:
            pass
        else:
            Ttb=visit
            highest=best_qual
    # Step 9
        itercount=itercount+1

    result=[Ttb,highest]

    #Step 10
    return(result)

            #---------------------The End Of Algorithm--------------------------------#
            
        
##            
##N= [4,5,6,7]#set of nodes from user
##E= [(4,5),(5,7),(7,6),(5,4)]#set of edges from user
##graph=adjlist(N,E) #unweighted
#print(iwd(graph))


#------------------------------------------------------------------------------
#    IMPLEMENTATION with input as WEIGHTED graph
#------------------------------------------------------------------------------

def HUD_weight(i,node_j,weight):
    HUD = weight[i][node_j]  #HUD is taken equal to the weight of the path
    return HUD
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------


def iwd_weighted(graph):
    soil={} #soil on path from some node to another
    weight={}
    #Step 1
    Ttb= -999         #total best solution set to worst value
    Niwd=len(graph)    #number of water drops
    
##    av=1                #velocity parameters a, b, c
##    bv=0.01
##    cv=1
    
##    asoil=1             #soil parameters a, b, c
##    bsoil=0.01
##    csoil=1
    
##    pn=0.9          #local soil parameter is set to less than 1
##    piwd=0.9            #global soil parameter
    
    iniSoil=10000       #initial soil
    iniVel=200      #intial velocity


    itercount=0             #iteration count is set to zero
    itermax=1000

    highest=0       #highest quality is set to 0

    lst=list(graph.keys())
    for node in graph:
        soil[node]={}
        weight[node]={}
        target=graph[node]
        for pair in target:
            weight[node][pair[0]]=pair[1]
            soil[node][pair[0]]=iniSoil

    for node in weight:
        for neighbour in lst:
            if neighbour not in weight[node]:
                weight[node][neighbour]=0
            if neighbour not in soil[node]:
                soil[node][neighbour]=0
    
                
    while itercount<itermax:
        soiliwd,visitiwd,veliwd=initializeIWD(Niwd,iniVel,iniSoil) #Step 2
       
        quality = []
        probability = {}
        
        for i in range(Niwd):
            node_j = False
            # Step 5.1 
            node=lst[i]
            target=graph[node]
            neighbour=[]
            for pair in target:
                neighbour.append(pair[0])
            for j in neighbour:
                if j not in visitiwd[i]:
                    probability[j] = int(probabilityJ(visitiwd[i], lst[i], j, soil)) #deducing the probability of j and storing it as a value of key j 
                    temp=visitiwd[i]
                    temp.append(j)
                    visitiwd[i]=temp  # adding newly visited node j to visited

            random_number=random.random()
            probability_sum=0
            
            for k in probability:       #this loop is verifying that the selected node j satisfy all constraints of the problem. It varies from problem to problem. Here we have taken a dummy constraint which j should satisfy in order to be selected.   
                if random_number > probability_sum and random_number < probability_sum+probability[k]: 
                    node_j = True
                    j=k
                    break
                else:
                    node_j=False
                probability_sum = probability_sum + probability[k]


            # Step 5.2 
            uv = veliwd[i] + 1 / (0.01 + 1 * soil[lst[i]][j] ** 2)   #uv = updated velocity 
            veliwd[i]=uv

            # Step 5.3 
            ds = 1/(0.01 + 1 * time(i,j,veliwd[i],HUD_weight(lst[i],j,soil)) ** 2)         #ds = delta soil 
            # Step 5.4 
            soil[lst[i]][j] = (1 - 0.9) * soil[lst[i]][j] - 0.9 * ds
            soiliwd[i] =  soiliwd[i] + ds                 #updated soil                   
            quality.append(q(visitiwd[i],soil))        #evaluating quality by q and storing it.

            
    # Step 6  
        best_qual = max(quality) #best quality of the iteartion is the maximum quality of that iteration
        location=quality.index(best_qual)
    # Step 7
        visit=visitiwd[location]
        i=visit[len(visit)-1]
        for j in visit:
            soil[i][j]=(1+0.9)*soil[i][j]-0.9*(1/(Niwd-1))*soiliwd[location]  #updating soil value of that iwd which is responsible for the best_qual
            i=j
    # Step 8
        if highest>best_qual:
            pass
        else:
            Ttb=visit
            highest=best_qual
    # Step 9
        itercount=itercount+1

    result=[Ttb,highest]

    # Step 10
    return(result)

            #---------------------The End Of Algorithm--------------------------------#

##graph={'A':[('B',5),("C",2)],'B':[('C',6),('A',5)],'C':[('A',2),('B',6)]} #undirected
##print(iwd_weighted(graph))


 

        
    

    
 					
    
          
