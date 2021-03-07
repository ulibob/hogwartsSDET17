import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestTmp():
    def test_address(self):
        # 声明chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址+

        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

        # 点击打开通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        # self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']").click()
        # 元素不可交互报错:
        # E       selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
        # E         (Session info: chrome=88.0.4324.190)
        #     1. 元素被遮挡：元素前面还有其它不可见元素
        #     2. 元素有多个，需要人工挑选合适的元素

        def wait_name(driver):
            print("********-------********")
            # 点击添加成员
            self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()

            eles = driver.find_elements(By.XPATH, "//*[@id='username']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)

        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("我叫小明")

        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("xm123456")

        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("15501863936")


        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()

