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
zmiennaNiewazneGlosy=dane["Number of invalid ballot papers"]
zmiennaNIePutin=(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())
zmiennaGlosujacy=(zmiennaVladimir.sum())+(zmiennaBaburin.sum())+(zmiennaTitov.sum())+(zmiennaGrudinin.sum())+(zmiennaSobchak.sum())+(zmiennaSuraikin.sum())+(zmiennaYavlinskiy.sum())+(zmiennaZhirinowskiy.sum())

# wykres kołowy/słupklowy putin  / inni / nieważne
print(zmiennaVladimir.sum())
print(zmiennaNIePutin.sum())
print(zmiennaNiewazneGlosy.sum())
wybory =['Głosy oddane na Putina','Głosy oddane na innych kandydatów','Głosy nieważne']
godziny=pd.Series([54348975,15743579,761342])
plt.figure(1 ,figsize=(6 ,6))
plt.pie(godziny,labels=wybory,autopct='%1.1f%%',shadow=False)
plt.show()
