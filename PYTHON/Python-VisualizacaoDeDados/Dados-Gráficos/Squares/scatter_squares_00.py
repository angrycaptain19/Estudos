import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 2, 9, 16, 25]


plt.scatter(y_values, x_values, s=100)

# Define o título do gráfico e nomeia os eixos
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()