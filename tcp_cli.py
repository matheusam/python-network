import socket

target_host = "www.google.com"
target_port = 80
#cria socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#conecta 
client.connect((target_host,target_port))
#envia data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#recebe resp
response = client.recv(4096)

print response


