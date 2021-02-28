# MÁGICOS
def show_magicians(magicians):
    """Exibe o nome de cada mágico da lista."""
    for magician in magicians:
        msg = "\nApresentando o mágico " + magician.title() + "!"
        print(msg)

magician_list = ['tirulipa', 'pogbá', 'richard']
show_magicians(magicians=magician_list)

# GRANDES MÁGICOS e MÁGICOS INALTERADOS
def mostrar_mágicos(magicians, presented_magicians):
    """
    Exibe o nome de cada mágico da lista.
    Transfere os nomes apresentados para presented_magicians após a apresentação.
    """

    while magicians:
        current_magician = magicians.pop()

        # Simula a apresentação do mágico
        print("\nApresentando o mágico " + current_magician.title() + "!")
        presented_magicians.append(current_magician)

def make_great(presented_magicians):
    """Exibe o nome do mágico de forma melhor."""
    for magicians in presented_magicians:
        print("\nApresentando o Grande " + magicians.title() + "!")

magicians = ['richard', 'pogbá', 'salamandra']
presented_magicians = []

mostrar_mágicos(magicians=magicians[:], presented_magicians=presented_magicians)
make_great(presented_magicians=presented_magicians)
