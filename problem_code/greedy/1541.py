from sys import stdin

expression = stdin.readline().rstrip().split('-')

minus = []

for e in expression:
    
    try:
        
        e = int(e)

        minus.append(e)

    except:
        
        plus = e.split('+')

        temp = 0

        for e in plus:
            
            temp += int(e)
        
        minus.append(temp)

answer = minus[0]

for m in minus[1:]:
    
    answer -= m

print(answer)