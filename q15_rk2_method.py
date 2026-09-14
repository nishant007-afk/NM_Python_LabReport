# Numerical Methods Lab Solution
# Run with: python filename.py

# Q15. RK2 (midpoint) method for y'=2x+y, y(0)=2, h=0.1; find y(0.2).
# Algorithm:
# 1. k1=f(x_n,y_n).
# 2. k2=f(x_n+h/2, y_n+h*k1/2).
# 3. y_(n+1)=y_n+h*k2.
# 4. Repeat for two steps and report y(0.2).

def f(x,y): return 2*x+y
x=0.0; y=2.0; h=0.1
for _ in range(2):
    k1=f(x,y); k2=f(x+h/2,y+h*k1/2)
    y=y+h*k2; x+=h
    print(f"x={x:.1f}, y={y:.8f}")
print(f"y(0.2) = {y:.8f}")
