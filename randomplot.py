#imports


import matplotlib.pyplot as plt 

import random 


#initializing variables


temp = 0

r = random.randint
x_vals = []
y_vals = []
z_vals = []


#adding random variables to the list


for i in range(1, 11):
    temp = r(1, 100)
    x_vals.append(temp)
for i in range(1, 11):
    temp = r(1, 100)
    y_vals.append(temp)
for i in range(1, 11):
    temp = r(1, 100)
    z_vals.append(temp)


#sorting lists


x_vals.sort()
y_vals.sort()
z_vals.sort()


#making 2nd graph even more random


temp = r(1,2)
if temp == 1:
    temp = y_vals
else:
    temp = x_vals

#making titles 


plt.title("Random plot")
plt.xlabel("x-values")
plt.ylabel("y-values")


#plotting and showing graph



plt.plot(x_vals, y_vals, color = "blue")
plt.plot(temp, z_vals, color = "red")
plt.show()