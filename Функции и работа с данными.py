#№1

import pandas as pd
ratings = pd.read_csv('ratings.csv')
ratings.head()
ratings = ratings.groupby('movieId').mean().reset_index()
ratings.head()
def classify(rating):
    if rating <= 2:
        return 'низкий рейтинг'
    if 2 < rating <= 4:
        return 'средний рейтинг'
    if 4 < rating <= 5:
        return 'высокий рейтинг'
ratings['class'] = ratings['rating'].apply(classify)
print(ratings.head(100))

#№2

import pandas as pd
data = pd.read_csv('keywords.csv')
data.head()
geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск'] }
new_geo_data = {}
for i in geo_data:
    for j in geo_data[i]:
        new_geo_data[j] = i
def define_reg(i):
    for j in new_geo_data.keys():
        if j.lower() in i.lower():
            return new_geo_data[j]
            break
    return 'undefined'
data['region'] = data['keyword'].apply(define_reg)
print(data.head(851))

