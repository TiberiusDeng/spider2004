import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

weibo_data = pd.read_csv('reult.csv')
st = datetime.date(2020, 2, 15)
et = datetime.date(2020, 4, 15)
day = datetime.timedelta(days=1)
date_list = []
sns.set(style="white", palette="muted", color_codes=True)

largecomment_num = weibo_data[weibo_data.comment_num > 100].groupby('time')['id'].count().reset_index(name = 'count')
print(largecomment_num)
total_num = weibo_data.groupby('time')['id'].count().reset_index(name = 'count')
print(total_num)
ax = sns.lineplot(x="time", y="count", data=total_num, color='g')
plt.show()
ax1 = sns.lineplot(x="time", y="count", data=largecomment_num, color='b')
plt.show()





