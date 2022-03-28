import csv
import json

with open('triplets.txt', 'r') as f:
    text = f.read()

rows = text.split('\n')
rows_to_write = []

for r in rows:
    if not r:
        continue
    r = r.split(',')
    try:
        rel = r[0]
        arg1 = r[1]
        arg2 = r[2]
    except:
        continue
    
    row = []
    rel_string = '/r/' + str(rel)
    arg1_string = '/c/en/' + str(arg1.replace(' ','_'))
    arg2_string = '/c/en/' + str(arg2.replace(' ','_'))
    arg2_string.replace(' ', '_')
    extra_info = {}
    extra_info['dataset'] = ''
    extra_info['license'] = ''
    extra_info['sources'] = [{'contributor':'', 'process':''}]
    extra_info['weight'] = 1.0
    extra_info_string = str(extra_info)
    extra_info_string = extra_info_string.replace('\'','\"')

    full_rel = '/a/[' + rel_string + ',' + arg1_string + ',' + arg2_string + '/]'
    row.append(full_rel)
    row.append(rel_string)
    row.append(arg1_string)
    row.append(arg2_string)
    row.append(extra_info_string)

    rows_to_write.append(row)


with open('arcnet.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar="\'", quoting=csv.QUOTE_NONE, escapechar='\\')
    for r in rows_to_write:    
        writer.writerow(r)
