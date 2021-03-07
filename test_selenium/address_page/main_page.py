
from selenium import webdriver
from selenium.webdriver.common.by import By




class MainPage:
    def __init__(self, driver=None):
        if driver != None:
            self.driver = driver
        else:
            chrome_args = webdriver.ChromeOptions()
            chrome_args.debugger_address = "127.0.0.1:9222"
            # 需手动启chrome并登录  'chrome -remote-debugging-port=9222' 进行复用
            self.driver = webdriver.Chrome(options=chrome_args)
            self.driver.implicitly_wait(5)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def goto_address(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # 防止循环引用报错：most likely due to a circular import，在使用时导入
        from test_selenium.address_page.address_page import AddressPage
        return AddressPage(self.driver)

    def goto_add_contacts(self):
        self.driver.find_element(By.XPATH, "//*[@class='ww_indexImg ww_indexImg_AddMember']")
        return self.driver
