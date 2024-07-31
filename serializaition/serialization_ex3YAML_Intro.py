#Need to install pyyaml 

import yaml

with open('patient.yml','r') as f:
    file_1=yaml.safe_load(f)

print(type(file_1))
print(file_1)



print(file_1['patient_details']['phone'])
    
with open('patient1.json', 'w') as file:
    yaml.dump(file_1, file)

with open('patient1.json','r')as file:
    file_2=yaml.safe_load(file)

           
print(type(file_2))
print(file_2)
#print(open('patient.yml').read())

