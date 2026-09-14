# Numerical Methods Lab Solution
# Run with: python filename.py

# Q11. Taylor series method for y'=2x+y, y(0)=3, h=0.2; find y(0.2), y(0.4).
# Algorithm:
# 1. From y'=2x+y obtain y''=2+2x+y.
# 2. Differentiating again gives y'''=2+2x+y and y''''=2+2x+y.
# 3. Use y(x+h)=y+h*y'+h^2*y''/2!+h^3*y'''/3!+h^4*y''''/4!.
# 4. Start with x=0,y=3 and take two steps of h=0.2.
# 5. Print both approximations.

def step(x,y,h):
    yp=2*x+y; y2=2+yp; y3=2+yp; y4=2+yp
    return y+h*yp+h*h*y2/2+h**3*y3/6+h**4*y4/24
x=0.0; y=3.0
for target in [0.2,0.4]:
    y=step(x,y,0.2); x+=0.2
    print(f"y({target}) = {y:.10f}")
