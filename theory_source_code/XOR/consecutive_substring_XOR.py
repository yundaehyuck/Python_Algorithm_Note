from sys import stdin

#1부터 i까지 연속하는 자연수의 XOR
#i를 4로 나눈 나머지에 따라 XOR값이 정해진다.
def value(i):
    
    r = i % 4
    
    if r == 0:
        
        return i
    
    elif r == 1:
        
        return 1
    
    elif r == 2:
        
        return i+1
    
    else:
        
        return 0

#L부터 R까지의 XOR
#1부터 L-1까지의 XOR과 1부터 R까지의 XOR을 구한다.
#두 값의 XOR이 L부터 R까지의 XOR
T = int(stdin.readline())

for _ in range(T):
    
    s,f = map(int,stdin.readline().split())

    v1 = value(s-1)
    v2 = value(f)

    print(v1 ^ v2)