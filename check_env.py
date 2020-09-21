#Script meant to check yaml script and check if packages are up to date
import os
import sys
import yaml
import importlib
import subprocess
import pkg_resources
#make list of packages in yaml file
a_yaml_file = open("environment.yml")
parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
#print(parsed_yaml_file)
pack_split = []
version = {}
for packs in parsed_yaml_file['dependencies']:
    pack = packs.split('=')
    if len(pack) == 2:
        version[pack[0]] = pack[1]
    pack_split += pack
#seperates package name from version number
packages = []

for index,packs in enumerate(pack_split):
    try:
        float(packs)
    except ValueError:
        packages.append(packs)
#has list of installed packages for environment
#print(packages)
for p in packages:
    #checks if package is installed
    if p != 'python' and importlib.util.find_spec(p) is None:
        print("[" + p + "] is not installed.")
    elif p in version:
        size = len(version[p])
        if p == 'python':
            sys_ver = sys.version[:size]
        else:
            sys_ver = str(subprocess.run([sys.executable, '-m', 'pip', 'show', '{}'.format(p)],
                                capture_output=True, text=True))
            
            sys_ver = sys_ver[sys_ver.find('Version:')+8:]
            sys_ver = sys_ver[:sys_ver.find('\\n')].replace(' ','')
            sys_ver = sys_ver[:size]
        if sys_ver != version[p]:
            print("[" + p + "] is not correct version. Correct version: " + version[p])
        else:
            print("[" + p + "] version is correct")
    else:
       # print(p +": " + pkg_resources.get_distribution(p).version)
        latest_version = str(subprocess.run([sys.executable, '-m', 'pip', 'install', '{}==random'.format(p)],
                                            capture_output=True, text=True))
        latest_version = latest_version[latest_version.find('(from versions:')+15:]
        latest_version = latest_version[:latest_version.find(')')]
        latest_version = latest_version.replace(' ','').split(',')[-1]
        #checks if current version is equal to latest version
        if(pkg_resources.get_distribution(p).version != latest_version):
            print("[" + p + "] is not up to date. Latest version is " + latest_version)
            
    #current_version = str(subprocess.run([sys.executable, '-m', 'pip', 'show', '{}'.format(name)],
    #        capture_output=True, text=True))
    #current_version = current_version[current_version.find('Version:')+8:]
    #current_version = current_version[:current_version.find('\\n')].replace(' ','')

