import os
import os.path
import subprocess
from subprocess import call
import sys
import config

current_dir = os.path.dirname(os.path.realpath(__file__))

lib_list = config.lib_list
group_id = config.group_id
repository_url = 'https://raw.githubusercontent.com/liaohuqiu/umeng-libs/master/repository'
latest_version = '1.0.1.1-SNAPSHOT'

read_me = ''
with open(current_dir + '/README-PATTEN.md') as f: read_me = f.read()

gradle_patten = "compile '%s:%s:%s@%s'\n"

maven_patten = """
<dependency>
    <groupId>%s</groupId>
    <artifactId>%s</artifactId>
    <version>%s</version>
    <type>%s</version>
</dependency>
"""

maven_dependencies = '';
gradle_dependencies = '';

for item in lib_list:
    version = item['version'];
    artifact_id = item['artifact_id'];
    type = item['type'];
    maven_dependencies += maven_patten % (group_id, artifact_id, version, type)
    gradle_dependencies += gradle_patten % (group_id, artifact_id, version, type)

outfile = open('README.md', 'w')
read_me = read_me.replace('{maven_dependencies}', maven_dependencies)
read_me = read_me.replace('{gradle_dependencies}', gradle_dependencies)
read_me = read_me.replace('{repository_url}', repository_url)
outfile.write(read_me)
outfile.close()
