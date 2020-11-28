# 学习笔记

## 函数和模块的区别

#### 常见模块

1. time
2. datetime
3. logging
4. random
5. json
6. pathlib
7. os.path

##### 自定义一个模块
###### 创建一个自定义文件夹，编写main.py、short.py
*main.py*
```
    import short
    short.short_func()
```
*short.py*
```
    def short_func():
        print('life is short')
    if __name__ == '__main__':
        short_func()
```
***`__name__ == '__main__'`的作用是，在程序本身执行时，作为主程序入口，而作为第三方模块导入的时候，忽略这部分代码***


---------------------------------------------
#### time模块与datetime模块
##### time
```
import time
time.time() #时间戳
time.localtime() #本地时间
time.strftime('%Y-%m-%d %X', time.localtime())
```
##### datetime
```
from datetime import *
datetime.today()
datetime.now() #都指当前时间
datetime.today() -timedelta(days=1) #昨天
```
*** timedelta 对象表示两个 date 或者 time 的时间间隔。***

`class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`
