# Numerical Methods Lab Solution
# Run with: python filename.py

# Q6. Newton's forward difference formula: find dy/dx and d2y/dx2 at x=0.0.
# Algorithm:
# 1. Form the forward-difference table from the given y values.
# 2. Put p=(x-x0)/h; here x=x0=0, so p=0.
# 3. Differentiate Newton's forward interpolation polynomial.
# 4. At p=0 use:
#    dy/dx=(1/h)[D1-D2/2+D3/3-D4/4+D5/5]
#    d2y/dx2=(1/h^2)[D2-D3+11D4/12-5D5/6].
# 5. Substitute h=0.2 and print results.

y=[0.0000,0.1987,0.3894,0.5646,0.7174,0.8415]
h=0.2
table=[y[:]]
while len(table[-1])>1:
    table.append([table[-1][i+1]-table[-1][i] for i in range(len(table[-1])-1)])
D=[row[0] for row in table]
d1=(D[1]-D[2]/2+D[3]/3-D[4]/4+D[5]/5)/h
d2=(D[2]-D[3]+11*D[4]/12-5*D[5]/6)/h**2
print("Forward difference table:")
for row in table: print(row)
print(f"dy/dx at x=0.0 = {d1:.6f}")
print(f"d2y/dx2 at x=0.0 = {d2:.6f}")
