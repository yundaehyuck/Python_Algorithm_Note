#p1,p2,p3를 소인수만으로 가진 자연수들의 배열에서 i번째 수를 찾는 문제

#p1**n1 * p2**n2 * p3**n3로 이루어지고 이것이 10^18보다 작아야하는데 2^60 > 10^18이므로, 
#n1,n2,n3 < 60
#60^3은 시간안에 충분히 돌아간다
p1,p2,p3,i = map(int,input().split())

A = []

for n1 in range(60):
    
    for n2 in range(60):
        
        for n3 in range(60):

            v = (p1**n1)*(p2**n2)*(p3**n3)

            if v > 1 and v < 10**18:

                A.append(v)
            
            elif v >= 10**18:
                
                break

A.sort()

print(A[i-1])