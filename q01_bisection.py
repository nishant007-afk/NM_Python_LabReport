# Numerical Methods Lab Solution
# Run with: python filename.py

# Q1. Find a real root of x^3 - 2x - 3 = 0 by Bisection Method.
# Algorithm:
# 1. Define f(x)=x^3-2x-3.
# 2. Choose an interval [a,b] such that f(a)*f(b)<0.
# 3. Compute c=(a+b)/2.
# 4. If f(a)*f(c)<0, set b=c; otherwise set a=c.
# 5. Repeat until the interval/error is sufficiently small.
# 6. Round the root to 3 decimal places.

def f(x): return x**3 - 2*x - 3

a, b = 1.0, 2.0
for i in range(100):
    c = (a+b)/2
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    if abs(b-a) < 0.5*10**(-3):
        break
print(f"Root = {c:.3f}")
