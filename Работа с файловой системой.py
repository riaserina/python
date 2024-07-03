#№1

import json

new_dict = {}
with open('purchase_log.txt', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        key = dict_['user_id']
        value = dict_['category']
        if key != 'user_id':
            new_dict.setdefault(key, value)

#№2

with open('visit_log.csv', 'r') as f, open('funnel.csv', 'w') as w_f:
    for row in f:
        line_list = row.strip().split(',')
        if line_list[0] in new_dict.keys():
            line_list.append(new_dict[line_list[0]])
            add_line = ','.join(line_list)
        elif line_list[0] == 'user_id':
            line_list.append('category')
            add_line = ','.join(line_list)
        else:
            add_line = ','.join(line_list)
        if 'None' in line_list:
            pass
        else:
            w_f.write(add_line+'\n')
