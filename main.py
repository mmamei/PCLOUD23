import json
'''
a = [1,2,3,'ciao',{'x':6}]
s = json.dumps(a)
with open('j.json','w') as f:
    json.dump(a,f)

b = json.loads(s)
print(s)
print(b[4]['x'])
'''
with open('data.json') as f:
    data = json.load(f)
data = data['timelineObjects']
print(len(data))
n_activity = 0
n_place = 0
segm = []
for diz in data:
    if 'activitySegment' in diz:
        n_activity += 1
        diz = diz['activitySegment']
        #print(diz)
        #print('-------------------------------')
        segm.append({'day':diz['duration']['startTimestamp'].split('T')[0]})
print(segm)