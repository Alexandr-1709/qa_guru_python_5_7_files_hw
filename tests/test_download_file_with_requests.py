import os.path
from os_path_scripts import PROJECT_ROOT_PATH
import requests


# TODO сохранять и читать из tmp, использовать универсальный путь


def test_downloaded_file_size():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    downloaded_file = os.path.join(PROJECT_ROOT_PATH, 'tmp', 'selenium_logo.png')
    r = requests.get(url)

    with open(downloaded_file, 'wb') as file:
        file.write(r.content)

    size = os.path.getsize(downloaded_file)

    assert size == 30803

