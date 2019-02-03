# Adatszerkezetek

# Listák, vagy tömbök, angolul list, array
nevek = [ 'Adam', 'Peter', 'Griffin' ]
pontszamok = [ 5, 1, 5, 5, 500, 10, 43, 56, 10 ]
# Listának eleme lehet bármi, akár másik lista is
adatok = [1, 2, [ 3, 4, 5 ], 'Szöveg', 1.2, 5 * 5, ['foo', 'bar']]

# Listák elemeit, az indexükkel érjük el:
print(nevek[1]) # Peter
print(adatok[2][0]) # 3

# Ciklusok
osszeg = 0

# bejáró, minden elemre lefut a ciklus magja
for pontszam in pontszamok:
    osszeg = osszeg + pontszam
    print(osszeg)

i = 0
# feltételes cilus, addig fut le újra és újra
# ameddig a benne lévő feltétel igaz, amint
# hamisra változik, a ciklus kilép
while i < len(nevek):
    print(nevek[i])
    i = i + 1

# Elágazás
if osszeg > 500:
    print('Jó sok pont!!!')
else:
    print('Ez ide kevés lesz!')

input('Üss entert a kilépéshez')
