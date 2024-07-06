#№1

import pandas as pd
data = pd.read_csv('ratings.csv')
print(data[data['rating'] == 5.0]['movieId'].value_counts().head(1))

#№2

#import pandas as pd
data = pd.read_csv('power.csv')
data.head()
filtered_country = data[(data['country'] == 'Latvia') | (data['country'] == 'Lithuania') | (data['country'] == 'Estonia')]
filtered_country.head()
filtered_category = filtered_country[(filtered_country['category'] == 4) | (filtered_country['category'] == 12) | (filtered_country['category'] == 21)]
filtered_category.head()
filtered_year = filtered_category[(filtered_category['year'] <= 2010) & (filtered_category['year'] >= 2005)]
filtered_year.head()
filtered_quantity = filtered_year[(filtered_year['quantity'] >= 0)]
print(filtered_quantity['quantity'].sum())

#№3

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
page = pd.read_html('https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8', attrs={'class':'wikitable'}, encoding='utf-8')[0]
for i,table in enumerate(page):
    print(table)

