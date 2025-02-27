from selenium import webdriver
import time
import math

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r'/usr/local/bin/chromedriver/chromedriver')
options = webdriver.ChromeOptions()

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(service=service, options=options)


# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button = driver.find_element(By.ID, "book").click()

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.ID, "answer")

def calculate_expression(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x = driver.find_element(By.ID, "input_value").text

# Напишем текст ответа в найденное поле
textarea.send_keys(calculate_expression(x))

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.ID, "solve").click()

time.sleep(10)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
