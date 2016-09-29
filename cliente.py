import socket

s = socket.socket()

s.connect(("localhost", 666))

while True:

    mensaje = raw_input("Mensaje a enviar >> ")
    s.send(mensaje)

    #cerrar el servidor
    if mensaje == "cerrar":
        break

print "Adios."

s.close()