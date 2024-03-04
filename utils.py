import matplotlib.pyplot as plt

U = 6.00

def f1(R):
    return U / R

R_values = range(1, 1000)
I_values = [f1(R) for R in R_values]

plt.plot(R_values, I_values)
plt.title('График зависимости I от R при U = 6.00В')
plt.xlabel('R')
plt.ylabel('I')
plt.grid(True)
plt.show()