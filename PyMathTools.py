# PyMathTools v1.0 by Sean-e

def isprime(primenum):
    primenum = int(primenum)
    if primenum <= 1:
        return False
    elif primenum <= 3:
        return True
    elif primenum % 2 == 0 or primenum % 3 == 0:
        return False
    else:
        return True
    
def rectanglearea(area1, area2):
    area1 = int(area1)
    area2 = int(area2)
    return area1 * area2

def trianglearea(area1, area2):
    area1 = int(area1)
    area2 = int(area2)
    numresponse = area1 * area2
    return numresponse / 2

def squarearea(area1):
    area1 = int(area1)
    return area1 * area1

def cubevolume(length, width, height):
    length = int(length)
    width = int(width)
    height = int(height)
    return length * width * height

def triangleperimeter(side1, side2, side3):
    side1 = int(side1)
    side2 = int(side2)
    side3 = int(side3)
    return side1 + side2 + side3

def squareperimeter(side1):
    side1 = int(side1)
    return side1 * 4

def parallelogramperimeter(side1, side2):
    side1 = int(side1)
    side2 = int(side2)
    numresponse = side1 + side2
    return numresponse * 2

def circlediameter(radius):
    radius = int(radius)
    return radius * 2

def circlearea(radius):
    radius = int(radius)
    # Note: 3.14 is used for pi
    radius = radius * radius
    return radius * 3.14

def mathmean(sum, number):
    sum = int(sum)
    number = int(number)
    return sum / number

def slopeofaline(y2, y1, x2, x1):
    y2 = int(y2)
    y1 = int(y1)
    x2 = int(x2)
    x1 = int(x1)
    y = y2 - y1
    x = x2 - x1
    return y / x

def cylindervolume(radius, height):
    height = int(height)
    radius = int(radius)
    radius = radius * radius
    ans = radius * height
    # Using 3.14 for pi
    return ans * 3.14