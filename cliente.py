class Cliente:
    
    def __init__(self):
        self.cliente = dict([])

    def createCliente(self,nombreCliente,id_cliente,correoCliente,celular):
        self.cliente[id_cliente] = {}
        self.cliente[id_cliente]["Name"] = nombreCliente
        self.cliente[id_cliente]["ID"] = id_cliente   
        self.cliente[id_cliente]["correo"] = correoCliente
        self.cliente[id_cliente]["celular"]= celular
        
    def printClienteList(self):
        print("esta es la funcion")
        for id_cliente in self.cliente.keys():
            print("\n------------------------------------")
            print(f"Name: ",self.cliente[id_cliente]["Name"])
            print(f"ID: ",self.cliente[id_cliente]["ID"])
            print(f"Correo: ", self.cliente[id_cliente]["correo"])
            print(f"celular: ",self.cliente[id_cliente]["celular"])
            print("------------------------------------\n")   
    
    def deleteCliente(self, id_cliente):
        print("Estas en la funcion deleteCliente")
        return self.cliente.pop(id_cliente)
    
    def getCliente(self,id_cliente):
        print("estas en getCliente")
        return self.cliente.get(id_cliente)
    
    def updateCliente(self,id_cliente,nombreCliente,correoCliente,celular):
        self.cliente[id_cliente]["Name"] = nombreCliente 
        self.cliente[id_cliente]["correo"] = correoCliente
        self.cliente[id_cliente]["celular"]= celular
        
    def insertCreateCliente(self):
         print("has ingresado en la seccion crear Cliente")
         nombreCliente = input("ingrese su nombre: ")
         id_cliente = input("ingrese su ID: ")
         correoCliente = input("ingrese su correo: ")
         celular = input("ingrese su numero de celular: ")
         self.createCliente(nombreCliente, id_cliente, correoCliente, celular)
         print("!nuevo Cliente creado¡\n")
         
    def insertUpdateCliente(self):
        id_cliente = str(input('ingrese el id de instructor'))
        nombreCliente = str(input('ingrese nuevo nombre de instructor'))
        correoCliente = str(input('ingrese correo nuevo'))
        celular = str(input('ingrese nuevo numero de celular'))
        self.updateCliente(id_cliente,nombreCliente,correoCliente,celular)
        print('el instructor se ha actualizado')
    
    def insertDeleteCliente(self):
        id_cliente = input('ingrese el id del cliente')
        self.deleteCliente(id_cliente)
            
    