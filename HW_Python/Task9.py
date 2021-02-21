import sys
import requests
import json
import os

if len(sys.argv)==1:
    argument=input('Enter environment: ')
    addr=os.getenv(argument)
    print(os.environ)
    print(addr)
else:
    addr=sys.argv[1]

filters1 = {
'status': ['dead', ]
}

filters2 = {
'status': ['exited', ]
}

for dead_container in requests.get("{}/containers/json?all=1&filters={}".format(addr, json.dumps(filters1))).json():
    print('Container with Id {} and name {} is dead!'.format(dead_container['Id'], dead_container['Names'][0][1:]))

for exited_container in requests.get("{}/containers/json?all=1&filters={}".format(addr, json.dumps(filters2))).json():
    print('Container with Id {} and name {} is stopped!'.format(exited_container['Id'], exited_container['Names'][0][1:]))

print('Containers list:')
container_info=requests.get("{}/containers/json?all=1".format(addr))
for container in container_info.json():
        print('ID: {}\t Image: {}\tCommand: {}\tCreated: {}\tStatus: {}\tPorts: {}\tNames: {}'.format(container['Id'], container['Image'], container['Command'], container['Created'], container['Status'], container['Ports'], container['Names'][0][1:]))

print('Images list:')

image_info=requests.get("{}/images/json?all=1".format(addr))
for image in image_info.json():
    print('RepoTags: {}\tID: {}\tCreated: {}\tSize: {}'.format(image['RepoTags'], image['Id'],  image['Created'], image['Size']))

print('Inspect info:')
for container in container_info.json():
    print('INFO FOR {}'.format(container['Names'][0][1:]))
    print(requests.get("{}/containers/{}/json?all=1".format(addr,container['Id'])).json())
