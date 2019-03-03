#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:43:11 2018

@author: yusufalicezik
"""

#sınav test olacak ve fonksiyon sorulacak

import os
import io ##klasörün içinde gezinmek ve içindekilere ulaşmak için os
import numpy as np 
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



def readFiles(path): #bu path içerisindeki tüm dosyaları tarayıp bana body döndürecek. (liste olarak)
    for root,dirNames,fileNames in os.walk(path): #gönderdiğim path deki tüm root dirname filename bilgilerini bana gönderiyor.
        for fileName in fileNames: #tek tek git gönderdiğim path deki sırayla bütün filename leri al.
            path=os.path.join(root,fileName) #okuyacağım dosyanın yolunu oluşturdum.
            
            inBody=False #ilk başta false. Ters slash n e kadar gitmesi için. body nin içinde miyim değil miyim diye tanımladım
            lines=[] #body nin içindeki satırları liste yaptım
            f = io.open(path,'r',encoding='latin1') #dosyayı açalım, readonlymode(r) da açtım, okuyabilmesi içinde latin1 dedik.
            for line in f: #tüm satırları teker teker aldım.
                if inBody: #eğer body satırını bulmuşsam
                    lines.append(line) #butun satırları tek tek listenin içine eklemeye başla
                elif line=="\n": #değilse ve \n ise body true olur ve artık body içindekileri tek tek listeye atarız.
                    inBody=True
            f.close() #işimiz bitince dosya kapa
            message='\n'.join(lines) #
            yield path,message #yield return gibi ama tek tek değil en son liste oluşturup döndürür.
            
            
            

def dataFrameFromDirectory(path,classification):
    rows=[]
    index=[]
    for fileName,message in readFiles(path): #path geldiği zaman napıcak : biraz önce benim belirttiğim tanımladığım readfiles a path i gönderiyorum, bu dosyaları bana path ve mesaj olarak geri döndürür.
        rows.append({'message':message,'class':classification}) #dönen mesajı append ettik.
        index.append(fileName) #file name i de buraya attım
    return DataFrame(rows,index=index) #return dataframe oluşturup, rows u ve index i oluştur. Bu bana gönderdiğim path deki tüm elemanları oluşturuyor.



data = DataFrame({'message':[],'class':[]}) #boş bir dataframe oluşturduk

##sırayla bunları okuyup dataframe in içine aktarabiliriz artık.

data=data.append(dataFrameFromDirectory(
        "/Users/yusufalicezik/Downloads/Dosyalar/emails/spam",'spam' #2. spam classification.
        ))
data= data.append(dataFrameFromDirectory(
    
        '/Users/yusufalicezik/Downloads/Dosyalar/emails/ham','ham'
        ))




data.head()


vectorizer=CountVectorizer() #bi metinde içerisinde geçen kelimeklerin frekansları ile bi vektör oluşturur.
counts = vectorizer.fit_transform(data['message'].values)#bütün mesajlarımın içerisinde hangi kelimeden kaç tane var buluyorum.


classifier=MultinomialNB() #(model=) naive bayes algoritmasının bir modeli bu multi.
target=data['class'].values #girişler üsttekiler(counts) çıkış bu.
classifier.fit(counts,target) ##modeli oluşturmuş olduk


examples=['CLICK HERE to Order Yours NOW!','Hi Bob, how about a game of golf tomorrow?',"sa kardeşim"]
example_counts=vectorizer.transform(examples) ##count vectorizer ile giriş verilerini elde ettim.
predictions=classifier.predict(example_counts) #tahmin ettik.
predictions

