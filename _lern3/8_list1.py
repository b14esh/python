cities = ['New York', 'Mosckow', 'new dehli', 'Simferopol', 'Toronto']
print(cities)
print(len(cities))
print(cities[0])
print(cities[4])
print(cities[-1])
print(cities[-2])
print(cities[2].title())
print(cities[2].upper())

cities[2] = 'Tula'
print(cities)

cities.append('Kursk')
print(cities)

cities.append('Yalta')
print(cities)

cities.insert(0, 'Zorcia')
print(cities)

cities.insert(2, 'Feadosya')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print("Delieted city is: "  + deleted_city)
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)

