#Need to install pyyaml 

import yaml

with open('patient1.yml','r') as f:
    files=yaml.safe_load_all(f)

    for each_file in files:
        print(each_file)
        print(each_file['patient_details']['phone'])

    


