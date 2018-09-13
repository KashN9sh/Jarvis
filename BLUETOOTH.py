import bluetooth

while 1:

    a=str(input())

    if a=="вкл":

        bd_addr = "98:D3:32:10:DE:A4"

        port = 1

        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((bd_addr, port))

        sock.send("1111")

        sock.close()
    elif a=="выкл" :

        bd_addr = "98:D3:32:10:DE:A4"

        port = 1

        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((bd_addr, port))

        sock.send("0000")

        sock.close()
