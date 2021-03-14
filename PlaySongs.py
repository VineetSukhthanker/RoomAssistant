from selenium import webdriver
from time import sleep

def play_songs(name):
    name = name.replace(" ", "%20")
    url = 'https://gaana.com/search/{name}'.format(name=name)
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(20)
    song = browser.find_element_by_class_name('loaded')
    song.click()
    sleep(5)
    time = browser.find_element_by_class_name('ttime').text
    time = int(time[0:2])*60 + int(time[3:])

    for x in range(time):
        sleep(1)

    browser.quit()