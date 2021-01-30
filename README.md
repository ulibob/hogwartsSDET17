# hogwartsSDET17
Development Test homework

- homework practice

    1、补全计算器（加法 除法）的测试用例
    2、使用参数化完成测试用例的自动生成
    3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
- 注意

    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()

- 2021年1月28日 23:54:48

分析：

- 将加法
    
    
    
-  区分：setup(), teardown() , setup_class(), teardown_class()
    函数级别方法：setup(), teardown()
                每个测试函数都会执行一次前处理和后处理
    类级别方法：setup_class(),teardown_class() 
                每个测试类运行之前\后只从一次（不关心类里有多少个测试用例）
                