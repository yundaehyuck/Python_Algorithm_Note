def permutation_with_same(i,n,r,cnt):
    
    if i == r: ##r개를 뽑으면 순열 완성
        
        print(p) ##완성된 순열 p로 할 행동
    
    else:
        
        for j in range(1,n+1): ##배열에는 1부터 n까지 원소가 존재함(적절하게 응용하기)
            
            if cnt[j] != 0: ##원소 j의 개수가 0개가 아니라면..
                
                p[i] = j #i번째에는 j를 넣고..

                cnt[j] -= 1 ##j 원소를 1개 사용함

                permutation_with_same(i+1,n,r,cnt) ##다음 i+1번째 원소를 선택하러

                cnt[j] += 1 ##재귀 끝나고 원상복구
    
n = 4

a = [1,1,2,3]

##counting 배열 완성
cnt = [0]*(n+1)

for i in range(n):
    
    cnt[a[i]] += 1

p = [0]*n

permutation_with_same(0,n,n,cnt)

"""
[1, 1, 2, 3]
[1, 1, 3, 2]
[1, 2, 1, 3]
[1, 2, 3, 1]
[1, 3, 1, 2]
[1, 3, 2, 1]
[2, 1, 1, 3]
[2, 1, 3, 1]
[2, 3, 1, 1]
[3, 1, 1, 2]
[3, 1, 2, 1]
[3, 2, 1, 1]
"""