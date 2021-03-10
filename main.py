from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://v4.eccube-plugin.net/")
assert "あずみ.net" in driver.title
driver.close()