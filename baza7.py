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

# głosy oddane na kobiety a inni poza putinem i nią
zmiennaGlosujacy=(zmiennaVladimir.sum())+(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
zmiennachlopyNIeputinowe=(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
zmiennaSobchak=dane["Sobchak Ksenia Anatolyevna"]
print(zmiennaSobchak.sum())
print(zmiennachlopyNIeputinowe.sum())
legia= pd.Series([1180028,14563551])
dni=range(len(legia))
plt.bar(dni,legia, color='g', label='legia')
podpisy=['kobita','chopy']
plt.xticks(dni, podpisy)
plt.xlabel("Kandydat")
plt.ylabel("Głosy")
plt.show()
'''dodac pozostale slupki dla innych kandydatów '''
