#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:47:36 2018

@author: yusufalicezik
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


x=np.arange(-3,3, 0.001)

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5)) #iki grafiği üst üste bindirmek için aynı plot sınıfını kullan

plt.savefig('/Users/yusufalicezik/Desktop/a.png', format='png') #grafiği png olarak kaydettik.

#Axisleri düzenlemek..() 
axes=plt.axes()
axes.set_xlim([-5,5]) #x ekseni nerden başlayıpp nerede bitecek
axes.set_ylim([0,2.0])
axes.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5]) #belirtilen noktaların x lerine tik yok.
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.5,2]) #y lere tik attık.


##ızgaralara bölme
axes.grid()



#şekil dğeiştirme
plt.plot(x, norm.pdf(x), "y-")
plt.plot(x, norm.pdf(x, 1.0, 0.5), "g:") 


#axislere etiket ve bilgi ekleme
plt.xlabel("X label")
plt.ylabel("Y label")

plt.plot(x, norm.pdf(x), "y-", label="Sarı")
plt.plot(x, norm.pdf(x, 1.0, 0.5), "g:", label="Yeşil") 

plt.legend(loc=3) #sol alt. 1 olursa sağ üst, 2 sol üst 4 sağ alt.


##pasta grafik çizme

