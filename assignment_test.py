import math

def tempConversion(a,b="Celcius"):
    if b=="Celcius":
        x=a*(9/5)+32
        x=round(x,1)
        return x
    elif b=="F":
        x=(a-32)*5/9
        x=round(x,1)
        return x

def factorPair():
    factors=[b]
    for i in range(1,a+1):
        if b*i==a:
            factors.append(i)
            factors.sort()
            return factors

def toRadians(y):
    x=(y*math.pi/180)   
    return x

def cosineLaw(a,b,c,oppositeside=True):
    if oppositeside==True:
        stepc1=math.pow(a,2)+math.pow(b,2)
        stepc2=(2*a*b)
        stepc3=toRadians(c)
        stepc4=math.cos(stepc3)
        stepc5=(stepc2*stepc4)
        stepc6=(stepc1)-(stepc5)
        stepc7=math.sqrt(stepc6)
        return stepc7
    elif oppositeside==False:
        d0=toRadians(c)
        print(d0)
        d1=math.sin(d0)*a/b
        print(d1)
        d2=math.asin(d1)
        print(d2)
        dc=d2*180/math.pi
        d3=180-dc-c
        print(d3)
        d4=toRadians(d3)
        print(d4)
        d5=(math.sin(d4)*180/math.pi)*b/(math.sin(d0)*180/math.pi)
        return d5









def solution(numbers):
    x=numbers[1]
    return x 

def quadratic(a,b,c):
    stepx1=(b*-1)
    stepx2=math.pow(b,2)-(4*a*c)
    stepx2=math.sqrt(stepx2)
    stepx3=(stepx1)+(stepx2) 
    stepx4=(stepx3)/(2*a)
    stepy1=(b*-1)
    stepy2=math.pow(b,2)-(4*a*c)
    stepy2=math.sqrt(stepy2)
    stepy3=(stepy1)-(stepy2) 
    stepy4=(stepy3)/(2*a)
    numlist=[stepy4,stepx4]
    numlist.sort()
    return numlist

