def matrix_input(m,rows,cols):
    for i in range(rows):
        for j in range(cols):
            m[i][j]=int(input(f"m[{i}][{j}]:"))

def print_matrix(matrix,rows,cols): 
    for a in range (rows): 
        for b in range (cols): 
            print(matrix[a][b]," ",end=' ') 
        print() 

def matrix_addition(): 
    if(rows1 != rows2 or cols1 != cols2): 
        print("Matrixes should be of equal dimensions") 
    else: 
        print("Result of Addition:") 
        add_matrix=[[0 for j in range (cols1)] for i in range (rows1)] 
        for a in range (rows1): 
            for b in range (cols1): 
                add_matrix[a][b]=matrix1[a][b]+matrix2[a][b] 
        print_matrix(add_matrix,rows1,cols1) 

def matrix_subtraction(): 
    if(rows1 != rows2 or cols1 != cols2):
        print("Matrixes should be of equal dimensions") 
    else: 
        print("Result of Subtraction:") 
        add_matrix=[[0 for j in range (cols1)] for i in range (rows1)] 
        for a in range (rows1): 
            for b in range (cols1): 
                add_matrix[a][b]=matrix1[a][b]-matrix2[a][b] 
        print_matrix(add_matrix,rows1, cols1)

def matrix_multiplication(): 
    if(cols1!=rows2): 
        print("Matrix multiplication not possiblle") 
    else: 
        print("Result of multiplication:") 
        multiplied_matrix=[[0 for j in range (cols1)] for i in range (rows1)] 
        for i in range (rows1): 
            for j in range (cols2): 
                for k in range (rows1): 
                    multiplied_matrix[i][j]+=m1[i][k]*m2[k][j] 
        print_matrix(multiplied_matrix,rows1, cols2)


rows1=int(input("Enter number of rows for matrix one: ")) 
cols1=int(input("Enter number of cols for matrix one: "))
m1=[[0 for j in range(cols1)]for i in range(rows1)]
matrix_input(m1,rows1,cols1)
print_matrix(m1,rows1,cols1)

rows2=int(input("Enter number of rows for matrix two: ")) 
cols2=int(input("Enter number of cols for matrix two: "))
m2=[[0 for j in range(cols2)]for i in range(rows2)]
matrix_input(m2,rows2,cols2)
print_matrix(m2,rows2,cols2)

print("addition for two matrices:") 
matrix_addition() 

print("subtraction for two matrices:") 
matrix_subtraction()

print("multiplication of two matrices:") 
matrix_multiplication() 
