class Node:
    def __init__(self, data):
        self.data = data
        self.prox = None

class LinkedList:

    def __init__(self):
        self.head = None

    def atStart(self, newData):
        newNode = Node(newData)
        newNode.prox = self.head
        self.head = newNode   

    def atEnd(self, newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
        else:
            aux = self.head
            while(aux.prox != None):           
                aux = aux.prox
            aux.prox = newNode
 
    def inBetween(self, newData, pos):
        qtd = self.contar()
        if (qtd == 0 and pos != 0) or (pos > qtd):
            print("posicao invalida")
            return

        newNode = Node(newData)

        if self.head == None:
            self.head = newNode
            return

        aux = self.head

        i = 0
        while i != pos - 1:
            i += 1
            aux = aux.prox
        
        newNode.prox = aux.prox
        aux.prox = newNode

    def contar(self):
        i = 0
        aux = self.head
        while aux != None:
            i += 1
            aux = aux.prox
        return i
    
    def listprint(self):
        aux = self.head
        while aux != None:
            print(aux.data,end = " ")
            aux = aux.prox
        print()

    def get(self,indice):
        x = 0
        aux = self.head
        while x != indice:
            x = x + 1
            aux = aux.prox
        
        return aux.data

    def set(self, indice, valor):
        x = 0
        aux = self.head
        while x != indice:
            x = x + 1
            aux = aux.prox

        aux.data = valor

    def contem(self, valor):
        aux = self.head
        while aux != None:
            if aux.data == valor:
                return True
            aux = aux.prox
            
        return False


