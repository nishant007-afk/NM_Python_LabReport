# Numerical Methods Lab Solution
# Run with: python filename.py

# Q3. Linear interpolation for (2,5), (6,37), estimate y at x=4.0.
# Algorithm:
# 1. Take the two known points (x0,y0) and (x1,y1).
# 2. Use y = y0 + (x-x0)*(y1-y0)/(x1-x0).
# 3. Substitute x=4.0 and print the estimate.

x0,y0=2,5
x1,y1=6,37
x=4.0
y=y0+(x-x0)*(y1-y0)/(x1-x0)
print(f"Estimated y at x={x} = {y:.4f}")
