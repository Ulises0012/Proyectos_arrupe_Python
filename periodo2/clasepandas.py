import pandas as pd


series = pd.Series([1,6,-2,11], index=['a','b','c','d'])

print(series)

print("---------------------------------------------")


series2 = pd.Series([2,-2,8,10], index=['a','b','c','d'])
print(series2['c'])


print("---------------------------------------------")


series3 = pd.Series([2,-2,8,10])
print(series>0)

print("------------------------------")


jugadores_BK = {
    23:'LeBron James', 30:'Stephen Curry', 35:'Kevin Durant', 24:'Koby bryant', 3:'Dayane Wade'
}

serie_jugador=pd.Series(jugadores_BK)

print(serie_jugador)

serie_jugador[11]='Klay Thompson'

print(serie_jugador)
print("---------------------------------")


Data = {
    'Departamento': ['Santa Ana', 'Ahuachapan','Chalatenango'],
    'Codigo postal':['2201','0301','1301'],
    'Lugar turistico': ['Lago de Coatepque', 'Ruta de las flores', 'El pital']

}

Frame = pd.DataFrame(Data)
print(Frame)
