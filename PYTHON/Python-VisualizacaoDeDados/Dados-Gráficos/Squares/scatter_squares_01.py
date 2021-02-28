import matplotlib.pyplot as plt


x_values = list(range(1001))
y_values = [x**2 for x in x_values]


plt.scatter(
    x_values, y_values, 
    c=y_values, 
    cmap=plt.cm.get_cmap("plasma"),
    edgecolor='none', 
    s=40,
    )

# Define o título do gráfico e nomeia os eixos
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# Define um intervalo para cada eixo
plt.axis([0,1100, 0,1100000])

#plt.savefig('DADOS_GRAFICOS/squares_plot.png', bbox_inches='tight')
plt.show()