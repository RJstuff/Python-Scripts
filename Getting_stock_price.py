import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

#style.use('ggplot')

#start = dt.datetime(2000,1,1)
#end = dt.datetime(2016,12,31)

#df = web.DataReader('TSLA','yahoo',start,end)

#df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
df.plot()
plt.show()
