from selenium import webdriver


url = 'https://gaana.com/search/survival%20by%20eminem'
browser = webdriver.Chrome()
browser.get(url)
sleep(20)
song = browser.find_element_by_class_name('loaded')
song.click()
