# Numerical Methods Lab Solution
# Run with: python filename.py

# Q19. Laplace's equation as given: d2f/dx2+d2f/dy2=3x+2y, f=1 on boundary, 0<=x,y<=3, h=1.
# Algorithm:
# 1. Make a 4x4 grid because x,y=0,1,2,3.
# 2. Put f=1 on all boundary grid points.
# 3. For each interior point use the five-point formula:
#    (f_E+f_W+f_N+f_S-4f_P)/h^2 = 3x+2y.
# 4. Rearrange: 4f_P = f_E+f_W+f_N+f_S - h^2*(3x+2y).
# 5. Solve the four simultaneous equations for the four interior points.

import numpy as np
pts=[(1,1),(1,2),(2,1),(2,2)]; idx={p:i for i,p in enumerate(pts)}
A=np.zeros((4,4)); B=np.zeros(4); h=1.0
for p,i in idx.items():
    x,y=p; A[i,i]=4; B[i]=-(3*x+2*y)*h*h
    for q in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if q in idx: A[i,idx[q]]-=1
        else: B[i]+=1
u=np.linalg.solve(A,B)
print("Interior values:")
for p,i in idx.items(): print(f"f{p} = {u[i]:.6f}")
print("Grid (rows are y-levels in increasing y if displayed by x,y indexing):")
grid=np.full((4,4),1.0)
for p,i in idx.items(): grid[p]=u[i]
print(grid)
