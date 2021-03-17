# pip install appium-python-client
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"  # 不清空缓存
        # 动态页面加载idle超时时长默认设置是（10000ms），重设以加快速度
        caps["settings[waitForIdleTimeout]"] = 500

        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        '''
        前提条件
            已登录状态（noReset=True）
        打卡用例：
        1.打开【企业微信】应用
        2.进入【工作台】
        3.点击【打卡】
        4.选择【外出打卡】tab
        5.点击【第N次打卡】
        6.验证【外出打卡成功】
        7.退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        # android_uiautomator是java语言写的， 里面字符串要用双引号，外面用单引号
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        # print(self.driver.page_source)
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        
        # 用find_element方法激活隐式等待，确保断言时内容已加载
        assert self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
