1. OSX Install python pakge Issue<br>
使用该命令 sudo pip install pandas <br>
如果没有安装 pip, 请首先使用下面的命令<br>
 sudo easy_install pip <br>
直接使用 
   sudo easy_install pandas ,出以以下错误：
   OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/pandas 

2. 安装xcode 开发工具包，在Terminal中运行：<br>
   xcode-select --install <br>
   在python中的一些Lib的支持， 如lxml HTML 解析器， 需要C语言库支持， 就包含在这个工具包中
