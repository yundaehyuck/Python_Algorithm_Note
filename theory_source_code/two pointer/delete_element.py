#delete element using two pointer

from sys import stdin

n,k = map(int,stdin.readline().split())

s = list(map(int,stdin.readline().split()))

i = 0
j = 0

answer = 0
len_s = 0

while i <= j and j != n:
    
    #포인터 j에 대해 s[j]가 홀수라면,
    if s[j] % 2 == 1:
        
        #홀수를 포함시킬 수 있는 기회 k가 0이하라면, 홀수를 포함시킬 수 없다
        if k <= 0:
            
            #s[i]를 버려야하는데, 짝수라면
            if s[i] % 2 == 0:
                
                #짝수 부분수열 길이를 1 감소시키고
                len_s -= 1
                
            #짝수가 아니라면, 홀수를 포함시킬 수 있는 기회가 1 증가
            else:
                
                k += 1
            
            #포인터 i를 1 증가시켜 실제로 s[i]를 버린다
            i += 1
                
        else:
            
            k -= 1
            j += 1
    
    #s[j]가 짝수라면, 그 값은 포함시켜야 최대 길이를 만들 수 있다
    else:
        
        #그리고 j를 1 이동하고, s[j]가 짝수니까 짝수 부분수열 길이가 1 증가
        j += 1
        len_s += 1
        
        #길이가 증가했으니까, 최대 길이가 갱신될 기회가 있다
        if answer < len_s:
            
            answer = len_s

print(answer)