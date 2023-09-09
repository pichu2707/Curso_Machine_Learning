import pandas 
import numpy 
import scipy
import matplotlib

print('-----VERSIÓN DE LIBREBRÍAS---------')
print('pandas -->', pandas.__version__)
print('numpy -->', numpy.__version__)
print('scipy -->', scipy.__version__)
print('matplotlib -->', matplotlib.__version__)
print('-----------------------------------')
#Empezamos comprobando que está bien hecha la importación

print('\n')
print(20*'*-')
print('Ejercicio de lectura de datos')
print(20*'*-')
print('\n')
name = ['edad','trabajo','educacion','estado_civil','relacion','raza','sexo','plusvalia','pérdida']
df = pandas.read_csv('nfloffenseweek3.csv')
print(df)
