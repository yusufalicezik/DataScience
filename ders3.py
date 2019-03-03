
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

#%%

np.random.seed(2)
sayfaHizi=np.random.normal(3.0, 1.0, 1000) ##ort s.sapma 1000 tane sayı

satisHasilati=np.random.normal(50,10.0, 1000) /sayfaHizi

plt.scatter(sayfaHizi, satisHasilati)
#her zaman x giriş verisini   // #y çıkış verisini gösterir.

x=sayfaHizi
y=satisHasilati

model=np.poly1d(np.polyfit(x,y,4)) #giriş çıkış al 4. mertebeden denklemi bul, poly1d ile fonksiyona dönüştür.

inputs=np.linspace(0,7, 100) ## 0 la 7 arasını 100 eşit parçaya bölerek bir dizi oluşturur.

plt.scatter(x,y)
plt.plot(inputs, model(inputs), c="r")

r2=r2_score(y, model(x))
print(r2)


#%%
df=pd.read_excel("/Users/yusufalicezik/Desktop/arabalar.xls")

X=df[["Km", "Silindir", "Kapi"]] #bunları iloc lu dene.
y=df[["Fiyat"]]


dfYeni=df[["Km", "Fiyat"]][5:11]
dfYeni["Fiyat"].plot(kind="hist", bins=5)

dfYeni2=df.iloc[5:11, [0,1]].values

listem=list(df.iloc[5:11, [0,1]].values)
for i in range(len(listem)):
    print(listem[i][0])

##verileri standardize normalize vs. etmek. biz standardize kulanıcaz.
df.corr()

sc=StandardScaler();

X[["Km", "Silindir", "Kapi"]]=sc.fit_transform(X[["Km", "Silindir", "Kapi"]].as_matrix()) #verileri normalize ettik.

"""
veri normalleştirmeye göre.
s.sapmasını ve ort unu buluyorz.
sapma=df["Km"].std()
ort=np.mean(df["Km"])
veri-ort /ssapma =normalize etmek
"""
model=sm.OLS(y,X).fit()
model.summary()
