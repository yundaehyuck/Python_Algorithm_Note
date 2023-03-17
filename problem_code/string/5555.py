from sys import stdin

target = stdin.readline().rstrip()

n = int(stdin.readline())

t = len(target)

count = 0

for _ in range(n):
    
    string = stdin.readline().rstrip()

    s  = len(string)
    
    #처음으로 되돌리기 위해, 
    #원래 문자열에서 비교하고자하는 문자열 길이만큼 붙여준다
    string += string[:t]

    find = False
    
    #처음부터 원래 문자열의 길이만큼 순회해준다
    for i in range(s):
        
        if target == string[i:i+t]:
            
            count += 1
            break
    
    
print(count)