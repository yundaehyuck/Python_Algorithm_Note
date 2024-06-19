#주어진 알파벳 개수로 만들수 있는 길이 1부터 k까지 모든 문자열의 개수
#주어진 알파벳들의 모든 조합만으로 일렬 배열하는 복수순열의 개수
#다이나믹 프로그래밍으로 구하는 방법
mod = 998244353

k = int(input())

C = list(map(int,input().split()))

#팩토리얼
factorial = [0]*(k+1)

factorial[0] = 1

for i in range(1,k+1):
    
    factorial[i] = factorial[i-1]*i
    factorial[i] %= mod

#inverse factorial
inverse = [0]*(k+1)

inverse[k] = pow(factorial[k],mod-2,mod)

for i in range(k-1,-1,-1):
    
    inverse[i] = inverse[i+1]*(i+1)
    inverse[i] %= mod

#이항계수 nCk
def c(n,k):
    
    return (factorial[n]*inverse[k]*inverse[n-k])% mod

dp = [[0]*(k+1) for _ in range(len(C)+1)]

#길이 0을 만드는 방법은 아무것도 안하면 되니 1가지
dp[0][0] = 1

for i in range(len(C)): #사용한 알파벳 번호 0~len(C)-1

    for j in range(k+1): #길이 0 ~ k

         #해당 알파벳 사용 개수
         #전체 길이 k에서 j만큼 알파벳이 정해져있다면, 나머지 k-j만큼 사용가능
         #물론 알파벳은 C[i]개 있는데, 이게 k-j보다 더 작다면..? C[i]개만큼 사용 가능
         #C[i]가 사용 제한 k-j보다 크다면 k-j까지만 사용가능
        for r in range(min(C[i],k-j)+1):

            dp[i+1][j+r] += (dp[i][j]*c(j+r,r))
            dp[i+1][j+r] %= mod

print(sum(dp[len(C)][1:]) % mod)