#------------IMPLEMENTATION OF INTELLIGENT WATER DROP ALGORITHM---------------------#

#Reference:  https://pdfs.semanticscholar.org/9d61/b5d40f561a08657e75350c58a0e842be00c7.pdf

N= [4,5,6,7]#set of nodes from user
E= [(4,5),(5,7),(7,6),(5,4)]#set of edges from user

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

def initializeIWD(Niwd,iniVel,iniSoil):
    iwd={} #it will hold key as the iwd and its value as a list in the form [soil,velocity,visited]
    for i in range(Niwd):
            
            val=[]
            val.append(0)
            val.append(iniVel)          # velocity is set to Initial Velocity. All IWDs are set to have zero amount of soil. 

            visited=[]
            visit=random.choice(list(graph.keys())) #Step 3  (Spread the IWDs randomly on the nodes of the graph as their first visited nodes)
            visited.append(visit) #Step 4   (Update the visited node list of each IWD to include the nodes just visited)
            val.append(visited)

            iwd[i]=val
    return(iwd)
    

            
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
    


graph=adjlist(N,E) #unweighted, undirected
def IWD(graph):
    soil={} #soil on path from some node to another
    
    #Step 1
    Ttb= -999         #total best solution set to worst value
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
    itermax=3

    highest=0

    lst=list(graph.keys())
    for node in (graph):
        soil[node]={}
        for j in graph[node]:
            soil[node][j]=iniSoil
        target=soil[node]
        for neighbour in graph:
            if neighbour not in target:
                soil[node][neighbour]=0


    while itercount<itermax:
        iwd=initializeIWD(Niwd,iniVel,iniSoil) #Step 2
        quality = []
        probability = {}
        for i in range(Niwd):
            target=iwd[i]
            while len(target[2]) < Niwd:
                node_j = False
                # Step 5.1 
                node=lst[i]
                for j in graph[node]:
                    if j not in target[2]:
                        probability[j] = probabilityJ(target[2], lst[i], j, soil) 
                        # add newly visited node j to visited
                        target[2].append(j)
                        iwd[i]=target
                        
                    
                random_number=random.random()
                probability_sum=0
                for k in probability:       #this loop is verifying that the selected node j satisfy all constraints of the problem. It varies from problem to problem. Here we have taken a dummy constraint.   
                    if probability_sum > 1:
                        node_j = False
                        break
                    if random_number > probability_sum and random_number < probability_sum+probability[k]: 
                        node_j = True
                        j=k
                        break
                    probability_sum = probability_sum + probability[k] 
                        
                if node_j == True:
                     # Step 5.2 
                        temp=iwd[i]
                        for ind in range(len(iwd[i])):
                                if ind==2:
                                        temp[2]=target[2]
                                elif ind==1:
                                        u_v = temp[1] + av / (bv + cv * soil[lst[i]][j] ** 2)   #u_v = updated velocity 
                                        temp[1]=u_v
                                else:
                                        # Step 5.3 
                                        ds = asoil/(bsoil + csoil * time(i,j,temp[1],HUD(lst[i],j,soil)) ** 2)         #ds = delta soil 
                                        # Step 5.4 
                                        soil[lst[i]][j] = (1 - pn) * soil[lst[i]][j] - pn * ds
                                        temp[0] =  temp[0] + ds            
                        iwd[i]=temp
                        
            quality.append(q(temp[2],soil))
            
    # Step 6  
        best_qual = max(quality)
        location=quality.index(best_qual)
    # Step 7
        target=iwd[location]
        visit=target[2]
        i=visit[len(visit)-1]
        for j in visit:
            soil[i][j]=(1+piwd)*soil[i][j]-piwd*(1/(Niwd-1))*target[0]
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
    print(result)
    #Step 10
    return(result)

            #---------------------The End Of Algorithm--------------------------------#
            
        
print(IWD(graph))        
