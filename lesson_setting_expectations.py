import time
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r'/usr/local/bin/chromedriver/chromedriver')
options = webdriver.ChromeOptions()

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(service=service, options=options)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/cats.html")
#time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.ID, "button")

#time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
