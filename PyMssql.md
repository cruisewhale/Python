##1. PyMssql 安装<br>

说明文档:    http://www.pymssql.org/en/stable/intro.html    <br>
微软说明文档: https://docs.microsoft.com/en-us/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development <br>
手工安装包:  http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql <br>
      

##2. 安装xcode 开发工具包，在Terminal中运行：<br>
​
   xcode-select --install <br>
 
   在python中的一些Lib的支持， 如lxml HTML 解析器， 需要C语言库支持， 就包含在这个工具包中

##3. 中文编码不能识别问题, 参考http://blog.csdn.net/zuyi532/article/details/8851316 ：
​
    import sys  
    reload(sys)  
    sys.setdefaultencoding('utf-8')  
    
    #在程序的开始加上上面的代d重码, 目的是重新装载 sys, 并将编码设为utf-8  
    对于变量, 可使用 .encode 重新编码"  
    filename=data[6].encode('utf-8')  
