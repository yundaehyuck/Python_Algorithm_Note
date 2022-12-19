fibonacci = [0]*10000

fibonacci[0] = 1
fibonacci[1] = 2

i = 2

answer = 2

while 1:
    
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

    if fibonacci[i] > 4000000:
        
        break
    
    else:
        
        if fibonacci[i] % 2 == 0:
            
            answer += fibonacci[i]
        
        i += 1

print(answer)