def zeckendorf(n):
    
    #find fibonacci sequence
    #n보다 작거나 같은 모든 피보나치 수를 찾는다.
    #현재 O(N) 다이나믹 프로그래밍이지만, 
    #필요에 따라 더 빠른 알고리즘을 선택
    fib = [1,1]

    i = 2

    while 1:
        
        x = fib[i-1] + fib[i-2]

        if x <= n:

            fib.append(x)
            i += 1
        
        else:
            
            break
    
    len_f = len(fib)
    
    #find zeckendorf representation
    
    zeck = []
    
    #n은 반드시 0이 될 수 있으며, 0이 될때까지 반복
    while n > 0:
        
        #가장 큰 피보나치 수부터 순회해서,
        for i in range(len_f-1,-1,-1):
            
            #n보다 작거나 같다면, 그것이 제켄도르프 분해이며,
            if n >= fib[i]:
                
                zeck.append(fib[i])
                
                #제켄도르프 분해를 뺀 값을 새로운 n으로 갱신
                n -= fib[i]
                break
    
    return zeck

print(zeckendorf(100))
[89, 8 ,3]