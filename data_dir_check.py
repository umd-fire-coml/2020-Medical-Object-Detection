#train, validate, test
#ISBI2016_ISIC_Part3_Training_Data
#  | train
#       | benign
#       | maligmant
#  | test
#       | benign
#       | maligmant
#images titled: ISIC_\d{7}.png
import os
import re

def check_dir ():
    home = os.path.expanduser('~')
    
    if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data'.format(home)):
        print('[ISBI2016_ISIC_Part3_Training_Data] directory does not exist')
        return False
    print('[ISBI2016_ISIC_Part3_Training_Data] directory exists')
    perf = True
   
    #checks test directory
    if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data/test'.format(home)):
        print('[test] directory does not exist')
        perf = False
    else:
        print('[test] directory exists')
        #checks if test/benign exists
        if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data/test/benign'.format(home)):
            print('[benign test] directory does not exist')
            perf = False
        else: 
            print('[benign test] directory exists')
            x = validate_dir('{}/ISBI2016_ISIC_Part3_Training_Data/test/benign'.format(home))
            perf = x if perf else perf
        #checks if test/maligmant exists
        if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data/test/maligmant'.format(home)):
            print('[maligmant test] directory does not exist')
            perf = False
        else:
            print('[maligmant test] directory exists')
            x = validate_dir('{}/ISBI2016_ISIC_Part3_Training_Data/test/maligmant'.format(home))
            perf = x if perf else perf
        
    #checks train directory
    if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data/train'.format(home)):
        print('[train] directory does not exist')
        perf = False
    else:
        print('[train] directory exists')
        #checks if train/benign exists
        if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data/train/benign'.format(home)):
            print('[benign train] directory does not exist')
            perf = False
        else: 
            print('[tumor train] directory exists')
            x = validate_dir('{}/ISBI2016_ISIC_Part3_Training_Data/train/benign'.format(home))
            perf = x if perf else perf
        #checks if train/maligmant exists
        if not os.path.isdir('{}/ISBI2016_ISIC_Part3_Training_Data/train/maligmant'.format(home)):
            print('[maligmant train] directory does not exist')
            perf = False
        else:
            print('[normal train] directory exists')
            x = validate_dir('{}/ISBI2016_ISIC_Part3_Training_Data/train/maligmant'.format(home))
            perf = x if perf else perf

    if not perf:
        return False
    print('Data directory and all subdirectories are correct, with correct data')
    return True

def validate_dir(name):
    s = True
    for filename in os.listdir(name):
        if not re.match('ISIC_(\d{7})\.png', filename):
            print('[{}] is not part of [{}] directory.'.format(filename, name))
                s = False
        
    return True if s else False

check_dir()
