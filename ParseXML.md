##1.解析XML中带命名空间的节点：
===========================

参考：

        http://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
        http://effbot.org/zone/element-namespaces.htm
        

如下面的XML, Event 下的节点都有命名空间 http://schemas.microsoft.com/win/2004/08/events/event，

'''xml

&lt;?xml version="1.0" encoding="UTF-8" standalone="true"?&gt;

&lt;Events&gt;

&lt;Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"&gt;

&lt;System&gt;

&lt;Provider Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" Name="Microsoft-Windows-Security-Auditing"/&gt;
  
&lt;EventID&gt;4663&lt;/EventID&gt;
&lt;Version&gt;1&lt;/Version&gt;
          
          &lt;Level&gt;0&lt;/Level&gt;
          &lt;Task&gt;12800&lt;/Task&gt;
          &lt;Opcode&gt;0&lt;/Opcode&gt;
          &lt;Keywords&gt;0x8020000000000000&lt;/Keywords&gt;
          &lt;TimeCreated SystemTime="2016-12-13T08:33:15.838807500Z"/&gt;
          &lt;EventRecordID&gt;2063547&lt;/EventRecordID&gt;
          &lt;Correlation/&gt;
          &lt;Execution ThreadID="1108" ProcessID="1092"/&gt;
          &lt;Channel&gt;Security&lt;/Channel&gt;
          &lt;Computer&gt;NSNNNNIS06.cccil.com&lt;/Computer&gt;
          &lt;Security/&gt;
          &lt;/System&gt;
          &lt;EventData&gt;
          &lt;Data Name="SubjectUserSid"&gt;S-1-5-21-2921067183-3118594533-2991758963-7115&lt;/Data&gt;
          &lt;Data Name="SubjectUserName"&gt;nn00001&lt;/Data&gt;
          &lt;Data Name="SubjectDomainName"&gt;CCCIL&lt;/Data&gt;
          &lt;Data Name="SubjectLogonId"&gt;0x867873&lt;/Data&gt;
          &lt;Data Name="ObjectServer"&gt;Security&lt;/Data&gt;
          &lt;Data Name="ObjectType"&gt;File&lt;/Data&gt;
          &lt;Data Name="ObjectName"&gt;D:\Test\55.txt&lt;/Data&gt;
          &lt;Data Name="HandleId"&gt;0x1a8&lt;/Data&gt;
          &lt;Data Name="AccessList"&gt;%%4417 &lt;/Data&gt;
          &lt;Data Name="AccessMask"&gt;0x2&lt;/Data&gt;
          &lt;Data Name="ProcessId"&gt;0x14d0&lt;/Data&gt;
          &lt;Data Name="ProcessName"&gt;C:\Windows\System32\notepad.exe&lt;/Data&gt;
          &lt;Data Name="ResourceAttributes"&gt;S:AI&lt;/Data&gt;
          &lt;/EventData&gt;
          &lt;/Event&gt;
          &lt;/Events&gt;     
'''

正常的解析代码如下：

      import xml.etree.ElementTree as ET
      fname = 'a3.xml'
      tree = ET.parse(fname)  #打开xml文档 
      all = tree.findall('Event/System',namespaces)
      print 'Dict count:', len(all)
  正常应能统计出共有2个节点 但因为节点带了命名空间，所以无法正确找出。

  这时需要使用 namespaces 属性：

      import xml.etree.ElementTree as ET
      fname = 'a3.xml'
      tree = ET.parse(fname)  #打开xml文档 

      #for elem in tree.getiterator():
      #    print elem.tag,elem.attrib
      #all = tree.findall('{http://schemas.microsoft.com/win/2004/08/events/event}Event')
      #也可使用上面的语名，在节点前加命名空间,会较麻烦,每个节点前都要加上命名空间

      namespaces={'owl':'http://schemas.microsoft.com/win/2004/08/events/event'}
      #可按需增加, 用逗号间隔

      all = tree.findall('owl:Event/System:System',namespaces)
      print 'Dict count:', len(all)
      
##2. 解析XML的所有节点：   
===========================
参考：   
http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/processing-xml-in-python-with-element-tree.html   

        import xml.etree.cElementTree as ET
        #对于XML文件：
        tree = ET.parse('doc1.xml').getroot()
        #对于XML字符串：
        #tree = ET.fromstring(xmlstring)
        #Element 对象有一个 iter 方法可以对子结点进行深度优先遍历
        for elem in tree.iter():
                print elem.tag, elem.attrib        
