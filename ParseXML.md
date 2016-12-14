##解析XML中带命名空间的节点：
如下面的XML, Event 下的节点都有命名空间 http://schemas.microsoft.com/win/2004/08/events/event，
  <?xml version="1.0" encoding="UTF-8" standalone="true"?>
  <Events>
  <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
  <Provider Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" Name="Microsoft-Windows-Security-Auditing"/>
  <EventID>4663</EventID>
  <Version>1</Version>
  <Level>0</Level>
  <Task>12800</Task>
  <Opcode>0</Opcode>
  <Keywords>0x8020000000000000</Keywords>
  <TimeCreated SystemTime="2016-12-13T08:33:15.838807500Z"/>
  <EventRecordID>2063547</EventRecordID>
  <Correlation/>
  <Execution ThreadID="1108" ProcessID="1092"/>
  <Channel>Security</Channel>
  <Computer>NSNNNNIS06.cccil.com</Computer>
  <Security/>
  </System>
  <EventData>
  <Data Name="SubjectUserSid">S-1-5-21-2921067183-3118594533-2991758963-7115</Data>
  <Data Name="SubjectUserName">nn00001</Data>
  <Data Name="SubjectDomainName">CCCIL</Data>
  <Data Name="SubjectLogonId">0x867873</Data>
  <Data Name="ObjectServer">Security</Data>
  <Data Name="ObjectType">File</Data>
  <Data Name="ObjectName">D:\Test\55.txt</Data>
  <Data Name="HandleId">0x1a8</Data>
  <Data Name="AccessList">%%4417 </Data>
  <Data Name="AccessMask">0x2</Data>
  <Data Name="ProcessId">0x14d0</Data>
  <Data Name="ProcessName">C:\Windows\System32\notepad.exe</Data>
  <Data Name="ResourceAttributes">S:AI</Data>
  </EventData>
  </Event>
  </Events>
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

  all = tree.findall('Event:Event/System:System',namespaces)
  print 'Dict count:', len(all)
