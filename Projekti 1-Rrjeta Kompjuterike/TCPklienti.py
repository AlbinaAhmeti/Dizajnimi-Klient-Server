from socket import *
import socket
import sys

print('             Programi TCP-Klient\n               ')

serverName = 'localhost'  #localhost
serverPort = 14000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((serverName,serverPort))

Kerkesa = ""

print("Serveri: ",serverName,", porti: ",serverPort)
print("\n")

print("Shtypni kërkesen tuaj: ")
print(" IP\n NRPORTIT\n NUMERO [NUMERO {Hapësire} tekst]\n ANASJELLTAS [ANASJELLTAS {Hapësire} tekst]\n PALINDROM [PALINDROM {Hapësire} tekst]\n KOHA\n LOJA\n GCF [GCF {Hapësire} Numër1 {Hapësire} Numër2]\n KONVERTO [KONVERTO {Hapësire} Opcioni {Hapësire} Numër]{Opcioni:cmNeInch,inchNeCm,kmNeMiles,mileNeKm}\n NUMRI [NUMRI {Hapësire} Numër]\n FIBONACCI [FIBONACCI {Hapësire} Numër]\n")

print("Shtyp exit per te ndaluar programin.\n")

while 1:
    try:
        Kerkesa = input('Shkruaj kërkesen dhe opsionin(nese ka): ')
        if Kerkesa!="" and Kerkesa.upper()!="EXIT":
        
            s.sendall(str(Kerkesa).encode())
        else:
            break
        
        data = s.recv(128)
        print('Të dhënat nga serveri: ')
        print(str(data.decode()).strip())
    except Exception as m:
        print("\n")
        print(str(m))
        break
    
s.close()   
