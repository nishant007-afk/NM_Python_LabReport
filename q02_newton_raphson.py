# Numerical Methods Lab Solution
# Run with: python filename.py

# Q2. Find a real root of x^3 - 3x - 7 = 0 by Newton-Raphson Method.
# Algorithm:
# 1. Define f(x)=x^3-3x-7 and f'(x)=3x^2-3.
# 2. Choose an initial approximation x0=2.
# 3. Use x_(n+1)=x_n-f(x_n)/f'(x_n).
# 4. Repeat until successive values differ by less than the required tolerance.
# 5. Round the root to 4 decimal places.

def f(x): return x**3 - 3*x - 7
def df(x): return 3*x**2 - 3
x=2.0
for i in range(100):
    xn=x-f(x)/df(x)
    if abs(xn-x)<0.5e-4:
        x=xn; break
    x=xn
print(f"Root = {x:.4f}")