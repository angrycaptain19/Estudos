import modulo_user as mu

import modulo_privilegios_e_admin as mpa

admin = mpa.Administrador(
        nome='alberto', sobrenome='mendes', idade=20, origem='brasil',
        sexo='masculino', escolaridade='médio completo'
        )
admin.descrição()
admin.privilégios.mostrar_privilégios()

usuario = mu.Usuário(
        nome='alberto', sobrenome='mendes', idade=20, origem='brasil',
        sexo='masculino', escolaridade='médio completo'
        )
admin.apresentar()
admin.descrição()