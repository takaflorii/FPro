def magic(mat):
    n = len(mat)
    somas = set()
    
    somas.update(sum(row) for row in mat)
    somas.update(sum(mat[i][j] for i in range(n)) for j in range(n))
    somas.add(sum(mat[i][i] for i in range(n)))
    somas.add(sum(mat[i][n - 1 - i] for i in range(n)))
    
    return len(somas) == 1
