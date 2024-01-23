def pacific_atlantic_water_flow(heights):
    # go the opposite
   # q all of the first row and the 0th indices of each row
    # dfs upwards if the nsew is greatr than the value

   # q the last row and all -1th indices of each row 
    pacific = set()
    atlantic = set()
    def dfs(i,j, ocean):
        ocean.add((i,j))
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            if 0 <= i + dx < len(heights) and 0 <= j + dy < len(heights[0]) and heights[i + dx][j + dy] >= heights[i][j] and (i + dx, j + dy) not in ocean:
                dfs(i + dx, j + dy, ocean)
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if i == 0 or j == 0:
                dfs(i,j,pacific)
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                dfs(i,j,atlantic)
    return [[a,b] for a,b in list(pacific.intersection(atlantic))]

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print("Input:", heights)
print("Expected:", [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
print("Received:", pacific_atlantic_water_flow(heights))

heights = [[2,1],[1,2]]
print("Input:", heights)
print("Expected:", [[0,0],[0,1],[1,0],[1,1]])
print("Received:", pacific_atlantic_water_flow(heights))