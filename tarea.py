import numpy as np
import pandas as pd

#lista = [1,2,4,6]

#nplista = np.array(lista)
#pdlista = pd.Series(lista)

#print(lista * 10)
#print(nplista * 2)
#print(pdlista * 2)


df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

#print(df.info()) #Nos muestra las variables a trabajar
#print(df.describe())

#print(df[['weekday','hour','Food%','Fresh%','Drinks%','Home%']].mean())
tabla = df[['order','total_items','discount%','weekday','hour','Food%','Fresh%','Drinks%','Home%', 'Beauty%', 'Health%','Baby%','Pets%']]

maximos = tabla.max()
minimos = tabla.min()

media = tabla.mean()
moda = tabla.mode()
mediana = tabla.quantile([0.5])

#print(media)
print(mediana)

#print(maximos)
#print(minimos)


