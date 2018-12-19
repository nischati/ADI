import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
dane=pd.read_csv("c:/Users/User/Desktop/baza/voting_data_eng.csv")

ruscy= 143369806

zmiennnaEnlisted=dane["Number of voters enlisted"]
zmiennaVladimir=dane["Putin Vladimir Vladimirovich"]
zmiennaBaburin=dane["Baburin Sergei Nikolaevich"]
zmiennaGrudinin=dane["Grudinin Pavel Nikolaevich"]
zmiennaZhirinowskiy=dane["Zhirinovskiy Vladimir Volfovich"]
zmiennaSobchak=dane["Sobchak Ksenia Anatolyevna"]
zmiennaSuraikin =dane["Suraikin Maksim Aleksandrovich"]
zmiennaTitov=dane["Titov Boris Yurievich"]
zmiennaYavlinskiy=dane["Yavlinskiy Gregory Alekseivich"]

#liczba niewaznych głosów wzrasta wraz z liczba głosów oddanych do urn zdalnych
zmiennaGlosujacy=(zmiennaVladimir.sum())+(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
print(dane.head(0))
zmiennaZdalna= dane["Number of ballot papers in portable ballot boxes"]
zmiennaNiewazneGlosy=dane["Number of invalid ballot papers"]

a= pd.Series(zmiennaNiewazneGlosy)
b= pd.Series(zmiennaZdalna)

plt.plot(a,label='Niewżne')
plt.plot(b,label='Zdalne')
plt.legend()
plt.xlabel("Region")
plt.ylabel("Liczba")
plt.show()
