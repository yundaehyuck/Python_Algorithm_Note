from sys import stdin

def permutation(i,n):

    global max_ans
    
    #n자리 순열을 모두 구성하면
    if i == n:
        
        #정수로 바꿔서 b와 크기 비교
        if int(''.join(p)) < b:
            
            ans = int(''.join(p))
            
            #b보다 작다면, 최댓값인지 검사하고 갱신함
            if max_ans < ans:
                
                max_ans = ans

    else:
        
        for j in range(n):

            if used[j] == 0:
      
                p[i] = a[j]

                used[j] = 1

                permutation(i+1,n)

                used[j] = 0


a,b = stdin.readline().rstrip().split()

b = int(b)

n = len(a)

a = list(a)

#a를 구성하는 원소의 개수를 센다
cnt = [0]*10

for i in range(n):
    
    cnt[int(a[i])] += 1

max_ans = 0

#a의 자리수에 0이 존재한다면..
if cnt[0] >= 1:
    
    for i in range(n):
        
        #0이 아닌 모든 경우에 대하여,
        if a[i] != '0':
        
            p = [0]*n
            used = [0]*n
            
      #맨 앞자리를 0이 아닌 수로 채워넣고
            p[0] = a[i]
            used[i] = 1
      #1번부터 n-1번까지 순열을 채워넣는다
            permutation(1,n)

#0이 존재하지 않는다면.. 그냥 순열을 구한다
else:
    p = [0]*n
    used = [0]*n

    permutation(0,n)

#최댓값이 갱신되지 않았다면, 찾을 수 없다는 뜻
if max_ans == 0:
    
    print(-1)

else:

    print(max_ans)