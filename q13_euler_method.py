# Numerical Methods Lab Solution
# Run with: python filename.py

# Q13. Euler's method for y'=2x+y, y(0)=3, h=0.1; find y(0.5).
# Algorithm:
# 1. Start from (x0,y0)=(0,3).
# 2. Calculate f=2x+y.
# 3. Use Euler formula y_(n+1)=y_n+h*f(x_n,y_n).
# 4. Increase x by h and repeat until x=0.5.

x=0.0; y=3.0; h=0.1
while x < 0.5-1e-12:
    y=y+h*(2*x+y); x+=h
    print(f"x={x:.1f}, y={y:.6f}")
print(f"y(0.5) = {y:.6f}")
