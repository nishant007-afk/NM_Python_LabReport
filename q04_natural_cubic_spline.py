# Numerical Methods Lab Solution
# Run with: python filename.py

# Q4. Natural cubic spline for (0,1),(1,5),(2,17),(3,41); estimate y at x=1.6.
# Algorithm:
# 1. Set up the spline second derivatives M_i.
# 2. For a natural spline, M_0=M_n=0.
# 3. Solve the tridiagonal equations for interior M_i.
# 4. For x in [x_i,x_(i+1)], use the cubic spline formula:
#    S(x)=M_i*(x_(i+1)-x)^3/(6h)+M_(i+1)*(x-x_i)^3/(6h)
#       +(y_i-M_i*h^2/6)*(x_(i+1)-x)/h
#       +(y_(i+1)-M_(i+1)*h^2/6)*(x-x_i)/h.
# 5. Evaluate at x=1.6.

x=[0.,1.,2.,3.]; y=[1.,5.,17.,41.]
n=len(x)-1
h=[x[i+1]-x[i] for i in range(n)]
A=[[0.0,0.0],[0.0,0.0]]; B=[0.0,0.0]
for i in range(1,n):
    j=i-1
    A[j][j]=2*(h[i-1]+h[i])
    if j>0: A[j][j-1]=h[i-1]
    if j<n-2: A[j][j+1]=h[i]
    B[j]=6*((y[i+1]-y[i])/h[i]-(y[i]-y[i-1])/h[i-1])
det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
M=[0.0,(B[0]*A[1][1]-B[1]*A[0][1])/det,(A[0][0]*B[1]-A[1][0]*B[0])/det,0.0]

def spline(xq):
    i=next(k for k in range(n) if x[k]<=xq<=x[k+1])
    i=max(0,min(i,n-1)); hi=h[i]
    return (M[i]*(x[i+1]-xq)**3/(6*hi)+M[i+1]*(xq-x[i])**3/(6*hi)
            +(y[i]-M[i]*hi**2/6)*(x[i+1]-xq)/hi
            +(y[i+1]-M[i+1]*hi**2/6)*(xq-x[i])/hi)
print("Second derivatives M =", M)
print(f"Spline estimate at x=1.6 = {spline(1.6):.4f}")
