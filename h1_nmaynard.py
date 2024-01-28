from pyamaze import maze, agent, textLabel
#rows and cols must are variables, so factual values are needed to avoid errors
rows = 5
cols = 5
m = maze(rows,cols)
m.CreateMaze() #create a maze with one path
a = agent(m, footprints = True)
m.tracePath({a:m.path})
l=textLabel(m,'Path Length',len(m.path)+1) #display the cost of the solution
m.run()