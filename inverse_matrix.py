def matrix_input(m,rows,cols):
    for i in range(rows):
        for j in range(cols):
            m[i][j]=int(input(f"m[{i}][{j}]:"))

def print_matrix(matrix,rows,cols): 
    for a in range (rows): 
        for b in range (cols): 
            print(matrix[a][b]," ",end=' ') 
        print()

def determinant(m,rows,cols):
    global flag
    if rows==cols:
        if rows==2:
            return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
        else:
            return (m[0][0]*minor(m,0,0) - m[0][1]*minor(m,0,1) + m[0][2]*minor(m,0,2))
    else:
        flag=False
        return "The determinant and inverse of the matrix is not possible"

def minor(m,row,col):
    temp=[]
    for i in range(3):
        if i==row:
            continue
        for j in range(3):
            if j==col:
                continue
            temp.append(m[i][j])
    return ((temp[0]*temp[3])-(temp[1]*temp[2]))
            
def cofactor(m,rows,cols):
    c=[[0 for j in range(cols)]for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            c[i][j]=int(pow(-1,(i+j)))*minor(m,i,j)
    return c

def transpose(m):
    trans=[[0 for j in range(len(m[0]))]for i in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            trans[i][j]=m[j][i]
    return trans

def inverse(m,rows,cols,det):
    inv=[[0 for j in range(rows)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            inv[i][j]=round(m[i][j]/det,2)
    return inv
        
    
rows=int(input("Enter number of rows for matrix: ")) 
cols=int(input("Enter number of cols for matrix: "))
m=[[0 for j in range(cols)]for i in range(rows)]
matrix_input(m,rows,cols)
print_matrix(m,rows,cols)

flag=True

det=determinant(m,rows,cols)
print("determinant of the matrix: ",determinant(m,rows,cols))

if flag:
    if rows==3:
        c=cofactor(m,rows,cols)
        print("Cofactor matrix:")
        print_matrix(c,rows,cols)

        adj=transpose(c)
        print("Adjoint matrix:")
        print_matrix(adj,rows,cols)

        inv=inverse(adj,rows,cols,det)
        print("Inverse matrix:")
        print_matrix(inv,rows,cols)
        
    if rows==2:
        matrix=[[0 for j in range(2)]for i in range(2)]
        matrix[0][0]=m[1][1]
        matrix[0][1]=(-1)*m[0][1]
        matrix[1][0]=(-1)*m[1][0]
        matrix[1][1]=m[0][0]

        print("Adjoint matrix:")
        print_matrix(matrix,rows,cols)

        inv=inverse(matrix,2,2,det)
        print("Inverse matrix:")
        print_matrix(inv,rows,cols)
            
        

        
