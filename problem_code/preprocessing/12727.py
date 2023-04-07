"""
from decimal import *

A = [0]*31

A[1] = Decimal(3)+Decimal(5).sqrt()

B = [0]*31

B[1] = str(int(A[1])%1000)

while len(B[1]) != 3:
    
    B[1] = '0' + B[1]

for i in range(2,31):
    
    A[i] = A[i-1]*A[1]

    B[i] = str(int(A[i])%1000)

    while len(B[i]) != 3:
        
        B[i] = '0' + B[i]

"""
from sys import stdin

T = int(stdin.readline())

compute = [0,
 '005',
 '027',
 '143',
 '751',
 '935',
 '607',
 '903',
 '991',
 '335',
 '047',
 '943',
 '471',
 '055',
 '447',
 '463',
 '991',
 '095',
 '607',
 '263',
 '151',
 '855',
 '527',
 '743',
 '351',
 '135',
 '407',
 '903',
 '791',
 '135',
 '647']

for t in range(1,T+1):
    
    n = int(stdin.readline())

    print(f'Case #{t}: {compute[n]}')