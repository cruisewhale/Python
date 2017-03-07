##1. PyMssql 安装<br>

说明文档:    http://www.pymssql.org/en/stable/intro.html    <br>
微软说明文档: https://docs.microsoft.com/en-us/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development <br>
手工安装包:  http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql <br>

##2. 其他提示：  

在pymssql的 sql 语句请使用 " 号来包括, 中间的字符变量用 ' 来包括:

    sqlstr="Insert Into FileAccessLog(EventUser,EventFile) Values ('"+EventUser+"','"+EventFile+"')" 

    cursor.execute(sqlstr)

    conn.commit()     #一定要加上这句才能确保sql语句正式提交
