from sys import stdin

n,q = map(int,stdin.readline().split())

c = 0

for _ in range(q):
    
    a,l,r = map(int,stdin.readline().split())

    if a == 1: #l번과 r번을 서로 바꾸면 반드시 반전수를 2로 나눈 나머지가 바뀐다
        
        if c == 0:
            
            c = 1
        
        else:
            
            c = 0
    
    else:
        
        #[l,r]을 뒤집는 과정은
        #i번 j번을 서로 바꾸는 과정을 (r-l+1)//2번 한 것이다.
        ex = (r-l+1)//2
        
        #i번, j번을 서로 바꾸는 과정을 1번 하면 반전수를 2로 나눈 나머지가 바뀐다.
        #따라서 짝수번 하면 그대로이고 홀수번 하면 바뀐다.
        if ex % 2 == 1:
            
            if c == 0:
                
                c = 1
            
            else:
                
                c = 0
                
    print(c)