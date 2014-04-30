import webbrowser
import time
print ("program started at " + time.ctime())
for i in range(1,4):
	time.sleep(8)
	print "this is break number " + str(i)
	webbrowser.open("http://mattlichti.github.io/2048/")


