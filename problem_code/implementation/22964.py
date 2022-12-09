from sys import stdin

n,k,x = map(int,stdin.readline().split())

sum_ax = k*(pow(x*(x+1)//2,2,998244353))

case = (pow(x,n-1,998244353)*pow(x,k-1,998244353))

value = sum_ax*case%998244353

print(*([value]*(n-k+1)))