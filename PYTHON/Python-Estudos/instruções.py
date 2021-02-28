answer = 17

if answer != 42: # '!=' siguinifica 'DIFERENTE DE...?'
    print("That is not thee correct answer. Please try angain!")

# VERIFICANDO A IGUALDADE
car = 'bmw'
car == 'bmw'    # o '==' pergunta se a variavel é = valor de interesse
# True

# IGNORANDO AS DIFERENÇAS ENTRE LETRAS MAIÚSCULAS E MINÚSCULAS
car = 'Audi'
car == 'audi' # maiúscula e minúscula na mesma palavra se tornam diferentes
# False

car = 'Audi'
car.lower() == 'audi' # deixa tudo minúsculo com o método lower
# true

# COMPARAÇÕES NUMÉRICAS
age = 18
age == 18
# True

age = 19
age < 21
# True
age <= 21
# True
age > 21
# False
age >= 21
# False

# USANDO and PARA TESTAR NOVAS CONDIÇÕES
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21) # a instrução 'and' diz se as duas expressões são True ou false
# False

age_1 = 22
(age_0 >= 21) and (age_1 >= 21)
# True

# USANDO or PARA TESTAR VARIAS CONDIÇÕES
age_0 = 22
age_1 = 18
(age_0 >= 21) or (age_1 >= 21) # a instrução 'or' pede para qualquer uma das expressões sejam True ou false
# True

age_0 = 18
(age_0 >= 21) or (age_1 >= 21)
# False

# VERIFICANDO SE UM VALOR ESTÁ NA LISTA
requested_toppings = ['mushrroms', 'onions', 'pineapple']

'mushrooms' in requested_toppings   # instrução 'in' (se x estiver em y)
# True
'pepperoni' in requested_toppings
# False

# VERIFICANDO SE UM VALOR NÃO ESTÁ EM UMA LISTA
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:    # instrução 'not' (se X 'não estiver' em Y)
    print("\n" + user.title() + ", you can post a response if you wish.")

# EXPRESSÕES BOOLEANAS
game_active = True
can_edit = False