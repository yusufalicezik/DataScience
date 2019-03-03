
import pandas as pd



r_columns=["user_id","movie_id","rating"]

ratings=pd.read_csv("/Users/yusufalicezik/Downloads/ders/u.data", sep="\t", names=r_columns, usecols=range(3))

m_columns=["movie_id","title"]

movies=pd.read_csv("/Users/yusufalicezik/Downloads/ders/u.item", sep="|", names=m_columns, usecols=range(2), 
                   encoding="latin-1")



ratings=pd.merge(movies,ratings) #ayrı ayrı dosyaları okuyup tek bir dosyada birleştirdi.(Sınavda çıkabilir)


user_ratings=ratings.pivot_table(index="user_id", columns="title", values="rating") #hangi kullanıcılar hangi filmleri
#izlemiş izlememiş izlediyse kaç puan vermiş pivot table ile bunu yaparız. tek satırda koca bir matris oluşur.
#nesnelerin matrisi oluşur.


#starwars ile aynı kategoride olan filmleri bulmak istiyoruz.

starWarsRatings=user_ratings["Star Wars (1977)"] #starwars a verilen rate ler.

#benzer filmleri bulmak için;

benzerFilmler=user_ratings.corrwith(starWarsRatings) #benzer filmleri bulduk. non olanları sil benzer olmayanlar yani

benzerFilmler=benzerFilmler.dropna() #non olan kayıtları siler.



#bunu artık bir dataframe e çevirelim;

df=pd.DataFrame(benzerFilmler) #starwars ile benzer filmleri içeren bir df yarattık.


import numpy as np

filmistatistik=ratings.groupby("title").agg({"rating" : [np.size, np.mean]})#her filmi kaç kişi oylamış ve ort. kaç puan vermiş
#agg hangi alana göre sıralar.(sınavda çıkabilir. agg gruplama)

##eğer bi filmi 100 den fazla değerlendirilmişse o filmi popüler seçelim

populerFilmler=filmistatistik['rating']["size"]>=100


sonuc=filmistatistik[populerFilmler].sort_values([("rating","mean")], ascending=False)[:15] ##ilk önce a ya sonra b ye göre sıralare şitse


##sepet analizi algoritmalaırndan en öçok kullanılanı bulup bunu uygula = cevap apriori