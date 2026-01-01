from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")

mailID = driver.find_element(By.ID, "email")
mailID.send_keys("test@gmail.com")

password = driver.find_element(By.ID, "pass")
password.send_keys("test123")

loginBtn = driver.find_element(By.NAME, "login")
loginBtn.click()

driver.quit()