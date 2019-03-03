

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
##pasta grafik çizme

plt.rcdefaults()
values=[12,55,4,32,14] #yüzdelik ne kadar değer alacağını gösterir.
colors=["r","g","b","c","m"] ##hangi renkler
explode=[0,0,0.2,0,0] #rusya hafif öne çıkar
labels=["Hindistan", "Türkiye","Rusya","Çin","Yunanistan"]
plt.pie(values, colors=colors, labels=labels, explode=explode) 


##bar grafiği için
plt.bar(range(0,5), values, color=colors)

#ya da
plt.bar(["a","b","c","d","e"], values, color=colors)




#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.rcdefaults()


#####Scatter için
x=np.random.randn(500)
y=np.random.randn(500)

plt.scatter(x,y)

#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



x=np.random.normal(3.0, 1.0, 1000)
y=np.random.normal(50.0,10.0, 1000) ##ortalama s.sapma  eleman sayısı

np.cov(x,y) #bize matris verir kovaryans matrisi


np.corrcoef(x,y) ##korelasyon matrisi

#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

from sklearn.linear_model import LinearRegression


df=pd.read_excel("/Users/yusufalicezik/Downloads/odev.xlsx")

corIliskisi=df.corr()

x=df.iloc[:, [0,2]].values
y=df.maas.values.reshape(-1,1)
plt.scatter(x[0:,1],y)
plt.show()


df.plot(kind="scatter", x="maas", y="deneyim")
#df.maas.plot(kind="hist", bins=50)

df.corr()
lr=LinearRegression()
lr.fit(x,y)
tt=lr.predict([[3,33]])

