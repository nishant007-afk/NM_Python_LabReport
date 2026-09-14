# Numerical Methods Lab Solution
# Run with: python filename.py

# Q17. Shooting method for y''=-4y, y(0)=0, y(pi/12)=0.25, h=pi/24, RK4.
# Algorithm:
# 1. Convert to first-order system: y'=v, v'=-4y.
# 2. Let the unknown initial slope be v(0)=s.
# 3. Choose two trial slopes, here s1=0 and s2=1.
# 4. Integrate each IVP from 0 to pi/12 using RK4 with h=pi/24.
# 5. Let F(s)=y(pi/12;s)-0.25. Use linear interpolation:
#    s=s1+(0.25-y1)*(s2-s1)/(y2-y1).
# 6. Integrate again using the estimated slope and report the BVP solution values.

pi=3.141592653589793
h=pi/24

def rhs(Y): return [Y[1],-4*Y[0]]
def add(Y,Z,c=1.0): return [Y[0]+c*Z[0],Y[1]+c*Z[1]]
def integrate(s):
    Y=[0.0,s]; x=0.0
    for _ in range(2):
        k1=rhs(Y); k2=rhs(add(Y,k1,h/2)); k3=rhs(add(Y,k2,h/2)); k4=rhs(add(Y,k3,h))
        Y=[Y[0]+h*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6,Y[1]+h*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6]; x+=h
    return Y
s1,s2=0.0,1.0
y1=integrate(s1)[0]; y2=integrate(s2)[0]
s=s1+(0.25-y1)*(s2-s1)/(y2-y1)
Y=integrate(s)
print(f"Trial y(pi/12) for s=0: {y1:.10f}")
print(f"Trial y(pi/12) for s=1: {y2:.10f}")
print(f"Estimated initial slope s = {s:.10f}")
print(f"Final y(pi/12) = {Y[0]:.10f}")
print("Expected exact solution is y=sin(2x)/2, so exact initial slope is 1.")
