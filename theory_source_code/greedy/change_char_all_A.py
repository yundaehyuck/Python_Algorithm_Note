#문자 하나를 바꾸거나, 처음부터 k개 문자를 뒤집어서 모든 문자를 A로 만드는 방법

n = int(input())

s = list(input())

count = 0

r = False

#뒤에서부터 순회하여, i번째 문자가 A라면 넘어간다
#B라면, 그 앞의 문자가 A라면 첫번째 연산 적용
#그 앞의 문자가 B라면 두번째 연산 적용

#flag로 r을 세워서 뒤집은 경우 r = True로 하면, 반대로 생각하기만 하면 직접 하나하나 바꾸지 않아도 된다
for i in range(n-1,0,-1):
    
    if r == False:

        if s[i] == 'B':

            if s[i-1] == 'A':

                count += 1

            else:

                r = True
                count += 1
    
    else:
        
        if s[i] == 'A':
            
            if s[i-1] == 'B':
                
                count += 1
            
            else:
                
                r = False
                count += 1

if r:
    
    if s[0] == 'A':
        
        count += 1

else:
    
    if s[0] == 'B':
        
        count += 1
        
print(count)
