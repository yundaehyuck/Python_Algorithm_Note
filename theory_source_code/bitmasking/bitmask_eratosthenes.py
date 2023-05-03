n = int(input())

#255를 원소로 가지는 n/8 크기의 체로 초기화
result = [255]*((n+1)//8+1)

for i in range(2,int((n+1)**(1/2))+1):
    
    if result[i >> 3] & (1 << (i & 7)): #i가 소수라면..
        
        for j in range(i*i, n+1,i):
            
            #i의 배수를 모두 소수가 아니라고 표시한다
            result[j >> 3] &= ~(1 << (j & 7))
    
prime_list = [i for i in range(2,n+1) if result[i >> 3]&(1<<(i&7))]

print(prime_list)
[2,3,5,7]