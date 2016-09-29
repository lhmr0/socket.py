import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 666))

#conexion entrante
s.listen(1)

sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    if recibido == "cerrar":
        break

    print str(addr[0]) + " dice: ", recibido
    sc.send(recibido)
print "Adios."


sc.close()
s.close()