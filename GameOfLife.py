import os
import time

l = '✺'
alive = l

o = '·'
dead = o

####### Formats the grid
###!!! NOT PURE


def print_grid(grid):
    for temp in grid:
        stringGrid = ' '.join(temp)
        print(stringGrid)

###### Inputs
dim = int(input('Dimensions(AxA) A = '))
gen = int(input('Generations: '))


###### SET INITIAL MATRICES 

###
init_matrix = [ [dead]*dim for count in range(dim)]

###Beginning state input
a = [[o,l,o,o],
     [o,l,o,o],
     [o,l,o,o],
     [o,l,l,o]]

###Intermediate template
b = a

###### COUNTS NUMBER OF ADJACENT SQUARES THAT ARE ALIVE

def num_adjacencies(i,j):

    adjacencies = 0
    
    ### Initialize wall conditions
    right_wall = False
    left_wall = False
    up_wall = False
    down_wall = False
    upleft_wall = False
    upright_wall = False
    downleft_wall = False
    downright_wall = False
    ######### Define direction checking variables if there is no wall
  
    ######  Orthogonal Assigning
    ### LEFT
    if j > 0:
        left_of = a[i][j-1]
    else:
        left_wall = True
      
    ### RIGHT
    if j < (len(a[i])-1):
        right_of = a[i][j+1]
    else: right_wall = True
      
    ### UP
    if i > 0:
        up_of = a[i-1][j]
    else:
        up_wall = True
      
    ### DOWN
    if i < (len(a)-1):    
        down_of = a[i+1][j]
    else:
        down_wall = True

      
    ###### Diagonal Assigning 
    ### UPLEFT
    if j > 0 and i > 0:
        upleft_of = a[i-1][j-1]
    else:
        upleft_wall = True
    ### UPRIGHT
    if j < (len(a[i])-1) and i > 0:
        upright_of = a[i-1][j+1]
    else:
        upright_wall = True
    ### DOWNLEFT
    if j > 0 and i < (len(a)-1):
        downleft_of = a[i+1][j-1]
    else:
        downleft_wall = True
    ### DOWNRIGHT
    if j < (len(a[i])-1) and i < (len(a)-1):
        downright_of = a[i+1][j+1]
    else:
        downright_wall = True


    ### Orthogonal adjacency summing
    if left_wall == False and left_of == alive:
        adjacencies += 1
    if right_wall == False and right_of == alive:
        adjacencies += 1
    if up_wall == False and up_of == alive:
          adjacencies += 1
    if down_wall == False and down_of == alive:
        adjacencies += 1
      
    ### Diagonal adjacency summing
    if upleft_wall == False and upleft_of == alive:
        adjacencies += 1
    if upright_wall == False and upright_of == alive:
        adjacencies += 1
    if downleft_wall == False and downleft_of == alive:
        adjacencies += 1
    if downright_wall == False and downright_of == alive:
        adjacencies += 1
      
    
    return adjacencies


###### CONDITIONALS FOR SETTING THE RULES OF THE GAME
def rules_of_life(i,j):
    adj = num_adjacencies(i,j)
    if a[i][j] == alive:
        if adj == 2 or adj == 3:
            return alive
        else:
            return dead
    if a[i][j] == dead:
        if adj == 3:
            return alive
        else:
            return dead



###### LOOPING OVER THE GRID
def iterate_over_grid(xdim,ydim):
    grid = [[dead]*ydim for count in range(ydim)]

    i = 0
    j = 0
  
    for y in a:
        j = 0

        for x in y:
            num_adjacencies(i,j)
            grid[i][j] = rules_of_life(i,j)
            j += 1
          
        i += 1

    return grid



###### State iteration

print_grid(a)
print('')
for times in range(gen):
  b = iterate_over_grid(dim,dim)
  a = b
  time.sleep(0.25)
  os.system('clear')
  print_grid(a) 
  print('')