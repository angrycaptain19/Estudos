def cidades(cidade, país, população=''):
    """Gera o nome da cidade seguida de seu respectivo país e sua 
    população total."""
    if população:
        conteudo = (cidade + ", " + país + 
            " - População: " + str(população) + " habitantes.")
    else:
        conteudo = cidade + ", " + país
    return conteudo.title()