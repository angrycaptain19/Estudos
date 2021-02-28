# IMPORTANDO UM MÓDULO COMPLETO
import pizza_função

pizza_função.make_pizza(16, 'pepperoni')
pizza_função.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# IMPORTANDO FUNÇÕES ESPECÍFICAS
from pizza_função import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# USANDO A PALAVRA RESERVADA (as) PARA ATRIBUIR UM 'ALIAS' A UMA FUNÇÃO
from pizza_função import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# USANDO A PALAVRA RESERVADA (as) PARA ATRIBUIR UM 'ALIAS' A UM MÓDULO
import pizza_função as pf

pf.make_pizza(16, 'pepperoni')
pf.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# IMPORTANDO TODAS AS FUNÇÕES DE UM MÓDULO
from pizza_função import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')