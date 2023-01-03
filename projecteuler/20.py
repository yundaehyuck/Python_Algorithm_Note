factorial = [1]*(101)

for i in range(1,101):
    
    factorial[i] = factorial[i-1]*i

print(sum(map(int,str(factorial[100]))))