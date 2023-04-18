from sys import stdin

INF = 1000000000000000000000

def prim(r,v):

    mst = [0]*v

    weights = [INF]*v

    #mst[r] = 1
    weights[r] = 0

    for _ in range(v-1):
        
        u = 0
        w = INF

        for i in range(v):
            
            if mst[i] == 0 and weights[i] < w:
                
                w = weights[i]
                u = i
        
        mst[u] = 1

        for w in range(v):
            
            if mst[w] == 0 and C[u][w] > 0:
                
                weights[w] = min(C[u][w],weights[w])
    
    return sum(weights)

n = int(stdin.readline())

C = [list(map(int,stdin.readline().split())) for _ in range(n)]

print(prim(0,n))