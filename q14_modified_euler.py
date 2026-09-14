# Numerical Methods Lab Solution
# Run with: python filename.py

# Q14. Modified Euler (Heun) method for y'=x+2y, y(0)=2, h=0.1; find y(0.3).
# Algorithm:
# 1. Compute k1=f(x_n,y_n).
# 2. Predict y_p=y_n+h*k1.
# 3. Compute k2=f(x_n+h,y_p).
# 4. Correct using y_(n+1)=y_n+h(k1+k2)/2.
# 5. Repeat 3 times to reach x=0.3.

def f(x,y): return x+2*y
x=0.0; y=2.0; h=0.1
for _ in range(3):
    k1=f(x,y); yp=y+h*k1; k2=f(x+h,yp)
    y=y+h*(k1+k2)/2; x+=h
    print(f"x={x:.1f}, y={y:.8f}")
print(f"y(0.3) = {y:.8f}")
