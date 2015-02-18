__author__ = 'ImpegI'
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Default socket timeout: %s",s.gettimeout())
s.timeout(100)
print("Current socket timeout: %s",s.gettimeout())