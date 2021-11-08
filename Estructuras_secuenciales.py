#La clase Nodo representa un solo nodo de la lista
class Nodo:
    def __init__(self, data = None, next= None):
        self.data = data  #En data se almacenan los datos que vamos a agregar
        self.next = next #Con next apuntamos al siguiente elemento de la lista

class ListaEnlazada:
    def __init__(self):
        self.head = None  #Establece la cabeza de la lista

    def inicio(self, data):
        nodo = Nodo(data, self.head) #Crea un nodo que apuntara a la cabeza de la lista
        self.head = nodo #Una vez creado el nodo, este asumira el papel cabeza de la lista

    def imprimir(self):
        temp_nodo = self.head
        while temp_nodo != None:
            print(temp_nodo.data, end='->')
            temp_nodo=temp_nodo.next

    def caracteres(self):
        secuencia = input()
        head = self.inicio(secuencia[0])
        actual = self.head
        for i in range(len(secuencia)-1):
            actual.next = self.inicio(secuencia[i+1])
            actual = actual.next
        return head
             



if __name__ == "__main__":
    ll = ListaEnlazada()
    ll.caracteres()
    ll.imprimir () 
  

