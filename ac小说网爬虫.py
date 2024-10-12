import time
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")
driver = selenium.webdriver.Chrome(options=option)
driver.get('https://www.acxsw.com/shu/30/30498/106188.html')


def save_xiaoshuo():
    # 等待某个元素出现
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/main/section'))
    )

    title = element.find_element(By.XPATH, 'div[2]/p').text

    content = element.find_element(By.ID, 'article').text

    # 打开或创建一个TXT文件，以写入模式（'w'）
    with open('output.txt', 'a', encoding='utf-8') as file:
        # 写入内容
        file.write(title + '\n' + content + '\n')
    return driver.find_element(
        By.ID, 'next_url')

try:
    btn = save_xiaoshuo()
  
    while (btn.get_attribute('class') != 'w_gray'):
        btn.click()
        btn = save_xiaoshuo()

finally:
    driver.quit()
