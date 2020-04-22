#n=Bütün deney sayısı
#r=İstenilen değerin tekrar sayısı (r tane gelme gibi)


from sympy import Symbol,pprint
import sympy as sym

p = Symbol('p')
x = Symbol('x')
n = Symbol('n')

my_f_3_part_0 = sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
pprint(my_f_3_part_0)

my_f_3_part_1 = p**x
pprint(my_f_3_part_1)

my_f_3_part_2 = (1-p)**(n-x)
pprint(my_f_3_part_2)

my_f_3 = my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
pprint(my_f_3)


sym.plot(my_f_3.subs({p:0.5,n:50}),(x,0,50),title ="Binomal distribution plot for n=50")
sym.show()


import matplotlib.pyplot as plt

x_value=[]
y_value=[]
for value in range(50):
    y=my_f_3.subs({p:0.5,n:50,x:value}).evalf()
    y_value.append(y)
    x_value.append(value)
plt.plot(x_value,y_value)
plt.show()
