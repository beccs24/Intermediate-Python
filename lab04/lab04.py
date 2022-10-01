from Stack import Stack

def printMaze(maze):
    for row in range(len(maze)):
    	for col in range(len(maze[0])):
    		print("|{:<2}".format(maze[row][col]), sep='',end='')
    	print("|")
    return

def solveMaze(maze, startX, startY):
    count = 1
    s = Stack()
    maze[startX][startY] = count
    s.push([startX, startY])
    
    while s.size() != 0:
        startX = s.peek()[0]
        startY = s.peek()[1]
        if maze[startX-1][startY] == ' ': 
            count += 1
            maze[startX-1][startY] = count
            s.push([startX-1, startY])
            
        elif maze[startX-1][startY] == 'G':
            return True
        
        elif maze[startX][startY-1] == ' ':
            count += 1
            maze[startX][startY-1] = count
            s.push([startX, startY-1])

        elif maze[startX][startY-1] == 'G':
            return True
        
        elif maze[startX+1][startY] == ' ':
            count += 1
            maze[startX+1][startY] = count
            s.push([startX+1, startY])

        elif maze[startX+1][startY] == 'G':
            return True
        
        elif maze[startX][startY+1] == ' ':
            count += 1
            maze[startX][startY+1] = count
            s.push([startX, startY+1])
        
        elif maze[startX][startY+1] == 'G':
            return True
        
        else:
            s.pop()
    return False
