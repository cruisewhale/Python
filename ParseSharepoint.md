  
   1） 安装requests_ntlm, 下载安装包, 手工安装:   
   requests_ntlm: https://pypi.python.org/pypi/requests_ntlm#downloads   
   2)  安装完成后, 检查requests_ntlm是否存在 Python27\Lib\site-packages下. 如果没有, 手工从 gihub :https://github.com/requests/requests-ntlm 直接得复制该目录
         
###Python   
      
      #-*- coding: utf-8 -*-
      #--声明编码， 防止处理中文出错

      import requests
      from requests_ntlm import HttpNtlmAuth


      sites="http://nsnnnnis07/mis/_api/web/lists/GetByTitle('BPM_车辆维修改项目跟进')/Items"
      username='cccil\\nn81291'
      password='suyi+729'

      #XML格式输出
      r=requests.get(sites,auth=HttpNtlmAuth(username,password))

      print r.status_code
      print r.content.decode('utf-8')   #加上.decode('utf-8'), 才可正常显示中文

      #如需转为json 格式输出,使用以下代码
      #headers = {'accept': 'application/json;odata=verbose'}
      #r = requests.get(sites, auth=HttpNtlmAuth(username, password), headers=headers)

      #print r.status_code
      #print r.json()
