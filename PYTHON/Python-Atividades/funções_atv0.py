# LIVRO FAVORITO
def favorite_book(livro):
    """Exibe o livro favorito"""
    print("O meu livro favorio é " + livro.title() + ".")

favorite_book('alice no país das maravilhas')

# MENSAGEM
def display_message(message):
    """Mostra o que eu aprendi até agora"""
    print("\nO que aprendi até agora foi:" + message)

display_message('\ndef: Definição de função.')
display_message('\nfunção(): Nome da função.')
display_message('\ndocstring("""): Descrição do que a função faz (apenas uma documentação).')
display_message('\ncorpo da função: Todas a linhas indentadas que forma o bloco de instrução.')
display_message('\nparâmetro: Informação que fica dentro do () da função.')
display_message('\nargumento: Informação que é guardada dentro do parâmetro.'
    ' Informação passada para uma função em sua chamada.')

# CAMISETA
def make_skirt(mensagem, tamanho):
    """Exibe o tamanho e a mensagem estampada na camiseta"""
    print("\nTamanho: " + tamanho.title())
    print("Mensagem na camiseta: " + mensagem)

make_skirt('Deus é vida!', 'm')
make_skirt(tamanho='p', mensagem='I love programar!')

# MATÉRIA FAVORITA
def matéria_favorita(
    pessoa, frase='Eu amo Python!', matéria='matemática'
    ):
    """Exibe o nome da pessoa e a matéria que mais gosta"""
    print("\nNome: " + pessoa.title())
    print(pessoa.title() + " gosta muito de " + matéria.title() + ".")
    print("Sua frase favorita é: " + frase)

matéria_favorita(pessoa='alberto')
matéria_favorita(pessoa='whanderson', frase='Eu amo engenharia!')
matéria_favorita(pessoa='samara', frase='PF, sim senhor!', matéria='direito penal')

# CIDADES
def describe_city(cidade, país='brasil'):
    """Exibe o nome da cidade e o seu país respectivo."""
    print("\n" + cidade.title() + " está localizada na/o(as/os) "
        + país.title() + ".")

describe_city(cidade='são paulo')
describe_city(país='canadá', cidade='toronto')
describe_city(cidade='nova york', país='estados unidos')