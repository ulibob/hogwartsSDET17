## 浏览器复用

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