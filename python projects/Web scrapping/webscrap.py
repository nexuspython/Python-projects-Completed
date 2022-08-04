from selenium import webdriver

driver = webdriver.Chrome("F:\python projects\Web scrapping\chromedriver.exe")
driver.get("https://www.siddharthacapital.com/check-share-allotment-ipo-fpo/")



company = driver.find_element("xpath",'//*[@id="company-name-i"]')
company.click


search = driver.find_element("xpath",'//*[@id="boid-i"]')
search.send_keys("1235636465454676")

searchbutton = driver.find_element("xpath",'//*[@id="ipo-check"]/div[3]/button[1]')

searchbutton.click()

