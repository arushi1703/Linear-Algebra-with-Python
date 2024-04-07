def matrix_input(m,rows,cols):
    for i in range(rows):
        for j in range(cols):
            m[i][j]=int(input(f"m[{i}][{j}]:"))

def print_matrix(matrix,rows,cols): 
    for a in range (rows): 
        for b in range (cols): 
            print(matrix[a][b]," ",end=' ') 
        print() 

def echelon(m,rows,cols):
    for i in range(rows):
        if m[i][i]==0:
            return "Invalid"
        for j in range(rows):
            if i!=j:
                factor=m[j][i]/m[i][i]
                for k in range(cols):
                    m[j][k]= m[j][k]- factor*m[i][k]

    result=[]
    for row in m:
        if any(row):
            result.append(row)
    return result

def rowCanonical(m):
    m = echelon(m)
    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        factor = m[i][i]
        for j in range(cols):
            m[i][j] = round(m[i][j] / factor)
    [print(row) for row in m]
    

rows=int(input("Enter number of rows: ")) 
cols=int(input("Enter number of cols: "))
m=[[0 for j in range(cols)]for i in range(rows)]
matrix_input(m,rows,cols)
print_matrix(m,rows,cols)



