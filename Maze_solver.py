def dfs(maze, row, col, visited):

    rows = len(maze)
    cols = len(maze[0])

    if (
        row < 0 or
        col < 0 or
        row >= rows or
        col >= cols or
        maze[row][col] == 1 or
        (row, col) in visited
    ): 
        return False
   
    if row == rows - 1 and col == cols - 1:
        return True

    visited.add((row, col))

    return (
        dfs(maze, row+1, col, visited) or
        dfs(maze, row-1, col, visited) or
        dfs(maze, row, col+1, visited) or
        dfs(maze, row, col-1, visited)
    )


maze = [
    [0,0,1],
    [0,0,0],
    [1,0,0]
]

print(dfs(maze, 0, 0, set()))
