import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gelirler=np.random.normal(27000,15000,10000)

#araya autlire koyma;

gelirler=np.append(gelirler, [10000000000])

plt.hist(gelirler, 50)


print(np.mean(gelirler))

def remove_outlier(gelir):
    o=np.median(gelir) #ortalamayı medyanla bulduk.
    sp=np.std(gelir)
    filitre=[e for e in gelir if(o-2*sp)< e < o + 2*sp]
    
    return filitre


sonuc=remove_outlier(gelirler)

plt.hist(sonuc, 50)
