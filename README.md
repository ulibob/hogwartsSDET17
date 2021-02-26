# hogwartsSDET17
Development Test homework

- practice20210128

    1、补全计算器（加法 除法）的测试用例
    2、使用参数化完成测试用例的自动生成
    3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
- 注意

    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()

- 2021年1月28日 23:54:48

分析：

    等价类：有效类 无效类
    加法
        有效类：
            int int
            bignum, bignum
            float, float
            ngt, ngt
            ngt, 0
            0, ngt
        无效类：
            字符串："dfafdasfhdrgft"
            特殊符号：@#￥%&\*……       
    边界值 0 
    
    减法：同加法
    乘法：同加法
    除法：        有效类：
            int int
            bignum, bignum
            float, float
            ngt, ngt
            ngt, 0
            0, ngt
        无效类：
            除数为零情况
            字符串："dfafdasfhdrgft"
            特殊符号：@#￥%&\*……     
             
    2021年1月30日 18:36:37  
    
- 补充：此处计算函数只支持int类型和float类型，complex复数无法进行计算直接返回"请输入正确数字"
 
   
-  区分：setup(), teardown() , setup_class(), teardown_class()
    函数级别方法：setup(), teardown()
                每个测试函数都会执行一次前处理和后处理
    类级别方法：setup_class(),teardown_class() 
                每个测试类运行之前\后只从一次（不关心类里有多少个测试用例）
                
                
                
#### pytest常用的插件
- pip install pytest-ordering      控制用例的执行顺序
- pip install pytest-dependency    控制用例的依赖关系 (可添加复杂的依赖关系)
- pip install pytest-xdist         分布式并发执行测试用例
- pip install pytest-rerunfailures 失败重跑  【用法】：`pytest test_rerun --reruns 5` `pytest test_run --reruns 5 --reruns-delay 1`
- pip install pytest-assume        多重校验
- pip install pytest-random-order  用例随机执行
- pip install pytest-html          测试报告


#### 测试用例的一些基本原则：
* 不要让case有顺序
* 不要让测试用例有依赖
* 如果你无法做到，可以临时性的用插件解决

### 插件的开发
* 内置plugin:
    *从代码内部的_pytest目录加载
    
* 外部插件（第三方插件）：
    * 通过 setuptools entry points 机制发现的第三方插件（https://docs.pytest.org/en/latest/plugins.html）
    
* conftest.py存放的本地插件：【重点关注】
    * 自动模块发现机制
    
* pytest --trace-config查看当前pytest中所有的plugin(带有hook方法的文件)