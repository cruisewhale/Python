# Windows Event Log Viewer
# By Suyi 2016-12-23

#Reload system for change the unicode to UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import win32evtlog # requires pywin32 pre-installed
import pymssql
import datetime

print
print 'Start:',datetime.datetime.now()

#win32evtlog parameter
server = 'localhost' # name of the target computer to get event logs
logtype = 'Security' # 'Application' # 'Security'
hand = win32evtlog.OpenEventLog(server,logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

#Mssql parameter
conn=pymssql.connect(server='210.76.150.26',user='FileAccessLogUser',password='asdfg123!!',database='DepartmentFileAccessLog')

cursor=conn.cursor()

def sql(EventRecordID,EventID,EventCategory,EventUser,EventComputer,EventFile,TimeGenerated):

    sqlstr="Insert Into FileAccessLog(EventRecordID,EventID,EventCategory,EventUser,EventComputer,EventFile,EventTime) Values ("+str(EventRecordID)+","+str(EventID)+","+str(EventCategory)+",'"+EventUser+"','"+EventComputer+"','"+EventFile+"','"+str(TimeGenerated)+"')"

    try:
        cursor.execute(sqlstr)
        conn.commit()

    except: 
        print
        print '*****'
        print
    else:
        print 'Record Success!'

    
while True:
    events = win32evtlog.ReadEventLog(hand, flags,0)
    #If Events is end, then Break.
    if not events:
        conn.close()
        print
        print 'End:',datetime.datetime.now()
        break
    
    if events:
        for event in events:
            #EventID=4663 + EventCategory=12800 is File Opertion, EventID=4565 + EventCategory=12800 is Delete File Opertion
            if (event.EventCategory==12800 and event.EventID==4663) or (event.EventCategory==12800 and event.EventID==4565):
 
                #print 'EventRecordID:', event.RecordNumber
                #print 'EventComputer:', event.ComputerName
                #print 'Event Category:', event.EventCategory
                #print 'Time Generated:', event.TimeGenerated
                #print 'Source Name:', event.SourceName
                #print 'Event ID:', event.EventID
                #print 'Event Type:', event.EventType
                data = event.StringInserts
                #Change filename unicode to utf-8 else 
                filename=data[6].encode('utf-8')

                sql(event.RecordNumber,event.EventID,event.EventCategory,data[1],data[2],filename,event.TimeGenerated)

                print
                try:
                    print 'data[1]',data[1]
                    print 'data[2]',data[2]
                    print 'data[6]',filename
                except:
                    print 'data error'



                #Print all event.data message
                #if data:
                #    print 'Event Data:'
                #    for msg in data:
                #        print msg
                #print


      


