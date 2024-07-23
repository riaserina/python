#№1

import pandas as pd
log = pd.read_csv('visit_log.csv', sep = ';')
log.head()
def filter(row):
    if row['traffic_source'] == 'yandex':
        return 'organic'
    elif row['traffic_source'] == 'google':
        return 'organic'
    elif row['traffic_source'] == 'paid':
        if row['region'] == 'Russia':
            return 'ad'
        else:
            return 'other'
    elif row['traffic_source'] == 'email':
        if row['region'] == 'Russia':
            return 'ad'
        else:
            return 'other'
    else:
        return row['traffic_source']
log['source_type'] = log.apply(filtered, axis = 1)
print(log.head(20))

#№2

import pandas as pd
import re
urls = pd.read_csv('URLs.txt')
urls.head()
print(urls[urls.url.str.contains('/[0-9]{8}-', regex = True)].head())

#№3

import pandas as pd
import numpy as np
tmp = pd.read_csv('ml-latest-small/ratings.csv')
tmp
uid_count_lt = tmp.groupby('userId')['timestamp']\
        .agg({'count', lambda x: max(x) - min(x)}).reset_index()\
        .rename(columns = {'<lambda_0>':'lt'})
print(uid_count_lt[uid_count_lt['count'] > 100]['lt'].mean())

#№4

import pandas as pd
rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
rzd
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
auto
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
air
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
client_base
table = rzd.merge(auto, how = 'outer', on = 'client_id')
table = table.merge(air, how = 'outer', on = 'client_id')
table.loc[table.rzd_revenue.isnull(), 'rzd_revenue',] = 0
table.loc[table.auto_revenue.isnull(), 'auto_revenue',] = 0
table.loc[table.air_revenue.isnull(), 'air_revenue',] = 0
full_table = table.merge(client_base, how = 'outer', on = 'client_id')
print(table)
print(full_table)