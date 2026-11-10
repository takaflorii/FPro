def dot(u, v):
    return sum(x * y for x, y in zip(u, v))

def mult(M, N):
    if not M or not N or not M[0] or not N[0]:
        return []
    
    rows_M = len(M)
    cols_M = len(M[0])
    rows_N = len(N)
    cols_N = len(N[0])
    
    if cols_M != rows_N:
        return []
    
    N_cols = [[N[r][c] for r in range(rows_N)] for c in range(cols_N)]
    
    return [[dot(row, col) for col in N_cols] for row in M]