import json
import os 

# get the config from json
jsonConfigFile = open('config.json')
configs = json.load(jsonConfigFile)

# create option screen
def generateTheOptionsScreen(object):
    print('{number} - {optionName}'.format(number=configs.index(object), optionName=object['name']))
list(map(generateTheOptionsScreen, configs))

# input
optionSelect = input('select the workspace > ')
if not optionSelect or not optionSelect.isnumeric():
    exit()

# start the command
print('Starting...')
os.system(configs[int(optionSelect)]['command'])