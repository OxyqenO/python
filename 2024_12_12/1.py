#a

zbior = {'Polska', 'Anglia', 'Portugalia', 'Rosja', 'Ukraina'}
print(zbior)
zbior.add('Polska')
print(zbior)

print('Polska' in zbior)

zbior.remove('Polska')
print(zbior)

#
Miasta1 = {'Szczytno', 'Olsztyn', 'Warszawa', 'Poznań', 'Gdańsk'}
Miasta2 = {'Szczytno', 'Zakopane', 'Warszawa', 'Lublin', 'Zatorze'}

print(Miasta1.union(Miasta2))

print(Miasta1.intersection(Miasta2))

print(Miasta1.difference(Miasta2))

print(Miasta1.issubset(Miasta2))