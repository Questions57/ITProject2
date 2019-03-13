import socket
import sys


DNSRS_table = {}
file = open("PROJ2-DNSRS.txt", "r")
tsHostname = ""
#looping through each line to fill table info
for line in file: 
	elems = line.split()
	hostname = elems[0].lower()
	value = elems[1]+" "+elems[2]
	print("RS ROW:", str(elems))
	DNSRS_table[hostname] = value

file.close()


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

queries = []

while True:
	data = conn.recv(BUFFER_SIZE)
	if data == "finished":
		break
	else:
		queries.append(data)


sendBackStrings = [] #list of addresses to send back to client

for query in queried_hostnames:
	query = query.lower()
	if query in DNSRS_table:
		resolvedEntry = query + " " + DNSRS_table[query]
		sendBackStrings.append(resolvedEntry)

finalSendBack = ""

for line in sendBackStrings:
	finalSendBack += line+','

print("SENDBACK: "+finalSendBack)
conn.sendAll(finalSendBack)

ss.close()
exit()