'''import math

def matrix_input(m):
    for i in range(2):
        for j in range(2):
            m[i][j]=int(input(f"m[{i}][{j}]:"))

def eigenvector(vector,value):
    for i in range(len(vector)):
        for j in range(len(vector[0])):
            if i==j:
                vector[i][j]-=value
    return vector

def findRoots(a,b,c):
    d=(b*b)-(4*a*c)
    s1=(-b - math.sqrt(d))/(a+a)
    s2=(-b + math.sqrt(d))/(a+a)
    return [-s1,-s2]

def eigenvalues(vector):
    a=1
    b=vector[0][0]-vector[1][1]
    c=vector[0][0]*vector[1][1] - vector[0][1]*vector[1][0]

    roots=round(findRoots(a,b,c),2)
    print(f"Roots: {roots}")

    for root in roots:
        print(f"Eigenvector of {root} : {eigenvector(vector,root)}")
        

print("Enter matrix:")
m=[[0 for j in range(2)]for i in range(2)]
matrix_input(m)
eigenvalues(m)'''

import math

def eigenvector(vector, value):
	for i in range(len(vector)):
		for j in range(len(vector[0])):
			if i == j: vector[i][j] -= value
	return vector

def findRoots(a, b, c):
	d = (b*b) - (4*a*c)
	s1 = (-b - math.sqrt(d)) / (a + a)
	s2 = (-b + math.sqrt(d)) / (a + a)
	return [-s1, -s2]

def eigenvalue(vector):
	a = 1
	b = vector[0][0] + vector[1][1]
	c = vector[0][0] * vector[1][1] - vector[0][1] * vector[1][0]

	roots = findRoots(a, b, c)
	print(f"Roots: {roots}")

	for root in roots:
		print(f"Eigenvector for {root}: {eigenvector(vector, root)}")

m = [[1, 2], [0, 3]]
eigenvalue(m)
