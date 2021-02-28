import matplotlib.pyplot as plt

eixo_x = [1, 2, 3, 4, 5]
eixo_y = [1, 8, 27, 64, 125]
plt.plot(eixo_x, eixo_y, linewidth=7)


# Define o título do gráfico e nomeia os eixos
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# define o tamanho dos rótulos e das marcações
plt.tick_params(axis='both', labelsize=14)


plt.show()