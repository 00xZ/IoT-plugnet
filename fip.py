import threading
import sys
import socket, ftplib
import random
import pickle ###serialize shit/ or make it kill itself before it gets too big a buffer 
import time
print "\n +-+-+-+-+-+-+-+-+-+-+-+"
print   " |----MASS FTP SCAN----|"
print   " +-+-+-+-+-+-+-+-+-+-+-+"
threads = str(sys.argv[1])
count = 0
ipf=open('ftpforhydra.txt', 'w')
ipf.write('')
ipf.close()
running = True

def yadigg():
#    for x in range(50): use thisif you on normal hydra not the shitty windows one
        while running == True: #lazy mans thread killing by making tog switch/ doesnt need on linux but the windows hydra is fucky
            a=random.randint(1,254)
            b=random.randint(1,254)
            c=random.randint(1,254)
            d=random.randint(1,254)
            global running
            ip=str(a) + "." +str(b) + "." +str(c) + "." +str(d)
            #print(ip)
            port = 23
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect((ip, port))
                print " [!] FTP: " + ip + " [!]\n"
            #count = count + 1 
                ipf=open('ftpforhydra.txt', 'a')
                ipf.write(ip +  '\n')
                ipf.close()
                running = False
            except Exception ,e:
                pass         
for threads in range(0, int(threads)):
	try:
		count = count + 1
		t = threading.Thread(target=yadigg)
		#t.daemon=True
		t.start()
	except:
		print('Thread failed: ' + str(count))
print('Threads: ' + str(count))
