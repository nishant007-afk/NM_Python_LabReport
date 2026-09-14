# Numerical Methods Lab Solution
# Run with: python filename.py

# Q18. Poisson equation: d2f/dx2+d2f/dy2=x+2y, f=3 on boundary, 0<=x,y<=3, h=1.
# Algorithm:
# 1. Make a 4x4 grid because x,y=0,1,2,3.
# 2. Put f=3 on all boundary grid points.
# 3. For each interior point use the five-point formula:
#    (f_E+f_W+f_N+f_S-4f_P)/h^2 = x+2y.
# 4. Rearrange: 4f_P = f_E+f_W+f_N+f_S - h^2*(x+2y).
# 5. Solve the four simultaneous equations for the four interior points.

pts=[(1,1),(1,2),(2,1),(2,2)]; idx={p:i for i,p in enumerate(pts)}
A=[[0.0]*4 for _ in range(4)]; B=[0.0]*4; h=1.0; u=[0.0]*4
for p,i in idx.items():
    x,y=p; A[i][i]=4; B[i]=-(x+2*y)*h*h
    for q in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if q in idx: A[i][idx[q]]-=1
        else: B[i]+=3
for _ in range(100):
    u=[(B[i]-sum(A[i][j]*u[j] for j in range(4) if j!=i))/4 for i in range(4)]
print("Interior values:")
for p,i in idx.items(): print(f"f{p} = {u[i]:.6f}")
print("Grid (rows are y-levels in increasing y if displayed by x,y indexing):")
grid=[[3.0]*4 for _ in range(4)]
for p,i in idx.items(): grid[p[0]][p[1]]=u[i]
print(grid)
