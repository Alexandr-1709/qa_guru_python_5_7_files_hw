from zipfile import ZipFile
import zipfile
import os
from os_path.os_path_scripts import resources

zip_path = resources
zip_file = 'zip_test_file.zip'


def test_add_zip_file():

    with zipfile.ZipFile(zip_file, 'w') as zip_files:
        for i in os.listdir(zip_path):
            file_path = os.path.join(zip_path, i)
            zip_files.write(file_path, i)

    with zipfile.ZipFile(zip_file, "r") as zip_files:
        for i in os.listdir(zip_path):
            assert i in zip_files.namelist()

    os.remove(zip_file)