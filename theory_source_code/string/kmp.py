def prefix_function(s):
    
    n = len(s)

    pi = [0]*n #pi[0] = 0으로 초기화

    for i in range(1,n): #i를 1부터 n-1까지 반복
        
        j = pi[i-1] #j = pi[i-1]로 초기화
        
        while j > 0 and s[i] != s[j]: #j > 0일때까지 반복하는데..
                
            j = pi[j-1] #s[i] != s[j]이면, j를 pi[j-1]로 감소시키고..
        
        #반복문을 탈출했는데.. s[i] = s[j]이면 j = j + 1로 만든다음,

        #j != 0인데, s[i] = s[j]이면 j+1이 될거고
        #j = 0인데 s[i] = s[j]이면 1이 될거고
        if s[i] == s[j]:
            
            j += 1
        
        #만들어진 j를 pi[i] = j에 대입
        #j = 0인데 s[i] = s[j]이면 위에서 1이 되어 여기서 1이 들어갈거고, 
        #j = 0인데 s[i] != s[j]이면, 결국에 0이 들어가고
        #j != 0이고 s[i] = s[j]이면 j+1이 들어간다.
        #j ! = 0인데, s[i] != s[j]이면 위에 while 반복문에서 탈출을 못함
        pi[i] = j
    
    return pi

print(prefix_function("abcabcd"))
print(prefix_function("aabaaab"))

[0, 0, 0, 1, 2, 3, 0]
[0, 1, 0, 1, 2, 2, 3]