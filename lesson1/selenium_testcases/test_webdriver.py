from selenium import webdriver

class TestTmp():
    def setup_method(self, method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver.get("http://www.baidu.com")


    def test_1(self):
        self.driver.get("http://www.baidu.com")
        cookies = self.driver.get_cookies()
        for i in cookies:
            pass
# todo: 需完善