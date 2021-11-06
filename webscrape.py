from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("https://benjaminbenben.com/lastfm-to-csv/")

elem = driver.find_element_by_name('lastfm-user')
elem.clear()
elem.send_keys('alexanderting')

driver.find_element_by_css_selector('btn btn-primary btn-lg').click()
driver.wait(10)

driver.close()
driver.quit()