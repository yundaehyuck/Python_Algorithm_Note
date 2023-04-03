from sys import stdin

"""
arr = list(range(1,44722))

power = []

for i in range(44720):
    
    arr[i+1] += arr[i]

    x = arr[i+1]

    z = int((x+1)**(1/2))

    if z**2 == x+1:
        
        power.append(x+1)

print(power)
[4, 16, 121, 529, 4096, 17956, 139129, 609961, 4726276, 20720704, 160554241, 703893961]
"""

power = [4, 16, 121, 529, 4096, 17956, 139129, 609961, 4726276, 20720704, 160554241, 703893961]

n = 1

while 1:
    
    a,b = map(int,stdin.readline().split())

    if a == 0 and b == 0:
        
        break

    count = 0

    for p in power:
        
        if p > a and p < b:
            
            count += 1
    
    print(f"Case {n}: {count}")

    n += 1