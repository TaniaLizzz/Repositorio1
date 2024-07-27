nombres = ['Juan', 'Luis', 'Melissa']
print(nombres)
print(nombres[1])
print(nombres[-1])
print(nombres[1:])
nombres[1] = 'Maria'
print(nombres)

print(len(nombres))
nombres.append('Johan')
print(nombres)

nombres.insert(1, 'Laura')
print(nombres)

nombres.remove('Laura')
print(nombres)

nombres.pop()
print(nombres)

del nombres[0]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombres)