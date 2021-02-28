def obter_nome_completo(nome, sobrenome, meio=''):
    """Gera um nome completo formatado de forma elegante."""
    if meio:
        nome_completo = nome + " " + meio + " " + sobrenome
    else:
        nome_completo = nome + " " + sobrenome
    return nome_completo.title()