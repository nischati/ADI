import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
dane=pd.read_csv("c:/Users/User/Desktop/baza/voting_data_eng.csv")
'''print(dane.head(0))'''

'''
# Jaki jest stosunek liczby głosujących do liczby zamieszkujących Rosję?

zmiennnaEnlisted=dane["Number of voters enlisted"]
print(zmiennnaEnlisted.sum())
zmiennaVladimir=dane["Putin Vladimir Vladimirovich"]
zmiennaBaburin=dane["Baburin Sergei Nikolaevich"]
zmiennaGrudinin=dane["Grudinin Pavel Nikolaevich"]
zmiennaZhirinowskiy=dane["Zhirinovskiy Vladimir Volfovich"]
zmiennaSobchak=dane["Sobchak Ksenia Anatolyevna"]
zmiennaSuraikin =dane["Suraikin Maksim Aleksandrovich"]
zmiennaTitov=dane["Titov Boris Yurievich"]
zmiennaYavlinskiy=dane["Yavlinskiy Gregory Alekseivich"]

zmiennaGlosujacy=(zmiennaVladimir.sum())+(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
print(zmiennaGlosujacy)
'''
'''
# 2 pytanie
zmiennaSobchak=dane["Sobchak Ksenia Anatolyevna"]
print(dane["region_name"]["Altajskij kraj"])


'''
zmiennaVladimir=dane["Putin Vladimir Vladimirovich"]
zmiennaBaburin=dane["Baburin Sergei Nikolaevich"]
zmiennaGrudinin=dane["Grudinin Pavel Nikolaevich"]
zmiennaZhirinowskiy=dane["Zhirinovskiy Vladimir Volfovich"]
zmiennaSobchak=dane["Sobchak Ksenia Anatolyevna"]
zmiennaSuraikin =dane["Suraikin Maksim Aleksandrovich"]
zmiennaTitov=dane["Titov Boris Yurievich"]
zmiennaYavlinskiy=dane["Yavlinskiy Gregory Alekseivich"]
zmiennaNIePutin=(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
zmiennaNiewazneGlosy=dane["Number of invalid ballot papers"]
zmiennaGlosujacy=(zmiennaVladimir.sum())+(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())

'''
#za trudne 3 pytanie korelacje
zmiennaNIePutin=(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
print(zmiennaNIePutin)

zmiennaNiewazneGlosy=dane["Number of invalid ballot papers"]
print(zmiennaNiewazneGlosy.sum())



print(st.pearsonr(a,b))
JAK ZROBIC KORELACJE????????????????????
'''
print("Głosy nieważne / Głosy na Putina / Głosy na Innych ")

print(zmiennaNiewazneGlosy.sum())
print(zmiennaVladimir.sum())
print(zmiennaNIePutin.sum())

a=pd.Series(zmiennaVladimir)
b=pd.Series(zmiennaNiewazneGlosy)

print(st.pearsonr(a,b))

'''
Pytanie 7 statystyki

plt.plot(zmiennaVladimir,label='Vladziu')
plt.plot(zmiennaNiewazneGlosy,label='Rebele')
plt.legend()
plt.xlabel("glosy")
plt.ylabel("ilosc")
plt.show()
'''
