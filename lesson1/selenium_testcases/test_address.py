import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestTmp():
    def setup_method(self, method):
        # 声明Chrome参数
        chrome_arg = webdriver.ChromeOptions()
        # 地址
        chrome_arg.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)



    def test_adduser(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # self.driver.implicitly_wait(5)
        time.sleep(3)
        # self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()
