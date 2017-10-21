import os
ListenerLogFile = r'listener.log'
i=0
cnt=0
INFO_ListenerLogFile = r'INFO_listener.log'

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
               if len(line) > 1 and 'CONNECT_DATA=' in line:
                   #if 'CONNECT_DATA=' in line:
                      cnt = cnt + 1
                      #print(line)
                      for t in line:
                         f1.write(t)
            print(cnt)

except Exception as err:
	print(err)
