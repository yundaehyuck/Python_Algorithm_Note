#prefix이면서 suffix를 모두 찾는 알고리즘

def z_function(s):
   
    n = len(s)

    z = [0]*n
    
    z[0] = n #z[0] = n으로 정의, 자기 자신도 접두사이면서 접미사가 된다

    left = 0
    right = 0

    for i in range(1,n):
      
        if i < right:
          
            z[i] = min(right-i, z[i-left])

        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
          
            z[i] += 1
      
        if i+z[i] > right:
          
            left = i
            right = i+z[i]
  
    return z

s = input()

z = z_function(s)

n = len(s)

answer = []

#z[i]는 접두사를 유일하게 결정짓는다.
#즉, 주어진 문자열에서 길이가 m인 접두사는 유일하다. (예) ABACABA에서 길이가 2인 접두사는 AB

#z[i]값 만큼 i번째 접미사 s[i,i+1,..,n-1]이 가져가기 때문에, 
#z[i]가 i번째 접미사 길이 n-i만큼 된다면? 
#따라서 prefix이면서 suffix일려면, z[i] = n-i인 모든 z[i]를 찾는다

#특히, n-1부터 0으로 역방향으로 순회해서, answer에 길이가 짧은 값부터 길이가 긴 값으로 들어가도록 한다
for i in range(n-1,-1,-1):

    if z[i] == n-i:

        answer.append((z[i]))

print(len(answer))

#z배열을 오름차순으로 정렬한다.
z.sort()

j = 0

#길이가 긴 접두사는 길이가 짧은 모든 접두사를 포함한다.
#예) ABACABA에서 길이가 3인 접두사 ABA는 길이가 1,2인 접두사 A, AB를 포함한다.

#정렬된 z배열을 순회하면서 처음으로 answer[j]인 위치 i를 찾았다면,
#answer[j]인 prefix이면서 suffix인 부분문자열은 n-i번 나타난다.
for i in range(n):
    
    if z[i] == answer[j]:

        print(answer[j],n-i)
        
        j += 1