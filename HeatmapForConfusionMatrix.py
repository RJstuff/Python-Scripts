import seaborn as sn

import pandas as pd
import matplotlib.pyplot as plt

array = [[0,2,4],
         [0,3,9],
         [0,4,8]]

df_confusion = pd.DataFrame(array, range(3), range(3))
print(df_confusion)

sn.set(font_scale=1.5)

sn.heatmap(df_confusion, annot = True, annot_kws = {"size":1.5})

plt.show()
