from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/")

print(driver.title)
print(driver.current_url)

driver.close()
#driver.quit()
