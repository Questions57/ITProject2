import socket
import sys


DNSRS_table = {}
file = open("PROJI-DNSTS.txt", "r")

#looping through each line to fill table info
for line in file: 
	elems = line.split()
	hostname = elems[0].lower()
	value = elems[1]+" "+elems[2]
	DNSRS_table[hostname] = value
	

file.close() 
#print(DNSRS_table)

try:
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("[S]: RS server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()


server_hostname = socket.gethostname()
port = sys.argv[1] #listening port specified by user
server_address = (server_hostname, int(port))
print("ADDRESS: "+ str(server_address))
ss.bind(server_address)
ss.listen(1)

print("[S]: Server host name is {}".format(server_hostname))
host_ip = (socket.gethostbyname(server_hostname))
print("[S]: Server IP address is {}".format(host_ip))
conn, addr = ss.accept()
#print ("[S]: Got a connection request from a client at {}".format(addr))


print('Connected by', addr)
queried_hostnames_str = conn.recv(2048)
queried_hostnames = queried_hostnames_str.split() #list of all hostnames being queried
print('query: '+ str(queried_hostnames))

sendBack = ""
for query in queried_hostnames:
	query = query.lower()
	sendBack += query + " " + DNSRS_table.get(query, "- Error:HOST NOT FOUND") + ","

print("SENDBACK: "+sendBack)
conn.sendall(sendBack)

ss.close()
exit()