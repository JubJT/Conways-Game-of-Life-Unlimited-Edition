"""
# From: Code Wars
# Title: Conway's Game of Life - Unlimited edition (Created by: constablebrew)
# URL: https://www.codewars.com/kata/52423db9add6f6fc39000354

"""
def get_generation(cells, generations):
    #Returns cells as it is if generations == 0
    if generations==0:
        return cells
    #Add walls of '0' (initial)
    cells_copy=[[0]+row+[0] for row in cells]
    cells_copy.insert(0,[0 for i in range(len(cells[0])+2)])
    cells_copy.append([0 for i in range(len(cells_copy[0]))])
    #Initialization of Next Generation 
    next_gen=[[0 for j in range(0,len(cells_copy[0]))] for i in range(0,len(cells_copy))]
    
    #Loops on each Generation
    for n in range(generations):
        
        if n>0:
            #Add walls of '0' (Keeps on adding as we loop on the generation)
            cells_copy=[[0]+row+[0] for row in next_gen]
            cells_copy.insert(0,[0 for i in range(len(next_gen[0])+2)])
            cells_copy.append([0 for i in range(len(cells_copy[0]))])
            #Initialization of Next Generation (to match with current cell dimensions)
            next_gen=[[0 for j in range(0,len(cells_copy[0]))] for i in range(0,len(cells_copy))]    
        #Loops on the rows    
        for i in range(0,len(cells_copy)):
            #Loops on the columns
            for j in range(0,len(cells_copy[0])):
                total=0
                
                #Top L Corner
                total+= cells_copy[i-1][j-1] if i>0 and j>0 else 0
                #L Side
                total+= cells_copy[i][j-1] if j>0 else 0
                #Bottom L Corner
                total+= cells_copy[i+1][j-1] if i<len(cells_copy)-1 and j>0 else 0
                #Top Side
                total+= cells_copy[i-1][j] if i>0 else 0
                #Bottom Side
                total+= cells_copy[i+1][j] if i<len(cells_copy)-1 else 0
                #Top R Corner
                total+= cells_copy[i-1][j+1] if i>0 and j<len(cells_copy[0])-1 else 0
                #R Side            
                total+= cells_copy[i][j+1] if j<len(cells_copy[0])-1 else 0
                #Bottom R Corner
                total+= cells_copy[i+1][j+1] if i<len(cells_copy)-1 and j<len(cells_copy[0])-1 else 0
                
                next_gen[i][j]= 1 if total==3 or (total==2 and cells_copy[i][j]==1) else 0
        #Checks if the cell contains all 0's (Dead Cell) 
        if all(j==0 for i in next_gen for j in i):
            return '[[]]'
        #Copyies the next generation cell to the previous one, to prepare for the next loop
        cells_copy=[[next_gen[i][j] for j in range(0,len(next_gen[0]))] for i in range(0,len(next_gen))]
    #Trims excess wall (Can be added inside the generation Loop)
    while(sum(next_gen[0])==0 or sum(next_gen[len(next_gen)-1])==0 or all(next_gen[row][0]==0 for row in range(len(next_gen))) or all(next_gen[row][-1]==0 for row in range(len(next_gen)))):
        #Crop dead walls (Top and Bottom)
        if sum(next_gen[0])==0:
            next_gen.pop(0)
        if sum(next_gen[len(next_gen)-1])==0:
            next_gen.pop(len(next_gen)-1)
        #Crop dead walls (Left and Right)
        if all(next_gen[row][0]==0 for row in range(len(next_gen))):
            for row in range(len(next_gen)):
                next_gen[row].pop(0)
        if all(next_gen[row][-1]==0 for row in range(len(next_gen))):
            for row in range(len(next_gen)):
                next_gen[row].pop(-1)
                     
    return next_gen   
