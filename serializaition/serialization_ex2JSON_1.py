#Serialization of a single object using JSON

import json

ball={'color':'blue','radius':5,'weight':100,'plasticball':True,'owner':None}


#serializing json string
json_str=json.dumps(ball,indent=4)

print(json_str)
print(type(json_str))


#serializing json file
with open('file2.json','w') as f2:
    json.dump(ball,f2, indent=4)

with open('file2.json','r') as f2:
    json.load(f2)

print(json.load(f2))

"""print('color is',ball_new['color'])

for k,v in ball_new.items():
    print('{}:{}'.format(k,v))


print(ball_new)"""


