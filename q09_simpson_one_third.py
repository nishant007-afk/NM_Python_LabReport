# Numerical Methods Lab Solution
# Run with: python filename.py

# Q9. Simpson's 1/3 Rule: integral from 0 to 2 of x^2+1, n=6.
# Algorithm:
# 1. Compute h=(b-a)/n; n must be even.
# 2. Evaluate f(x)=x^2+1 at all grid points.
# 3. Use I=h/3*[f0+fn+4(sum of odd-index terms)+2(sum of even-index terms)].
# 4. Print the result.

n=6; a=0.0; b=2.0; h=(b-a)/n
x=[a+i*h for i in range(n+1)]
f=[t*t+1 for t in x]
I=h/3*(f[0]+f[-1]+4*sum(f[1:-1:2])+2*sum(f[2:-1:2]))
print(f"Integral = {I:.6f}")
