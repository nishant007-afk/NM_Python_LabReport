# Numerical Methods Lab Solution
# Run with: python filename.py

# Q12. Picard method for y'=2x+y^2, y(0)=0; find y(0.3), third approximation.
# Algorithm:
# 1. Start with y0(x)=0.
# 2. Use y_(n+1)(x)=0+integral_0^x [2t+y_n(t)^2]dt.
# 3. First approximation: y1=x^2.
# 4. Second: y2=x^2+x^5/5.
# 5. Third: substitute y2 into the integral and expand/integrate.
# 6. Evaluate the third approximation at x=0.3.

x=0.3
# y3 = x^2 + x^5/5 + x^8/20 + x^11/275
# This follows from integrating 2t + (x^2+x^5/5)^2.
y3=x**2+x**5/5+x**8/20+x**11/275
print(f"Third Picard approximation y(0.3) = {y3:.10f}")
