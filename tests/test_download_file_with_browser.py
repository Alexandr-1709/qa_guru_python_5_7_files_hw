import time
import os
from os_path.os_path_scripts import PROJECT_ROOT_PATH
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


def test_download_file_with_browser():
    download_dir = os.path.join(PROJECT_ROOT_PATH, 'resources')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)

    browser.config.driver = driver

    browser.open("https://demoqa.com/upload-download")
    browser.element('[id = downloadButton]').click()
    time.sleep(10)
    file_name = os.path.join(download_dir, 'sampleFile.jpeg')
    file_size = os.path.getsize(file_name)
    assert file_size == 4096
