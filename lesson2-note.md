### fixture 
- 数据的准备，测试前环境准备

* 1、类似setUp, tearDown功能，但比setUp, tearDown更灵活
* 2、直接通过函数名字调用或使用装饰器@pytest.markk.userfixture("test1")
* 3、允许使用多个Fixture
* 4、使用 autouse 自动应用，如果需要返回值，需要传fixture 函数名
* 5、作用域 （session > module > class > function）
* 6、也可以提供测试数据，实现参数化的功能
* 7、fixture 也可以调用fixture

* --setup-show 回溯fixture的执行过程


### conftest.py用法

- 数据共享的文件，名字固定，不能修改
- 可以存放fixture, hook函数
- 就近生效（如果不在同一个文件夹下，离测试文件最近的conftest.py生效）
- 当前目录一定要有__init__.py文件，即：当前的目录是一个包

