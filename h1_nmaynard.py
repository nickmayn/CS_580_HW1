from pyamaze import maze, agent, textLabel
from queue import PriorityQueue
import math
from time import time

#Coded by Loreto Gonzalez-Hernandez
#Introduction to AI
def DFS(m):
    """
    Depth First Search algorithm for solving the maze. In this implementation we pass a maze object and from here
    solve the maze using DFS.

    :param m: a maze object as defined in pyamaze.
    :returns: the path solution for the maze as solved by the algorithm.
    """
    start= (m.rows, m.cols) #coordinate of the start cell >> here is low rigth corner
    explored=[start] #Explored nodes in the frontier
    frontier=[start]
    #if there are no more nodes to explore
    dfsPath={}
    while len(frontier)>0: #if there are still nodes to explore
        currCell=frontier.pop() #node to explore, 
        if currCell == (1,1):   #if curret node is the goal, stop
            break
        #explore each node, the order for visit is 'East,South, West, North
        for d in 'EWSN':
            #verify if the direction is open, i.e. there is not a "wall" between nodes
            if m.maze_map[currCell][d] == True:     #The path is open
                if d=='E':
                    childCell = (currCell[0],currCell[1]+1) #move agent to the right column
                elif d=='W':
                    childCell = (currCell[0],currCell[1]-1) #move agent to the left column
                elif d=='S':
                    childCell = (currCell[0]+1,currCell[1]) #move agent to the bottom row  
                elif d=='N':
                    childCell = (currCell[0]-1,currCell[1]) #move agent to the up row
                if childCell in explored:   #if node has been explored
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                #store the coordinates of the path in a dictionary
                dfsPath[childCell]=currCell
    #The path is stored in backwards, so we need to change it
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath

def AStar(m):
    """
    A* algorithm for solving the maze. In this implementation we pass a maze object and from here
    solve the maze using A*.

    :param m: a maze object as defined in pyamaze.
    :returns: the path solution for the maze as solved by the algorithm.
    """
    start= (m.rows, m.cols) # coordinate of the start cell >> here is low rigth corner
    goal = (1,1) # coordinate of the goal cell
    explored=[start] # Explored nodes in the frontier
    frontier = PriorityQueue() # Define a priority queue for sorting our heuristic functioned nodes
    frontier.put((0, start)) # Put our initial node in the frontier
    AStarPath={} # Dictionary for our solution path
    while PriorityQueue.qsize(frontier)>0: # if there are still nodes to explore
        currCell=frontier.get()[1] # node to explore,
        if currCell == goal:   # if curret node is the goal, stop
            break
        # explore each node, the order for visit is 'East,South, West, North
        for d in 'EWSN':
            # verify if the direction is open, i.e. there is not a "wall" between nodes
            if m.maze_map[currCell][d] == True:     # The path is open
                if d=='E':
                    childCell = (currCell[0],currCell[1]+1) # move agent to the right column
                elif d=='W':
                    childCell = (currCell[0],currCell[1]-1) # move agent to the left column
                elif d=='S':
                    childCell = (currCell[0]+1,currCell[1]) # move agent to the bottom row  
                elif d=='N':
                    childCell = (currCell[0]-1,currCell[1]) # move agent to the up row
                if childCell in explored:   # if node has been explored
                    continue


                explored.append(childCell) # Append our explored node
                frontier.put((f(currCell, start, goal),childCell)) # Put our new potential nodes in the queue
                #store the coordinates of the path in a dictionary
                AStarPath[childCell]=currCell

    #The path is stored in backwards, so we need to change it
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[AStarPath[cell]]=cell
        cell=AStarPath[cell]
    return fwdPath

def f(n, sn, gn):
    """
    This method represents the minimum cost function.
    
    :param n: the current node
    :param sn: the starting node
    :param gn: the goal node

    :returns: the cost function for a* in the current state.
    """
    return g(n, sn) + h(n, gn)

def g(n, sn):
    """
    This method is meant to calculate the euclidian distance of the node n. It is also the cost
    to reach node n from the start node.

    :param n: the current node.
    :param sn: the start node.

    :return: the euclidian distance of the node compared to the starting node.
    """
    return math.sqrt((n[0] - sn[0])**2 + (n[1] - sn[1])**2)

def h(n, gn):
    """
    This method is meant to calculate the manhattan distance of the node n. It is also the cost
    to reach the goal from node n.

    :param n: the current node.
    :param gn: the goal node.

    :return: the manhattan distance of the current node and the goal node.
    """
    return abs(n[0] - gn[0]) + abs(n[1] - gn[1])


# Build the maze, solve, and visualize.
m= maze(10,10)
m.CreateMaze() #loopPercent=100 generates more than one path

# Generate out our solution paths
path = AStar(m)
path2 = DFS(m)

# Generate out our agents for solving the maze
a = agent(m,footprints=True)
a2 = agent(m,footprints=True)

# Trace out both paths
m.tracePath({a:path}, delay=10)
m.tracePath({a2:path2}, delay=10)

# Run the maze
m.run()