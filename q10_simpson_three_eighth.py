# Numerical Methods Lab Solution
# Run with: python filename.py

# Q10. Simpson's 3/8 Rule: integral from 0 to 3 of 1/(2+x^2), n=6.
# Algorithm:
# 1. Compute h=(b-a)/n; n must be a multiple of 3.
# 2. Evaluate f(x)=1/(2+x^2).
# 3. Use I=3h/8*[f0+fn+3(sum of terms whose index is not a multiple of 3)
#    +2(sum of interior terms whose index is a multiple of 3)].
# 4. Print the result.

n=6; a=0.0; b=3.0; h=(b-a)/n
x=[a+i*h for i in range(n+1)]
f=[1/(2+t*t) for t in x]
I=3*h/8*(f[0]+f[-1]+3*(f[1]+f[2]+f[4]+f[5])+2*f[3])
print(f"Integral = {I:.6f}")
