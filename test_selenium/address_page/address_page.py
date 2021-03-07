from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.address_page.main_page import MainPage


class AddressPage:
    def __init__(self, driver1: webdriver):
        self.driver = driver1

    def goto_main_page(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_index']").click()
        return MainPage(self.driver)

    def goto_addcontacts(self):
        '''

        注意：这里的添加成员元素，完全加载出来和可点击并不是同步的需要设置显示等待，确保“添加成员”元素点击生效
        :return:
        '''
        def _wait_name(driver):
            print("********----显式等待执行---********")
            # 点击添加成员
            self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()

            eles = self.driver.find_elements(By.XPATH, "//*[@id='username']")
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(_wait_name)

        from test_selenium.address_page.addcontacts_page import AddcontactsPage
        return AddcontactsPage(self.driver)

