import socket
import sys


queries = []
file = open("PROJ2-HNS.txt", "r")

#looping through each line to fill table info
for line in file: 
	queries.append(line)

file.close() 
print(queries)

#def client():
try:
	cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("[C]: Client socket created")
except:
	print('socket open error: {} \n'.format(err))
	exit()


rs_port = sys.argv[2] #port on which RS is listening
rs_hostname = sys.argv[1] #hostname of machine running RS

rs_host_addr = socket.gethostbyname(rs_hostname) #address of RS host
print("ADDRESS: "+rs_host_addr)

rs_binding = (rs_host_addr, int(rs_port))
cs.connect(rs_binding)

for query in queries:
	print("SENDING TO RS: "+ query)
	cs.sendall(query)

cs.sendall("finish") #keyword to send to close connection with RS

data = cs.recv(1024)
print("DATA: "+data)
rawOutput = data.split(',')

outputFile = open("RESOLVED2.txt", "w")


for line in rawOutput:
	outputFile.write(line+"\n")

outputFile.close()


cs.close()
exit()



