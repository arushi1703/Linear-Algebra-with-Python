def matrix_input(m,rows,cols):
    for i in range(rows):
        for j in range(cols):
            m[i][j]=int(input(f"m[{i}][{j}]:"))

def gaussianElimination(m,rows,cols):
    for i in range(rows):
        if m[i][i] == 0.0:
            return "Invalid"
        for j in range(rows):
            if i != j:
                factor = m[j][i] /m[i][i]
                for k in range(cols):
                    m[j][k] = m[j][k] - factor * m[i][k]
    print("Echelon form:")
    [print(row) for row in m]
    
    for i in range(rows):
        factor = m[i][i]
        for j in range(cols):
            m[i][j] = round(m[i][j] / factor)
    print("Row cannonical form:")
    [print(row) for row in m]
    
    return [row[-1] for row in m]
    
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of cols:"))
print("Enter elements:")
m=[[0 for j in range(cols)]for i in range(rows)]
matrix_input(m,rows,cols)
print(f"[x,y,z]={gaussianElimination(m,rows,cols)}")

