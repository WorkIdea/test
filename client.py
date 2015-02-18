__author__ = 'ImpegI'
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Default socket timeout: %s",s.gettimeout())
s.settimeout(100)
print("Current socket timeout: %s",s.gettimeout())

host_name = socket.gethostname()

print("Host Name: %s",host_name)

print("IP address: %s",socket.gethostbyname(hostname))