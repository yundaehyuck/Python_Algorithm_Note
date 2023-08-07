#polynomial rolling hash function
n = int(input())

s = input()

r = 31
m = 1234567891

answer = 0

for i in range(n):
    
    answer += (ord(s[i]) - ord('a') + 1)*pow(r,i,m)
    answer %= m

print(answer)