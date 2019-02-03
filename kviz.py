kerdesek = [
    'Mi az élet értelme?',
    'Mi az a váltotó?',
    'Mennyi egy töketlen fecske repülési sebessége?',
    'Hány programozó kell egy villanykörte kicseréléséhez?'
]

valaszok = [
    ['A sör', '42'],
    ['Adat terület', 'Egy kifejezés'],
    ['Attól függ, afrikai vagy európai?', 'Azt nem tudom'],
    [2 ** 10, 'Egy sem, mert ez hardverhiba']
]

helyes = [
    'b',
    'a',
    'a',
    'b'
]

kerdesindex = 0
while kerdesindex < len(kerdesek):
    print(kerdesek[kerdesindex])
    print('a =', valaszok[kerdesindex][0])
    print('b =', valaszok[kerdesindex][1])

    valasz = input('Add meg a választ! ')
    
    h = helyes[kerdesindex]
    if valasz == h:
        print('Helyes válasz!')
    else:
        print('Helytelen! Noob! #lol')

    kerdesindex = kerdesindex + 1

input('Üss entert a kilépéshez')
