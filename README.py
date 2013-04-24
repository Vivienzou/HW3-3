HW3-3
=====
%time
def f(b,c,a):
    b = 0
    c = 0
    for i in range(10001):
        if isprime(i):
            a = i
            b = a + b 
            c = b-1

%time
cython("""
b = 0
c = 0
def isprime(startnumber):
     startnumber*=1.0
     for divisor in range(2,int(startnumber**0.5)+1):
         if startnumber/divisor==int(startnumber/divisor):
             return False
     return True
    
for i in range(10001):
    if isprime(i):
        a = i
        b = a + b 
        c = b-1
""")
