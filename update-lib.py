import os
import os.path
import subprocess
from subprocess import call
import config

current_dir = os.path.dirname(os.path.realpath(__file__))

lib_list = config.lib_list
group_id = config.group_id

src_dir = current_dir + '/libs/'
dst_dir = current_dir + '/repository/'

def get_cmd(jar_file, group_id, artifact_id, version, dst_path):
    s = """mvn org.apache.maven.plugins:maven-install-plugin:2.5.2:install-file \
        -Dfile=%s -DgroupId=%s -DartifactId=%s -Dversion=%s  -Dpackaging=jar -DlocalRepositoryPath=%s""" % (jar_file, group_id, artifact_id, version, dst_path)
    print s
    return s.split()

for item in lib_list:
    file_name = item['file_name']
    artifact_id = item['artifact_id']
    version = item['version']
    print "install: %s,  %s", file_name, version
    src_file = src_dir + file_name
    cmd = get_cmd(src_file, group_id, artifact_id, version, dst_dir)
    call(cmd)
