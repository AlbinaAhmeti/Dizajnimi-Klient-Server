from socket import *

print('Programi UDP-Klient\n')

serverName = '127.0.0.1'  #localhost
serverPort = 14000

s = socket(AF_INET, SOCK_DGRAM)

print("Serveri: ",serverName,", porti: ",serverPort)
print("\n")

print("Shtypni kërkesen tuaj: ")
print("\n")
print(" IP\n NRPORTIT\n NUMERO [NUMERO {Hapësire} tekst]\n ANASJELLTAS [ANASJELLTAS {Hapësire} tekst]\n PALINDROM [PALINDROM {Hapësire} tekst]\n KOHA\n LOJA\n GCF [GCF {Hapësire} Numër1 {Hapësire} Numër2]\n KONVERTO [KONVERTO {Hapësire} Opcioni {Hapësire} Numër]{Opcioni:cmNeInch,inchNeCm,kmNeMiles,mileNeKm}\n NUMRI [NUMRI {Hapësire} Numër]\n FIBONACCI [FIBONACCI {Hapësire} Numër]\n")

print("Shtyp exit per te ndaluar programin.\n")

while 1:
    try:
        Kerkesa = input('Shkruaj kërkesen dhe opsionin(nese ka): ')
        if Kerkesa!="" and Kerkesa.upper()!="EXIT":

            s.sendto(str(Kerkesa).encode(), (serverName, serverPort))
        else:
            break
        
        data, serverAddress = s.recvfrom(128)
        print('Të dhënat nga serveri: ')
        print(str(data.decode()).strip())
        print("\n")
    except Exception as m:
        print(str(m))
        break

s.close()   




