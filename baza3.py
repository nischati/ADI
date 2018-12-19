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

#korelacja - głosy nieważne a głosy zmiennaNIePutin

a=pd.Series(zmiennaVladimir)
b=pd.Series(zmiennaNiewazneGlosy)

print("Korelacja głosów na Putina i głosów nieważnych")
print(st.pearsonr(a,b))
