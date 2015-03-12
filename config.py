import os
from os import listdir
from os.path import isfile, join

group_id = 'com.umeng'
share_lib_version = '4.2.3'

def all_file(mypath):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    return onlyfiles

jars = all_file('libs')

lib_list = [
        {
            'version': '1.0.1',
            'type': 'jar',
            'artifact_id': 'SocialSDK_QQZone_3',
            'file_name': 'SocialSDK_QQZone_3.jar'
            },
        {
            'version': share_lib_version,
            'type': 'jar',
            'artifact_id': 'umeng_social_sdk',
            'file_name': 'umeng_social_sdk.jar'
            },
        {
            'version': '5.4.1',
            'type': 'jar',
            'file_name': 'umeng-analytics-v5.4.1.jar',
            'artifact_id': 'umeng-analytics',
            }
        ]

for jar in jars:
    if 'SocialSDK_' not in jar:
        continue

    artifact_id = os.path.splitext(jar)[0]
    info = {}
    info['type'] = 'jar'
    info['version'] = share_lib_version
    info['artifact_id'] = artifact_id
    info['file_name'] = jar
    lib_list.append(info)

