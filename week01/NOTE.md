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
    (```)
    import short
    short.short_func()
    (```)
    *short.py*
    (```)
    def short_func():
        print('life is short')
    
    if __name__ == '__main__':
        short_func()
    (```)
    *** __name__ == '__main__' 的作用是，在程序本身执行时，作为主程序入口，而作为第三方模块导入的时候，忽略这部分代码***