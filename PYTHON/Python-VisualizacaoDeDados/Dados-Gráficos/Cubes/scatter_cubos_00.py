import matplotlib.pyplot as plt

x_valores = list(range(5001))
y_valores = [x**3 for x in x_valores]


plt.scatter(
    x_valores, y_valores,
    c=y_valores,
    cmap=plt.cm.get_cmap("magma"),
    edgecolor='none',
    s=40,
    )

# Define o título do gráfico e nomeia os eixos
plt.title("Números ao cubo", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Valores ao quadrado", fontsize=14)

# Define o intervalo de cada eixo
plt.axis([0,5100, 0,1.30e11])

plt.savefig('DADOS_GRAFICOS/cubos_plot.png', bbox_inches='tight')
plt.show()
