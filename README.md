# New-York-City-Taxi-Trip-Duration

## Description

In this competition, Kaggle is challenging you to build a model that predicts the total ride duration of taxi trips in New York City. Your primary dataset is one released by the NYC Taxi and Limousine Commission, which includes pickup time, geo-coordinates, number of passengers, and several other variables.

Longtime Kagglers will recognize that this competition objective is similar to the ECML/PKDD trip time challenge we hosted in 2015. But, this challenge comes with a twist. Instead of awarding prizes to the top finishers on the leaderboard, this playground competition was created to reward collaboration and collective learning.

We are encouraging you (with cash prizes!) to publish additional training data that other participants can use for their predictions. We also have designated bi-weekly and final prizes to reward authors of kernels that are particularly insightful or valuable to the community.

## Structure

data: 数据集目录，可从https://www.kaggle.com/competitions/nyc-taxi-trip-duration/data上下载train.csv和test.csv至该文件夹

preprocessing.py: 数据预处理及特征工程

feature.ipynb: 特征工程的jupyter文件记录

main.ipynb: 数据可视化及GBDT和随机森林代码实现

Stacking_lgb: LightGBM代码实现

Stacking_xgb: XGBoost代码实现

perception.ipynb: 全连接网络代码实现

Line_stacking: LightGBM和XGBoost线性组合

Data Analysis And Visualization.ipynb：数据分析与可视化

