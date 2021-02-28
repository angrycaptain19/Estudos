import matplotlib.pyplot as plt

from random_walk import RandonWalk


# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandonWalk()
    rw.fill_walk()


    # Define o tamanho da janela de plotagem
    plt.figure(dpi=80, figsize=(15, 9))


    # Estiliza o nosso gráfico linear
    plt.plot(rw.x_values, rw.y_values, 
        linewidth=0.5,
        c='blue',
)
    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0,
    c='yellow',
    s=80
)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
    c='red',
    s=80
)


    # Remove os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    #plt.savefig('DADOS_GRAFICOS/movimento_molecular.png', bbox_inches='tight')
    plt.show()


    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
