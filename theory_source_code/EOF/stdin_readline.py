from sys import stdin

while 1:
    
    s = stdin.readline()
    
    if s == '':
        
        break
    
    else:
        
        answer = [0,0,0,0]

        for c in s:

            if c.islower():

                answer[0] += 1

            elif c.isupper():

                answer[1] += 1

            elif c.isdigit():

                answer[2] += 1

            elif c == ' ':

                answer[3] += 1

        print(*answer)