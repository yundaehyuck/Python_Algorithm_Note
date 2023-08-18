from sys import stdin

def convert(x,y):

    return ord(maps[y][x]) - ord('A') + 1

def dfs(x,y):

    stack = [(0,0,maps[y][x])]
    visited = [[0]*c for _ in range(r)]

    d = [[0,1],[1,0],[0,-1],[-1,0]]

    answer = 0

    while stack:

        x,y,alpha = stack.pop()

        if answer < len(alpha):

            answer = len(alpha)

        if answer == 26:

            break
        
        if visited[y][x] == alpha:
            continue
        
        visited[y][x] = alpha

        for i in range(4):

            dx = x + d[i][0]
            dy = y + d[i][1]

            if dx >= 0 and dx <= c-1 and dy >= 0 and dy <= r-1:

                if maps[dy][dx] not in alpha:

                    stack.append((dx,dy,alpha+maps[dy][dx]))

    return answer

r,c = map(int,stdin.readline().split())

maps = [stdin.readline() for _ in range(r)]

print(dfs(0,0))