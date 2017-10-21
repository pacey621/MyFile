import os
import datetime
ListenerLogFile = r'listener.log'
MonthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
i=0
cnt=0
INFO_ListenerLogFile = r'INFO_listener.log'
now = datetime.datetime.now()

try:
    with open(ListenerLogFile,'r') as f:
        list_allline = f.readlines()
        rowcount=len(list_allline)
        f.seek(0,0)

        if os.path.exists(os.getcwd() + '\\' + INFO_ListenerLogFile):
            os.remove(os.getcwd() + '\\' + INFO_ListenerLogFile)
        with open(INFO_ListenerLogFile, 'a') as f1:
            while i < rowcount:
               i = i + 1
               line = f.readline()


               if line[4:8] in MonthList:
                    line_date = datetime.datetime.strptime(line[0:24], "%a %b %d %X %Y")
               elif '月 -' in str(line[0:20]):
                    line_date = datetime.datetime.strptime(line[0:20], "%d-%m月 -%Y %X")
                    #print(line[0:20])
               elif '月-' in str(line[0:20]):
                    line_date = datetime.datetime.strptime(line[0:20], "%d-%m月-%Y %X")
                    #print(line[0:20])
               else:
                    continue

               if len(line) > 1 and 'CONNECT_DATA=' in line and (now-line_date).days < 7:
                   #if 'CONNECT_DATA=' in line:
                      cnt = cnt + 1
                      #print(line)
                      for t in line:
                         f1.write(t)
            print(cnt)

except Exception as err:
	print(err)
