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

import math
import numpy as np
h=math.pi/24

def rhs(Y): return np.array([Y[1],-4*Y[0]],float)
def integrate(s):
    Y=np.array([0.0,s]); x=0.0
    for _ in range(2):
        k1=rhs(Y); k2=rhs(Y+h*k1/2); k3=rhs(Y+h*k2/2); k4=rhs(Y+h*k3)
        Y=Y+h*(k1+2*k2+2*k3+k4)/6; x+=h
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
