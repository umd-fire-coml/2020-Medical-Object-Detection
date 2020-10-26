#train, validate, test
#data
#  | train
#  | test
#images titled: normal_00x.tif , tumor_00x.tif
import os
import re

def check_dir ():
    home = os.path.expanduser('~')
    
    if not os.path.isdir('{}/data'.format(home)):
        print('[data] directory does not exist')
        return False
    print('[data] directory exists')
    perf = True
   
"""
    #checks validate directory
    if not os.path.isdir('{}/data/validate'.format(home)):
        print('[validate] directory does not exist')
        perf = False
    else:
        print('validate directory exists')
        if not os.path.isdir('{}/data/validate/tumor'.format(home)):
            print('[tumor validate] directory does not exist')
            perf = False
        else: 
            print('[tumor validate] directory exists')
            x = validate_dir('{}/data/validate/tumor'.format(home), "tumor")
            perf = x if perf else perf
        if not os.path.isdir('{}/data/validate/normal'.format(home)):
            print('[normal validate] directory does not exist')
            perf = False
        else:
            print('[normal validate] directory exists')
            x = validate_dir('{}/data/validate/normal'.format(home), "normal")
            perf = x if perf else perf
  """
    #checks test directory
    if not os.path.isdir('{}/data/test'.format(home)):
        print('[test] directory does not exist')
        perf = False
    else:
        print('[test] directory exists')
        x = validate_dir('{}/data/test'.format(home), "both")
        perf = x if perf else perf
    #checks train directory
    if not os.path.isdir('{}/data/train'.format(home)):
        print('[train] directory does not exist')
        perf = False
    else:
        print('[train] directory exists')
        if not os.path.isdir('{}/data/train/tumor'.format(home)):
            print('[tumor train] directory does not exist')
            perf = False
        else: 
            print('[tumor train] directory exists')
            x = validate_dir('{}/data/train/tumor'.format(home), "tumor")
            perf = x if perf else perf
        if not os.path.isdir('{}/data/train/normal'.format(home)):
            print('[normal train] directory does not exist')
            perf = False
        else:
            print('[normal train] directory exists')
            x = validate_dir('{}/data/train/normal'.format(home), "normal")
            perf = x if perf else perf

    if not perf:
        return False
    print('Data directory and all subdirectories are correct, with correct data')
    return True

def validate_dir(name, typ):
    s = True

    for filename in os.listdir(name):
        if typ == "tumor":
            if not re.match('tumor_(\d{3}).tif', filename):
                print('[{}] is not part of [{}] directory.'.format(filename, name))
                s = False
        elif typ == "normal":
            if not re.match('normal_(\d{3}).tif', filename):
                print('[{}] is not part of [{}] directory.'.format(filename, name))
                s = False
        else:
            if not re.match('normal_(\d{3}).tif', filename)and not re.match('tumor_(\d{3}).tif', filename):
                print('[{}] is not part of [{}] directory.'.format(filename, name))
                s = False
        
    return True if s else False



