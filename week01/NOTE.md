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
## time模块与datetime模块
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
***timedelta 对象表示两个 date 或者 time 的时间间隔。***

`class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`


---------------------------------------------
## logging模块
##### 日志级别
###### 日志功能应以所追踪事件级别或严重性而定。各级别适用性如下（以严重性递增）：
1. debug()     #细节信息，仅当诊断问题时使用。
2. info()      #确认程序按预期运行
3. warning()   #表明有已经或即将发生的意外。程序仍按照预期运行 
4. error()     #由于严重的问题，程序的某些功能已经不能正常执行
5. critical()  #严重的错误，表明程序已经不能继续执行

###### 示例：
```
import logging
logging.warning('Watch out!')
logging.info('I told you so')
```
**info信息没有打印，因为默认级别是warning**

###### 记录日志到文件中
```
import logging
logging.basicConfig(filename='example.log', level=logging.BEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

###### 修改日志记录格式
```
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                    )
logging.info('info message')
```


---------------------------------------------
