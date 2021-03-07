from selenium import webdriver
from selenium.webdriver.common.by import By


class AddcontactsPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def contact_save_and_continue_add(self):
        # 需调用add_message方法，添加成员信息再调用保存，否则给与提示
        # 添加一个成员后继续添加成员，页面不跳转
        # if self.driver.find_element(By.XPATH, "//*[@id='username']").get_attribute("value"):
        a = self.driver.find_element(By.XPATH, "//*[@id='username']").get_attribute("value")
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_cancel']").click()

    def contact_cancel(self):
        # 取消成员添加，返回到通讯录页 AddressPage

        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_cancel']")[-1].click()
        from test_selenium.address_page.address_page import AddressPage
        return AddressPage(self.driver)

    def have_base_mssge(self):
        '''
        用以验证，输入框内是否已经包含必填信息(暂时用不着)
        :return: True  False
        '''
        name = self.driver.find_element(By.XPATH, "//*[@id='username']").get_attribute("value")
        acctid = self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").get_attribute("value")
        mobile = self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").get_attribute("value")
        return bool(name and acctid and mobile)

    def contact_save(self):
        '''
        save contact message and return to AddressPage
        :return:  AddressPage
        '''
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")[-1].click()
        from test_selenium.address_page.address_page import AddressPage
        return AddressPage(self.driver)

    def add_message(self):
        name = "test00002"
        acctid = "test10002"
        moblie = "13900011102"

        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(name)

        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys(acctid)
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys(moblie)
