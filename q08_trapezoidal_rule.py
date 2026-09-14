# Numerical Methods Lab Solution
# Run with: python filename.py

# Q8. Trapezoidal Rule: integral from 1 to 4 of 1/(1+x), n=6.
# Algorithm:
# 1. Divide [a,b] into n equal intervals; h=(b-a)/n.
# 2. Compute x_i=a+ih and f_i=1/(1+x_i).
# 3. Use I=h/2*[f0+fn+2(f1+...+f(n-1))].
# 4. Print the approximate integral.

n=6; a=1.0; b=4.0; h=(b-a)/n
x=[a+i*h for i in range(n+1)]
f=[1/(1+t) for t in x]
I=h/2*(f[0]+f[-1]+2*sum(f[1:-1]))
print("x =",x); print("f(x) =",f)
print(f"Integral = {I:.6f}")
