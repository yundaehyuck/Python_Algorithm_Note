#길이 n인 정수 문자열이 어떤 수 x의 제곱수라는 것은
#x는 아무리 커봐야 10^(n/2)

#두 문자열 s,t가 서로 순열이 될려면, s,t의 구성이 동일해야한다.
#s와 t를 정렬했을때, 동일한 문자열이 된다

n = int(input())

s = sorted(input())

count = 0

max_value = pow(10,n)

i = 0

while i*i < max_value:
    
    t = list(str(i**2))

    while len(s) != len(t):
        
        t.append('0')
    
    t.sort()
        
    find = False
    
    for j in range(len(s)):
        
        if s[j] != t[j]:
            
            find = True
            break
    
    if find == False:
        
        count += 1

    i += 1

print(count)

"""
n = int(input())

s = sorted(input())

count = 0

for i in range(int((10**n)**(1/2))+1):
    
    t = list(str(i**2))
    
    if len(t) > len(s):
        continue

    while len(s) != len(t):
        
        t.append('0')
    
    t.sort()
        
    find = False
    
    for j in range(len(s)):
        
        if s[j] != t[j]:
            
            find = True
            break
    
    if find == False:
        
        count += 1

print(count)
"""