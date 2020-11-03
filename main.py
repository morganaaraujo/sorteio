from random import randint
from lista import LinkedList
import time


def ordenar(sorteados):
    for _ in range(sorteados.contar()-1):
        for j in range(sorteados.contar()-1):
            a = sorteados.get(j)
            b = sorteados.get(j+1)

            if a > b:
                sorteados.set(j,b)
                sorteados.set(j+1,a)

if __name__ == "__main__":

    sorteados = LinkedList()

    print("Bem-vindo ao sorteio!")
    print("São 6 números da sorte! Vai começar!")

    for i in range(6):
        x= randint(1,50)
        while sorteados.contem(x):
            x = randint(1,50)
        sorteados.atEnd(x)
        print()
        time.sleep(1)
        print("Sorteando ...")
        print()
        time.sleep(3)
        sorteados.listprint()
       
    ordenar(sorteados)
    print()
    time.sleep(1)
    print("Nossos computadores estão processando o resultado final")
    print()
    time.sleep(3)
    print("Os números sorteados:")
    sorteados.listprint()
    print()
    input("Pressione ENTER para sair")