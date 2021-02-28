lugares = ['paris', 'china', 'canadá', 'nova york']

###
print(lugares)

###
print("\nMostrsndo a lista em ordem alfabética:")
print(sorted(lugares))

print("\nMostrando a lista original novamente:")
print(lugares)

###
print("\nMudando a ordem da lista:")
lugares.reverse()
print(lugares)

print("\nDesfazendo a ordem da lista para a lista original:")
lugares.reverse()
print(lugares)

###
print("\nMudando a ordem da lista com o método sort():")
lugares.sort()
print(lugares)

print("\nMudando a ordem da lista para o sentido inverso:")
lugares.sort(reverse=True)
print(lugares)