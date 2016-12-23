##目的：解析windoows 事件日志，并将需要的事件写入SQLSERVER, 方便查询##
##参考文档： 
### 1. ActivePython :  

安装ActivePython, ActivePython 包含了一个完整的 Python 内核，直接调用 Python 官方的开源内核，此外还有 Python 编程需要用到的 IDE，并附加了一些    Python 的 Windows扩展，同时还提供了全部的访问 Windows APIs 的服务。ActivePython 虽然不像纯 Python 那样是开源的，但是也可以免费下载使用。http://www.activestate.com/active   

### 2. PYMSSQL: 

安装 PYMSSQL 下载地址：  http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql    
使用参考：https://docs.microsoft.com/en-us/azure/sql-database/sql-database-develop-python-simple  
注意事项： 如果安装不成功, 试着升级 pip 工具, 在python环境: 
  
    pip install --upgrade pip

其他提示：在pymssql的 sql 语句请使用 " 号来包括, 中间的字符变量用 ' 来包括：  
    sqlstr="Insert Into FileAccessLog(EventUser,EventFile) Values ('"+EventUser+"','"+EventFile+"')"  
否则语句将无法正确执行
