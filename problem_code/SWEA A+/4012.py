from itertools import combinations
 
T = int(input())
 
for t in range(1,T+1):
     
    n = int(input())
 
    s = [list(map(int,input().split())) for _ in range(n)]
    
    ##음식 재료 0~n-1
    
    ingredient = range(0,n)
    
    ##n개중에 n/2개를 뽑는 조합
 
    all_combs = list(combinations(ingredient,n//2))
 
    len_c = len(all_combs)
 
    min_s = 20000
 
   ##전체 조합에서 절반만 순회하여
    for i in range(len_c//2):
   
   #i번째 조합과 len_c-1-i번째 조합은 서로 배반이면서 합집합이 0~n-1이 되는
   #n/2, n/2개로 나눠지는 집합이다.
   
        comb = all_combs[i]
        comb2 = all_combs[len_c-1-i]
 
        a_taste = 0
        b_taste = 0
   
   #각 조합의 길이는 n/2이므로, 각 조합에서 2개를 뽑는 조합 인덱스 x,y를 구한다.
   #조합을 구하면서 동시에 맛도 누적해서 더해준다
   
        for x in range(n//2-1): 
             
            for y in range(x+1,n//2):
                 
                a_taste += (s[comb[x]][comb[y]]+s[comb[y]][comb[x]])
                b_taste += (s[comb2[x]][comb2[y]]+s[comb2[y]][comb2[x]])
   
   ##맛의 차이의 절댓값을 구하고
        taste = abs(a_taste-b_taste)
   
   ##최솟값을 갱신
 
        if min_s > taste:
             
            min_s = taste
     
    print('#'+str(t),min_s)