from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp():
    def setup_method(self, method):
        # 声明 chrome 的函数
        chrome_arg = webdriver.ChromeOptions

        # 加入调试地址
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.vars = {}


    def teardown_method(self, method):
        self.driver.quit()


    def test_main_tmp(self):
        '''

        基于首页登录
        :return:
        '''
        self. driver.get("https://work.weixin.qq.com")
        self.driver.find_element(By.XPATH, "//*[@class='index_to_operation']")
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_']")
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']")

        sleep(6)
        self.driver.close()