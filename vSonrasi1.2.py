
import pandas as pd
import numpy as np
from sklearn import tree


from IPython.display import Image
from sklearn.externals.six import StringIO
import pydotplus as pyd

df=pd.read_csv("/Users/yusufalicezik/Downloads/Dosyalar/EskiCalisanlar.csv")

df.head()

 d={'Y': 1,'N': 0}
 
 df["Hired"]=df["Hired"].map(d)
 df["Employed?"]=df["Employed?"].map(d)
  df["Top-tier school"]=df["Top-tier school"].map(d)
   df["Interned"]=df["Interned"].map(d)
   
   
    d={"BS":0,"MS":1, "phD":2}
    df["Level of Education"]=df["Level of Education"].map(d)
    
    df.head()



y=df["Hired"]


x=df[features]

model=tree.DecisionTreeClassifier()
model=model.fit(x,y)


