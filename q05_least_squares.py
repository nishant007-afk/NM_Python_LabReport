# Numerical Methods Lab Solution
# Run with: python filename.py

# Q5. Fit y=a+bx by the Least Squares Method.
# Algorithm:
# 1. Enter x and y data.
# 2. Compute n, sum(x), sum(y), sum(x^2), sum(xy).
# 3. Calculate b=[n*sum(xy)-sum(x)*sum(y)]/[n*sum(x^2)-(sum(x))^2].
# 4. Calculate a=[sum(y)-b*sum(x)]/n.
# 5. Write the fitted line y=a+bx.

x=[2,4,6,8,10]; y=[3.3,6.8,10.5,13.9,17.6]
n=len(x)
sx=sum(x); sy=sum(y); sx2=sum(v*v for v in x); sxy=sum(a*b for a,b in zip(x,y))
b=(n*sxy-sx*sy)/(n*sx2-sx*sx)
a=(sy-b*sx)/n
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"Fitted line: y = {a:.4f} + {b:.4f}x")
