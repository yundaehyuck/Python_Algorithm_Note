from sys import stdin

while 1:
    
    try:

        a,b,c,d,e,f = map(float,stdin.readline().split())

        k1 = (c**2 - a**2 + d**2 - b**2)/2
        k2 = (e**2 - c**2 + f**2 - d**2)/2

        x = (k1*(f-d)-k2*(d-b))/((f-d)*(c-a) - (d-b)*(e-c))

        y = (k1*(e-c)-k2*(c-a))/((e-c)*(d-b) - (c-a)*(f-d))


        pi = 3.141592653589793

        circumference = 2*pi*(((x-a)**2+(y-b)**2)**(1/2))

        print(f"{circumference:.2f}")
    
    except:
        
        break