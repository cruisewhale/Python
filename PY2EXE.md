##1. 安装  
    说明文档: http://www.py2exe.org/  
    安装文件: https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/  
    注意： 一定要确定你使用PYTHON的版本及32位还是64位, 否则将无法安装
##2. 使用
###1)   使用PYMSSQL:
    **一定要在你的程序中加入以下代码：  
    #--保证使用py2exe 编译文件时, pymssql 能正常编译  
    
    import _mssql  
    import uuid  
    import decimal  
    
    **setup.py 文件需写成:  
    
    from distutils.core import setup  
    import py2exe  
    import os,pymssql  
    data_files = []  
    data_files.append(os.path.join(os.path.split(pymssql.__file__)[0], 'ntwdblib.dll'))  
    py2exe_options = {"includes": ['decimal']}  
    setup(console=['fileaccesslog.py'],   
    options={"py2exe": py2exe_options},   
    data_files=data_files)  
    
    **ntwdblib.dll 将该文件复制到 Python\Lib\site-packages 下
