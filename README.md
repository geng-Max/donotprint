<h1 style="color: blue">模块介绍</h1>

这个模块封装了一个类，类中有一个__init__方法和一个print方法，

当初始化传入的时True时，print方法等同于内置函数print，

当传入False时，print方法不会打印任何东西。

<h1 style="color: blue">代码示例</h1>

```python
from donotprint.donotprint import Print

my_str = 'string'

a = Print(True)
a.print(my_str)  # 此时会输出值

b = Print(False)
b.print(my_str)  # 此时不会输出值
```
