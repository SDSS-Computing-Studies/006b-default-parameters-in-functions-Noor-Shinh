#! python3

import math

def tempConversion():
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



def cosineLaw():


def toRadians(y):
    x=(y*math.pi/180)
    return x




def solution():


def quadratic(a,b,c):
    x=(-b)+math.sqrt(b**-(4*a*c))/(2*a)
    y=((-b)-math.sqrt(b**-(4*a*c)))/(2*a)
    return x and y

c=quadratic(1,4,3)
print(c)
