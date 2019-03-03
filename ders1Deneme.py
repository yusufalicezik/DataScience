import pandas as pd


df=pd.read_excel("/Users/yusufalicezik/Downloads/veriler.xlsx")

ilkBesVeri=df.head()

ilkUcVeri=df.head(3)

sonSekizVeri=df.tail(8)

df.shape ##kaç satır ve sütun var ona bakar. çıktısı(7584, 9) ilki satır sonrası sütun(kaça kaçlık tablo oldugunu gösterir yani)

df.shape[1] #kaç sütun var onu gösterir:9 çıkar.

df.shape[0] #buda kaç satır  : 7584 çıkar.

df.size #toplam veriyi tutar. satır*sutun

len(df) #toplam veri uzunluğunu(yani satır sayısını) verir. 7584

df.columns #tablodaki sütun başlıklarını verir. tuple biçiminde. çıktısı: Index(['cdatetime', 'address', 'district', 'beat', 'grid', 'crimedescr',
      # 'ucr_ncic_code', 'latitude', 'longitude'],
     #   dtype='object')
     
    
    
listem=list(df)
for i in range(len(listem)):
    print(listem[i])

## eğer df nın sadece bir sütununu görmek istersek;(tüm verileri)
df["Şehir"] #seçtiğimiz sütuna ait tüm verileri gösterir.

df["Şehir"].head() #yukarıdaki gibi ama ilk 5 ini getirir.


##eğer birden fazla sütun okumak istersek;
df[["Şehir", "Maaş"]] ##liste biçiminde yazarız..(**iç içe 2 köşeli**)




##eğer tek columnun tüm verilerini değil de ilk 5 yada 3 den basla hepsini ver
df["Şehir"][3:] ## ilk 5 deseydi [:5] sol sıfırdan başla sağ 5 e kadar


################################################################################


df["Şehir"].value_counts() #her şehir verisinden kaç tane var ör: a şehri 5 b şehri 3 c şehri 1 vs..
#(sütun olarak bakar. yazdığımız sütundaki veriler arasında bakar biz şehir yazdık.)


df.plot(kind="bar")##bar biçiminde grafik getirir.(sayısal verileiri)

##df.plot(kind="scatter", x="Maaş", y="Yaş")
##df.plot(kind="bar", x="Maaş", y="Yaş")

######mean kullanımı 
import numpy as np
dizi=[1,2,3,4,5,6,7,8,9,10]

dizi2=[i for i in range(1,11)] ##otomatik oluşturma. üstteki ile aynı.

np.mean(dizi) ##dizinin aritmetik ortalaması..



gelirler=np.random.normal(27000,15000,10000)
## rastgele 10 bin değer oluştur ortalaması 27 bin s.sapması 15 bin olsun.

np.mean(gelirler) ##ortalama 27 bin cıkar.



import matplotlib.pyplot as plt ##verileri grafiksel almak için


plt.hist(gelirler, 50)
plt.show() ##verileri 50 şer gruba ayırarak grafiksel olarak verir.(histogram olarak.)



##############


from scipy import stats

yaslar=np.random.randint(18, high=90, size=500)
## min 18 max 90 500 tane sayı oluştur dmeek




stats.mode(yaslar) ## modu bulur. en cok tekrar eden ve kaç kere tekrar ettiğini yazar.

####medyanı bulmak istersek;

np.median(yaslar) #tam ortasını bulur.



######## standart sapma

gelirler=np.random.normal(100.0, 20.0, 10000)

gelirler.std()
gelirler.var() ##standart sapma ve varyans bulur.



####uniform:
degerler=np.random.uniform(-10, 10, 10000) ##-10 ile 10 araında 10 bin deger oluşturdu.
plt.hist(degerler, 50) ##50 gruba ayır
plt.show()




##normal dağılım
import numpy as np

from scipy.stats import norm

degerler=np.arange(-3,3,0.001) ##-3 den baslayarak 0.001 arttırarak 3 e gel


plt.plot(degerler, norm.pdf(degerler))  
plt.show()




##üstel:

from scipy.stats import expon
degerler=np.arange(0, 10, 0.001)#0 la 10 arasında 0.001 artarak verileri oluştur. kaç tane varsa..
plt.plot(degerler, expon.pdf(degerler))  



#binom
from scipy.stats import binom

n,p=10, 0.5

degerler=np.arange(0, 10, 0.001)

plt.plot(degerler, binom.pmf(degerler, n, p)) #olasılık gösteririz.


##poison

from scipy.stats import poisson

degerler=np.arange(400, 600, 0.5)

plt.plot(degerler, poisson.pmf(degerler,500)) 

