import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

#importing all the required ML packages
from sklearn.linear_model import LogisticRegression #logistic regression
from sklearn import svm #support vector Machine
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.naive_bayes import GaussianNB #Naive bayes
from sklearn.tree import DecisionTreeClassifier #Decision Tree
from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
from sklearn.metrics import confusion_matrix #for confusion matrix

# 读取数据
path = 'C:/Users/yangsong/Desktop/dataset/'
# path = 'C:/Users/Administrator/Desktop/dataset/'

# 参考网址 http://datawhale.club/t/topic/197
#####train
trn_click = pd.read_csv(path+'train_click_log.csv')
item_df = pd.read_csv(path+'articles.csv')
item_df = item_df.rename(columns={'article_id': 'click_article_id'})  #重命名，方便后续match
item_emb_df = pd.read_csv(path+'articles_emb.csv')

#####test
# tst_click = pd.read_csv(path+'testA_click_log.csv')

# 对每个用户的点击时间戳进行排序
trn_click['rank'] = trn_click.groupby(['user_id'])['click_timestamp'].rank(ascending=False).astype(int)
# tst_click['rank'] = tst_click.groupby(['user_id'])['click_timestamp'].rank(ascending=False).astype(int)

#新闻文章数据集浏览
print(item_df.head().append(item_df.tail()))

    # 统计文章的字数与数量
print(item_df['words_count'].value_counts())

# 461个文章主题
print(item_df['category_id'].nunique())
# 直方图
item_df['category_id'].hist()

#用户重复点击
#####merge
user_click_merge = trn_click.append(trn_click)
user_click_count = user_click_merge.groupby(['user_id', 'click_article_id'])['click_timestamp'].agg({'count'}).reset_index()
user_click_count[:10]

# 364047篇文章 查数量
item_df.shape

# 新闻文章embedding向量表示
item_emb_df.head()