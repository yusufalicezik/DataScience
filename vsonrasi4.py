import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import Imputer #eksik verileri tamamlamak için

from sklearn.preprocessing import LabelEncoder, OneHotEncoder #sözel verileri sayısala çevirme için

from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("/Users/yusufalicezik/Downloads/veridata.csv", sep=";")


X=df.iloc[:, :-1].values #ilk 3 veriyi giriş olarak belirledik

y=df.iloc[:, -1].values #sonu aldık. büyük X giriş küçük y çıkış

imputer = Imputer(missing_values="NaN", strategy="mean", axis=0) #0 demek eksik veri sütunlarda demek #sözel verilerde frequency(en çok tekrar eden) kullan

X[:,1:3]=imputer.fit_transform(X[:,1:3])

lbl_encoder=LabelEncoder()#bunu yaparak label encoder sınıfından bir nesneyi tanımladım

X[:,0]=lbl_encoder.fit_transform(X[:,0]) #onehotencoder bu sayısalların bi anlam ifade etmediğini, birbirinden üstün olnmadığnı söylemek için kullanırız.

one_encoder=OneHotEncoder(categorical_features=[0])

X=one_encoder.fit_transform(X).toarray()


cikis_encoder=LabelEncoder()

y=cikis_encoder.fit_transform(y)


#standard: ve normalize verileri küçültür. normalizasyonda aralığı biz belirleriz.biz normalizasoyn yapalım.

minmax=MinMaxScaler()

X=minmax.fit_transform(X) #default olarak 0-1 arasında verir. ama istersek o aralığı biz belirleyebilirz.

##outlies: aşırı değerler. veriler normal dağolımmış gibi -3,+3 aralıktaymış gibi veriler.


