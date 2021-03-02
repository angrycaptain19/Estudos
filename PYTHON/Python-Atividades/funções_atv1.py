# NOMES DE CIDADES
def city_country(city, country):
    """Devolve o nome da cidade seguido de seu respectivo país."""
    cidade_país = city + ", " + country
    return cidade_país.title()

exibir = city_country(country='brasil', city='alagoinha')
print(exibir)

exibir = city_country(city='nova york', country='estados unidos')
print(exibir)

exibir = city_country(country='hungria', city='budapeste')
print(exibir)

# ÁLBUM
def make_album(artista, titulo, categoria=''):
    dados = {
        'artista': artista, 'titulo': titulo
    }
    if categoria:
        dados['categoria'] = categoria
    return(dados)

cantor = make_album(artista='mc rogerinho', titulo='na pressão', categoria='funk')
print(cantor)

cantor = make_album(titulo='sogra', artista='diguinho')
print(cantor)

cantor = make_album(categoria='sertanejo', artista='zé neto e cristiano', titulo='marcha de núpsias')
print(cantor)

# ÁLBUNS DOS USUÁRIOS
def artista_musica(artista, musica):
    """Devolve o nome do artista e sua musica."""
    return {
        'artista': artista, 'musica': musica
    }

while True:
    print("\nPor favor, informe os dados nescessários para essa pesquisa:")
    print("(digite 'q' e dê ENTER para sair da pesquisa)")

    artista = input("Nome do artista: ")
    if artista == 'q':
        break

    musica = input("Nome da musica: ")
    if musica == 'q':
        break

    exibir = artista_musica(artista=artista, musica=musica)
    print(exibir)