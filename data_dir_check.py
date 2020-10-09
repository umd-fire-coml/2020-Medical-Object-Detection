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
        print('data directory does not exist')
        return False
    print('data directory exists')
    perf = True
    def validate_dir(name):
        s = True
        for filename in os.listdir(name):
            if not re.match('normal_(\d{3}).tif', filename)and not re.match('tumor_(\d{3}).tif', filename):
                print('{} is not part of validate directory.'.format(filename))
                s = False
        return True if s else False
    #checks validate directory
    if not os.path.isdir('{}/data/validate'.format(home)):
        print('validate directory does not exist')
        perf = False
    else:
        print('validate directory exists')
        perf = validate_dir('{}/data/validate'.format(home))
    #checks test directory
    if not os.path.isdir('{}/data/test'.format(home)):
        print('test directory does not exist')
        perf = False
    else:
        print('test directory exists')
        x = validate_dir('{}/data/test'.format(home))
        perf = x if perf else perf
    #checks train directory
    if not os.path.isdir('{}/data/train'.format(home)):
        print('train directory does not exist')
        perf = False
    else:
        print('train directory exists')
        x = validate_dir('{}/data/train'.format(home))
        perf = x if perf else perf
        
    if not perf:
        return False
    print('Data directory and all subdirectories are correct, with correct data')
    return True




