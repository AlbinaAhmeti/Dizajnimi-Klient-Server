from socket import *
import random
import time
import datetime
import sys
import threading
import cmath

print('             Programi TCP-Server             \n')

serverPort = 14000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

print('Serveri: ' + str(gethostbyname(gethostname())) + " , porti: " + str(serverPort))

serverSocket.listen(5)

print('\nServeri është duke punuar dhe është duke pritur per kerkesa...\n')

#IP
 
def IP(address):
    return str(address[0])

#NRPORTIT

def NRPORTIT(address):
    return str(address[1])

#NUMERO {Hapësire} tekst

def NUMERO(str):
    vnr = 0
    cnr = 0
    str = str.lower()
    for i in range(0, len(str)):
        if str[i] in ('a', "e", "i", "o", "u"):
            vnr = vnr + 1;
        elif (str[i] >= 'a' and str[i] <= 'z'):
            cnr = cnr + 1;
    return vnr, cnr

#ANASJELLTAS {Hapësire} tekst

def ANASJELLTAS(s):
    return s[::-1]

#PALINDROM {Hapësire} tekst

def PALINDROM(tekst):
    tekst = tekst.replace(" ", "")
    rev = ANASJELLTAS(tekst)
    if (tekst == rev):
         return str('Është fjali palindrom.')
    else:
         return str('Nuk është fjali palindrom.')

#KOHA

def KOHA():
    return str(datetime.datetime.now())

#LOJA

def LOJA():
    listaNR = []
    for i in range(5):
        listaNR.append(random.randint(1, 35))
    listaNR.sort()
    return str(listaNR)

#GCF {Hapësire} Numër1 {Hapësire} Numër2

def GCF(nr1, nr2):
    if (nr2 == 0):
        return nr1
    else:
        return GCF(nr2, nr1 % nr2)
   

#KONVERTO {Hapësire} Opcioni {Hapësire} Numër

def KONVERTO(type, nr):
    nrKonvertuar = 0
    nr = float(nr)

    if type == "cmNeInch":
        return str(nr / 2.54)
    elif type == "inchNeCm":
        return str(nr * 2.54)
    elif type == "kmNeMiles":
        return str(nr / 1.609)
    elif type == "mileNeKm":
        return str(nr * 1.609)
    else:
        return "Shënoni përsëri."
    
#NUMRI

def NUMRI(nr):
    nr = float(nr)

    if (nr > 0):
        num = "Numri është numer pozitiv."
        return num
    elif (nr < 0):
        num = "Numri është negativ."
        return num
    else:
        num = "Numri është ZERO."
        return num

# FIBONACCI

