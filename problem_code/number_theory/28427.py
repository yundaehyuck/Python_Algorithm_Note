#3개 이상의 연속된 자연수의 합은 반드시 합성수이다.

from sys import stdin

def get_prime(n):

    result = [1]*(n+1)

    result[1] = 0

    for i in range(2,int((n+1)**(1/2))+1):

        if result[i] == 1:

            for j in range(i*i,n+1,i):

                result[j] = 0

    return result

prime_list = get_prime(1000000)

prefix = [0,0]

for i in range(2,500000):
    
    x = i + i + 1

    if prime_list[x] == 1:
        
        prefix.append(prefix[-1] + 1)
    
    else:
        
        prefix.append(prefix[-1])

q = int(stdin.readline())

for _ in range(q):

    l,r = map(int,stdin.readline().split())

    print(prefix[r-1] - prefix[l-1])