from donotprint.donotprint import Print

my_str = 'string'

a = Print(True)
a.print(my_str + '1')  # 此时会输出值

b = Print(False)
b.print(my_str + '2')  # 此时不会输出值
