from selenium import webdriver
from time import sleep

url = 'https://gaana.com/search/survival%20by%20eminem'
browser = webdriver.Chrome()
browser.get(url)
sleep(12)
song = browser.find_element_by_class_name('loaded')
song.click()
