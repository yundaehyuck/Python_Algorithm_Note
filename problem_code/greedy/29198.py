from sys import stdin

n,m,k = map(int,stdin.readline().split())

string = []

#각 문자열을 정렬해주고
for _ in range(n):
    
    s = list(stdin.readline().rstrip())
    s.sort()
    string.append(''.join(s))

#문자열 리스트를 정렬해서 k개를 고르고
string.sort()

string2 = []

for i in range(k):
    
    string2.append(string[i])

#이렇게 붙인 문자열을 또 정렬해주고
string2 = list(''.join(string2))

string2.sort()

print(''.join(string2))