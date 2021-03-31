
import math
def f(x):
    return math.pow(x,2)-3
a=1.0
b=2.0
p=(a+b)/2
TOL=math.pow(10,-4)
N0=20
n=0
FA=f(a)
FP=f(p)
while n<N0:
    while FP!=0 and (b-a)/abs(a)>=TOL:
        print(p)
        if FA*FP>0:
            a=p
            FA=FP
        else:
            b=p
        p=(a+b)/2
        FP=f(p)
    n=n+1
    p=(a+b)/2
print("Answer is",p)
    

