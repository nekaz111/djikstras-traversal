#Jeremiah Hsieh ICSI 502 Dijkstra's implementation
#class implementation useses binary heap and adjacency list for dijkstras
#current implementation uses adjacency list so probably not as efficient as it could be
#also currently does not store actual shortest path data, just distance data

import random
import math
import time

#generates adjacency list data
#list index number is corresponding node number
#values stored in index are adjacent nodes and their weight
#use 2d list?
#currently use basic numerical node representation (ie. vertex 0, vertex 1, etc.)
#not guarenteed to be complete graph (all nodes connected)
def genData(size):
    nodes = []
    #loop until graph designated size
    for x in range(size):
        #append another list to node
        edges = []
        for y in range(size):
            if x != y:
                #randomly decide if another node should be considered connected
                #make it so weight of x -> y != y -> x for now?
                #or maybe make it bidirecetional?
                if random.randint (0, 1) == 1 and abs(x - y) < 10:
#                    nodes.append((str(y), random.randint(1, 25)))
                    #add value to list
                    edges.append((y, random.randint(1, 20)))
        #add edge list to node list
        nodes.append(edges)
    return nodes


#dijkstra function
#shortest distance from 1 node to every other node
#1. pick starting node
#2. set 0 vertex cost for start, infinity for others
#3. look at adjacent vertex, change adjacent vertex values to current node weight + edge weight
#4. greedy traversal by going to smallest edge of vertex not yet chosen
#5. repeat 3 and 4 until all nodes have been visited
#currently finds distance to any point from 1 point, but doesn't store the path to reach it
def mydijkstras(graph, start):
    #stores visited nodes
    visited = []
    #current node
    current = start
    #make binary heap tree to track node traversal that that shortest paths can be stored (?)
    
    #stores current node costs from start to node
    #totalcaost[8] doesn't work since python doesn't initialize arrays in the same manner since they are not static like in c
    totalcost = [math.inf for x in range(len(graph))]
    #starting node cost is 0
    totalcost[start] = 0
    #stores paths that not have been traversed yet (for min comparisan purposes)
    untraversed = []
    #stores the actual path taken (so that shortest path can be extracted)
    traversepath = []
    #loop until every node has been visited
    while len(visited) < len(graph):
        #store shortest edge from current node
        shortest = (0, 0, math.inf)
        
        #add current node to visited list
        visited.append(current)
        #access current node adjacency data
        for iterx, x in enumerate(graph[current]):
            #overwrite adjacent node cost if current weight + edge weight is less
            if x[1] + totalcost[current] < totalcost[x[0]]:
                totalcost[x[0]] = x[1] + totalcost[current]
            #store current shortest path to traverse at the end of loop (as long as it hasn't already been traversed)
            #currently this only gets shortest node from current node
            #dijkstras compared shortest node in entire traversed tree
            if x[0] not in visited:
#                untraversed.append((current, *x))
                untraversed.append((current, x[0], totalcost[x[0]]))
        #if shortest is still (0, math.inf) then that means that all 
        #lazy compare stored paths
        #remove any nodes already visited
#        print(untraversed)
        untraversed = [y for y in untraversed if y[1] not in visited]
        #get shortest path out of all untraversed nodes
        for z in untraversed:
            if z[2] < shortest[2]:
                shortest = z
        #traverse shortest edge and make that node current node
        #shortest edge out of any already traversed nodes
        current = shortest[1]
        if shortest[2] != math.inf:
            traversepath.append(shortest)  
#        print(totalcost)              
#    print(visited)
    return totalcost, traversepath

#slight formatting of data    
def formatGraph(cost, start):
    for iterx, x in enumerate(cost):
        print("distance from node " + str(start) + " to node " + str(iterx)  + " = " + str(x))

#returns distance from start node to end node
#rember to store path so that can be returned
def getDistance(cost, start, end):
    print("\ndistance from starting node " + str(start) + " to ending node " + str(end)  + " = " + str(cost[end]))


#lazy getpath
#since I was having some trouble thinking of how to properly copy the values over I just have the standard edge list
    #starts from end and goes to front since there is only a single chain to check (as opposed to if you started from the fornt and went to the end)
def getPath(links, head, tail, finalpath):
    for x in links:
        #check if value is end
        if x[1] == tail:
            #insert value
            finalpath.insert(0, x)
            #if starting position has been reached
            if x[0] == head:
                return finalpath
            else:
                #recursive loop chaining from end to start
                return getPath(links, head, x[0], finalpath)

    
#main  
#user input
size = int(input("enter graph generator size: "))
start = int(input("enter starting node: "))
end = int(input("enter end node: "))
#size = 20
#start = 2
#end = 16

#generate graph data
nodes = genData(size);
print("\nnode list: ")
for iterx, x in enumerate(nodes):
    print("node " + str(iterx) + ": " + str(x))

print("\n\ndata from node: " + str(start) + " to node: " + str(end))
#start program clock
starttime = time.time()
#run dijkstra
graphcost, traversed = mydijkstras(nodes, start)
print("\ntraversal path: ")
print(traversed)
#print time taken
runtime = time.time() - starttime
print("\n\ndijkstras runtime: ", runtime , " seconds to run")    
print("\ntotal graph cost: ")
#can get path cost from start to any other node
#also store traversed path?
#print(graphcost)
#for iterx, x in enumerate(graphcost):
#    print("node " + str(iterx) + ": " + str(x))
#shows distance from start node to any node
formatGraph(graphcost, start)
#gets distance between 2 specific nods
getDistance(graphcost, start, end)
startpath = []
#gets path needed to traverse to go from start to end
startend = getPath(traversed, start, end, startpath)
print("\ntraversal order for path: ")
for x in startend:
    print(x)



##clean up functions if time permits
##start program clock
#starttime = time.time()
#graphcost, reverse = mydijkstras(nodes, end)
#print("\ntraversal path: ")
#print(reverse)
##print time taken
#runtime = time.time() - starttime
#print("\n\ndijkstras runtime: ", runtime , " seconds to run")    
#
#print("\ntotal graph cost: ")
#for iterx, x in enumerate(graphcost):
#    print("node " + str(iterx) + ": " + str(x))
#getDistance(graphcost, end, start)
#endpath = []
#endstart = getPath(reverse, end, start, endpath)
#print("\ntraversal order for path: ")
#for y in endstart:
#    print(y)