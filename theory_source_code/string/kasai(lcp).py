#LCP(Longest common prefix) 배열을 구하는 알고리즘

def kasai(suffix_array, s):
    
    n = len(s)

    lcp = [0]*n

    #suffix_array[i] = 사전순으로 i번째 원소가 몇번째 접미사인지.
    #reverse_suffix_array[i] = i번째 접미사가 사전 순으로 몇번째 원소인지

    #suffix_array[k] = i <<>> reverse_suffix_array[i] = k

    #i번째 접미사 suffix_array[k] = i에서 앞 한글자를 지운 
    #i+1번째 접미사 suffix_array[?] = i+1의 ?를 알아야함

    reverse_suffix_array = [0]*n

    for i in range(n):
        
        #suffix_array[i] = k <<<>>> reverse_suffix_array[k] = i
        reverse_suffix_array[suffix_array[i]] = i
    
    #lcp 배열을 구한다

    #가장 긴 접미사인 0번째 접미사부터 시작

    #0번째 접미사는 reverse_suffix_array[0] = i위치에 존재하고
    #0번째 접미사와 인접한 접미사는... suffix_array[i-1] = suffix_array[reverse_suffix_array[0]-1]에 존재
    #두 접미사를 비교해서 몇개가 일치하는지 구한다

    k = 0 #lcp값

    for i in range(n):

        #lcp[0]는 정의하지 않는다
        #suffix_array의 0번째 원소의 접미사는 이전 접미사가 존재하지 않는다
        if reverse_suffix_array[i] == 0: 
            
            k = 0
            continue
        
        #i번째 접미사와 인접한 접미사의 위치
        adj = suffix_array[reverse_suffix_array[i]-1]

        #i번째 접미사와 인접한 접미사의 글자를 하나씩 비교하면서
        #lcp값 k를 1씩 증가시킨다.
        while i+k < n and adj+k < n and s[i+k] == s[adj+k]:
            
            k += 1
        
        #반복문을 탈출하면, i번째 접미사에 대응하는 lcp값은 k가 된다.
        lcp[reverse_suffix_array[i]] = k

        # 그 다음 반복문에서 앞 1글자를 지우므로, lcp는 적어도 1 감소해야한다.
        if k > 0:
            
            k -= 1
    
    return lcp