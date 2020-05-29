#------------------------------------------------------------------------------
#    IMPLEMENTATION WITH INPUT AS UN-WEIGHTED graph
#------------------------------------------------------------------------------

#graph=adjlist(N,E) #unweighted, undirected, adjency list representation of graph
def IWD(graph):
    soil={} #soil on path from some node to another
    
    #Step 1
    #Ttb= -999         total best solution set to worst value
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
            ds = 1/(0.01 + 1 * time(i,j,veliwd[i],HUD(lst[i],j,soil)) ** 2)         #ds = delta soil 
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
            
        
#print(iwd(graph))
