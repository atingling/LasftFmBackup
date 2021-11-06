from selenium import webdriver

driver = webdriver.Firefox(executable_path='geckodriver')
driver.get("https://benjaminbenben.com/lastfm-to-csv/")

elem = driver.find_element_by_name('lastfm-user')
elem.clear()
elem.send_keys('alexanderting')

button = driver.find_element_by_xpath("/html/body/div/form/button")
button.click()

flag = True
while flag:
    current_sheet = driver.find_element_by_xpath('/html/body/div/section/h1').text
    if current_sheet == 'finished':
        flag = False

save = driver.find_element_by_xpath('/html/body/div/section/p[2]/a[1]')
save.click()

driver.close()
driver.quit()