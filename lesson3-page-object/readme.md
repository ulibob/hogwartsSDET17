## Web企业微信实战：
- 实现通讯录添加成员
- 三种等待机制强化理解
- 了解Page Object 模式
- 利用PO封装企业微信通讯录

### 

## 浏览器复用

### 环境变量配置
```angular2
self.driver = webdriver.Chrome()
```
*1 chrome的配置问题：
    * Chrome driver 版本要与 chrome 版本一致
    * 将chromedriver配置到系统（或用户）变量中
    * 重启命令行以及pycharm
    
*2 如果报错，分析报错信息
*3 浏览器不要设置缩放

### 浏览器调试
`chrome --remote-debugging-port=9222`


- 命令：
`chrome remote-debugging=9222`
- 测试用例中代码：
```python
from selenium import webdriver

class TestTmp():
    def setup_method(self, method):
        # 声明Chrome参数
        chrome_arg = webdriver.ChromeOptions()
        # 地址
        chrome_arg.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.get("http://www.baidu.com")

```