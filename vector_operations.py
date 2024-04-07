from math import *

def userinput():
    rows=int(input("Enter number of rows:"))
    vector=[0 for i in range(rows)]
    print("Enter numbers:")
    for i in range(rows):
        vector[i]=int(input(f"v[{i}]:"))
    return vector

def add(v1,v2):
    if len(v1)!=len(v2):
        print("Addition not possible")
        return None
    v3=[0 for i in range(len(v1))]
    for i in range(len(v1)):
        v3[i]=v1[i]+v2[i]
    return v3

def sub(v1,v2):
    if len(v1)!=len(v2):
        print("Subtraction not possible")
        return None
    v3=[0 for i in range(len(v1))]
    for i in range(len(v1)):
        v3[i]=v1[i]-v2[i]
    return v3

def dot_product(v1,v2):
    if len(v1)!=len(v2):
        print("Dot product not possible")
        return None
    result=0
    for i in range(len(v1)):
        result+=v1[i]*v2[i]
    return result

def determinant(v1,v2):
    v3=[]
    if len(v1)==2:
        v3=[ v1[0]*v2[1], v1[1]*v2[0]]
    else:
        d1=(v1[1]*v2[2])-(v1[2]*v2[1])
        d2=(v1[0]*v2[2])-(v1[2]*v2[0])
        d3=(v1[0]*v2[1])-(v1[1]*v2[0])
        v3=[d1,(-1)*d2,d3]
    return v3

def distance(v1,v2):
    d=0
    for i in range(len(v1)):
        d+=((v1[i]-v2[i])**2)
    return sqrt(d)

def magnitude(v):
    s=0
    for i in v:
        s+=(i**2)
    return sqrt(s)

def angle(v1,v2):
    ang=dot_product(v1,v2)/(magnitude(v1)*magnitude(v2))
    return ang

def projection(u,v):
    proj=dot_product(u,v)/pow(magnitude(v),2)
    proj2=[0 for i in range(len(u))]
    for i in range(len(u)):
        proj2[i]=round(proj*v[i],2)
    return proj2

print("First vector:")
v1=userinput()
print("Seond vector:")
v2=userinput()

print("Result of addition:")
v3=add(v1,v2)
print(v3)

print("Result of subtraction:")
v4=sub(v1,v2)
print(v4)

print("Dot product: ",dot_product(v1,v2))

cp=determinant(v1,v2)
print("Cross product:",cp[0],"i ",cp[1],"j ",cp[2],"k")

print("Distance: ",round(distance(v1,v2),2))

print("Angle:", round(angle(v1,v2),2))

print("Projection of v1 onto v2:",projection(v1,v2))
print("Projection of v2 onto v1:",projection(v2,v1))
