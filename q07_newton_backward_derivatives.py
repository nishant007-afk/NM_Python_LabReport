# Numerical Methods Lab Solution
# Run with: python filename.py

# Q7. Newton's backward difference formula at x=0.6.
# Note: The requested x=0.6 is near the end, while the backward formula is based at
# the LAST point x_n=1.0. Therefore p=(0.6-1)/0.2=-2 and the formula interpolates.
# Algorithm:
# 1. Build the ordinary difference table.
# 2. Read backward differences from the last element of each row.
# 3. Form Newton's backward polynomial using p=(x-x_n)/h.
# 4. Differentiate the polynomial with respect to p and divide by h (first derivative)
#    or h^2 (second derivative).
# 5. Evaluate at p=-2.

import math
x=[0,0.2,0.4,0.6,0.8,1]
y=[0.0000,0.1987,0.3894,0.5646,0.7174,0.8415]
h=0.2
# backward differences at x_n are y_n-y_(n-1), etc.
table=[y[:]]
while len(table[-1])>1:
    table.append([table[-1][i+1]-table[-1][i] for i in range(len(table[-1])-1)])
back=[table[k][-1] for k in range(len(table))]
p=(0.6-x[-1])/h
# Derivatives of the backward basis p(p+1)...(p+k-1)/k! computed numerically by products.
def basis(k,p):
    r=1.0
    for j in range(k): r*=p+j
    return r/math.factorial(k)
def basis_d1(k,p):
    if k==0:return 0.0
    s=0.0
    for m in range(k):
        prod=1.0
        for j in range(k):
            if j!=m: prod*=p+j
        s+=prod
    return s/math.factorial(k)
def basis_d2(k,p):
    if k<2:return 0.0
    s=0.0
    for m in range(k):
        for r in range(k):
            if r==m: continue
            prod=1.0
            for j in range(k):
                if j!=m and j!=r: prod*=p+j
            s+=prod
    return s/math.factorial(k)
d1=sum(back[k]*basis_d1(k,p) for k in range(len(back)))/h
d2=sum(back[k]*basis_d2(k,p) for k in range(len(back)))/h**2
print("Backward differences =", back)
print("p =",p)
print(f"dy/dx at x=0.6 = {d1:.6f}")
print(f"d2y/dx2 at x=0.6 = {d2:.6f}")
