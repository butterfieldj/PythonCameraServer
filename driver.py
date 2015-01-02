from socket_listener import Socket_Listener
import time

s = Socket_Listener()
print 'starting'
s.start_command("start")
time.sleep(20)
print 'stopping'
s.start_command("stop")
exit()
