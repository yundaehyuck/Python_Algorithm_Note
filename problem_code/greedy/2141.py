from sys import stdin

n = int(stdin.readline())

post = []

total_human = 0

for _ in range(n):
    
    x,a = map(int,stdin.readline().split())

    post.append((x,a))

    total_human += a

post.sort()

left = 0
right = total_human

for i in range(n):
       
    dleft = left + post[i][1]
    dright = right - post[i][1]

    if dleft >= dright:
        
        break
    
    else:
        
        left = dleft
        right = dright

print(post[i][0])