def FIBONACCI(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        return (nr - 1) + (nr - 2)

def ShtypTeDhenat(teDhenat):
    print("Të dhënat e dërguara te klienti:  \n", teDhenat)
    return


def Klienti(connectionSocket, addr):
    Kerkesa = (bytes)("empty".encode())
    try:
        while str(Kerkesa.decode()).upper() != "EXIT" and str(Kerkesa.decode()) != "":
            
            Kerkesa = connectionSocket.recv(128)
                        
            KerkesaStr = str(Kerkesa.decode()).strip()
                        
            KerkesaArray = KerkesaStr.split(' ')

            KerkesaArray[0] = KerkesaArray[0].upper()

            #IP
            if KerkesaArray[0] == "IP":
                if len(KerkesaArray) == 1:
                    connectionSocket.send(("IP adresa juaj është: " + IP(addr)).encode())
                    ShtypTeDhenat(("IP adresa e klientit: " + IP(addr)))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")

            #NRPORTIT
            elif KerkesaArray[0] == "NRPORTIT":
                if len(KerkesaArray) == 1:
                    connectionSocket.send(("Numri i NRPORTIT tuaj është: " + NRPORTIT(addr)).encode())
                    ShtypTeDhenat(("Numri i NRPORTIT te klientit është: " + NRPORTIT(addr)))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")
                    
            #NUMERO
            elif KerkesaArray[0] == "NUMERO":
                if len(KerkesaArray) == 2:
                    var1, var2 = NUMERO(KerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    connectionSocket.send(
                        ("Numri i zanoreve është " + var1 + " kurse numri i bashtinglloreve është " + var2).encode())
                    ShtypTeDhenat(("Numri i zanoreve është " + var1 + " kurse numri i bashtinglloreve është " + var2))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")
                    
            #ANASJELLTAS
            elif KerkesaArray[0] == "ANASJELLTAS":
                if len(KerkesaArray) == 2:
                    connectionSocket.send(("Fjala anasjelltas është : " + ANASJELLTAS(KerkesaArray[1])).encode())
                    ShtypTeDhenat(("Fjala anasjelltas është : " + ANASJELLTAS(KerkesaArray[1])))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")

            #PALINDROM
            elif KerkesaArray[0] == "PALINDROM":
                if len(KerkesaArray) == 2:
                    connectionSocket.send(("Fjala e dhene është : " + PALINDROM(KerkesaArray[1])).encode())
                    ShtypTeDhenat(("Fjala e dhene është : " + PALINDROM(KerkesaArray[1])))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")

            #KOHA
            elif KerkesaArray[0] == "KOHA":
                if len(KerkesaArray) == 1:
                    connectionSocket.send(("Koha e tanishme është: " + KOHA()).encode())
                    ShtypTeDhenat(("Koha e tanishme është: " + KOHA()))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")

            #LOJA
            elif KerkesaArray[0] == "LOJA":
                if len(KerkesaArray) == 1:
                    connectionSocket.send(("Rezultati nga loja: " + LOJA()).encode())
                    ShtypTeDhenat(("Rezultati nga loja: " + LOJA()))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")

             #GCF
            elif KerkesaArray[0] == "GCF":
                if len(KerkesaArray) == 3:
                    connectionSocket.send(("GCF është : " + GCF(KerkesaArray[1], KerkesaArray[2])).encode())
                    ShtypTeDhenat(("GCF është : " + GCF(KerkesaArray[1], KerkesaArray[2])))
                else:
                    connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                    ShtypTeDhenat("Gabim")
           
            #KONVERTO
            elif KerkesaArray[0] == "KONVERTO":
                for i in range(len(KerkesaArray)):
                    if "" in KerkesaArray:
                        KerkesaArray.remove("")
                if len(KerkesaArray) == 0 :
                    connectionSocket.send( ("Kerkesa është shtypur ose shënuar gabim, provoni perseri!").encode())
                    ShtypTeDhenat("Gabim")
                else:
                    Konvertimi = str(KerkesaArray[1]).lower().split("Ne")
                    pergjigja = KerkesaArray[2] + " " + str(Konvertimi[0]) + " jane te barabarte me " + KONVERTO(str(KerkesaArray[1]).upper(), KerkesaArray[2]) + " " + str(Konvertimi[1])
                    connectionSocket.send(str(pergjigja).encode())
                    ShtypTeDhenat(pergjigja)

 	    #NUMRI
            elif KerkesaArray[0]=="NUMRI":
                if len(KerkesaArray) == 2:
                    connectionSocket.send(("Numri i "+KerkesaArray[1]+" është: "+ NUMRI(KerkesaArray[1])).encode())
                    ShtypTeDhenat(("Numri i "+KerkesaArray[1]+" është: "+NUMRI(KerkesaArray[1])))                            
                else:
                    connectionSocket.send(("Kerkesa është shtypur ose shënuar gabim, provoni perseri!").encode())
                    ShtypTeDhenat("Gabim") 

	    #FIBONACCI
            elif KerkesaArray[0]=="FIBONACCI":
                for i in range(len(KerkesaArray)):
                    if "" in KerkesaArray:
                        KerkesaArray.remove("")
                if len(KerkesaArray)==1 or len(KerkesaArray)>2:
                    connectionSocket.send(("Kerkesa është shtypur ose shënuar gabim, provoni perseri!").encode())
                    ShtypTeDhenat("Gabim")
                else:
                    connectionSocket.send(("Numri i "+KerkesaArray[1]+" ne serine fibonacci është: "+FIBONACCI(KerkesaArray[1])).encode())
                    ShtypTeDhenat(("Numri i "+KerkesaArray[1]+" ne serine fibonacci është: "+FIBONACCI(KerkesaArray[1])))
 
            else:
                connectionSocket.send("Kerkesa është shtypur ose shënuar gabim, provoni perseri!".encode())
                ShtypTeDhenat("Gabim")
                  
        connectionSocket.close()
    except Exception as msg:
        print("\n Gabim: ")
        print(str(msg))
        connectionSocket.close()



while 1:
    
    connectionSocket, addr = serverSocket.accept()
    print('Klienti me IP adrese %s dhe me numrin e Portin %s është lidhur me server' % (addr))
    print("\n")

    threading._start_new_thread(Klienti, (connectionSocket, addr))

    