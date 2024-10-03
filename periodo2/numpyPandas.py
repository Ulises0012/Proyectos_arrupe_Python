import pandas as pd
import numpy as np

Data2 = {
    'Nombre':['Katherine', 'Juan', 'Raúl', 'Carmen'],
    'Notas': ['8','6', np.nan,'8'],
    'Deportes': ['Beisbol', 'Futbol', 'Padel', 'Tennis'],
    'Materias': ['Matematica', 'ciencias', 'lenguaje', 'Fisica']
}
Frame2 = pd.DataFrame(Data2)

print(Frame2)

print('--------------------')


Data3 = {
    'Nombre':['Katherine', 'Juan', 'Raúl', 'Carmen'],
    'Notas': ['8','6', np.nan,'8'],
    'Deportes': ['Beisbol', 'Futbol', 'Padel', 'Tennis'],
    'Materias': ['Matematica', 'ciencias', 'lenguaje', 'Fisica']
}
Frame3 = pd.DataFrame(Data3)

remplazo = Frame3.replace(np.nan, '0')


print(remplazo)

print('------------------------------------')

Data4 = {
    'Nombre':['Katherine', 'Juan', 'Raúl', 'Carmen'],
    'Notas': ['8','6', np.nan,'8'],
    'Deportes': ['Beisbol', 'Futbol', 'Padel', 'Tennis'],
    'Materias': ['Matematica', 'ciencias', 'lenguaje', 'Fisica']
}
Frame4 = pd.DataFrame(Data4)

remplazo['Analisis de Notas']=remplazo.Notas.astype(int)

print(remplazo.describe())


