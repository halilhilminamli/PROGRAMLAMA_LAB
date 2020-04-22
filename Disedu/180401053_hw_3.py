from sympy import * 
import matplotlib.pyplot as plt
x,n,p,k = Symbol('x'),Symbol('n'),Symbol('p'),Symbol('k')
f = binomial(n,k) * p ** k * (1-p)**(n-k)
plot(f.subs({p:0.58,k:10}),(n,1,40),title="Binomial Distribution Grafigi")
xDegerleri,yDegerleri=[],[]
for i in range(1,40):
    y = f.subs({p:0.58,k:10,n:i})
    xDegerleri.append(i)
    yDegerleri.append(y)
plt.plot(xDegerleri,yDegerleri)
plt.show()
