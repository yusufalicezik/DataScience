#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:50:19 2018

@author: yusufalicezik
"""

import numpy as np

def veriOlustur(N,k):  #N kaç veri, k kaç küme olacağı.
    np.random.seed(10)
    pointPerCluster=N/k #her kümede kaç veri olacak.
    X=[] #giriş verisinde X büyüktür.
    for i in range(k): #küme sayısı kadar çalıştır.
        gelir=np.random.uniform(20000.0, 200000) #uniform: bitin  durumların ortaya çıkma ihtimali birbirine eşitse bu uniform dağılımdır.
        yas=np.random.uniform(20.0, 70.0)
        for j in range(int(pointPerCluster)):
            X.append([np.random.normal(gelir, 10000.0), np.random.normal(yas, 2)])  #her seferinde listenin sonuna eleman ekliyoruz.
            
    
    X=np.array(X)
    return X

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt #grafik çizzdirmek için
from sklearn.preprocessing import scale #Scale: Veriler standardize edilir. Veriler neden standardize edilir? : sayısal değerler büyük verilere sahipse, gerek makine öğr. gerek yapay zekada işlem süresi uzamaması için verileri küçültür, işlem süresini kısaltırız.
##normalizasyon  da yapabiliriz.

data=veriOlustur(100,5)

model=KMeans(n_clusters=5) ##default olarak 8 kümeye böler./ Sen ilerde model oluşturacaksın benim gönderdiğim verileri bunu yaparken 5 kümeye böl.

scaledData=scale(data) #verileri scale ettik, ölçeklendirdik. -1 ile 1 arasında  sıkıştırıldı.

model=model.fit(scaledData)

print(model.labels_) ##hangi veri hangi kümeye ait söyler.

plt.figure(figsize=(8,6))
plt.scatter(scaledData[:,0], scaledData[:,1],
            c=model.labels_.astype(float)) ##verileri KMeans algoritmasıı ile gösteriyoruz.
