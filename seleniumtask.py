from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Users/Q1/PythonAlgoritmika/Ders8/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://userinyerface.com/game.html")

input("Press Enter to close the browser...")

driver.quit()
