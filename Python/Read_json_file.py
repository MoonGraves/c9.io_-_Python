import json 

with open('data.json') as json_file:  
    data = json.load(json_file)
    for p in data['ihminen']:
        print('Name: '      + p['name'])
        print('Website: '   + p['website'])
        print('From: '      + p['from'])
        print('Born: '      + p['born'])
        print('')
