import math
from sys import stdin

fact_dict = {}

fact_dict = {'1':1, '2':2, '6':3, '24':4, '120':5, '720':6}

n = stdin.readline().rstrip()

n_digit = len(n)

value = fact_dict.get(n,-1)

#입력이 6! 이내의 값이라면..
if value != -1:
    
    print(value)

else:
    
    #7!부터는 자리수가 유일하게 결정된다.
    digit = math.log10(5040)
    
    i = 7
    
    while 1:
        
        if n_digit == int(digit) + 1:
            
            break
        
        else:
            
            digit += math.log10(i+1)
            
            i += 1
    
    print(i)