

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

      #sharepoint的XML输出带有命名空间, 解析时需带上命名空间名称
      namespaces={'owl':'http://www.w3.org/2005/Atom'}
      results = tree.findall('owl:entry',namespaces)
      print 'User count:', len(results)

      for child in tree.iter(tag='{http://schemas.microsoft.com/ado/2007/08/dataservices}Title'):
	        print child.tag,child.text
      #for child in tree:
      #	#print child.tag,child.attrib
      #	for child1 in child:
      #		if child1.tag=='{http://www.w3.org/2005/Atom}content':
      #			print child1.attrib
      #			print child1[0][5].text
      #			print child1.find('Title').text
