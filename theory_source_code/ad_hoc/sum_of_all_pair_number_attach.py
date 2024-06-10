#모든 순서쌍 (ai,aj)를 그대로 붙인 aiaj의 합
#aiaj를 10진법으로 바꿔본다
n = int(input())

A = list(map(int,input().split()))

prefix = [A[0]]

for i in range(1,n):
    
    prefix.append(prefix[-1]+A[i])

# a1 a2 a3 a4

# a1*(10^(len(a2))+10^(len(a3))+10^(len(a4))) + (a2+a3+a4)

# a2*(10^(len(a3))+10^(len(a4))) + (a3+a4)

# a3*(10^(len(a4)))+a4

v = 0

mod = 998244353

for i in range(1,n):
    
    v += (prefix[i-1]*10**(len(str(A[i]))) + (prefix[n-1] - prefix[i-1]))
    v %= mod

print(v)