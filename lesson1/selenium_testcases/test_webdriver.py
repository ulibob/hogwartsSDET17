from selenium import webdriver

class TestTmp():
    def setup_method(self, method):
        # 声明Chrome参数
        chrome_arg = webdriver.ChromeOptions()
        # 地址
        chrome_arg.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(5)


    def test_1(self):
        self.driver.get("http://www.baidu.com")
        cookies = self.driver.get_cookies()
        for i in cookies:
            print(i)
# todo: 需完善