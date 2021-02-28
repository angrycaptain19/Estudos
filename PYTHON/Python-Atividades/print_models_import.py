# IMPORTANDO UM MÓDULO COMPLETO
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(
        unprinted_designs=unprinted_designs,
        completed_models=completed_models
        )
printing_functions.show_completed_models(
        completed_models=completed_models
        )

# IMPORTANDO FUNÇÕES ESPECÍFICAS
from printing_functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(
        unprinted_designs=unprinted_designs,
        completed_models=completed_models
        )
show_completed_models(
        completed_models=completed_models
        )

# USANDO A PALAVRA RESERVADA (as) PARA ATRIBUIR UM 'ALIAS' A UMA FUNÇÃO
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(
        unprinted_designs=unprinted_designs,
        completed_models=completed_models
        )
scm(
        completed_models=completed_models
        )

# USANDO A PALAVRA RESERVADA (as) PARA ATRIBUIR UM 'ALIAS' A UM MÓDULO
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(
        unprinted_designs=unprinted_designs,
        completed_models=completed_models
        )
pf.show_completed_models(
        completed_models=completed_models
        )

# IMPORTANDO TODAS AS FUNÇÕES DE UM MÓDULO
from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(
    unprinted_designs=unprinted_designs,
    completed_models=completed_models
    )
show_completed_models(
    completed_models=completed_models
    )