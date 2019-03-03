#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:47:01 2018

@author: yusufalicezik
"""

from sklearn.datasets import load_iris #iris datasetini import ettim
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
  

#cycle grafik çizdirirken kolaylık sağlar

iris=load_iris() #veri setini yükledik

#boyutunu öğrenmem gerek. kaç giriş kaç veri

ornekSayisi, oznitelik=iris.data.shape #150 veri, 4 giriş verim varmış (2 şerden toplam 4 tane)

#çıkışları görmek için;
print(iris.target_names) #her bi irisi getirdi. özelliklerine göre 3 farklı sınıfta etiketledi(gruba ayırdı)

X=iris.data

pca=PCA(n_components=2, whiten=True).fit(X)#dönüştürülecek boyut sayısını belirleriz
X_pca=pca.transform(X)



print(sum(pca.explained_variance_ratio_)) #4 boyutlu verilerinizi 2 boyuta indirdim. 2 boyutta verilerin yüzde kaçını açıklayabilir onu söyler: 97




colors=cycle('rgb')  #stringi iterable bir eleman haline getirir yani forma, içinden veri çekebiliriz.


target_ids=range(len(iris.target_names)) #3 elemanlı alan getirdi

#grafiği çizelim;
pl.figure()

for i,c,label in zip(target_ids, colors, iris.target_names): #zip fonk: bi çok iterable elemandan aynı anda veri çekmeyi sağlıyor
    pl.scatter(X_pca[iris.target==i,0],
               X_pca[iris.target==i,1], c =c,
               label=label)
    
pl.legend()
pl.show()