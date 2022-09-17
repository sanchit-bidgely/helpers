
# python3 deploy_configs.py {base_url} {acess_token}
# python3 deploy_configs.py http://btocdevapi.bidgely.com d9ae051d-f4ed-4701-a8bf-ba4f7cbb5a7c
# python3 deploy_configs.py https://btobdevapi.bidgely.com d9ae051d-f4ed-4701-a8bf-ba4f7cbb5a7c
# python3 deploy_configs.py https://hydroottwauatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py https://nonprodqaapi.bidgely.com 95aad116-86cb-42e2-81f4-9a1647de4347
# python3 deploy_configs.py https://dukuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py https://naapi.bidgely.com 9ebad28e-aace-4ca2-83c2-082fc26b74d6
# python3 deploy_configs.py https://hydrooneuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py https://oucuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://napreprodapi.bidgely.com 38464d4a-6157-4938-8e6f-9a242cd7eb22
# python3 deploy_configs.py http://amerenuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://amerendevapi.bidgely.com d9ae051d-f4ed-4701-a8bf-ba4f7cbb5a7c
# python3 deploy_configs.py http://avistauatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://nspuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://merdevapi.bidgely.com d9ae051d-f4ed-4701-a8bf-ba4f7cbb5a7c
# python3 deploy_configs.py http://pseguatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://amerenuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://pporuatapi.bidgely.com 56b02db5-b83c-4c5c-b75d-3b6eaee03438
# python3 deploy_configs.py http://herdevapi.bidgely.com d9ae051d-f4ed-4701-a8bf-ba4f7cbb5a7c
# python3 deploy_configs.py http://amerendevapi.bidgely.com d9ae051d-f4ed-4701-a8bf-ba4f7cbb5a7c

from os import listdir
from os.path import isfile, join
from os import getcwd
import json
import requests
import sys

arguments = sys.argv[1:]
base_url = arguments[0]
token = arguments[1]
path = '/Users/sanchit/Desktop/configs/'
headers = {'content-type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}
print (headers)
deploy_config_url = "/v2.0/launchpad/deploy/configs"


files = [file for file in listdir(path) if isfile(join(path, file)) and file.endswith(".json")]
for file in files:
    try:
        with open(path + file) as json_file:
            data = json.load(json_file)
            api_url = base_url + deploy_config_url
            print(api_url)
            #print(data)
            config_response = requests.post(api_url, json=data, verify=False, headers=headers)
            print (file, config_response,config_response.reason)
    except Exception as error:
        print ( "Error while deploying configs : {}".format(error) )

