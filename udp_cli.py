import socket

target_host = "127.0.0.1"
target_port = 80

#cria socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#envia data (nao conecta pois udp n orienta conex)
client.sendto("AAABBBCCC", (target_host,target_port))

#recebe resp
data, addr = client.recvfrom(4096)

print data

