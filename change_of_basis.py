def matrix_input(m,rows,cols):
    for i in range(rows):
        for j in range(cols):
            m[i][j]=int(input(f"m[{i}][{j}]:"))

def transpose(m):
    trans=[[0 for j in range(len(m[0]))]for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            trans[i][j]=m[j][i]
    return trans
    

def determinant(m):
    rows=len(m)
    cols=len(m[0])
    if rows==cols:
        if rows==2:
            return (m[0][0]*m[1][1] - m[0][1]*m[1][0])
        else:
            return (m[0][0]*minor(m,0,0) - m[0][1]*minor(m,0,1) + m[0][2]*minor(m,0,2))

def minor(m,row,col):
    temp=[]
    for i in range(3):
        if i==row:
            continue
        for j in range(3):
            if j==col:
                continue
            temp.append(m[i][j])
    return (temp[0]*temp[3] - temp[1]*temp[2])

def cofactor(m):
    rows=len(m)
    cols=len(m[0])
    c=[[0 for j in range(cols)]for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            c[i][j]=int(pow(-1,(i+j)))*minor(m,i,j)
    return c

def inverse(m):
    det=determinant(m)
    if len(m)==2:
        matrix=[[0 for j in range(2)]for i in range(2)]
        matrix[0][0]=m[1][1]
        matrix[0][1]=(-1)*m[0][1]
        matrix[1][0]=(-1)*m[1][0]
        matrix[1][1]=m[0][0]
        return matrix
    else:
        cofactor_m= cofactor(m)
        adj= transpose(cofactor)
        inv=[[0 for j in range(3)]for i in range(3)]
        for i in range(3):
            for j in range(3):
                inv[i][j]=round(adj[i][j]/det,2)
        return inv

def multiply(m1,m2):
    rows=len(m1)
    cols=len(m2[0])
    result=[[0 for j in range(cols)]for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(rows):
                result[i][j]+=m1[i][k]*m2[k][j]
    return result

def multiply_vector(m,v):
    v3=[0 for i in range(len(v))]
    k=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            v3[k]+=m[i][j]*v[j]
        k+=1
    return v3
                
         
def changeBasis(old, new, vector):
    adj1=transpose(old)
    v1=multiply_vector(adj1,vector)
    print(f"In standard basis:{v1}")
    adj2=transpose(new)
    inv2=inverse(adj2)
    result=multiply_vector(inv2,v1)
    print("In new basis:")
    print(result)



rows=cols=int(input("Enter dimensions:"))
print("Enter old basis:")
m1=[[0 for j in range(cols)]for i in range(rows)]
matrix_input(m1,rows,cols)

print("Enter new basis:")
m2=[[0 for j in range(cols)]for i in range(rows)]
matrix_input(m2,rows,cols)


print("Enter vector:")
v=[0 for i in range(rows)]
for i in range(rows):
    v[i]=int(input(f"v[{i}]:"))

changeBasis(m1,m2,v)

