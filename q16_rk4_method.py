# Numerical Methods Lab Solution
# Run with: python filename.py

# Q16. RK4 method for y'=x+2y, y(0)=4, h=0.1; find y(0.1), y(0.2).
# Algorithm:
# 1. k1=f(x,y).
# 2. k2=f(x+h/2,y+h*k1/2).
# 3. k3=f(x+h/2,y+h*k2/2).
# 4. k4=f(x+h,y+h*k3).
# 5. y_(n+1)=y+h(k1+2k2+2k3+k4)/6.
# 6. Repeat for two steps.

def f(x,y): return x+2*y
def rk4(x,y,h):
    k1=f(x,y); k2=f(x+h/2,y+h*k1/2); k3=f(x+h/2,y+h*k2/2); k4=f(x+h,y+h*k3)
    return y+h*(k1+2*k2+2*k3+k4)/6
x=0.0; y=4.0
for target in [0.1,0.2]:
    y=rk4(x,y,0.1); x+=0.1
    print(f"y({target}) = {y:.10f}")
