import os
from pathlib import Path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#This functions runs only if the steps to download


def download_images():

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
    drive = GoogleDrive(gauth)

    #Change this to the parent directory of your choice
    parent_dir = "C:/Cancer_Data/"

    os.mkdir(parent_dir)
    os.mkdir(parent_dir + "training")
    os.mkdir(parent_dir + "validate")
    os.mkdir(parent_dir + "test")

    os.mkdir(parent_dir + "training/normal")
    os.mkdir(parent_dir + "training/tumor")

    os.mkdir(parent_dir + "validate/normal")
    os.mkdir(parent_dir + "validate/tumor")

    fileList_normal = drive.ListFile(
        {'q': "'0BzsdkU4jWx9BNUFqRE81QS04eDg' in parents and trashed=false"}).GetList()

    #download 100 images from this folder (001 - 110) into training/normal
    #download 40 images from this folder (111 - 160) into validate/normal

    """""
    for i, file1 in enumerate(sorted(fileList_normal, key=lambda x: x['title']), start=1):
        print('Downloading {} from GDrive ({}/{})'.format(file1['title'], i, len(fileList_normal)))
        file1.GetContentFile(file1['title'])
    """""

    i = 1
    for file1 in fileList_normal():
        if(i <= 100):
            #put file into training/normal
            file1.GetContentFile(file1['title'])
        else:
            #put file into training/validate
            file1.GetContentFile(file1['title'])

    fileList_tumor = drive.ListFile(
        {'q': "'0BzsdkU4jWx9BUzVXeUg0dUNOR1U' in parents and trashed=false"}).GetList()

    # download 77 images from this folder (001 - 077) into training/tumor
    # download 34 images from this folder (078 - 111) into validate/tumor

    """""
    for i, file1 in enumerate(sorted(fileList_tumor, key=lambda x: x['title']), start=1):
        print('Downloading {} from GDrive ({}/{})'.format(file1['title'], i, len(fileList_tumor)))
        file1.GetContentFile(file1['title'])
    """""

    j = 1
    for file1 in fileList_tumor():
        if (j <= 77):
            # put file into training/normal
            file1.GetContentFile(file1['title'])
        else:
            # put file into training/validate
            file1.GetContentFile(file1['title'])

    fileList_test = drive.ListFile(
        {'q': "'0BzsdkU4jWx9BUzVXeUg0dUNOR1U' in parents and trashed=false"}).GetList()

    # download all images from this folder into test
    """""
    for i, file1 in enumerate(sorted(fileList_test, key=lambda x: x['title']), start=1):
        print('Downloading {} from GDrive ({}/{})'.format(file1['title'], i, len(fileList_test)))
        file1.GetContentFile(file1['title'])
    """""

    for file1 in fileList_test():
        file1.GetContentFile(file1['title'])