import matplotlib.pyplot as plt

imput_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(imput_values, squares, linewidth=5)


# Define o título do gráfico e nomeia os eixos
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# define o tamanho dos rótulos e das marcações
plt.tick_params(axis='both', labelsize=14)


plt.show()