#stirling formula

import math

def factorial_approximation(n):
    
    return (n/math.e)**(n) * (2*math.pi*n)**(1/2)

#natural log approximation

def log_approximation(n):
    
    return math.log(2*math.pi*n)/2 + n*(math.log(n) - 1)

#10에 대한 log를 취한 스털링 근사
def log_approximation(n):
    
    return math.log10((2*math.pi*n))/2 + n * (math.log10(n)-math.log10(math.e))